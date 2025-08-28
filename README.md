# pyAirfocus

Advanced Python client for Airfocus API analysis - generates comprehensive field presence reports organized by workspace groups with status information.

## Features

- **Field Presence Analysis**: Analyzes which fields are populated (True/False) across all items
- **Workspace Group Organization**: Automatically organizes results by workspace groups
- **Status Information**: Includes human-readable status names for each item
- **Comprehensive Filtering**: Filter by workspace name or workspace group name
- **Performance Optimized**: Minimizes API calls through intelligent data gathering
- **Configurable**: Customizable ignored fields and output options
- **Rich Statistics**: Provides workspace-level and global totals

## Output Structure

The tool generates a JSON file (`field_statuses.json`) with the following structure:

```json
{
  "Group Name": {
    "Workspace Name": {
      "Item Name": {
        "Field Name 1": true,
        "Field Name 2": false,
        "_status": "In Progress"
      },
      "_WORKSPACE_TOTALS": {
        "total_true_fields": 150,
        "total_false_fields": 75,
        "total_items": 25,
        "total_unique_fields": 8,
        "ignored_fields": ["mirror target", "insights"]
      }
    }
  },
  "_GLOBAL_TOTALS": {
    "total_true_fields": 4010,
    "total_false_fields": 37075,
    "total_items": 1245,
    "total_workspaces": 28,
    "total_unique_fields": 33,
    "ignored_fields": ["mirror target", "insights"]
  }
}
```

## Requirements
- Python 3.10+
- Dependencies listed in `requirements.txt`

## Installation
```bash
# Clone the repo
git clone <your-repo-url> && cd pyAirfocus

# (Optional) Create and activate a virtual environment
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows (PowerShell)
.venv\\Scripts\\Activate.ps1

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

## Configuration
The script expects configuration in two places:

### 1. Environment Variable
Set `AIRFOCUS_KEY` to your API token (see instructions below)

### 2. Constants File
Create a `constants.py` file with:

```python
# constants.py
URL = "https://app.airfocus.com/api"  # Note: /api endpoint, not root URL
IGNORED_FIELDS = [
    "mirror target",
    "insights"
]
```

The `IGNORED_FIELDS` list allows you to exclude certain fields from the analysis. Fields in this list will not appear in the output or be counted in statistics.

## Set the environment variable from the command line

### Windows (PowerShell)
```powershell
# Current session only
$env:AIRFOCUS_KEY = "<your_api_token_here>"

# Persist for your user (requires a new shell to take effect)
[Environment]::SetEnvironmentVariable("AIRFOCUS_KEY", "<your_api_token_here>", "User")
```

### Windows (Command Prompt / cmd.exe)
```bat
REM Current session only
set AIRFOCUS_KEY=<your_api_token_here>

REM Persist for your user
setx AIRFOCUS_KEY "<your_api_token_here>"
```

### Linux/macOS (bash/zsh)
```bash
# Current shell session only
export AIRFOCUS_KEY="<your_api_token_here>"

# Persist by adding to your shell profile
# For bash:
echo 'export AIRFOCUS_KEY="<your_api_token_here>"' >> ~/.bashrc && source ~/.bashrc
# For zsh:
echo 'export AIRFOCUS_KEY="<your_api_token_here>"' >> ~/.zshrc && source ~/.zshrc
```

## Usage

The script provides command-line options. Running with no arguments shows the help.

### Show help
```bash
python main.py
```

### Options
- `--workspace-filter TEXT`: Filter workspaces whose name contains TEXT (partial match)
- `--group-filter TEXT`: Filter workspaces whose group name contains TEXT (partial match; use `<no-group>` for ungrouped)
- `-o, --output FILE`: Output JSON file (default: `field_statuses.json`)

### Examples
```bash
# Partial match by workspace name
python main.py --workspace-filter alpha

# Partial match by group name
python main.py --group-filter product

# Combine both filters and set custom output filename
python main.py --workspace-filter alpha --group-filter product --output result.json
```

### Output

The script generates:
- **Console output**: Progress information and statistics
- **field_statuses.json**: Complete field presence analysis

### Typical Output Statistics
```
INFO:__main__:Found 28 filtered workspaces
INFO:__main__:Loaded 19 workspace groups covering 71 workspaces  
INFO:__main__:Data gathering complete. Processing 28 workspaces with 33 unique fields...
INFO:__main__:Field presence data saved to field_statuses.json
```

## Run

```

## API Functions

The tool provides several key functions for interacting with the Airfocus API:

### Core Functions

- **`get_workspaces()`**: Retrieve workspaces with optional filtering by name or group
- **`get_workspace_groups()`**: Load workspace group mappings
- **`get_all_fields()`**: Load field definitions and selection options
- **`get_items_by_workspace_id()`**: Retrieve all items from a specific workspace
- **`get_workspace_statuses_from_embedded()`**: Extract status mappings from workspace data
- **`create_field_statuses_json()`**: Generate the complete field presence analysis

### Filtering Options (Programmatic)

- **Workspace Name Filter**: `name_filter="alpha"` - matches workspaces containing "alpha" (partial match)
- **Group Name Filter**: `group_name_filter="product"` - matches workspaces in groups containing "product" (partial match)
- **Case Sensitivity**: `case_sensitive=True` - enables exact case matching
- **Combined Filters**: Use both name and group filters together

### Example Usage

```python
# Get all workspaces in groups containing "product"
workspaces = get_workspaces(client, group_name_filter="product")

# Get workspaces with "alpha" in the name from groups containing "product"
workspaces = get_workspaces(client, name_filter="alpha", group_name_filter="product")

# Generate field analysis with custom ignored fields
ignored = ["mirror target", "insights", "internal notes"]
result = create_field_statuses_json(client, field_mapping, workspaces, ignored)
```

## Notes

### Performance & API Optimization
- **Efficient API Usage**: The client minimizes API calls by gathering data in batches
- **Status Extraction**: Status names are extracted from workspace embedded data (no additional API calls)
- **Single HTTP Client**: Uses one `httpx.Client` instance with appropriate timeouts
- **Smart Caching**: Field mappings and workspace groups are loaded once per execution

### Data Processing
- **Field Presence Logic**: A field is considered "present" (True) if it has any non-empty, non-null values
- **Status Integration**: Each item includes a `_status` field with the human-readable status name
- **Group Organization**: Workspaces are automatically organized by their group membership
- **Flexible Filtering**: Support for workspace name, group name, and case sensitivity options

### Output Details
- **Hierarchical Structure**: Group → Workspace → Items → Fields
- **Comprehensive Totals**: Both workspace-level and global statistics
- **UTF-8 Encoding**: Proper handling of international characters
- **JSON Format**: Human-readable with proper indentation

### Error Handling
- **Missing Environment Variables**: Clear error messages if `AIRFOCUS_KEY` is not set
- **API Failures**: Graceful handling of network and API errors
- **Missing Data**: Safe handling of workspaces without groups or items without statuses

### Security
- **SSL Verification**: Currently disabled for corporate network compatibility (`verify=False`)
- **Token Security**: API token is loaded from environment variable (not hardcoded)

### Logging
- **INFO Level**: Progress information and statistics are logged
- **DEBUG Level**: Detailed API request/response information (can be enabled by changing log level)

If the environment variable is not set, the script will exit with an error message.