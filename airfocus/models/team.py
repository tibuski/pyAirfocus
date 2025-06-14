"""
Pydantic models for team-related Airfocus API objects.
"""

from typing import Optional, Dict, List
from pydantic import BaseModel, Field, validator
from airfocus.constants import SUPPORTED_ROLES

class UserState(BaseModel):
    """Model representing the state of a user in an Airfocus team."""
    pending: bool
    # Add other state properties as needed based on the API response

class TeamUser(BaseModel):
    """Model representing a user in an Airfocus team."""
    userId: str
    teamId: str
    email: Optional[str] = None  # Email is optional and can be empty
    fullName: str
    role: str
    state: UserState
    isTeamCreator: bool
    disabled: bool
    emailVerified: bool
    createdAt: str
    updatedAt: str
    avatarAttachmentId: Optional[str] = None
    lastSeenAt: Optional[str] = None
    
    @validator('role')
    def validate_role(cls, v):
        """Validate user role is supported."""
        if v not in SUPPORTED_ROLES:
            raise ValueError(f'Role must be one of: {", ".join(SUPPORTED_ROLES)}')
        return v
    
    @validator('fullName')
    def validate_full_name(cls, v):
        """Validate full name is not empty."""
        if not v or not v.strip():
            raise ValueError('Full name cannot be empty')
        return v.strip()

class Team(BaseModel):
    """Model representing an Airfocus team."""
    id: str = Field(..., alias="teamId")
    name: str
    # Add other team properties based on the API response
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
    
    @validator('name')
    def validate_name(cls, v):
        """Validate team name is not empty."""
        if not v or not v.strip():
            raise ValueError('Team name cannot be empty')
        return v.strip()