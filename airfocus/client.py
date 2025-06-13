"""
Base client for interacting with the Airfocus API.
"""

import os
import httpx
from typing import List, Dict, Any, Optional, TypeVar, Type
from pydantic import BaseModel
from dotenv import load_dotenv, find_dotenv

T = TypeVar('T', bound=BaseModel)

class AirfocusClient:
    """
    Base client for interacting with the Airfocus API.
    Handles authentication, requests, and error handling.
    """
    
    def __init__(self, api_key: Optional[str] = None, verify_ssl: Optional[bool] = None):
        # Load from .env if not provided
        if api_key is None:
            load_dotenv(find_dotenv(), override=True)
            api_key = os.getenv("AIRFOCUS_API_KEY")
            
        if verify_ssl is None:
            verify_ssl_str = os.getenv("VERIFY_SSL", "true")
            verify_ssl = verify_ssl_str.lower() == "true"
            
        if not api_key:
            raise ValueError("API key is required. Set it in .env file or pass to constructor.")
            
        self.api_key = api_key
        self.verify_ssl = verify_ssl
        self.base_url = "https://app.airfocus.com/api"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json"
        }
        
        # Initialize API endpoint handlers lazily
        self._team_api = None
        self._workspaces_api = None
        
    def _get_full_url(self, endpoint: str) -> str:
        """Construct the full URL for an API endpoint."""
        # Ensure endpoint starts with /
        if not endpoint.startswith('/'):
            endpoint = f"/{endpoint}"
        return f"{self.base_url}{endpoint}"
    
    def request(self, method: str, endpoint: str, **kwargs) -> Any:
        """
        Make a request to the Airfocus API.
        
        Args:
            method: HTTP method (get, post, put, delete, etc.)
            endpoint: API endpoint (e.g., "/team/users")
            **kwargs: Additional arguments to pass to httpx
            
        Returns:
            Parsed JSON response
            
        Raises:
            httpx.HTTPStatusError: If the request fails
        """
        url = self._get_full_url(endpoint)
        
        # Add headers to any existing ones in kwargs
        headers = kwargs.pop('headers', {})
        headers.update(self.headers)
        
        with httpx.Client(verify=self.verify_ssl) as client:
            response = getattr(client, method.lower())(url, headers=headers, **kwargs)
            response.raise_for_status()
            return response.json()
            
    def get(self, endpoint: str, **kwargs) -> Any:
        """Perform a GET request."""
        return self.request('get', endpoint, **kwargs)
        
    def post(self, endpoint: str, **kwargs) -> Any:
        """Perform a POST request."""
        return self.request('post', endpoint, **kwargs)
        
    def put(self, endpoint: str, **kwargs) -> Any:
        """Perform a PUT request."""
        return self.request('put', endpoint, **kwargs)
        
    def delete(self, endpoint: str, **kwargs) -> Any:
        """Perform a DELETE request."""
        return self.request('delete', endpoint, **kwargs)
        
    def get_collection(self, endpoint: str, model_class: Type[T], **kwargs) -> List[T]:
        """
        Get a collection of items and parse them into the specified model.
        
        Args:
            endpoint: API endpoint
            model_class: Pydantic model class to parse the response into
            **kwargs: Additional arguments for the request
            
        Returns:
            List of parsed models
        """
        data = self.get(endpoint, **kwargs)
        
        # Handle both list responses and responses with a 'data' field
        if isinstance(data, list):
            items = data
        else:
            items = data.get('data', [])
            
        return [model_class(**item) for item in items]
    
    @property
    def team(self):
        """Access team-related endpoints."""
        if self._team_api is None:
            from airfocus.endpoints.team import TeamEndpoints
            self._team_api = TeamEndpoints(self)
        return self._team_api
    
    @property
    def workspaces(self):
        """Access workspace-related endpoints."""
        if self._workspaces_api is None:
            from airfocus.endpoints.workspaces import WorkspacesEndpoints
            self._workspaces_api = WorkspacesEndpoints(self)
        return self._workspaces_api