from airfocus.client import AirfocusClient
import time

def print_group_hierarchy_with_users(client):
    """
    Print the workspace group hierarchy with user counts for each group and workspace.
    Uses efficient API calls to minimize requests.
    """
    print("Fetching groups...")
    # Step 1: Get all workspace groups in a single API call
    all_groups = client.workspaces.get_workspace_groups()
    
    # Create lookup dictionary for groups
    groups_by_id = {group.id: group for group in all_groups}
    
    # Step 2: Build the hierarchy (parent-child relationships)
    print("Building group hierarchy...")
    # Initialize child_groups lists for all groups
    for group in all_groups:
        if not hasattr(group, 'child_groups'):
            group.child_groups = []
        if not hasattr(group, 'workspace_ids'):
            group.workspace_ids = []
    
    # Set up parent-child relationships
    for group in all_groups:
        if hasattr(group, 'parentGroupId') and group.parentGroupId:
            parent_id = group.parentGroupId
            if parent_id in groups_by_id:
                parent = groups_by_id[parent_id]
                if not hasattr(parent, 'child_groups'):
                    parent.child_groups = []
                parent.child_groups.append(group.id)
        
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
    
    # Step 3: Collect all workspace IDs referenced in any group
    print("Collecting workspace IDs...")
    all_workspace_ids = set()
    for group in all_groups:
        all_workspace_ids.update(getattr(group, 'workspace_ids', []))
    
    # Step 4: Fetch all workspaces in a single API call using the efficient list endpoint
    print(f"Fetching {len(all_workspace_ids)} workspaces in a single API call...")
    workspace_map = client.workspaces.get_workspaces_by_ids(list(all_workspace_ids))
    
    # Step 5: Fetch team users
    print("Fetching team users...")
    team_users = client.team.get_users()
    
    # Step 6: Get workspace permissions to determine user counts
    print("Getting workspace permissions...")
    workspace_user_counts = {}
    group_user_counts = {}
    
    # Initialize all counts to 0
    for ws_id in all_workspace_ids:
        workspace_user_counts[ws_id] = 0
    
    for group in all_groups:
        group_user_counts[group.id] = 0
    
    # We need to make API calls to get permissions for each workspace
    # Let's use the client's method to get workspace permissions
    for ws_id in all_workspace_ids:
        try:
            # Fetch permissions for this workspace - this is a custom endpoint we'll add
            permissions = client.get(f"/workspaces/{ws_id}/permissions")
            
            if isinstance(permissions, dict) and "items" in permissions:
                # Count unique users with access to this workspace
                workspace_user_counts[ws_id] = len(permissions["items"])
            elif isinstance(permissions, list):
                workspace_user_counts[ws_id] = len(permissions)
            else:
                workspace_user_counts[ws_id] = 0
                
        except Exception as e:
            print(f"  Error getting permissions for workspace {ws_id}: {str(e)}")
            workspace_user_counts[ws_id] = 0
            
    # Calculate group user counts (sum of all workspaces in the group)
    for group in all_groups:
        user_count = 0
        workspace_ids = getattr(group, 'workspace_ids', [])
        for ws_id in workspace_ids:
            user_count += workspace_user_counts.get(ws_id, 0)
        group_user_counts[group.id] = user_count
    
    # Identify top-level groups (no parent)
    top_level_groups = [
        group for group in all_groups 
        if not hasattr(group, 'parentGroupId') or not group.parentGroupId
    ]
    
    # Define the print function
    def print_group(group, indent=0):
        user_count = group_user_counts.get(group.id, 0)
        print("  " * indent + f"- Group: {group.name} ({user_count} users)")
        
        # Print workspaces in this group
        workspace_ids = getattr(group, 'workspace_ids', [])
        if workspace_ids:
            for ws_id in workspace_ids:
                ws = workspace_map.get(ws_id)
                if ws:
                    ws_user_count = workspace_user_counts.get(ws_id, 0)
                    print("  " * (indent + 1) + f"* Workspace: {ws.name} ({ws_user_count} users)")
                else:
                    print("  " * (indent + 1) + f"* Unknown Workspace ({workspace_user_counts.get(ws_id, 0)} users)")
        else:
            print("  " * (indent + 1) + "(No workspaces)")
        
        # Print child groups recursively
        child_group_ids = getattr(group, 'child_groups', [])
        sorted_child_ids = sorted(child_group_ids, 
                                key=lambda cid: groups_by_id[cid].name if cid in groups_by_id else "")
        for child_id in sorted_child_ids:
            child = groups_by_id.get(child_id)
            if child:
                print_group(child, indent + 1)

    # Print the hierarchy
    print("\nWorkspace Hierarchy with User Counts:")
    sorted_top_level_groups = sorted(top_level_groups, key=lambda g: g.name)
    for group in sorted_top_level_groups:
        print_group(group)

if __name__ == "__main__":
    client = AirfocusClient()  # Make sure your .env is set up
    print_group_hierarchy_with_users(client)
