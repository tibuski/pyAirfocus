from airfocus.client import AirfocusClient

def debug_group_and_workspace_links(client):
    groups = client.workspaces.get_workspace_groups()
    workspaces = client.workspaces.get_workspaces(include_archived=True)

    print("Groups:")
    for group in groups:
        print(f"- Group: {group.name} (ID: {group.id}) | parentGroupId: {getattr(group, 'parentGroupId', None)}")

    print("\nWorkspaces:")
    for ws in workspaces:
        print(f"- Workspace: {ws.name} (ID: {ws.id}) | groupId: {getattr(ws, 'groupId', None)}")

if __name__ == "__main__":
    client = AirfocusClient()
    debug_group_and_workspace_links(client)
