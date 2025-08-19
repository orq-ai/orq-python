"""Client for communicating with Orq API."""
# pylint: disable=no-else-return

import atexit
import inspect
import queue
import threading
import sys
import time
from typing import List, Optional, TYPE_CHECKING, Any, Dict
import requests
from urllib.parse import urljoin

from .config import Config, get_config, set_config
from .span import Span

if TYPE_CHECKING:
    from orq_ai_sdk.sdk import Orq

class OrqClient:
    """Client for sending spans to Orq API."""
    
    def __init__(self, config: Optional[Config] = None):
        """Initialize the client with configuration."""
        self.config = config or get_config()
        self.config.validate()
        
        # Initialize queue for batching
        self._queue: queue.Queue[Span] = queue.Queue()
        self._flush_lock = threading.Lock()
        
        # Start background thread for flushing
        self._stop_event = threading.Event()
        self._flush_thread = None
        
        if self.config.enabled:
            self._start_flush_thread()
            # Register cleanup on exit
            atexit.register(self.shutdown)
    
    def _start_flush_thread(self):
        """Start the background thread for flushing spans."""
        self._flush_thread = threading.Thread(target=self._flush_worker, daemon=True)
        self._flush_thread.start()
    
    def _flush_worker(self):
        """Background worker for flushing spans."""
        while not self._stop_event.is_set():
            try:
                # Wait for flush interval
                self._stop_event.wait(self.config.flush_interval)
                
                # Flush any pending spans
                self._flush()
            except Exception as e:
                if self.config.debug:
                    print(f"Error in flush worker: {e}")
    
    def submit_span(self, span: Span) -> None:
        """Submit a span for transmission."""
        if not self.config.enabled:
            return
        
        try:
            self._queue.put(span, block=False)
            
            # Check if we should flush immediately
            if self._queue.qsize() >= self.config.batch_size:
                self._flush()
        except queue.Full:
            if self.config.debug:
                print("Span queue is full, dropping span")
    
    def _flush(self) -> None:
        """Flush pending spans to the API."""
        with self._flush_lock:
            spans_to_send: List[Span] = []
            
            # Collect spans from queue
            while not self._queue.empty() and len(spans_to_send) < self.config.batch_size:
                try:
                    span = self._queue.get_nowait()
                    spans_to_send.append(span)
                except queue.Empty:
                    break
            
            if spans_to_send:
                self._send_spans(spans_to_send)
    
    def _send_spans(self, spans: List[Span]) -> None:
        """Send spans to the Orq API."""

        if not spans:
            return
        
        # Prepare payload
        payload = {
            "spans": [span.to_dict() for span in spans]
        }

        # Prepare headers
        headers = {
            "Authorization": f"Bearer {self.config.api_key}",
            "Content-Type": "application/json"
        }
        
        if self.config.workspace_id:
            headers["x-orq-workspace-id"] = self.config.workspace_id
        
        url = urljoin(self.config.api_url, "/v2/traces/v1/traces")
        
        # Send request with retries
        for attempt in range(self.config.max_retries):
            try:
                response = requests.post(
                    url,
                    json=payload,
                    headers=headers,
                    timeout=self.config.timeout
                )
                
                if response.status_code == 200:
                    if self.config.debug:
                        print(f"Successfully sent {len(spans)} spans - Server response: {response.status_code}")
                        print(f"Response body: {response.text}")
                    return
                else:
                    if self.config.debug:
                        print(f"Failed to send spans: {response.status_code} - {response.text}")
                    
                    # Don't retry on client errors
                    if 400 <= response.status_code < 500:
                        return
            
            except Exception as e:
                if self.config.debug:
                    print(f"Error sending spans (attempt {attempt + 1}): {e}")
                
                # Wait before retry
                if attempt < self.config.max_retries - 1:
                    time.sleep(2 ** attempt)  # Exponential backoff
    
    def flush(self) -> None:
        """Manually flush all pending spans."""
        self._flush()
    
    def shutdown(self) -> None:
        """Shutdown the client and flush remaining spans."""
        if self._flush_thread and self._flush_thread.is_alive():
            # Stop the flush thread
            self._stop_event.set()
            self._flush_thread.join(timeout=5.0)
        
        # Final flush
        self._flush()


# Global client instance
_client: Optional[OrqClient] = None


def get_client() -> OrqClient:
    """Get the global client instance."""
    global _client  # pylint: disable=global-statement

    # Try to find an Orq instance and auto-initialize from it
    orq_instance = _find_orq_instance()
    if orq_instance:
        try:
            init_from_orq(orq_instance)
        except Exception:
            # If auto-init fails, fall back to default client
            _client = OrqClient()
    else:
        _client = OrqClient()

    assert _client is not None  # This should always be true
    return _client


def init_from_orq(orq_instance: "Orq") -> None:
    """
    Initialize the traced client using configuration from an existing Orq instance.
    
    Args:
        orq_instance: An initialized Orq SDK instance
    """
    global _client  # pylint: disable=global-statement

    # Extract configuration from Orq instance
    config_kwargs: Dict[str, Any] = {}
    
    # Get API key from the Orq instance's security configuration
    if orq_instance.sdk_configuration.security:
        security = orq_instance.sdk_configuration.security
        if callable(security):
            security_obj = security()
            if security_obj and security_obj.api_key:
                config_kwargs["api_key"] = str(security_obj.api_key)
        elif hasattr(security, 'api_key'):
            api_key = security.api_key
            if api_key is not None:
                config_kwargs["api_key"] = str(api_key)
    
    # Get API Base URL from the Orq instance
    server_url, _ = orq_instance.sdk_configuration.get_server_details()

    if server_url:
        config_kwargs["api_url"] = str(server_url)

    # Extract debug flag from logger
    if orq_instance.sdk_configuration.debug_logger:
        # If a debug logger is set, enable debug mode
        config_kwargs["debug"] = bool(orq_instance.sdk_configuration.debug_logger)

    # Extract timeout if available
    if orq_instance.sdk_configuration.timeout_ms:
        config_kwargs["timeout"] = float(orq_instance.sdk_configuration.timeout_ms) / 1000.0

    # Create config with extracted values
    config = Config(**config_kwargs)
    set_config(config)
    
    # Reset client to use new config
    if _client:
        _client.shutdown()
    _client = OrqClient(config)

def _find_orq_instance() -> Optional["Orq"]:
    """
    Try to find an Orq instance in the calling context.
    This searches through the call stack frames to find an Orq instance.
    """
    try:
        from orq_ai_sdk.sdk import Orq  # pylint: disable=import-outside-toplevel

        # Check the main module first
        main_module = sys.modules.get('__main__')
        if main_module:
            for _, obj in vars(main_module).items():
                if isinstance(obj, Orq):
                    return obj

        # Check through the call stack
        for frame_info in inspect.stack():
            frame = frame_info.frame

            # Check local variables
            for _, obj in frame.f_locals.items():
                if isinstance(obj, Orq):
                    return obj

            # Check global variables in the frame's module
            for _, obj in frame.f_globals.items():
                if isinstance(obj, Orq):
                    return obj

    except Exception as e:
        config = get_config()
        if config.debug:
            print(f"Failed to find orq instance for init: {e}")

    return None
