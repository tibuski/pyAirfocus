import httpx
import logging
import os
import sys
import json
from typing import Any, Dict, List

from constants import URL, IGNORED_FIELDS


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_token() -> str:
    token = os.getenv("AIRFOCUS_KEY")
    if not token:
        logger.error("Environment variable AIRFOCUS_KEY needs to be set")
        sys.exit(1)
    return token


def make_client(token: str) -> httpx.Client:
    return httpx.Client(
        base_url=URL,
        headers={"Authorization": f"Bearer {token}", "Accept": "application/json"},
        timeout=httpx.Timeout(10.0, read=30.0),
        # Add to disable SSL verification to make it work from work ...
        verify=False,
    )


def post_api(client: httpx.Client, endpoint: str, data: Dict[str, Any]) -> httpx.Response:
    logger.debug(f"Making POST request to {endpoint} with data: {data}")
    response = client.post(endpoint, json=data)
    logger.debug(f"Response status: {response.status_code}")
    logger.debug(f"Response content: {response.text[:500]}...")  # First 500 chars
    response.raise_for_status()
    return response


def get_workspaces(client: httpx.Client, name_filter: str = None, group_name_filter: str = None, case_sensitive: bool = False) -> List[Dict[str, Any]]:
    """
    Get workspaces, optionally filtered by name or workspace group name containing a specific string.
    
    Args:
        client: HTTP client configured with authentication
        name_filter: Optional string to filter workspace names (case-insensitive by default)
        group_name_filter: Optional string to filter workspace group names (case-insensitive by default)
        case_sensitive: Whether the filters should be case-sensitive
        
    Returns:
        List of workspace dictionaries matching the filter criteria
        
    Examples:
        # Get all workspaces
        workspaces = get_workspaces(client)
        
        # Filter by workspace name containing "Crew"
        crew_workspaces = get_workspaces(client, name_filter="Crew")
        
        # Filter by workspace group name containing "Development"
        dev_workspaces = get_workspaces(client, group_name_filter="Development")
        
        # Filter by both workspace name AND group name
        specific_workspaces = get_workspaces(client, name_filter="Crew", group_name_filter="Dev")
        
        # Case-sensitive filtering
        exact_workspaces = get_workspaces(client, name_filter="CreW", case_sensitive=True)
        
        # Find workspaces that are not in any group
        ungrouped = get_workspaces(client, group_name_filter="<no-group>")
    """
    # Get workspace groups first if we need to filter by group name
    workspace_to_group = {}
    if group_name_filter:
        workspace_to_group = get_workspace_groups(client)
    
    # Base search query structure
    search_query = {
        "archived": False,
        "sort": {
            "type": "name",
            "direction": "asc"
        }
    }
    
    # Add name filter if provided
    if name_filter:
        search_query["filter"] = {
            "type": "and",
            "inner": [
                {
                    "type": "name",
                    "mode": "contain",
                    "text": name_filter,
                    "caseSensitive": case_sensitive
                }
            ]
        }
    
    response = post_api(client, "workspaces/search", search_query)
    workspaces = response.json().get("items", [])
    
    # Apply group name filter if provided
    if group_name_filter:
        filtered_workspaces = []
        filter_text = group_name_filter if case_sensitive else group_name_filter.lower()
        
        for workspace in workspaces:
            workspace_id = workspace.get("id", "")
            group_info = workspace_to_group.get(workspace_id)
            
            if group_info:
                group_name = group_info["group_name"]
                group_name_to_check = group_name if case_sensitive else group_name.lower()
                
                if filter_text in group_name_to_check:
                    filtered_workspaces.append(workspace)
            # Also include workspaces without groups if the filter might match "<no-group>"
            elif not case_sensitive and filter_text in "<no-group>":
                filtered_workspaces.append(workspace)
            elif case_sensitive and group_name_filter in "<no-group>":
                filtered_workspaces.append(workspace)
        
        return filtered_workspaces
    
    return workspaces


def get_items_by_workspace_id(client: httpx.Client, workspace_id: str) -> List[Dict[str, Any]]:
    response = post_api(client, f"workspaces/{workspace_id}/items/search", {})
    return response.json().get("items", [])


def get_all_fields(client: httpx.Client) -> tuple[Dict[str, str], Dict[str, Dict[str, str]]]:
    """
    Get all fields and return mappings for field names and selection options.
    
    Args:
        client: HTTP client configured with authentication
        
    Returns:
        Tuple of:
        - Dictionary mapping field IDs to field names
        - Dictionary mapping field IDs to their selection options (option_id -> option_name)
    """
    # Search for all fields (both team fields and workspace fields)
    search_query = {}
    response = post_api(client, "fields/search", search_query)
    fields = response.json().get("items", [])
    
    # Create mappings for field names and selection options
    field_mapping = {}
    selection_mapping = {}
    
    for field in fields:
        field_id = field.get("id")
        field_name = field.get("name", "<no-name>")
        field_type = field.get("typeId", "")
        
        if field_id:
            field_mapping[field_id] = field_name
            
            # If this is a select field, extract the selection options
            if field_type == "select":
                settings = field.get("settings", {})
                options = settings.get("options", [])
                
                option_mapping = {}
                for option in options:
                    option_id = option.get("id")
                    option_name = option.get("name", "<no-name>")
                    if option_id:
                        option_mapping[option_id] = option_name
                
                if option_mapping:
                    selection_mapping[field_id] = option_mapping
                    logger.debug(f"Field '{field_name}' has {len(option_mapping)} selection options")
    
    logger.info(f"Loaded {len(field_mapping)} field mappings and {len(selection_mapping)} selection fields")
    return field_mapping, selection_mapping


def get_workspace_statuses_from_embedded(workspace: Dict[str, Any]) -> Dict[str, str]:
    """
    Extract status mappings from workspace embedded data.
    
    Args:
        workspace: Workspace dictionary containing _embedded.statuses
        
    Returns:
        Dictionary mapping status IDs to status names
        
    Examples:
        # Extract status mappings from workspace data
        status_mapping = get_workspace_statuses_from_embedded(workspace)
        
        # Look up status name by ID
        status_name = status_mapping.get("status-456", "<unknown-status>")
        
        # Example output structure:
        # {
        #     "status-id-1": "To Do",
        #     "status-id-2": "In Progress", 
        #     "status-id-3": "Done"
        # }
    """
    status_mapping = {}
    
    # Get status data from embedded workspace information
    embedded = workspace.get("_embedded", {})
    statuses = embedded.get("statuses", {})
    
    # Create mapping of status ID to status name
    for status_id, status_data in statuses.items():
        status_name = status_data.get("name", "<no-name>")
        status_mapping[status_id] = status_name
    
    logger.debug(f"Extracted {len(status_mapping)} statuses from workspace {workspace.get('name', '<unknown>')}")
    return status_mapping


def create_field_statuses_json(client: httpx.Client, field_id_to_name: Dict[str, str], workspaces: List[Dict[str, Any]], ignored_field_names: List[str] = None) -> Dict[str, Any]:
    """
    Create a JSON structure showing field presence (True/False) for each item in each workspace, organized by workspace groups.
    
    Args:
        client: HTTP client configured with authentication
        field_id_to_name: Mapping of field IDs to field names
        workspaces: List of workspace dictionaries
        ignored_field_names: List of field names to ignore (case-insensitive)
        
    Returns:
        Dictionary with group -> workspace -> items -> fields structure
        
    Examples:
        # Basic usage with default ignored fields
        field_mapping, _ = get_all_fields(client)
        workspaces = get_workspaces(client, name_filter="Crew")
        result = create_field_statuses_json(client, field_mapping, workspaces)
        
        # Custom ignored fields
        custom_ignored = ["mirror target", "insights", "created by"]
        result = create_field_statuses_json(client, field_mapping, workspaces, custom_ignored)
        
        # Example output structure:
        # {
        #     "Development Team": {
        #         "Crew Athena": {
        #             "Item 1": {
        #                 "Field A": true,
        #                 "Field B": false
        #             },
        #             "_WORKSPACE_TOTALS": {
        #                 "total_true_fields": 150,
        #                 "total_false_fields": 75,
        #                 "total_items": 25
        #             }
        #         }
        #     },
        #     "<no-group>": {
        #         "Ungrouped Workspace": { ... }
        #     },
        #     "_GLOBAL_TOTALS": {
        #         "total_true_fields": 500,
        #         "total_false_fields": 300,
        #         "total_workspaces": 5
        #     }
        # }
    """
    if ignored_field_names is None:
        ignored_field_names = IGNORED_FIELDS  # Default ignored fields from constants
    
    # Get workspace groups mapping
    logger.info("Loading workspace groups...")
    workspace_to_group = get_workspace_groups(client)
    
    # Convert to lowercase for case-insensitive comparison
    ignored_field_names_lower = [name.lower() for name in ignored_field_names]
    
    result = {}
    
    # Initialize global totals
    global_true_count = 0
    global_false_count = 0
    global_total_items = 0
    global_workspace_count = 0
    
    # First, gather ALL data from ALL workspaces in a single pass
    logger.info("Gathering all workspace data...")
    workspace_data = {}  # workspace_id -> {name, items, status_mapping}
    all_field_names = set()
    
    for workspace in workspaces:
        workspace_name = workspace.get("name", "<no-name>")
        workspace_id = workspace.get("id", "")
        
        logger.info(f"Fetching data for workspace: {workspace_name}")
        items = get_items_by_workspace_id(client, workspace_id)
        
        # Get status mappings from embedded workspace data (no API call needed)
        status_mapping = get_workspace_statuses_from_embedded(workspace)
        
        workspace_data[workspace_id] = {
            "name": workspace_name,
            "items": items,
            "status_mapping": status_mapping
        }
        
        # Collect all field names from this workspace's items
        for item in items:
            fields = item.get("fields") or {}
            for field_id in fields.keys():
                field_name = field_id_to_name.get(field_id, "Unknown Field")
                # Skip ignored fields
                if field_name.lower() not in ignored_field_names_lower:
                    all_field_names.add(field_name)
    
    logger.info(f"Data gathering complete. Processing {len(workspace_data)} workspaces with {len(all_field_names)} unique fields...")
    
    # Organize workspaces by groups
    groups_structure = {}
    
    # Now process the gathered data locally (no more API calls)
    for workspace in workspaces:
        workspace_name = workspace.get("name", "<no-name>")
        workspace_id = workspace.get("id", "")
        
        # Get group information for this workspace
        group_info = workspace_to_group.get(workspace_id, {"group_name": "<no-group>", "group_id": None})
        group_name = group_info["group_name"]
        
        # Initialize group if not exists
        if group_name not in groups_structure:
            groups_structure[group_name] = {}
        
        # Get the items from our local data
        workspace_info = workspace_data[workspace_id]
        items = workspace_info["items"]
        status_mapping = workspace_info["status_mapping"]
        groups_structure[group_name][workspace_name] = {}
        
        # Initialize workspace totals
        workspace_true_count = 0
        workspace_false_count = 0
        
        # Count this workspace
        global_workspace_count += 1
        global_total_items += len(items)
        
        for item in items:
            item_name = item.get("name", "<no-name>")
            item_status_id = item.get("statusId", "")
            item_status_name = status_mapping.get(item_status_id, "<unknown-status>")
            fields = item.get("fields") or {}
            
            # Initialize all fields as False
            item_fields = {field_name: False for field_name in all_field_names}
            
            # Set to True for fields that have values
            for field_id, field_data in fields.items():
                field_name = field_id_to_name.get(field_id, "Unknown Field")
                
                # Skip ignored fields
                if field_name.lower() in ignored_field_names_lower:
                    continue
                
                # Check if field has any non-empty values
                has_value = False
                if field_data:
                    for attr_key, attr_value in field_data.items():
                        if attr_value is not None and attr_value != "" and attr_value != []:
                            has_value = True
                            break
                
                item_fields[field_name] = has_value
            
            # Add status information to the item
            item_fields["_status"] = item_status_name
            
            # Count True/False for workspace totals (excluding _status)
            for field_name, field_value in item_fields.items():
                if field_name != "_status":  # Don't count status in field statistics
                    if field_value:
                        workspace_true_count += 1
                        global_true_count += 1
                    else:
                        workspace_false_count += 1
                        global_false_count += 1
            
            groups_structure[group_name][workspace_name][item_name] = item_fields
        
        # Add workspace totals
        groups_structure[group_name][workspace_name]["_WORKSPACE_TOTALS"] = {
            "total_true_fields": workspace_true_count,
            "total_false_fields": workspace_false_count,
            "total_items": len(items),
            "total_unique_fields": len(all_field_names),
            "ignored_fields": ignored_field_names
        }
    
    # Copy the groups structure to result
    result = groups_structure
    
    # Add global totals at the end
    result["_GLOBAL_TOTALS"] = {
        "total_true_fields": global_true_count,
        "total_false_fields": global_false_count,
        "total_items": global_total_items,
        "total_workspaces": global_workspace_count,
        "total_unique_fields": len(all_field_names),
        "ignored_fields": ignored_field_names
    }
    
    return result


def get_workspace_groups(client: httpx.Client) -> Dict[str, Dict[str, Any]]:
    """
    Get all workspace groups and return a mapping of workspace IDs to group information.
    
    Args:
        client: HTTP client configured with authentication
        
    Returns:
        Dictionary mapping workspace IDs to their group information
        
    Examples:
        # Get workspace groups mapping
        workspace_to_group = get_workspace_groups(client)
        
        # Check if a workspace belongs to a group
        workspace_id = "workspace-123"
        if workspace_id in workspace_to_group:
            group_info = workspace_to_group[workspace_id]
            print(f"Workspace belongs to group: {group_info['group_name']}")
        else:
            print("Workspace is not in any group")
            
        # Example output structure:
        # {
        #     "workspace-id-1": {
        #         "group_id": "group-123",
        #         "group_name": "Development Team"
        #     },
        #     "workspace-id-2": {
        #         "group_id": "group-456", 
        #         "group_name": "Production Team"
        #     }
        # }
    """
    search_query = {}
    
    response = post_api(client, "workspaces/groups/search", search_query)
    groups = response.json().get("items", [])
    
    # Create mapping of workspace ID to group info
    workspace_to_group = {}
    
    for group in groups:
        group_id = group.get("id")
        group_name = group.get("name", "<no-group-name>")
        
        # Get workspace IDs from the embedded data
        embedded = group.get("_embedded", {})
        workspace_ids = embedded.get("workspaceIds", [])
        
        logger.debug(f"Processing group '{group_name}' with {len(workspace_ids)} workspaces")
        
        for workspace_id in workspace_ids:
            workspace_to_group[workspace_id] = {
                "group_id": group_id,
                "group_name": group_name
            }
    
    logger.info(f"Loaded {len(groups)} workspace groups covering {len(workspace_to_group)} workspaces")
    return workspace_to_group


def main() -> None:
    token = get_token()
    with make_client(token) as client:
        # First, load all field mappings and selection options
        logger.info("=== Loading field mappings ===")
        field_id_to_name, field_selections = get_all_fields(client)
        
        logger.info("\n=== Getting workspaces with filter ===")
        # You can filter by workspace name or workspace group name
        # First test: get all workspaces without filter to see basic functionality
        filtered_workspaces = get_workspaces(client, group_name_filter="Cluster CC")  # Filter by workspace name
        # Alternative: filter by group name instead
        # filtered_workspaces = get_workspaces(client, group_name_filter="Your Group Name")
        
        logger.info(f"Found {len(filtered_workspaces)} filtered workspaces:")
        for workspace in filtered_workspaces:
            name = workspace.get("name", "<no-name>")
            workspace_id = workspace.get("id", "<no-id>")
            logger.info(f"  - {name} (ID: {workspace_id})")
        
        # Process the filtered results (or fall back to all if none found)
        if not filtered_workspaces:
            logger.info("No filtered workspaces found, getting all workspaces...")
            filtered_workspaces = get_workspaces(client)
        
        # Create field presence JSON
        logger.info("\n=== Creating field presence JSON ===")
        # You can customize the ignored fields in constants.py or override here
        field_statuses_data = create_field_statuses_json(client, field_id_to_name, filtered_workspaces, IGNORED_FIELDS)
        
        # Save to JSON file
        output_file = "field_statuses.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(field_statuses_data, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Field presence data saved to {output_file}")
        
if __name__ == "__main__":
    main()

