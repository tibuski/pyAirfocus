"""
Pydantic models for workspace-related Airfocus API objects.
"""

from typing import Optional, Dict, List, Any, Union, Set
from pydantic import BaseModel, Field, root_validator, validator

class RichTextDescription(BaseModel):
    """Model for rich text descriptions that use blocks."""
    blocks: List[Dict[str, Any]] = []

class Workspace(BaseModel):
    """Model representing an Airfocus workspace."""
    id: str
    teamId: str
    name: str
    description: Optional[Union[str, RichTextDescription, Dict[str, Any]]] = ""
    progressMode: Optional[str] = None
    createdAt: Optional[str] = None
    lastUpdatedAt: Optional[str] = None
    namespace: Optional[Union[str, Dict[str, Any]]] = None
    order: Optional[int] = 0
    
    # Additional fields based on API response
    groupId: Optional[str] = None
    archived: Optional[bool] = False
    type: Optional[str] = None
    itemType: Optional[str] = None
    itemColor: Optional[str] = None
    alias: Optional[str] = None
    defaultPermission: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    _embedded: Optional[Dict[str, Any]] = None
    
    @validator('name')
    def validate_name(cls, v):
        """Validate workspace name is not empty."""
        if not v or not v.strip():
            raise ValueError('Workspace name cannot be empty')
        return v.strip()
    
    @validator('order')
    def validate_order(cls, v):
        """Validate order is a non-negative integer."""
        if v is not None and v < 0:
            raise ValueError('Order must be a non-negative integer')
        return v
    
    # Make the model flexible to handle various field names
    @root_validator(pre=True)
    def handle_field_variations(cls, values):
        # Handle different date field names
        if 'created_at' in values and 'createdAt' not in values:
            values['createdAt'] = values['created_at']
        if 'updated_at' in values and 'lastUpdatedAt' not in values:
            values['lastUpdatedAt'] = values['updated_at']
        if 'last_updated_at' in values and 'lastUpdatedAt' not in values:
            values['lastUpdatedAt'] = values['last_updated_at']
            
        # Handle different ID field names
        if 'workspace_id' in values and 'id' not in values:
            values['id'] = values['workspace_id']
        if 'team_id' in values and 'teamId' not in values:
            values['teamId'] = values['team_id']
        if 'group_id' in values and 'groupId' not in values:
            values['groupId'] = values['group_id']
            
        # Handle embedded data if present
        if '_embedded' in values and isinstance(values['_embedded'], dict):
            # Extract any useful fields from _embedded
            embedded = values['_embedded']
            
            # Some fields might be in the embedded data
            if 'groupId' not in values and 'groupId' in embedded:
                values['groupId'] = embedded['groupId']
                
        return values
    
    def get_description_text(self) -> str:
        """Extract text from description regardless of format."""
        if not self.description:
            return ""
        if isinstance(self.description, str):
            return self.description
        if isinstance(self.description, dict) and 'blocks' in self.description:
            # Try to extract text from rich text blocks
            try:
                text_blocks = []
                for block in self.description['blocks']:
                    if 'text' in block:
                        text_blocks.append(block['text'])
                return " ".join(text_blocks)
            except Exception:
                return "[Rich Text]"
        return str(self.description)

class WorkspaceGroup(BaseModel):
    """Model representing a workspace group (folder)."""
    id: str
    teamId: Optional[str] = None
    name: str
    order: Optional[int] = 0
    createdAt: Optional[str] = None
    lastUpdatedAt: Optional[str] = None
    parentGroupId: Optional[str] = None
    defaultPermission: Optional[str] = None
    
    # Additional fields based on API response
    _embedded: Optional[Dict[str, Any]] = None
    
    # References to child groups and workspaces (not from API, populated by client)
    child_groups: List[str] = Field(default_factory=list)
    workspace_ids: List[str] = Field(default_factory=list)
    
    @validator('name')
    def validate_name(cls, v):
        """Validate group name is not empty."""
        if not v or not v.strip():
            raise ValueError('Group name cannot be empty')
        return v.strip()
    
    @validator('order')
    def validate_order(cls, v):
        """Validate order is a non-negative integer."""
        if v is not None and v < 0:
            raise ValueError('Order must be a non-negative integer')
        return v
    
    # Make the model flexible to handle various field names
    @root_validator(pre=True)
    def handle_field_variations(cls, values):
        # Handle different date field names
        if 'created_at' in values and 'createdAt' not in values:
            values['createdAt'] = values['created_at']
        if 'updated_at' in values and 'lastUpdatedAt' not in values:
            values['lastUpdatedAt'] = values['updated_at']
            
        # Handle different ID field names
        if 'group_id' in values and 'id' not in values:
            values['id'] = values['group_id']
        if 'team_id' in values and 'teamId' not in values:
            values['teamId'] = values['team_id']
        if 'parent_group_id' in values and 'parentGroupId' not in values:
            values['parentGroupId'] = values['parent_group_id']
        
        # Extract workspace IDs from _embedded if present
        if '_embedded' in values and isinstance(values['_embedded'], dict):
            embedded = values['_embedded']
            if 'workspaceIds' in embedded and isinstance(embedded['workspaceIds'], list):
                values['workspace_ids'] = embedded['workspaceIds']
                
        return values
    
    @property
    def has_workspaces(self) -> bool:
        """Check if this group has any workspaces."""
        return len(self.workspace_ids) > 0
    
    @property
    def has_child_groups(self) -> bool:
        """Check if this group has any child groups."""
        return len(self.child_groups) > 0
    
    def add_child_group(self, group_id: str) -> None:
        """Add a child group to this group."""
        if not group_id:
            raise ValueError("Group ID cannot be empty")
        if group_id not in self.child_groups:
            self.child_groups.append(group_id)
    
    def add_workspace(self, workspace_id: str) -> None:
        """Add a workspace to this group."""
        if not workspace_id:
            raise ValueError("Workspace ID cannot be empty")
        if workspace_id not in self.workspace_ids:
            self.workspace_ids.append(workspace_id)