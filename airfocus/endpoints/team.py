"""
Endpoints for team-related operations in the Airfocus API.
"""

from typing import List, Optional, Dict, Any
from airfocus.client import AirfocusClient
from airfocus.models.team import TeamUser, Team

class TeamEndpoints:
    """
    Handles all team-related API endpoints.
    """
    
    def __init__(self, client: AirfocusClient):
        self.client = client
        
    def get_users(self) -> List[TeamUser]:
        """
        Get all users in the team.
        
        Returns:
            List[TeamUser]: A list of team users
        """
        return self.client.get_collection("/team/users", TeamUser)
    
    def get_user(self, user_identifier: str) -> Optional[TeamUser]:
        """
        Get a specific user by ID or email.
        
        Args:
            user_identifier: The user's ID or email
            
        Returns:
            TeamUser: User information if found, None otherwise
        """
        users = self.get_users()
        
        # Try to find by user ID first
        for user in users:
            if user.userId == user_identifier:
                return user
                
        # If not found by ID, try by email
        for user in users:
            if user.email.lower() == user_identifier.lower():
                return user
                
        return None
    
    def get_last_login(self, user_identifier: str) -> Optional[str]:
        """
        Get the last login time for a specific user.
        
        Args:
            user_identifier: The user's ID or email
            
        Returns:
            str: The last login time (lastSeenAt) if available, None otherwise
        """
        user = self.get_user(user_identifier)
        if user:
            return user.lastSeenAt
        return None
    
    def get_team(self) -> Team:
        """
        Get information about the current team.
        
        Returns:
            Team: Team information
        """
        data = self.client.get("/team")
        return Team(**data)
    
    def change_user_role(self, user_id: str, role: str) -> None:
        """
        Change a user's role.
        
        Args:
            user_id: The user's ID
            role: The new role (admin, editor, contributor)
        """
        payload = {
            "userId": user_id,
            "role": role
        }
        self.client.post("/team/users/role", json=payload)
    
    def disable_user(self, user_id: str, disabled: bool = True) -> None:
        """
        Enable or disable a user.
        
        Args:
            user_id: The user's ID
            disabled: Whether to disable (True) or enable (False) the user
        """
        payload = {
            "userId": user_id,
            "disabled": disabled
        }
        self.client.post("/team/users/disabled", json=payload)
        
    def invite_user(self, email: str, full_name: str, role: str) -> Dict[str, Any]:
        """
        Invite a new user to the team.
        
        Args:
            email: The user's email
            full_name: The user's full name
            role: The user's role (admin, editor, contributor)
            
        Returns:
            Dict: Response data from the API
        """
        payload = {
            "email": email,
            "fullName": full_name,
            "role": role
        }
        return self.client.post("/team/users/invite", json=payload)
        
    def kick_user(self, user_id: str) -> None:
        """
        Remove a user from the team.
        
        Args:
            user_id: The user's ID
        """
        payload = {
            "userId": user_id
        }
        self.client.post("/team/users/kick", json=payload)