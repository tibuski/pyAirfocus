import httpx
import logging
import os
import sys
from typing import Any, Dict, List

from constants import URL


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


def get_workspaces(client: httpx.Client, name_filter: str = None, case_sensitive: bool = False) -> List[Dict[str, Any]]:
    """
    Get workspaces, optionally filtered by name containing a specific string.
    
    Args:
        client: HTTP client configured with authentication
        name_filter: Optional string to filter workspace names (case-insensitive by default)
        case_sensitive: Whether the name filter should be case-sensitive
        
    Returns:
        List of workspace dictionaries matching the filter criteria
    """
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
    return response.json().get("items", [])


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


def main() -> None:
    token = get_token()
    with make_client(token) as client:
        # First, load all field mappings and selection options
        logger.info("=== Loading field mappings ===")
        field_id_to_name, field_selections = get_all_fields(client)
        
        logger.info("\n=== Getting workspaces with filter ===")
        filtered_workspaces = get_workspaces(client, name_filter="Phi")
        logger.info(f"Found {len(filtered_workspaces)} filtered workspaces:")
        for workspace in filtered_workspaces:
            name = workspace.get("name", "<no-name>")
            logger.info(f"  - {name}")
        
        # Process the filtered results (or fall back to all if none found)
        if not filtered_workspaces:
            logger.info("No filtered workspaces found, getting all workspaces...")
            filtered_workspaces = get_workspaces(client)
        
        logger.info(f"\n=== Processing {len(filtered_workspaces)} workspaces ===")
        
        for workspace in filtered_workspaces:
            name = workspace.get("name", "<no-name>")
            logger.info(name)

            workspace_id = workspace.get("id", "")
            items = get_items_by_workspace_id(client, workspace_id)
            for item in items:
                item_name = item.get("name", "<no-name>")
                logger.info(f"-- {item_name}")

                fields = item.get("fields") or {}
                for field_id, field_data in fields.items():
                    # Get the human-readable field name from our mapping
                    field_name = field_id_to_name.get(field_id, "Unknown Field")
                    logger.info(f"--- Field: {field_name} [{field_id}]")
                    
                    nested = field_data or {}
                    for attr_key, attr_value in nested.items():
                        # Check if this field has selection options and the attribute contains selection IDs
                        if field_id in field_selections and attr_key == "selection":
                            # attr_value could be a single ID or a list of IDs for multi-select
                            if isinstance(attr_value, list):
                                # Multi-select field
                                selection_names = []
                                for selection_id in attr_value:
                                    selection_name = field_selections[field_id].get(selection_id, f"Unknown ({selection_id})")
                                    selection_names.append(selection_name)
                                logger.info(f"---- {attr_key} : {selection_names}")
                            else:
                                # Single-select field
                                selection_name = field_selections[field_id].get(attr_value, f"Unknown ({attr_value})")
                                logger.info(f"---- {attr_key} : {selection_name}")
                        else:
                            # Regular attribute
                            logger.info(f"---- {attr_key} : {attr_value}")


if __name__ == "__main__":
    main()

