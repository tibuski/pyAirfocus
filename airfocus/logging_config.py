"""
Logging configuration for the pyAirfocus library.
"""

import logging
import sys
from typing import Optional

def setup_logging(
    level: int = logging.INFO,
    format_string: Optional[str] = None,
    stream: Optional[logging.StreamHandler] = None
) -> None:
    """
    Set up logging configuration for the pyAirfocus library.
    
    Args:
        level: Logging level (default: INFO)
        format_string: Custom format string for log messages
        stream: Custom stream handler (default: sys.stdout)
    """
    if format_string is None:
        format_string = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    
    if stream is None:
        stream = logging.StreamHandler(sys.stdout)
    
    # Configure root logger
    logging.basicConfig(
        level=level,
        format=format_string,
        handlers=[stream]
    )
    
    # Set specific loggers to avoid too verbose output from external libraries
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)

def get_logger(name: str) -> logging.Logger:
    """
    Get a logger instance for the specified module.
    
    Args:
        name: Logger name (usually __name__)
        
    Returns:
        Configured logger instance
    """
    return logging.getLogger(name) 