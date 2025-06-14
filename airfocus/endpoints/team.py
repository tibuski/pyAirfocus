"""
Endpoints for team-related operations in the Airfocus API.
"""

import logging
from typing import List, Optional, Dict, Any
from airfocus.client import AirfocusClient
from airfocus.models.team import TeamUser, Team
from airfocus.constants import (
    ENDPOINT_TEAM, ENDPOINT_TEAM_USERS, SUPPORTED_ROLES,
    ERROR_USER_NOT_FOUND
)

# Configure logger for this module
logger = logging.getLogger(__name__)

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
        return self.client.get_collection(ENDPOINT_TEAM_USERS, TeamUser)
    
    def get_user(self, user_identifier: str) -> Optional[TeamUser]:
        """
        Get a specific user by ID or email.
        
        Args:
            user_identifier: The user's ID or email
            
        Returns:
            TeamUser: User information if found, None otherwise
        """
        if not user_identifier:
            logger.warning("User identifier is empty")
            return None
            
        users = self.get_users()
        
        # Try to find by user ID first
        for user in users:
            if user.userId == user_identifier:
                return user
                
        # If not found by ID, try by email
        for user in users:
            if user.email.lower() == user_identifier.lower():
                return user
                
        logger.debug(f"User not found: {user_identifier}")
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
        data = self.client.get(ENDPOINT_TEAM)
        return Team(**data)
    
    def change_user_role(self, user_id: str, role: str) -> None:
        """
        Change a user's role.
        
        Args:
            user_id: The user's ID
            role: The new role (admin, editor, contributor)
            
        Raises:
            ValueError: If role is not supported or user_id is empty
        """
        if not user_id:
            raise ValueError("User ID cannot be empty")
            
        if role not in SUPPORTED_ROLES:
            raise ValueError(f"Role must be one of: {', '.join(SUPPORTED_ROLES)}")
            
        payload = {
            "userId": user_id,
            "role": role
        }
        self.client.post("/team/users/role", json=payload)
        logger.info(f"Changed role for user {user_id} to {role}")
    
    def disable_user(self, user_id: str, disabled: bool = True) -> None:
        """
        Enable or disable a user.
        
        Args:
            user_id: The user's ID
            disabled: Whether to disable (True) or enable (False) the user
            
        Raises:
            ValueError: If user_id is empty
        """
        if not user_id:
            raise ValueError("User ID cannot be empty")
            
        payload = {
            "userId": user_id,
            "disabled": disabled
        }
        self.client.post("/team/users/disabled", json=payload)
        action = "disabled" if disabled else "enabled"
        logger.info(f"{action.capitalize()} user {user_id}")
        
    def invite_user(self, email: str, full_name: str, role: str) -> Dict[str, Any]:
        """
        Invite a new user to the team.
        
        Args:
            email: The user's email
            full_name: The user's full name
            role: The user's role (admin, editor, contributor)
            
        Returns:
            Dict: Response data from the API
            
        Raises:
            ValueError: If any parameter is invalid
        """
        if not email or '@' not in email:
            raise ValueError("Valid email is required")
            
        if not full_name or not full_name.strip():
            raise ValueError("Full name is required")
            
        if role not in SUPPORTED_ROLES:
            raise ValueError(f"Role must be one of: {', '.join(SUPPORTED_ROLES)}")
            
        payload = {
            "email": email.lower().strip(),
            "fullName": full_name.strip(),
            "role": role
        }
        result = self.client.post("/team/users/invite", json=payload)
        logger.info(f"Invited user {email} with role {role}")
        return result
        
    def kick_user(self, user_id: str) -> None:
        """
        Remove a user from the team.
        
        Args:
            user_id: The user's ID
            
        Raises:
            ValueError: If user_id is empty
        """
        if not user_id:
            raise ValueError("User ID cannot be empty")
            
        payload = {
            "userId": user_id
        }
        self.client.post("/team/users/kick", json=payload)
        logger.info(f"Removed user {user_id} from team")