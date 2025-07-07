#!/usr/bin/env python
"""
Permission management tool for Airfocus workspaces and groups.

This script allows you to:
- Print current permissions on a workspace or group
- Apply permissions from a CSV file
- Print the resulting permissions

Usage:
    python manage_permissions.py [--workspace "WORKSPACE_NAME" or WORKSPACE_ID] [--group "GROUP_NAME" or GROUP_ID] [--file PERMISSIONS_FILE.csv]

Notes:
    - You can provide either the name (in quotes) or ID of the workspace/group
    - Workspace IDs typically start with "ws_" 
    - Group IDs typically start with "wsg_"
    - If multiple workspaces have the same name, the first one found will be used

Example CSV format:
    email,permission
    user1@example.com,full
    user2@example.com,write
    user3@example.com,comment
    user4@example.com,read
"""

import os
import csv
import sys
import argparse
import logging
import httpx
from typing import Dict, List, Optional, Any, Tuple
from dotenv import load_dotenv
from airfocus.client import AirfocusClient
from airfocus.constants import PERMISSION_LEVELS
from airfocus.endpoints.team import TeamEndpoints
from airfocus.endpoints.workspaces import WorkspacesEndpoints

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.ERROR,  # Change from WARNING to ERROR to hide warning logs
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def get_client() -> AirfocusClient:
    """Initialize and return the Airfocus client."""
    # The client will automatically read API_KEY from environment variables
    # which are loaded from .env file by load_dotenv() above
    return AirfocusClient()

def get_user_by_email(team_endpoints: TeamEndpoints, email: str) -> Optional[Dict[str, Any]]:
    """Find a user by email."""
    all_users = team_endpoints.get_users()
    for user in all_users:
        if user.email.lower() == email.lower():
            return {
                "userId": user.userId,
                "email": user.email,
                "fullName": user.fullName,
                "role": user.role
            }
    return None

def get_workspace_permissions(client: AirfocusClient, workspace_id: str) -> List[Dict[str, Any]]:
    """Get current permissions for a workspace."""
    try:
        data = client.get(f"/workspaces/{workspace_id}/permissions")
        if not isinstance(data, list):
            logger.warning(f"Unexpected response format for workspace permissions: {data}")
            return []
        return data
    except Exception as e:
        logger.error(f"Error getting workspace permissions: {e}")
        return []

def get_group_permissions(client: AirfocusClient, group_id: str) -> List[Dict[str, Any]]:
    """Get current permissions for a workspace group.
    
    Group permissions are not available through a dedicated permissions endpoint like workspaces.
    Instead, we need to get the group details and extract the user permissions from there.
    """
    try:
        group_data = client.get(f"/workspaces/groups/{group_id}")
        permissions = []
        # Extract permissions from _embedded['permissions'] as a dict of userId: permission
        if isinstance(group_data, dict) and '_embedded' in group_data:
            embedded = group_data['_embedded']
            if 'permissions' in embedded and isinstance(embedded['permissions'], dict):
                for user_id, permission in embedded['permissions'].items():
                    permissions.append({
                        'userId': user_id,
                        'permission': permission
                    })
            return permissions
        return permissions
    except Exception as e:
        print(f"Error getting group permissions: {e}")
        return []

def set_workspace_permission(client: AirfocusClient, workspace_id: str, user_id: str, permission: str) -> bool:
    """Set permission for a user on a workspace."""
    if permission not in PERMISSION_LEVELS:
        logger.error(f"Invalid permission: {permission}. Must be one of: {', '.join(PERMISSION_LEVELS)}")
        return False
    
    try:
        data = client.put(f"/workspaces/{workspace_id}/permissions", json={
            "userId": user_id,
            "permission": permission
        })
        logger.info(f"Set permission on workspace {workspace_id} for user {user_id} to {permission}")
        return True
    except Exception as e:
        logger.error(f"Error setting workspace permission: {e}")
        return False

def set_group_permission(client: AirfocusClient, group_id: str, user_id: str, permission: str) -> bool:
    """Set permission for a user on a workspace group."""
    if permission not in PERMISSION_LEVELS:
        logger.error(f"Invalid permission: {permission}. Must be one of: {', '.join(PERMISSION_LEVELS)}")
        return False
    
    try:
        # According to the OpenAPI spec, the format is {"permissions": {userId: permission}}
        endpoint = f"/workspaces/groups/{group_id}/permissions"
        url = f"{client.base_url}{endpoint}"
        
        # Use httpx directly to avoid JSON parsing of a 204 No Content response
        with httpx.Client(verify=client.verify_ssl) as http_client:
            # Print the request payload for debugging
            print(f"Setting permission: User {user_id} to {permission} on group {group_id}")
            
            # Use the correct JSON structure according to the OpenAPI spec
            response = http_client.post(
                url,
                headers=client.headers,
                json={"permissions": {user_id: permission}},
                timeout=client.timeout
            )
            
            # Check if the request was successful (no need to parse JSON for 204 response)
            if response.status_code >= 200 and response.status_code < 300:
                print(f"Successfully set permission for user {user_id} to {permission}")
                return True
            else:
                print(f"Failed to set permission: HTTP {response.status_code} - {response.text}")
                return False
    except Exception as e:
        print(f"Error setting group permission: {e}")
        return False

def delete_workspace_permission(client: AirfocusClient, workspace_id: str, user_id: str) -> bool:
    """Delete permission for a user on a workspace."""
    try:
        client.delete(f"/workspaces/{workspace_id}/permissions/{user_id}")
        logger.info(f"Deleted permission on workspace {workspace_id} for user {user_id}")
        return True
    except Exception as e:
        logger.error(f"Error deleting workspace permission: {e}")
        return False

def delete_group_permission(client: AirfocusClient, group_id: str, user_id: str) -> bool:
    """Delete permission for a user on a workspace group."""
    try:
        client.delete(f"/workspaces/groups/{group_id}/permissions/{user_id}")
        logger.info(f"Deleted permission on group {group_id} for user {user_id}")
        return True
    except Exception as e:
        logger.error(f"Error deleting group permission: {e}")
        return False

def read_permissions_from_csv(file_path: str) -> List[Dict[str, str]]:
    """Read permissions from a CSV file."""
    if not os.path.exists(file_path):
        logger.error(f"File not found: {file_path}")
        return []
    
    permissions = []
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            # Read raw content and clean it
            content = csvfile.read()
            # Print the raw content for debugging
            logger.debug(f"Raw CSV content: {content}")
            
            # Reset file pointer to beginning
            csvfile.seek(0)
            
            # Read the CSV with DictReader
            reader = csv.DictReader(csvfile)
            
            # Get the actual field names from the reader
            field_names = reader.fieldnames
            logger.debug(f"CSV field names: {field_names}")
            
            # Find the email and permission column names (case insensitive, ignore whitespace)
            email_col = None
            perm_col = None
            
            for field in field_names:
                if field.strip().lower() == 'email':
                    email_col = field
                elif field.strip().lower() == 'permission':
                    perm_col = field
            
            # If we couldn't find the columns, try one more approach
            if not email_col or not perm_col:
                # This is a fallback - assume first column is email, second is permission
                if len(field_names) >= 2:
                    email_col = field_names[0]
                    perm_col = field_names[1]
                    logger.warning(f"CSV headers not found. Using first column '{email_col}' for email and second column '{perm_col}' for permission")
                else:
                    logger.error("CSV does not have enough columns")
                    return []
            
            # Reset file pointer again and skip header
            csvfile.seek(0)
            next(csvfile)  # Skip header line
            
            # Read each line manually
            for line in csvfile:
                line = line.strip()
                if not line:
                    continue
                
                parts = line.split(',')
                if len(parts) < 2:
                    logger.warning(f"Skipping invalid line: {line}")
                    continue
                
                email = parts[0].strip()
                permission = parts[1].strip().lower()
                
                if not email:
                    logger.warning(f"Skipping row with empty email: {line}")
                    continue
                
                if permission not in PERMISSION_LEVELS:
                    logger.warning(f"Invalid permission '{permission}' for user {email}. Must be one of: {', '.join(PERMISSION_LEVELS)}")
                    continue
                
                permissions.append({
                    'email': email,
                    'permission': permission
                })
                logger.info(f"Added permission entry: {email} -> {permission}")
    except Exception as e:
        logger.error(f"Error reading CSV file: {e}")
    
    return permissions

def print_permissions(permissions: List[Dict[str, Any]], users_by_id: Dict[str, Dict[str, Any]], label: str, entity_name: str = "") -> None:
    """Print permissions in a formatted table with user emails and entity name, hiding IDs."""
    if not permissions:
        print(f"\n{label} for {entity_name} - No permissions found")
        return
    print(f"\n{label} for {entity_name}")
    print("-" * 80)
    print(f"{'Email':<40} | {'Name':<30} | {'Permission':<10}")
    print("-" * 80)
    for perm in permissions:
        user_id = perm.get('userId', '')
        user_info = users_by_id.get(user_id, {})
        email = user_info.get('email', 'Unknown')
        name = user_info.get('fullName', 'Unknown')
        permission = perm.get('permission', 'Unknown')
        print(f"{email:<40} | {name:<30} | {permission:<10}")
    print("-" * 80)

def apply_permissions(
    client: AirfocusClient,
    team_endpoints: TeamEndpoints,
    permissions_to_apply: List[Dict[str, str]],
    workspace_id: Optional[str] = None,
    group_id: Optional[str] = None
) -> Tuple[int, int, int]:
    """
    Apply permissions from the CSV file.
    
    Returns:
        Tuple[int, int, int]: (added, updated, failed) counts
    """
    if not workspace_id and not group_id:
        logger.error("Either workspace_id or group_id must be provided")
        return 0, 0, 0
    
    # Get current permissions
    current_permissions = []
    if workspace_id:
        current_permissions = get_workspace_permissions(client, workspace_id)
    else:
        current_permissions = get_group_permissions(client, group_id)
    
    # Build a map of current permissions by user ID
    current_perms_by_user_id = {perm['userId']: perm for perm in current_permissions}
    
    added = 0
    updated = 0
    failed = 0
    
    for perm_data in permissions_to_apply:
        email = perm_data['email']
        permission = perm_data['permission']
        
        # Find the user by email
        user = get_user_by_email(team_endpoints, email)
        if not user:
            logger.warning(f"User not found with email: {email}")
            failed += 1
            continue
        
        user_id = user['userId']
        success = False
        
        if user_id in current_perms_by_user_id:
            # User already has permission, update it if different
            current_permission = current_perms_by_user_id[user_id]['permission']
            if current_permission != permission:
                if workspace_id:
                    success = set_workspace_permission(client, workspace_id, user_id, permission)
                else:
                    success = set_group_permission(client, group_id, user_id, permission)
                
                if success:
                    updated += 1
                else:
                    failed += 1
            else:
                # Permission already matches, nothing to do
                logger.info(f"User {email} already has {permission} permission, no change needed")
                updated += 1  # Count as updated even though no change was needed
        else:
            # User doesn't have permission yet, add it
            if workspace_id:
                success = set_workspace_permission(client, workspace_id, user_id, permission)
            else:
                success = set_group_permission(client, group_id, user_id, permission)
            
            if success:
                added += 1
            else:
                failed += 1
    
    return added, updated, failed

def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description='Manage permissions for Airfocus workspaces and groups')
    parser.add_argument('--workspace', help='Workspace name (in quotes) or ID to manage permissions for')
    parser.add_argument('--group', help='Group name (in quotes) or ID to manage permissions for')
    parser.add_argument('--file', help='Path to CSV file with permissions to apply')
    
    args = parser.parse_args()
    
    if not args.workspace and not args.group:
        parser.error("Either --workspace or --group must be specified")
    
    if args.workspace and args.group:
        parser.error("Only one of --workspace or --group can be specified")
    
    try:
        # Initialize client and endpoints
        client = get_client()
        team_endpoints = TeamEndpoints(client)
        workspaces_endpoints = WorkspacesEndpoints(client)
        
        # Get all users for reference
        all_users = team_endpoints.get_users()
        users_by_id = {user.userId: {
            'userId': user.userId,
            'email': user.email,
            'fullName': user.fullName,
            'role': user.role
        } for user in all_users}
        
        # Determine which entity we're working with and resolve ID if name is provided
        entity_type = "Workspace" if args.workspace else "Group"
        entity_id = None
        entity_name = None
        
        if entity_type == "Workspace":
            # Check if input is a name or ID
            if args.workspace.startswith("ws_"):
                # Input looks like an ID
                entity_id = args.workspace
                # Verify workspace exists
                workspace = workspaces_endpoints.get_workspace(entity_id)
                if not workspace:
                    logger.error(f"Workspace not found with ID: {entity_id}")
                    return 1
                entity_name = workspace.name
            else:
                # Input is a name, search for the workspace
                workspaces = workspaces_endpoints.search_workspaces(name=args.workspace)
                if not workspaces or not workspaces.items:
                    logger.error(f"No workspace found with name: {args.workspace}")
                    return 1
                if len(workspaces.items) > 1:
                    logger.warning(f"Multiple workspaces found with name: {args.workspace}. Using the first one.")
                    for idx, ws in enumerate(workspaces.items):
                        logger.info(f"  {idx+1}. {ws.name} (ID: {ws.workspaceId})")
                
                workspace = workspaces.items[0]
                entity_id = workspace.workspaceId
                entity_name = workspace.name
                logger.info(f"Resolved workspace name '{args.workspace}' to ID: {entity_id}")
        else:
            # For groups, try to get it from the hierarchy
            groups_by_id, _ = workspaces_endpoints.get_group_hierarchy()
            
            if args.group.startswith("wsg_"):
                # Input looks like an ID
                entity_id = args.group
                if entity_id not in groups_by_id:
                    logger.error(f"Group not found with ID: {entity_id}")
                    return 1
                entity_name = groups_by_id[entity_id].name
            else:
                # Input is a name, search for the group
                found = False
                for group_id, group in groups_by_id.items():
                    if group.name == args.group:
                        entity_id = group_id
                        entity_name = group.name
                        found = True
                        logger.info(f"Resolved group name '{args.group}' to ID: {entity_id}")
                        break
                
                if not found:
                    logger.error(f"No group found with name: {args.group}")
                    return 1
        
        print(f"\n{entity_type}: {entity_name}")
        
        # Get current permissions
        current_permissions = []
        if entity_type == "Workspace":
            current_permissions = get_workspace_permissions(client, entity_id)
        else:
            current_permissions = get_group_permissions(client, entity_id)
        
        # Print current permissions (no IDs)
        print_permissions(current_permissions, users_by_id, "Current Permissions", entity_name)
        
        # If file is provided, read and apply permissions
        if args.file:
            permissions_to_apply = read_permissions_from_csv(args.file)
            
            if not permissions_to_apply:
                logger.error(f"No valid permissions found in file: {args.file}")
                return 1
            
            # Simplify logs to only show what we're applying
            print(f"\nApplying permissions from: {args.file}")
            print(f"Found {len(permissions_to_apply)} permission entries to apply")
            
            # Apply permissions
            added, updated, failed = apply_permissions(
                client,
                team_endpoints,
                permissions_to_apply,
                workspace_id=entity_id if entity_type == "Workspace" else None,
                group_id=entity_id if entity_type == "Group" else None
            )
            
            print(f"\nPermission updates summary:")
            print(f"  Added: {added}")
            print(f"  Updated: {updated}")
            print(f"  Failed: {failed}")
            
            # Get updated permissions
            updated_permissions = []
            if entity_type == "Workspace":
                updated_permissions = get_workspace_permissions(client, entity_id)
            else:
                updated_permissions = get_group_permissions(client, entity_id)
            
            # Print updated permissions (no IDs)
            print_permissions(updated_permissions, users_by_id, "Updated Permissions", entity_name)
        
        return 0
    
    except Exception as e:
        # Hide traceback and only show the error message
        logger.error(f"Error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())