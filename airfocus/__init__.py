"""
Airfocus API Client Library

A Python client for interacting with the Airfocus API.
"""

from airfocus.client import AirfocusClient
from airfocus.endpoints.team import TeamEndpoints
from airfocus.endpoints.workspaces import WorkspacesEndpoints

__version__ = "0.1.0"

__all__ = [
    "AirfocusClient",
    "TeamEndpoints", 
    "WorkspacesEndpoints",
    "__version__"
]