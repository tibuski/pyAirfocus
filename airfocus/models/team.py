"""
Pydantic models for team-related Airfocus API objects.
"""

from typing import Optional, Dict, List
from pydantic import BaseModel, Field

class UserState(BaseModel):
    """Model representing the state of a user in an Airfocus team."""
    pending: bool
    # Add other state properties as needed based on the API response

class TeamUser(BaseModel):
    """Model representing a user in an Airfocus team."""
    userId: str
    teamId: str
    email: str
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

class Team(BaseModel):
    """Model representing an Airfocus team."""
    id: str = Field(..., alias="teamId")
    name: str
    # Add other team properties based on the API response
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None