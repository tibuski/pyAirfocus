from airfocus.client import AirfocusClient
from airfocus.constants import ENDPOINT_WORKSPACES_GROUPS_LIST
from airfocus.models.workspace import WorkspaceGroup

# ANSI color codes for terminal colors and text formatting
class Colors:
    # Text formatting
    RESET = "\033[0m"
    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    
    # Group level colors (different color per level)
    GROUP_COLORS = [
        "\033[1;36m",  # Level 0: Bold Cyan
        "\033[1;35m",  # Level 1: Bold Magenta
        "\033[1;33m",  # Level 2: Bold Yellow
        "\033[1;32m",  # Level 3: Bold Green
        "\033[1;34m",  # Level 4+: Bold Blue
    ]
    
    # Workspace color (light green with italic)
    WORKSPACE = "\033[3;92m"  # Italic Light green
    
    # Tree characters
    TREE_BRANCH = "├── "
    TREE_CORNER = "└── "
    TREE_VERTICAL = "│   "
    TREE_SPACE = "    "

def print_group_hierarchy_with_users(client):
    """
    Print the workspace group hierarchy with user counts as a colorful tree view.
    Uses efficient bulk API calls to minimize requests.
    """
    print("Fetching groups...")
    # Step 1: Get all workspace groups in a single API call (basic info only)
    all_groups = client.workspaces.get_workspace_groups()
    
    # Step 2: Get the IDs of all groups
    group_ids = [group.id for group in all_groups]
    
    # Step 3: Let's try to use the bulk API to get all groups in one call first
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
                                print(f"Group {group.name}: Found {user_count} users")
                        
                        group_user_counts[gid] = user_count
                except Exception as e:
                    print(f"Error processing group data: {e}")
        else:
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
                            print(f"Group {group.name}: Found {user_count} users")
                    
                    group_user_counts[gid] = user_count
                    
                except Exception as e:
                    print(f"Error fetching group {gid}: {e}")
    except Exception as e:
        print(f"Error with bulk group fetch: {e}")
        # Fall back to using the groups we already have
        groups_by_id = {group.id: group for group in all_groups}
        group_user_counts = {group.id: 0 for group in all_groups}
    
    # Step 4: Build the hierarchy (parent-child relationships)
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
    print("Collecting workspace IDs...")
    all_workspace_ids = set()
    for group_id, group in groups_by_id.items():
        all_workspace_ids.update(getattr(group, 'workspace_ids', []))
    
    # Step 6: Fetch all workspaces in a single API call using the efficient list endpoint
    print(f"Fetching {len(all_workspace_ids)} workspaces in a single API call...")
    workspace_map = client.workspaces.get_workspaces_by_ids(list(all_workspace_ids))
    
    # Step 7: Identify top-level groups (no parent)
    top_level_groups = [
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
            print(f"{new_prefix}{branch}{Colors.WORKSPACE}{ws.name}{Colors.RESET}")
        
        # Print child groups recursively
        for i, child in enumerate(sorted_child_groups):
            is_last_group = (i == len(sorted_child_groups) - 1)
            print_tree(child, level + 1, new_prefix, is_last_group)

    # Print the hierarchy as a colorful tree
    print("\nWorkspace Hierarchy with User Counts:")
    sorted_top_level_groups = sorted(top_level_groups, key=lambda g: g.name)
    for i, group in enumerate(sorted_top_level_groups):
        is_last = (i == len(sorted_top_level_groups) - 1)
        print_tree(group, 0, "", is_last, is_root=(i == 0))

if __name__ == "__main__":
    client = AirfocusClient()  # Make sure your .env is set up
    print_group_hierarchy_with_users(client)
