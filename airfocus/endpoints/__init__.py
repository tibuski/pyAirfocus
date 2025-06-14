"""
Endpoint classes for interacting with the Airfocus API.
"""

from airfocus.endpoints.team import TeamEndpoints
from airfocus.endpoints.workspaces import WorkspacesEndpoints

__all__ = [
    "TeamEndpoints",
    "WorkspacesEndpoints"
]