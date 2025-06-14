"""
Constants used throughout the pyAirfocus library.
"""

# API Configuration
BASE_URL = "https://app.airfocus.com/api"
DEFAULT_TIMEOUT = 30

# User Roles
SUPPORTED_ROLES = ["admin", "editor", "contributor", "viewer"]

# Permission Levels
PERMISSION_LEVELS = ["admin", "editor", "viewer"]

# HTTP Status Codes
HTTP_OK = 200
HTTP_CREATED = 201
HTTP_NO_CONTENT = 204
HTTP_BAD_REQUEST = 400
HTTP_UNAUTHORIZED = 401
HTTP_FORBIDDEN = 403
HTTP_NOT_FOUND = 404
HTTP_INTERNAL_SERVER_ERROR = 500

# Environment Variables
ENV_API_KEY = "AIRFOCUS_API_KEY"
ENV_VERIFY_SSL = "VERIFY_SSL"

# API Endpoints
ENDPOINT_TEAM = "/team"
ENDPOINT_TEAM_USERS = "/team/users"
ENDPOINT_WORKSPACES = "/workspaces"
ENDPOINT_WORKSPACES_SEARCH = "/workspaces/search"
ENDPOINT_WORKSPACES_GROUPS = "/workspaces/groups"
ENDPOINT_WORKSPACES_GROUPS_SEARCH = "/workspaces/groups/search"

# Response Fields
FIELD_ITEMS = "items"
FIELD_DATA = "data"
FIELD_WORKSPACES = "workspaces"
FIELD_GROUPS = "groups"
FIELD_EMBEDDED = "_embedded"
FIELD_WORKSPACE_IDS = "workspaceIds"

# Error Messages
ERROR_API_KEY_REQUIRED = "API key is required. Set it in .env file or pass to constructor."
ERROR_WORKSPACE_NOT_FOUND = "Workspace not found"
ERROR_GROUP_NOT_FOUND = "Workspace group not found"
ERROR_USER_NOT_FOUND = "User not found" 