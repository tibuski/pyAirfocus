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


def main() -> None:
    token = get_token()
    with make_client(token) as client:
        logger.info("\n=== Getting workspaces with 'Sigma' filter ===")
        filtered_workspaces = get_workspaces(client, name_filter="Sigma")
        logger.info(f"Found {len(filtered_workspaces)} filtered workspaces:")
        for workspace in filtered_workspaces:
            name = workspace.get("name", "<no-name>")
            logger.info(f"  - {name}")
        
        # Process the filtered results (or fall back to all if none found)
        workspaces_to_process = filtered_workspaces if filtered_workspaces else all_workspaces
        logger.info(f"\n=== Processing {len(workspaces_to_process)} workspaces ===")
        
        for workspace in workspaces_to_process:
            name = workspace.get("name", "<no-name>")
            logger.info(name)

            workspace_id = workspace.get("id", "")
            items = get_items_by_workspace_id(client, workspace_id)
            for item in items:
                item_name = item.get("name", "<no-name>")
                logger.info(f"-- {item_name}")

                fields = item.get("fields") or {}
                for field_key, field_data in fields.items():
                    nested = field_data or {}
                    for attr_key, attr_value in nested.items():
                        logger.info(f"---- {attr_key} : {attr_value}")


if __name__ == "__main__":
    main()

