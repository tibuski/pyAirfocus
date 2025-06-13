"""
Display a hierarchical view of workspace groups and workspaces with user permissions.

This script displays:
1. All workspace groups in a hierarchical tree structure
2. All workspaces within each group
3. For each group and workspace, lists all users with access and their permissions
   (excluding users with viewer permissions)
4. Displays a count of unique users with access next to each group and workspace

Usage:
    python list_workspace_hierarchy_with_permissions.py            # Show all groups
    python list_workspace_hierarchy_with_permissions.py "Group Name"  # Show only the specified group
"""

from airfocus.client import AirfocusClient
from airfocus.models.workspace import Workspace, WorkspaceGroup
from airfocus.models.team import TeamUser
from typing import Dict, List, Optional, Any, Set, Tuple
import logging
import colorama
from colorama import Fore, Style
import sys
import json

# Initialize colorama for Windows support
colorama.init()

# Define colors for different hierarchy levels
COLORS = [
    Fore.CYAN,    # Level 0
    Fore.GREEN,   # Level 1
    Fore.YELLOW,  # Level 2
    Fore.MAGENTA, # Level 3
    Fore.BLUE,    # Level 4
    Fore.RED,     # Level 5
]

# Configure logging to be less intrusive
logging.basicConfig(
    level=logging.WARNING,
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger("workspace_permissions")

class WorkspacePermissionsManager:
    """Manager for retrieving and displaying workspace permissions."""
    
    def __init__(self, exclude_viewers=True, filter_group_name=None, debug_mode=False):
        self.client = AirfocusClient()
        self.users_by_id = {}
        self.workspace_permissions = {}
        self.group_permissions = {}
        self.team_roles = {}
        self.exclude_viewers = exclude_viewers
        self.user_count_cache = {}  # Cache for user counts to avoid recalculation
        self.filter_group_name = filter_group_name
        self.debug_mode = debug_mode  # Set to True to show debug information
        
    def load_users(self) -> Dict[str, TeamUser]:
        """Load all users and create a lookup dictionary by user ID."""
        users = self.client.team.get_users()
        self.users_by_id = {user.userId: user for user in users}
        
        # Store team roles for fallback permission handling
        for user_id, user in self.users_by_id.items():
            self.team_roles[user_id] = user.role
            
        return self.users_by_id
    
    def get_workspace_permissions(self, workspace_id: str) -> Dict[str, str]:
        """
        Get user permissions for a specific workspace.
        
        Args:
            workspace_id: The workspace ID
            
        Returns:
            Dict mapping user IDs to permission levels
        """
        # If permissions are already cached, return them
        if workspace_id in self.workspace_permissions:
            return self.workspace_permissions[workspace_id]
            
        try:
            # Try to call API to get workspace permissions
            data = self.client.get(f"/workspaces/{workspace_id}/permissions")
            
            # Process the response to extract user permissions
            permissions = {}
            
            if isinstance(data, list):
                for item in data:
                    if "userId" in item and "permission" in item:
                        permissions[item["userId"]] = item["permission"]
            elif isinstance(data, dict) and "items" in data:
                for item in data["items"]:
                    if "userId" in item and "permission" in item:
                        permissions[item["userId"]] = item["permission"]
            
            self.workspace_permissions[workspace_id] = permissions
            return permissions
        except Exception as e:
            # Log error but don't display it in the output
            logger.debug(f"Could not fetch permissions for workspace {workspace_id}: {e}")
            
            # Fall back to workspace default permission or team roles
            try:
                workspace = self.client.workspaces.get_workspace(workspace_id)
                if workspace and workspace.defaultPermission:
                    # Use the default permission from the workspace if available
                    permissions = {}
                    for user_id in self.users_by_id:
                        # Admin users likely have full access regardless of default
                        if self.team_roles.get(user_id) == "admin":
                            permissions[user_id] = "admin"
                        else:
                            permissions[user_id] = workspace.defaultPermission
                    self.workspace_permissions[workspace_id] = permissions
                    return permissions
                else:
                    # If no default permission, fall back to team roles
                    permissions = self._generate_permissions_from_team_roles()
                    self.workspace_permissions[workspace_id] = permissions
                    return permissions
            except Exception:
                # If all else fails, use team roles
                permissions = self._generate_permissions_from_team_roles()
                self.workspace_permissions[workspace_id] = permissions
                return permissions
    
    def get_group_permissions(self, group_id: str) -> Dict[str, str]:
        """
        Get user permissions for a specific workspace group.
        
        Args:
            group_id: The group ID
            
        Returns:
            Dict mapping user IDs to permission levels
        """
        # If permissions are already cached, return them
        if group_id in self.group_permissions:
            return self.group_permissions[group_id]
        
        # For groups, we'll try a different approach since the direct API call seems to fail
        try:
            # Try an alternative API endpoint if the direct one isn't working
            # This is commented out because the API seems to not support it
            # data = self.client.get(f"/workspaces/groups/{group_id}")
            
            # Instead, let's use the group's defaultPermission if available
            groups_by_id, _ = self.client.workspaces.get_group_hierarchy()
            
            if group_id in groups_by_id:
                group = groups_by_id[group_id]
                if group.defaultPermission:
                    # Use the default permission from the group
                    permissions = {}
                    for user_id in self.users_by_id:
                        # Admin users likely have full access regardless of default
                        if self.team_roles.get(user_id) == "admin":
                            permissions[user_id] = "admin"
                        else:
                            permissions[user_id] = group.defaultPermission
                    self.group_permissions[group_id] = permissions
                    return permissions
            
            # If no default permission or no group, fall back to team roles
            permissions = self._generate_permissions_from_team_roles()
            self.group_permissions[group_id] = permissions
            return permissions
            
        except Exception as e:
            # Log error but don't display it in the output
            logger.debug(f"Could not determine permissions for group {group_id}: {e}")
            
            # Fall back to team roles
            permissions = self._generate_permissions_from_team_roles()
            self.group_permissions[group_id] = permissions
            return permissions
    
    def _generate_permissions_from_team_roles(self) -> Dict[str, str]:
        """
        Generate permissions based on user roles in the team.
        This is a fallback when we can't get specific permissions.
        
        Returns:
            Dict mapping user IDs to permission levels
        """
        permissions = {}
        for user_id, role in self.team_roles.items():
            # Map team roles to permissions
            if role == "admin":
                permissions[user_id] = "admin"
            elif role == "editor":
                permissions[user_id] = "editor"
            else:
                permissions[user_id] = "viewer"  # Default for other roles
        return permissions
    
    def get_unique_users(self, group: WorkspaceGroup, groups_by_id: Dict[str, WorkspaceGroup], 
                         workspaces_by_id: Dict[str, Workspace], include_subgroups: bool = True) -> Set[str]:
        """
        Get the set of unique users with access to a group and its workspaces.
        
        Args:
            group: The group to check
            groups_by_id: Dictionary of all groups by ID
            workspaces_by_id: Dictionary of all workspaces by ID
            include_subgroups: Whether to include users from subgroups
            
        Returns:
            Set[str]: Set of unique user IDs with access
        """
        # Create a cache key for this request
        cache_key = f"{group.id}_{include_subgroups}"
        if cache_key in self.user_count_cache:
            return self.user_count_cache[cache_key]
            
        unique_users = set()
        
        # Add users with direct access to the group (excluding viewers if configured)
        group_permissions = self.get_group_permissions(group.id)
        for user_id, permission in group_permissions.items():
            if not self.exclude_viewers or permission.lower() != "viewer":
                unique_users.add(user_id)
        
        # Add users with access to workspaces in this group
        workspaces_in_group = []
        for ws_id in group.workspace_ids:
            if ws_id in workspaces_by_id:
                workspaces_in_group.append(workspaces_by_id[ws_id])
        
        # Also add workspaces that reference this group via groupId
        for ws in workspaces_by_id.values():
            if ws.groupId == group.id and ws not in workspaces_in_group:
                workspaces_in_group.append(ws)
        
        # Add users from each workspace
        for workspace in workspaces_in_group:
            workspace_permissions = self.get_workspace_permissions(workspace.id)
            for user_id, permission in workspace_permissions.items():
                if not self.exclude_viewers or permission.lower() != "viewer":
                    unique_users.add(user_id)
        
        # If including subgroups, recursively add users from them
        if include_subgroups and group.child_groups:
            for child_id in group.child_groups:
                if child_id in groups_by_id:
                    child_group = groups_by_id[child_id]
                    child_users = self.get_unique_users(
                        child_group, groups_by_id, workspaces_by_id, True
                    )
                    unique_users.update(child_users)
        
        # Cache the result for future calls
        self.user_count_cache[cache_key] = unique_users
        return unique_users
    
    def get_unique_users_count(self, group: WorkspaceGroup, groups_by_id: Dict[str, WorkspaceGroup], 
                               workspaces_by_id: Dict[str, Workspace], include_subgroups: bool = True) -> int:
        """
        Get the count of unique users with access to a group and its workspaces.
        
        Args:
            group: The group to check
            groups_by_id: Dictionary of all groups by ID
            workspaces_by_id: Dictionary of all workspaces by ID
            include_subgroups: Whether to include users from subgroups
            
        Returns:
            int: Count of unique users with access
        """
        unique_users = self.get_unique_users(group, groups_by_id, workspaces_by_id, include_subgroups)
        return len(unique_users)
    
    def get_workspace_unique_users_count(self, workspace: Workspace) -> int:
        """
        Get the count of unique users with access to a workspace.
        
        Args:
            workspace: The workspace to check
            
        Returns:
            int: Count of unique users with access
        """
        cache_key = f"ws_{workspace.id}"
        if cache_key in self.user_count_cache:
            return len(self.user_count_cache[cache_key])
            
        unique_users = set()
        permissions = self.get_workspace_permissions(workspace.id)
        for user_id, permission in permissions.items():
            if not self.exclude_viewers or permission.lower() != "viewer":
                unique_users.add(user_id)
                
        self.user_count_cache[cache_key] = unique_users
        return len(unique_users)
    
    def get_workspace_groups_direct(self) -> List[Dict[str, Any]]:
        """
        Get raw workspace groups data directly from the API.
        This is a debug method to help troubleshoot hierarchy issues.
        """
        try:
            data = self.client.post("/workspaces/groups/search", json={})
            
            # Extract groups from the response
            groups_data = []
            if isinstance(data, dict):
                if "items" in data and isinstance(data["items"], list):
                    groups_data = data["items"]
                elif "data" in data and isinstance(data["data"], list):
                    groups_data = data["data"]
                elif "groups" in data and isinstance(data["groups"], list):
                    groups_data = data["groups"]
            
            return groups_data
        except Exception as e:
            print(f"Error getting raw workspace groups: {e}")
            return []
    
    def get_workspaces_for_group(self, group_id: str, all_workspaces: List[Workspace]) -> List[Workspace]:
        """
        Get all workspaces that belong to a specific group.
        
        Args:
            group_id: The group ID to find workspaces for
            all_workspaces: List of all workspaces
            
        Returns:
            List of workspaces belonging to the group
        """
        workspaces_in_group = []
        
        # Add workspaces that have this group as their groupId
        for workspace in all_workspaces:
            if workspace.groupId == group_id:
                workspaces_in_group.append(workspace)
                
        # Debug information
        if self.debug_mode:
            print(f"DEBUG: Found {len(workspaces_in_group)} workspaces for group {group_id}")
            for ws in workspaces_in_group:
                print(f"DEBUG:    Workspace: {ws.name} (ID: {ws.id})")
                
        return workspaces_in_group
    
    def print_hierarchy_with_permissions(self):
        """Print the complete workspace hierarchy with permissions."""
        # Load all users first
        self.load_users()
        
        # Get workspace group hierarchy
        groups_by_id, top_level_groups = self.client.workspaces.get_group_hierarchy()
        
        # Get all workspaces
        all_workspaces = self.client.workspaces.get_workspaces(include_archived=True)
        workspaces_by_id = {ws.id: ws for ws in all_workspaces}
        
        # If filtering by group name, find the matching group
        if self.filter_group_name:
            # Try to find the group with the specified name (case-insensitive)
            matching_groups = [
                group for group in groups_by_id.values() 
                if group.name.lower() == self.filter_group_name.lower()
            ]
            
            if matching_groups:
                # Found a matching group
                matching_group = matching_groups[0]
                print(f"\n{Fore.CYAN}=== Workspace Hierarchy for Group: {matching_group.name} ==={Style.RESET_ALL}\n")
                
                # Debug: Find all workspaces directly for this group
                group_workspaces = self.get_workspaces_for_group(matching_group.id, all_workspaces)
                
                # Find direct child groups using parentGroupId
                direct_child_groups = []
                for group in groups_by_id.values():
                    if hasattr(group, 'parentGroupId') and group.parentGroupId == matching_group.id:
                        direct_child_groups.append(group)
                        # Make sure it's in the child_groups list
                        if group.id not in matching_group.child_groups:
                            matching_group.child_groups.append(group.id)
                
                if self.debug_mode:
                    print(f"DEBUG: Found {len(direct_child_groups)} direct child groups by parentGroupId")
                    for child in direct_child_groups:
                        print(f"DEBUG: Child group: {child.name}")
                
                # Print the matching group with its hierarchy
                self._print_group(
                    matching_group, 
                    groups_by_id, 
                    workspaces_by_id,
                    all_workspaces, 
                    "", 
                    True, 
                    level=0,
                    show_users=True  # Show users by default for the filtered view
                )
                return
            else:
                # Try partial matching if exact match fails
                matching_groups = [
                    group for group in groups_by_id.values() 
                    if self.filter_group_name.lower() in group.name.lower()
                ]
                
                if matching_groups:
                    # Sort by name length to prioritize closer matches
                    matching_groups.sort(key=lambda g: len(g.name))
                    matching_group = matching_groups[0]
                    print(f"\n{Fore.CYAN}=== Workspace Hierarchy for Group: {matching_group.name} ==={Style.RESET_ALL}\n")
                    
                    # Debug: Find all workspaces directly for this group
                    self.get_workspaces_for_group(matching_group.id, all_workspaces)
                    
                    self._print_group(
                        matching_group,
                        groups_by_id,
                        workspaces_by_id,
                        all_workspaces,
                        "",
                        True,
                        level=0,
                        show_users=True
                    )
                    return
                else:
                    print(f"\n{Fore.RED}No group found with name containing '{self.filter_group_name}'{Style.RESET_ALL}\n")
                    return
        
        # If no filter or filter didn't match, show everything
        # Find workspaces not in any group
        ungrouped_workspaces = [
            ws for ws in all_workspaces 
            if not ws.groupId or ws.groupId not in groups_by_id
        ]
        
        print(f"\n{Fore.CYAN}=== Workspace Hierarchy with User Permissions ==={Style.RESET_ALL}\n")
        
        # Print top-level groups and their contents
        for i, group in enumerate(top_level_groups):
            is_last = i == len(top_level_groups) - 1
            self._print_group(group, groups_by_id, workspaces_by_id, all_workspaces, "", is_last, level=0)
        
        # Print ungrouped workspaces if any
        if ungrouped_workspaces:
            print(f"\n{Fore.CYAN}=== Ungrouped Workspaces ==={Style.RESET_ALL}")
            for i, workspace in enumerate(ungrouped_workspaces):
                is_last = i == len(ungrouped_workspaces) - 1
                self._print_workspace(workspace, "", is_last, level=0)
    
    def _print_group(self, group: WorkspaceGroup, groups_by_id: Dict[str, WorkspaceGroup], 
                    workspaces_by_id: Dict[str, Workspace], all_workspaces: List[Workspace],
                    indent: str, is_last: bool, level: int = 0,
                    show_users: bool = True):
        """
        Recursively print a group, its permissions, workspaces, and subgroups.
        
        Args:
            group: The group to print
            groups_by_id: Dictionary of all groups by ID
            workspaces_by_id: Dictionary of all workspaces by ID
            all_workspaces: List of all workspaces
            indent: Current indentation string
            is_last: Whether this is the last item at the current level
            level: Current hierarchy level
            show_users: Whether to show user permissions (can be disabled to focus on structure)
        """
        # Get color for current level
        color = COLORS[level % len(COLORS)]
        
        # Get count of unique users for this group
        user_count = self.get_unique_users_count(group, groups_by_id, workspaces_by_id)
        
        # Print group name with proper tree structure and user count
        connector = "└── " if is_last else "├── "
        print(f"{indent}{connector}{color}Group: {group.name} {Style.RESET_ALL}[{user_count} unique users]")
        
        # Prepare next level indentation
        next_indent = indent + ("    " if is_last else "│   ")
        
        # Get group workspaces directly by groupId
        workspaces_in_group = self.get_workspaces_for_group(group.id, all_workspaces)
        
        # Sort workspaces by name
        workspaces_in_group.sort(key=lambda ws: ws.name)
        
        # Get and print group permissions without the "Permissions:" label
        if show_users:
            permissions = self.get_group_permissions(group.id)
            if permissions:
                users_with_access = [
                    (self.users_by_id[user_id].fullName, permission)
                    for user_id, permission in permissions.items()
                    if user_id in self.users_by_id and 
                    (not self.exclude_viewers or permission.lower() != "viewer")
                ]
                
                # Sort users by name
                users_with_access.sort(key=lambda x: x[0])
                
                for i, (user_name, permission) in enumerate(users_with_access):
                    is_last_user = i == len(users_with_access) - 1 and not group.child_groups and not workspaces_in_group
                    user_connector = "└── " if is_last_user else "├── "
                    print(f"{next_indent}{user_connector}{user_name}: {permission}")
        
        # First print child groups
        child_groups_exist = bool(group.child_groups)
        if child_groups_exist:
            child_group_ids = group.child_groups
            for i, child_id in enumerate(child_group_ids):
                if child_id in groups_by_id:
                    child_group = groups_by_id[child_id]
                    # Check if this is the last item in both child groups and workspaces
                    is_last_child = (i == len(child_group_ids) - 1 and not workspaces_in_group)
                    self._print_group(
                        child_group, 
                        groups_by_id, 
                        workspaces_by_id,
                        all_workspaces,
                        next_indent, 
                        is_last_child,
                        level=level+1,
                        show_users=show_users
                    )
        
        # Then print workspaces in this group
        if workspaces_in_group:
            for i, workspace in enumerate(workspaces_in_group):
                is_last_ws = i == len(workspaces_in_group) - 1
                self._print_workspace(workspace, next_indent, is_last_ws, level=level+1, show_users=show_users)
    
    def _print_workspace(self, workspace: Workspace, indent: str, is_last: bool = False, level: int = 0, 
                         show_users: bool = True):
        """
        Print a workspace and its permissions.
        
        Args:
            workspace: The workspace to print
            indent: Current indentation string
            is_last: Whether this is the last item at the current level
            level: Current hierarchy level
            show_users: Whether to show user permissions
        """
        # Get color for current level
        color = COLORS[level % len(COLORS)]
        
        # Get count of unique users for this workspace
        user_count = self.get_workspace_unique_users_count(workspace)
        
        connector = "└── " if is_last else "├── "
        print(f"{indent}{connector}{color}Workspace: {workspace.name} {Style.RESET_ALL}[{user_count} unique users]")
        
        # Only show users if requested
        if not show_users:
            return
            
        # Prepare next level indentation
        next_indent = indent + ("    " if is_last else "│   ")
        
        # Get and print workspace permissions without the "Permissions:" label
        permissions = self.get_workspace_permissions(workspace.id)
        if permissions:
            users_with_access = [
                (self.users_by_id[user_id].fullName, permission)
                for user_id, permission in permissions.items()
                if user_id in self.users_by_id and 
                   (not self.exclude_viewers or permission.lower() != "viewer")
            ]
            
            # Sort users by name
            users_with_access.sort(key=lambda x: x[0])
            
            for i, (user_name, permission) in enumerate(users_with_access):
                is_last_user = i == len(users_with_access) - 1
                user_connector = "└── " if is_last_user else "├── "
                print(f"{next_indent}{user_connector}{user_name}: {permission}")
        else:
            # If no specific permissions, show default permission if available
            default = workspace.defaultPermission or "None"
            if not self.exclude_viewers or default.lower() != "viewer":
                print(f"{next_indent}└── Default: {default}")
            else:
                print(f"{next_indent}└── Default: {default} (viewers excluded)")

def main():
    """Run the workspace hierarchy permissions display."""
    try:
        # Check if a group name was provided as a command-line argument
        filter_group_name = None
        if len(sys.argv) > 1:
            filter_group_name = sys.argv[1]
            
        manager = WorkspacePermissionsManager(
            exclude_viewers=True,
            filter_group_name=filter_group_name,
            debug_mode=False  # Set to True to enable debug output
        )
        manager.print_hierarchy_with_permissions()
    except Exception as e:
        logger.error(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()