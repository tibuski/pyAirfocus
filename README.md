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
# (Optional) Create and activate a virtual environment
python -m venv .

# Linux/macOS
source ./bin/activate

# Windows (PowerShell)
.\Scripts\Activate.ps1

# Install dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Configuration
The script expects configuration in two places:

### 1. Environment Variable
Set `AIRFOCUS_KEY` to your API token (see instructions below)

### 2. Constants File
Modify the `constants.py` file with:

```python
# constants.py

# Airfocus API Url. Documentation at https://developer.airfocus.com
URL = "https://app.airfocus.com/api"

# Field names to ignore when processing data (case-insensitive)
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