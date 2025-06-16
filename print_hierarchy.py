from airfocus.client import AirfocusClient
from airfocus.constants import ENDPOINT_WORKSPACES_GROUPS_LIST
from airfocus.models.workspace import WorkspaceGroup
import argparse
import sys
import time

# ANSI color codes for terminal colors and text formatting
class Colors:
    # Text formatting
    RESET = "\033[0m"
    BOLD = "\033[1m"      # Bold may not work in all terminals
    ITALIC = "\033[3m"    # Italic may not work in all terminals
    UNDERLINE = "\033[4m"
    
    # Group level colors (different distinct colors instead of shades of blue)
    GROUP_COLORS = [
        "\033[1;35m",     # Level 0: Bold Purple
        "\033[1;34m",     # Level 1: Bold Blue
        "\033[1;36m",     # Level 2: Bold Cyan
        "\033[1;32m",     # Level 3: Bold Green
        "\033[1;33m"      # Level 4+: Bold Yellow
    ]
    
    # Workspace format (yellow italic)
    WORKSPACE = "\033[3;33m"  # Yellow italic
    
    # Tree characters
    TREE_BRANCH = "├── "
    TREE_CORNER = "└── "
    TREE_VERTICAL = "│   "
    TREE_SPACE = "    "

def print_group_hierarchy_with_users(client, target_group_name=None, show_debug=False):
    """
    Print the workspace group hierarchy with user counts as a colorful tree view.
    Uses efficient bulk API calls to minimize requests.
    
    Args:
        client: AirfocusClient instance
        target_group_name: Optional name of a specific group to show hierarchy for
        show_debug: Whether to show debug information during processing
    """
    if show_debug:
        print("Fetching groups...")
    else:
        print("Preparing workspace hierarchy... Please wait...")
        
    # Step 1: Get all workspace groups in a single API call (basic info only)
    all_groups = client.workspaces.get_workspace_groups()
    
    # Step 2: Get the IDs of all groups
    group_ids = [group.id for group in all_groups]
    
    # Step 3: Let's try to use the bulk API to get all groups in one call first
    if show_debug:
        print(f"Fetching detailed information for {len(group_ids)} groups...")
    
    try:
        # Try to use the bulk endpoint to get groups
        raw_data = client.post(ENDPOINT_WORKSPACES_GROUPS_LIST, json=group_ids)
        groups_by_id = {}
        group_user_counts = {}
        
        # Process each group from the bulk response
        if isinstance(raw_data, list):
            # Bulk response is a list of group objects
            for data in raw_data:
                try:
                    gid = data.get('id')
                    if gid:
                        # Create WorkspaceGroup object
                        group = WorkspaceGroup(**data)
                        groups_by_id[gid] = group
                        
                        # Extract permissions count
                        user_count = 0
                        if '_embedded' in data and 'permissions' in data['_embedded']:
                            permissions = data['_embedded']['permissions']
                            if isinstance(permissions, dict):
                                user_count = len(permissions)
                                if show_debug:
                                    print(f"Group {group.name}: Found {user_count} users")
                        
                        group_user_counts[gid] = user_count
                except Exception as e:
                    if show_debug:
                        print(f"Error processing group data: {e}")
        else:
            if show_debug:
                print("Bulk API didn't return a list, falling back to individual requests")
            # Fall back to individual requests
            for gid in group_ids:
                try:
                    # Fetch each group directly to get the permissions data
                    data = client.get(f"/workspaces/groups/{gid}")
                    # Create WorkspaceGroup object directly from the data
                    group = WorkspaceGroup(**data)
                    groups_by_id[gid] = group
                    
                    # Extract permissions count directly from the raw data
                    user_count = 0
                    if '_embedded' in data and 'permissions' in data['_embedded']:
                        permissions = data['_embedded']['permissions']
                        if isinstance(permissions, dict):
                            user_count = len(permissions)
                            if show_debug:
                                print(f"Group {group.name}: Found {user_count} users")
                    
                    group_user_counts[gid] = user_count
                    
                except Exception as e:
                    if show_debug:
                        print(f"Error fetching group {gid}: {e}")
    except Exception as e:
        if show_debug:
            print(f"Error with bulk group fetch: {e}")
        # Fall back to using the groups we already have
        groups_by_id = {group.id: group for group in all_groups}
        group_user_counts = {group.id: 0 for group in all_groups}
    
    # Step 4: Build the hierarchy (parent-child relationships)
    if show_debug:
        print("Building group hierarchy...")
    
    # Initialize child_groups and workspace_ids for all groups
    for group_id, group in groups_by_id.items():
        if not hasattr(group, 'child_groups'):
            group.child_groups = []
        if not hasattr(group, 'workspace_ids'):
            group.workspace_ids = []
    
    # Set up parent-child relationships
    for group_id, group in groups_by_id.items():
        if hasattr(group, 'parentGroupId') and group.parentGroupId and group.parentGroupId in groups_by_id:
            parent = groups_by_id[group.parentGroupId]
            if group_id not in parent.child_groups:
                parent.child_groups.append(group_id)
        
        # Extract workspaces from the _embedded data if present
        if hasattr(group, '_embedded') and group._embedded:
            embedded = group._embedded
            if isinstance(embedded, dict):
                # Try to get workspaceIds from embedded data
                if 'workspaceIds' in embedded and isinstance(embedded['workspaceIds'], list):
                    for ws_id in embedded['workspaceIds']:
                        if ws_id not in group.workspace_ids:
                            group.workspace_ids.append(ws_id)
                
                # Also try to get workspaces from embedded data
                if 'workspaces' in embedded and isinstance(embedded['workspaces'], list):
                    for ws_data in embedded['workspaces']:
                        if isinstance(ws_data, dict) and 'id' in ws_data:
                            ws_id = ws_data['id']
                            if ws_id not in group.workspace_ids:
                                group.workspace_ids.append(ws_id)
    
    # Step 5: Collect all workspace IDs referenced in any group
    if show_debug:
        print("Collecting workspace IDs...")
    
    all_workspace_ids = set()
    for group_id, group in groups_by_id.items():
        all_workspace_ids.update(getattr(group, 'workspace_ids', []))
    
    # Step 6: Optimize workspace fetching
    if show_debug:
        print(f"Fetching detailed information for {len(all_workspace_ids)} workspaces...")
    
    workspace_map = {}
    workspace_user_counts = {}
    start_time = time.time()
    
    # First, try to get all workspaces in a single bulk API call
    try:
        # Use the bulk API to get all workspaces at once
        ws_list_data = client.post("/workspaces/list", json=list(all_workspace_ids))
        
        if isinstance(ws_list_data, list):
            # Process all workspaces from the bulk response
            permissions_in_bulk = False  # Flag to check if bulk response includes permissions
            
            for data in ws_list_data:
                try:
                    ws_id = data.get('id')
                    if ws_id:
                        from airfocus.models.workspace import Workspace
                        workspace = Workspace(**data)
                        workspace_map[ws_id] = workspace
                        
                        # Try to extract permissions from bulk response
                        user_count = 0
                        if '_embedded' in data and 'permissions' in data['_embedded']:
                            permissions = data['_embedded']['permissions']
                            if isinstance(permissions, dict):
                                user_count = len(permissions)
                                permissions_in_bulk = True
                        
                        workspace_user_counts[ws_id] = user_count
                except Exception as e:
                    if show_debug:
                        print(f"Error processing workspace data: {e}")
            
            # If no workspaces had permissions in the bulk response, we can skip individual fetching
            if not permissions_in_bulk and show_debug:
                print("Bulk API response doesn't include permissions data.")
                print("User counts for workspaces will be shown as 0.")
                
                # We could fetch permissions individually, but that would be slow
                # So we'll just leave the counts as 0 unless you specifically need them
                
                # Alternatively, we could fetch permissions for a small subset of workspaces
                # For example, only the ones in the target group if specified
                if target_group_name:
                    target_workspace_ids = set()
                    for group in groups_by_id.values():
                        if group.name.lower() == target_group_name.lower():
                            target_workspace_ids.update(getattr(group, 'workspace_ids', []))
                            
                            # Also include workspaces from child groups
                            for child_id in getattr(group, 'child_groups', []):
                                if child_id in groups_by_id:
                                    child = groups_by_id[child_id]
                                    target_workspace_ids.update(getattr(child, 'workspace_ids', []))
                    
                    if target_workspace_ids and show_debug:
                        print(f"Fetching permissions for {len(target_workspace_ids)} workspaces in the target group...")
                        for ws_id in target_workspace_ids:
                            if ws_id in workspace_map:
                                try:
                                    data = client.get(f"/workspaces/{ws_id}")
                                    if '_embedded' in data and 'permissions' in data['_embedded']:
                                        permissions = data['_embedded']['permissions']
                                        if isinstance(permissions, dict):
                                            user_count = len(permissions)
                                            workspace_user_counts[ws_id] = user_count
                                except Exception:
                                    pass
        else:
            # If bulk API didn't return a list, fall back to the basic workspace info
            if show_debug:
                print("Bulk API didn't return expected format.")
    except Exception as e:
        if show_debug:
            print(f"Error with workspace bulk fetch: {e}")
    
    end_time = time.time()
    if show_debug:
        print(f"Workspace fetching completed in {end_time - start_time:.2f} seconds")
    
    # Step 7: Identify top-level groups (no parent) or find the target group if specified
    if target_group_name:
        # Find the target group by name (case-insensitive)
        target_groups = [
            group for group_id, group in groups_by_id.items()
            if group.name.lower() == target_group_name.lower()
        ]
        
        if not target_groups:
            print(f"\nError: Group '{target_group_name}' not found.")
            # Try to suggest similar group names
            print("Available groups:")
            for group in sorted(groups_by_id.values(), key=lambda g: g.name):
                print(f"  - {group.name}")
            return
        
        # Use the target group as the starting point
        roots_to_print = target_groups
    else:
        # Use all top-level groups
        roots_to_print = [
            group for group_id, group in groups_by_id.items()
            if not hasattr(group, 'parentGroupId') or not group.parentGroupId
        ]
    
    # Define the print function with tree view and colors
    def print_tree(group, level=0, prefix="", is_last=True, is_root=False):
        # Get the appropriate color for this group level
        color_index = min(level, len(Colors.GROUP_COLORS) - 1)
        group_color = Colors.GROUP_COLORS[color_index]
        
        # Get user count
        user_count = group_user_counts.get(group.id, 0)
        
        # Print the group with its color and user count
        if is_root:
            print(f"{group_color}{group.name} ({user_count} users){Colors.RESET}")
        else:
            branch = Colors.TREE_CORNER if is_last else Colors.TREE_BRANCH
            print(f"{prefix}{branch}{group_color}{group.name} ({user_count} users){Colors.RESET}")
        
        # Prepare the prefix for children
        new_prefix = prefix
        if not is_root:
            new_prefix += Colors.TREE_SPACE if is_last else Colors.TREE_VERTICAL
        
        # Get all child items (workspaces and groups)
        workspace_ids = getattr(group, 'workspace_ids', [])
        child_group_ids = getattr(group, 'child_groups', [])
        
        # Sort workspaces alphabetically
        sorted_workspaces = []
        for ws_id in workspace_ids:
            ws = workspace_map.get(ws_id)
            if ws:
                sorted_workspaces.append(ws)
        sorted_workspaces.sort(key=lambda ws: ws.name)
        
        # Sort child groups alphabetically
        sorted_child_groups = []
        for child_id in child_group_ids:
            child = groups_by_id.get(child_id)
            if child:
                sorted_child_groups.append(child)
        sorted_child_groups.sort(key=lambda g: g.name)
        
        # Print workspaces
        for i, ws in enumerate(sorted_workspaces):
            is_last_workspace = (i == len(sorted_workspaces) - 1) and len(sorted_child_groups) == 0
            branch = Colors.TREE_CORNER if is_last_workspace else Colors.TREE_BRANCH
            ws_user_count = workspace_user_counts.get(ws.id, 0)
            print(f"{new_prefix}{branch}{Colors.WORKSPACE}{ws.name} ({ws_user_count} users){Colors.RESET}")
        
        # Print child groups recursively
        for i, child in enumerate(sorted_child_groups):
            is_last_group = (i == len(sorted_child_groups) - 1)
            print_tree(child, level + 1, new_prefix, is_last_group)

    # Print the hierarchy as a colorful tree
    print("\nWorkspace Hierarchy with User Counts:")
    if target_group_name:
        print(f"Showing hierarchy for group: {target_group_name}")
    
    sorted_roots = sorted(roots_to_print, key=lambda g: g.name)
    for i, group in enumerate(sorted_roots):
        is_last = (i == len(sorted_roots) - 1)
        # Make sure all roots (including the first one) are printed with tree characters
        print_tree(group, 0, "", is_last, is_root=False)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Print Airfocus workspace hierarchy with user counts')
    parser.add_argument('--group', '-g', type=str, help='Show hierarchy for a specific group (by name)')
    parser.add_argument('--debug', '-d', action='store_true', help='Show debug information during processing')
    args = parser.parse_args()
    
    # Initialize the Airfocus client
    client = AirfocusClient()
    
    # Run the main function with the target group name if provided
    print_group_hierarchy_with_users(client, args.group, args.debug)

if __name__ == "__main__":
    main()
