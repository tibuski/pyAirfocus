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
    )


def post_api(client: httpx.Client, endpoint: str, data: Dict[str, Any]) -> httpx.Response:
    response = client.post(endpoint, json=data)
    response.raise_for_status()
    return response


def get_workspaces(client: httpx.Client) -> List[Dict[str, Any]]:
    response = post_api(client, "workspaces/search", {})
    return response.json().get("items", [])


def get_items_by_workspace_id(client: httpx.Client, workspace_id: str) -> List[Dict[str, Any]]:
    response = post_api(client, f"workspaces/{workspace_id}/items/search", {})
    return response.json().get("items", [])


def main() -> None:
    token = get_token()
    with make_client(token) as client:
        all_workspaces = get_workspaces(client)
        for workspace in all_workspaces:
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

