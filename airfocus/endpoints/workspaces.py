"""
Endpoints for workspace-related operations in the Airfocus API.
"""

from typing import List, Optional, Dict, Any, Tuple, Set
from airfocus.client import AirfocusClient
from airfocus.models.workspace import Workspace, WorkspaceGroup

class WorkspacesEndpoints:
    """
    Handles all workspace-related API endpoints.
    """
    
    def __init__(self, client: AirfocusClient):
        self.client = client
        
    def get_workspaces(self, include_archived: bool = False) -> List[Workspace]:
        """
        Get all workspaces in the team.
        
        Args:
            include_archived: Whether to include archived workspaces
            
        Returns:
            List[Workspace]: A list of workspaces
        """
        # Based on our testing, the search endpoint is the correct one
        data = self.client.post("/workspaces/search", json={
            "archived": include_archived
        })
        
        # If the response has no data, return an empty list
        if not data or not isinstance(data, dict):
            return []
            
        # Extract workspaces from the response - primarily from "items" based on our findings
        workspaces_data = []
        if "items" in data and isinstance(data["items"], list):
            workspaces_data = data["items"]
        elif "data" in data and isinstance(data["data"], list):
            workspaces_data = data["data"]
        elif "workspaces" in data and isinstance(data["workspaces"], list):
            workspaces_data = data["workspaces"]
        
        # Parse workspaces into models, handling any errors
        workspaces = []
        for ws_data in workspaces_data:
            try:
                workspace = Workspace(**ws_data)
                workspaces.append(workspace)
            except Exception as e:
                print(f"Warning: Could not parse workspace: {e}")
        
        return workspaces
    
    def get_workspace(self, workspace_id: str) -> Optional[Workspace]:
        """
        Get a specific workspace by ID.
        
        Args:
            workspace_id: The workspace ID
            
        Returns:
            Optional[Workspace]: The workspace details or None if not found
        """
        try:
            # First try the direct endpoint
            data = self.client.get(f"/workspaces/{workspace_id}")
            return Workspace(**data)
        except Exception:
            # If that fails, try to find it in the list of all workspaces
            workspaces = self.get_workspaces(include_archived=True)
            for workspace in workspaces:
                if workspace.id == workspace_id:
                    return workspace
            return None
    
    def create_workspace(self, name: str, description: str, order: int = 0, group_id: Optional[str] = None) -> Workspace:
        """
        Create a new workspace.
        
        Args:
            name: The workspace name
            description: The workspace description
            order: The workspace order (default 0)
            group_id: Optional group ID to place the workspace in
            
        Returns:
            Workspace: The created workspace
        """
        payload = {
            "name": name,
            "description": description,
            "order": order
        }
        
        if group_id:
            payload["groupId"] = group_id
            
        data = self.client.post("/workspaces", json=payload)
        return Workspace(**data)
    
    def update_workspace(self, workspace_id: str, **kwargs) -> Workspace:
        """
        Update a workspace.
        
        Args:
            workspace_id: The workspace ID
            **kwargs: Fields to update (name, description, etc.)
            
        Returns:
            Workspace: The updated workspace
        """
        data = self.client.put(f"/workspaces/{workspace_id}", json=kwargs)
        return Workspace(**data)
    
    def delete_workspace(self, workspace_id: str) -> None:
        """
        Delete a workspace.
        
        Args:
            workspace_id: The workspace ID
        """
        self.client.delete(f"/workspaces/{workspace_id}")
    
    def get_workspace_groups(self) -> List[WorkspaceGroup]:
        """
        Get all workspace groups (folders).
        
        Returns:
            List[WorkspaceGroup]: A list of workspace groups
        """
        try:
            data = self.client.post("/workspaces/groups/search", json={})
            
            # Extract groups from the response - primarily from "items" based on our findings
            groups_data = []
            if isinstance(data, dict):
                if "items" in data and isinstance(data["items"], list):
                    groups_data = data["items"]
                elif "data" in data and isinstance(data["data"], list):
                    groups_data = data["data"]
                elif "groups" in data and isinstance(data["groups"], list):
                    groups_data = data["groups"]
            
            # Parse groups into models, handling any errors
            groups = []
            for group_data in groups_data:
                try:
                    group = WorkspaceGroup(**group_data)
                    groups.append(group)
                except Exception as e:
                    print(f"Warning: Could not parse workspace group: {e}")
            
            return groups
        except Exception as e:
            # If the endpoint fails, return an empty list
            print(f"Error getting workspace groups: {e}")
            return []
    
    def get_group_hierarchy(self) -> Tuple[Dict[str, WorkspaceGroup], List[WorkspaceGroup]]:
        """
        Get the workspace group hierarchy with parent-child relationships.
        
        Returns:
            Tuple containing:
                - Dict[str, WorkspaceGroup]: Dictionary of all groups by ID
                - List[WorkspaceGroup]: List of top-level groups (groups with no parent)
        """
        # Get all groups
        groups = self.get_workspace_groups()
        
        # Create a dictionary of groups by ID for easy lookup
        groups_by_id = {group.id: group for group in groups}
        
        # Build the parent-child relationships between groups
        for group in groups:
            # If the group has a parent, add it as a child to that parent
            if group.parentGroupId and group.parentGroupId in groups_by_id:
                parent = groups_by_id[group.parentGroupId]
                parent.add_child_group(group.id)
        
        # Get top-level groups (groups with no parent)
        top_level_groups = [
            group for group in groups 
            if not group.parentGroupId or group.parentGroupId not in groups_by_id
        ]
        
        # Try to get workspace-to-group relationships
        try:
            # Method 1: Use _embedded.workspaceIds in group data
            for group in groups:
                if group._embedded and isinstance(group._embedded, dict):
                    workspace_ids = group._embedded.get("workspaceIds", [])
                    if isinstance(workspace_ids, list):
                        for ws_id in workspace_ids:
                            group.add_workspace(ws_id)
        except Exception as e:
            print(f"Error processing group workspace relationships from _embedded: {e}")
        
        # Method 2: Get all workspaces and map them to groups by groupId
        try:
            workspaces = self.get_workspaces(include_archived=True)
            for workspace in workspaces:
                if workspace.groupId and workspace.groupId in groups_by_id:
                    group = groups_by_id[workspace.groupId]
                    group.add_workspace(workspace.id)
        except Exception as e:
            print(f"Error mapping workspaces to groups by groupId: {e}")
        
        return groups_by_id, top_level_groups
    
    def get_workspaces_in_group(self, group_id: str, include_subgroups: bool = True) -> List[Workspace]:
        """
        Get all workspaces in a group, optionally including subgroups.
        
        Args:
            group_id: The group ID to search in
            include_subgroups: Whether to include workspaces in subgroups
            
        Returns:
            List[Workspace]: List of workspaces in the group
        """
        # Get all workspaces and groups
        workspaces = self.get_workspaces(include_archived=True)
        groups_by_id, _ = self.get_group_hierarchy()
        
        if group_id not in groups_by_id:
            return []
            
        # Get the target group
        target_group = groups_by_id[group_id]
        
        # Set of group IDs to search in
        group_ids_to_search = {group_id}
        
        # If including subgroups, collect all descendant groups
        if include_subgroups:
            self._collect_descendant_groups(target_group, groups_by_id, group_ids_to_search)
        
        # Get all workspace IDs in these groups (first from the _embedded.workspaceIds)
        workspace_ids_in_groups = set()
        for g_id in group_ids_to_search:
            group = groups_by_id[g_id]
            workspace_ids_in_groups.update(group.workspace_ids)
        
        # Filter workspaces to those in the target groups, using two methods:
        # 1. Workspace ID is in the group's workspace_ids (from _embedded)
        # 2. Workspace's groupId is in the target groups
        result_workspaces = []
        for workspace in workspaces:
            if workspace.id in workspace_ids_in_groups:
                result_workspaces.append(workspace)
            elif workspace.groupId and workspace.groupId in group_ids_to_search:
                result_workspaces.append(workspace)
        
        return result_workspaces
    
    def _collect_descendant_groups(self, group: WorkspaceGroup, groups_by_id: Dict[str, WorkspaceGroup], collected_ids: Set[str]) -> None:
        """
        Recursively collect all descendant group IDs.
        
        Args:
            group: The group to get descendants for
            groups_by_id: Dictionary of all groups by ID
            collected_ids: Set to add collected IDs to
        """
        for child_id in group.child_groups:
            if child_id in groups_by_id:
                collected_ids.add(child_id)
                # Recursively collect descendants of this child
                self._collect_descendant_groups(groups_by_id[child_id], groups_by_id, collected_ids)
                
    def move_workspace_to_group(self, workspace_id: str, group_id: str) -> bool:
        """
        Move a workspace to a different group.
        
        Args:
            workspace_id: The ID of the workspace to move
            group_id: The ID of the target group
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Get the workspace to verify it exists
            workspace = self.get_workspace(workspace_id)
            if not workspace:
                return False
                
            # Update the workspace with the new group ID
            self.update_workspace(workspace_id, groupId=group_id)
            return True
        except Exception as e:
            print(f"Error moving workspace to group: {e}")
            return False
            
    def create_workspace_group(self, name: str, parent_group_id: Optional[str] = None) -> Optional[WorkspaceGroup]:
        """
        Create a new workspace group (folder).
        
        Args:
            name: The name of the group
            parent_group_id: Optional ID of the parent group
            
        Returns:
            Optional[WorkspaceGroup]: The created group or None if creation failed
        """
        try:
            payload = {"name": name}
            
            if parent_group_id:
                payload["parentGroupId"] = parent_group_id
                
            data = self.client.post("/workspaces/groups", json=payload)
            return WorkspaceGroup(**data)
        except Exception as e:
            print(f"Error creating workspace group: {e}")
            return None