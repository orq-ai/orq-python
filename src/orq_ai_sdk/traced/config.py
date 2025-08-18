"""Configuration management for Orq decorator SDK."""

import os
from typing import Optional, Dict, Any
from dataclasses import dataclass, field


@dataclass
class Config:
    """Configuration for Orq decorator SDK."""
    
    api_key: Optional[str] = None
    api_url: str = "https://my.orq.ai"
    workspace_id: Optional[str] = None
    batch_size: int = 25
    flush_interval: float = 1.0  # seconds
    timeout: float = 30.0  # seconds
    max_retries: int = 3
    enabled: bool = True
    debug: bool = False
    extra_attributes: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        """Load configuration from environment variables if not provided."""
        if not self.api_key:
            self.api_key = os.environ.get("ORQ_API_KEY")
        
        # Override from environment
        self.api_url = os.environ.get("ORQ_API_URL", self.api_url)
        self.debug = os.environ.get("ORQ_DEBUG", "false").lower() == "true"
    
    def validate(self):
        """Validate the configuration."""
        if self.enabled and not self.api_key:
            raise ValueError("ORQ_API_KEY is required when tracing is enabled")


# Global configuration instance
_config: Optional[Config] = None


def get_config() -> Config:
    """Get the global configuration instance."""
    global _config  # pylint: disable=global-statement
    if _config is None:
        _config = Config()
    return _config


def set_config(config: Config):
    """Set the global configuration."""
    global _config  # pylint: disable=global-statement
    _config = config
