"""Client for communicating with Orq API."""

import atexit
import json
import queue
import threading
import time
from typing import List, Optional
import requests
from urllib.parse import urljoin

from traced.config import Config, get_config, set_config
from traced.span import Span


class OrqClient:
    """Client for sending spans to Orq API."""
    
    def __init__(self, config: Optional[Config] = None):
        """Initialize the client with configuration."""
        self.config = config or get_config()
        self.config.validate()
        
        # Initialize queue for batching
        self._queue = queue.Queue()
        self._batch = []
        self._batch_lock = threading.Lock()
        
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
            with self._batch_lock:
                if self._queue.qsize() >= self.config.batch_size:
                    self._flush()
        except queue.Full:
            if self.config.debug:
                print("Span queue is full, dropping span")
    
    def _flush(self) -> None:
        """Flush pending spans to the API."""
        spans_to_send = []
        
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

        print("send spans")

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
                print("payload")
                print(json.dumps(payload, indent=2))
                # response = requests.post(
                #     url,
                #     json=payload,
                #     headers=headers,
                #     timeout=self.config.timeout
                # )
                
                # if response.status_code == 200:
                #     if self.config.debug:
                #         print(f"Successfully sent {len(spans)} spans")
                #     return
                # else:
                #     if self.config.debug:
                #         print(f"Failed to send spans: {response.status_code} - {response.text}")
                    
                #     # Don't retry on client errors
                #     if 400 <= response.status_code < 500:
                #         return

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
    global _client
    if _client is None:
        _client = OrqClient()
    return _client


def init(
    api_key: Optional[str] = None,
    api_url: Optional[str] = None,
    debug: Optional[bool] = None,
    enabled: Optional[bool] = None,
    **kwargs
) -> None:
    """
    Initialize the Orq SDK with configuration.
    
    Args:
        api_key: API key for authentication
        api_url: Base URL for Orq API
        debug: Enable debug logging
        enabled: Enable/disable tracing
        **kwargs: Additional configuration options
    """
    global _client
    
    # Create config with provided values
    config_kwargs = {
        k: v for k, v in {
            "api_key": api_key,
            "api_url": api_url,
            "debug": debug,
            "enabled": enabled,
            **kwargs
        }.items() if v is not None
    }
    
    config = Config(**config_kwargs)
    set_config(config)

    print('config')
    print(config)
    
    # Reset client to use new config
    if _client:
        _client.shutdown()
    _client = OrqClient(config)