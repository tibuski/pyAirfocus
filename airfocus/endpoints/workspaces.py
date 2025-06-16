"""
Endpoints for workspace-related operations in the Airfocus API.
"""

import logging
from typing import List, Optional, Dict, Any, Tuple, Set
from airfocus.client import AirfocusClient
from airfocus.models.workspace import Workspace, WorkspaceGroup
from airfocus.constants import (
    ENDPOINT_WORKSPACES, ENDPOINT_WORKSPACES_SEARCH, ENDPOINT_WORKSPACES_GROUPS,
    ENDPOINT_WORKSPACES_GROUPS_SEARCH, ENDPOINT_WORKSPACES_LIST, FIELD_ITEMS, FIELD_DATA, 
    FIELD_WORKSPACES, FIELD_GROUPS, FIELD_EMBEDDED, FIELD_WORKSPACE_IDS, 
    ERROR_WORKSPACE_NOT_FOUND, ERROR_GROUP_NOT_FOUND
)

# Configure logger for this module
logger = logging.getLogger(__name__)

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
        data = self.client.post(ENDPOINT_WORKSPACES_SEARCH, json={
            "archived": include_archived
        })
        
        # If the response has no data, return an empty list
        if not data or not isinstance(data, dict):
            return []
            
        # Extract workspaces from the response - primarily from "items" based on our findings
        workspaces_data = []
        if FIELD_ITEMS in data and isinstance(data[FIELD_ITEMS], list):
            workspaces_data = data[FIELD_ITEMS]
        elif FIELD_DATA in data and isinstance(data[FIELD_DATA], list):
            workspaces_data = data[FIELD_DATA]
        elif FIELD_WORKSPACES in data and isinstance(data[FIELD_WORKSPACES], list):
            workspaces_data = data[FIELD_WORKSPACES]
        
        # Parse workspaces into models, handling any errors
        workspaces = []
        for ws_data in workspaces_data:
            try:
                workspace = Workspace(**ws_data)
                workspaces.append(workspace)
            except Exception as e:
                logger.warning(f"Could not parse workspace: {e}")
        
        return workspaces
    
    def get_workspace(self, workspace_id: str) -> Optional[Workspace]:
        """
        Get a specific workspace by ID.
        
        Args:
            workspace_id: The workspace ID
            
        Returns:
            Optional[Workspace]: The workspace details or None if not found
        """
        if not workspace_id:
            logger.warning("Workspace ID is empty")
            return None
            
        try:
            # First try the direct endpoint
            data = self.client.get(f"{ENDPOINT_WORKSPACES}/{workspace_id}")
            return Workspace(**data)
        except Exception as e:
            logger.debug(f"Direct workspace endpoint failed for {workspace_id}: {e}")
            # If that fails, try to find it in the list of all workspaces
            workspaces = self.get_workspaces(include_archived=True)
            for workspace in workspaces:
                if workspace.id == workspace_id:
                    return workspace
            logger.debug(f"Workspace not found: {workspace_id}")
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
            
        Raises:
            ValueError: If name is empty or order is negative
        """
        if not name or not name.strip():
            raise ValueError("Workspace name cannot be empty")
            
        if order < 0:
            raise ValueError("Order must be a non-negative integer")
            
        payload = {
            "name": name.strip(),
            "description": description,
            "order": order
        }
        
        if group_id:
            payload["groupId"] = group_id
            
        data = self.client.post(ENDPOINT_WORKSPACES, json=payload)
        workspace = Workspace(**data)
        logger.info(f"Created workspace: {workspace.name} (ID: {workspace.id})")
        return workspace
    
    def update_workspace(self, workspace_id: str, **kwargs) -> Workspace:
        """
        Update a workspace.
        
        Args:
            workspace_id: The workspace ID
            **kwargs: Fields to update (name, description, etc.)
            
        Returns:
            Workspace: The updated workspace
            
        Raises:
            ValueError: If workspace_id is empty
        """
        if not workspace_id:
            raise ValueError("Workspace ID cannot be empty")
            
        data = self.client.put(f"{ENDPOINT_WORKSPACES}/{workspace_id}", json=kwargs)
        workspace = Workspace(**data)
        logger.info(f"Updated workspace: {workspace.name} (ID: {workspace.id})")
        return workspace
    
    def delete_workspace(self, workspace_id: str) -> None:
        """
        Delete a workspace.
        
        Args:
            workspace_id: The workspace ID
            
        Raises:
            ValueError: If workspace_id is empty
        """
        if not workspace_id:
            raise ValueError("Workspace ID cannot be empty")
            
        self.client.delete(f"{ENDPOINT_WORKSPACES}/{workspace_id}")
        logger.info(f"Deleted workspace: {workspace_id}")
    
    def get_workspace_groups(self) -> List[WorkspaceGroup]:
        """
        Get all workspace groups (folders).
        
        Returns:
            List[WorkspaceGroup]: A list of workspace groups
        """
        try:
            data = self.client.post(ENDPOINT_WORKSPACES_GROUPS_SEARCH, json={})
            
            # Extract groups from the response - primarily from "items" based on our findings
            groups_data = []
            if isinstance(data, dict):
                if FIELD_ITEMS in data and isinstance(data[FIELD_ITEMS], list):
                    groups_data = data[FIELD_ITEMS]
                elif FIELD_DATA in data and isinstance(data[FIELD_DATA], list):
                    groups_data = data[FIELD_DATA]
                elif FIELD_GROUPS in data and isinstance(data[FIELD_GROUPS], list):
                    groups_data = data[FIELD_GROUPS]
            
            # Parse groups into models, handling any errors
            groups = []
            for group_data in groups_data:
                try:
                    group = WorkspaceGroup(**group_data)
                    groups.append(group)
                except Exception as e:
                    logger.warning(f"Could not parse workspace group: {e}")
            
            return groups
        except Exception as e:
            # If the endpoint fails, return an empty list
            logger.error(f"Error getting workspace groups: {e}")
            return []
    
    def get_group_hierarchy(self) -> Tuple[Dict[str, WorkspaceGroup], List[WorkspaceGroup]]:
        """
        Get the workspace group hierarchy with parent-child relationships.
        For each group, fetch its details using /workspaces/groups/{workspaceGroupId}.
        Returns:
            Tuple containing:
                - Dict[str, WorkspaceGroup]: Dictionary of all groups by ID
                - List[WorkspaceGroup]: List of top-level groups (groups with no parent)
        """
        # Step 1: Get all group IDs
        groups = self.get_workspace_groups()
        group_ids = [group.id for group in groups]
        
        # Step 2: Fetch each group by ID for full details
        detailed_groups = []
        for gid in group_ids:
            try:
                data = self.client.get(f"/workspaces/groups/{gid}")
                detailed_groups.append(WorkspaceGroup(**data))
            except Exception as e:
                logger.warning(f"Could not fetch group {gid}: {e}")
        
        # Step 3: Build lookup and relationships
        groups_by_id = {group.id: group for group in detailed_groups}
        for group in detailed_groups:
            if group.parentGroupId and group.parentGroupId in groups_by_id:
                parent = groups_by_id[group.parentGroupId]
                parent.add_child_group(group.id)
        top_level_groups = [
            group for group in detailed_groups
            if not group.parentGroupId or str(group.parentGroupId).strip() == ""
        ]
        # Workspace-to-group relationships (same as before)
        try:
            for group in detailed_groups:
                if group._embedded and isinstance(group._embedded, dict):
                    workspace_ids = group._embedded.get(FIELD_WORKSPACE_IDS, [])
                    if isinstance(workspace_ids, list):
                        for ws_id in workspace_ids:
                            group.add_workspace(ws_id)
        except Exception as e:
            logger.debug(f"Error processing group workspace relationships from _embedded: {e}")
        try:
            workspaces = self.get_workspaces(include_archived=True)
            for workspace in workspaces:
                if workspace.groupId and workspace.groupId in groups_by_id:
                    group = groups_by_id[workspace.groupId]
                    group.add_workspace(workspace.id)
        except Exception as e:
            logger.debug(f"Error mapping workspaces to groups by groupId: {e}")
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
        if not group_id:
            logger.warning("Group ID is empty")
            return []
            
        # Get all workspaces and groups
        workspaces = self.get_workspaces(include_archived=True)
        groups_by_id, _ = self.get_group_hierarchy()
        
        if group_id not in groups_by_id:
            logger.debug(f"Group not found: {group_id}")
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
        if not workspace_id:
            logger.warning("Workspace ID is empty")
            return False
            
        if not group_id:
            logger.warning("Group ID is empty")
            return False
            
        try:
            # Get the workspace to verify it exists
            workspace = self.get_workspace(workspace_id)
            if not workspace:
                logger.warning(f"Workspace not found: {workspace_id}")
                return False
                
            # Update the workspace with the new group ID
            self.update_workspace(workspace_id, groupId=group_id)
            logger.info(f"Moved workspace {workspace_id} to group {group_id}")
            return True
        except Exception as e:
            logger.error(f"Error moving workspace to group: {e}")
            return False
            
    def create_workspace_group(self, name: str, parent_group_id: Optional[str] = None) -> Optional[WorkspaceGroup]:
        """
        Create a new workspace group (folder).
        
        Args:
            name: The name of the group
            parent_group_id: Optional ID of the parent group
            
        Returns:
            Optional[WorkspaceGroup]: The created group or None if creation failed
            
        Raises:
            ValueError: If name is empty
        """
        if not name or not name.strip():
            raise ValueError("Group name cannot be empty")
            
        try:
            payload = {"name": name.strip()}
            
            if parent_group_id:
                payload["parentGroupId"] = parent_group_id
                
            data = self.client.post(ENDPOINT_WORKSPACES_GROUPS, json=payload)
            group = WorkspaceGroup(**data)
            logger.info(f"Created workspace group: {group.name} (ID: {group.id})")
            return group
        except Exception as e:
            logger.error(f"Error creating workspace group: {e}")
            return None
    
    def get_workspaces_by_ids(self, workspace_ids: List[str]) -> Dict[str, Workspace]:
        """
        Get multiple workspaces by their IDs in a single API call using the workspaces/list endpoint.
        This is much more efficient than making individual API calls for each workspace.
        
        Args:
            workspace_ids: List of workspace IDs to retrieve
            
        Returns:
            Dict[str, Workspace]: Dictionary of workspaces by their IDs
        """
        if not workspace_ids:
            return {}
            
        try:
            # Use the more efficient list endpoint - API expects a direct JSON array, not an object
            data = self.client.post(ENDPOINT_WORKSPACES_LIST, json=workspace_ids)
            
            # Extract workspaces from the response
            workspaces_data = []
            if isinstance(data, dict):
                if FIELD_ITEMS in data and isinstance(data[FIELD_ITEMS], list):
                    workspaces_data = data[FIELD_ITEMS]
                elif FIELD_DATA in data and isinstance(data[FIELD_DATA], list):
                    workspaces_data = data[FIELD_DATA]
                elif FIELD_WORKSPACES in data and isinstance(data[FIELD_WORKSPACES], list):
                    workspaces_data = data[FIELD_WORKSPACES]
                elif isinstance(data.get("workspaces"), list):
                    workspaces_data = data["workspaces"]
            elif isinstance(data, list):
                # The API might directly return an array
                workspaces_data = data
            
            # Parse workspaces into models and build the lookup dictionary
            workspace_map = {}
            for ws_data in workspaces_data:
                try:
                    workspace = Workspace(**ws_data)
                    workspace_map[workspace.id] = workspace
                except Exception as e:
                    logger.warning(f"Could not parse workspace: {e}")
            
            return workspace_map
        except Exception as e:
            logger.error(f"Error getting workspaces by IDs: {e}")
            return {}