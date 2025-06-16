# pyAirfocus

A Python client library and CLI tools for interacting with the Airfocus API.

## Overview

pyAirfocus is a Python package that provides a simple and intuitive interface for working with the Airfocus API. With this library, you can:

- Access Airfocus workspaces and their data
- Retrieve user information and activity data
- Programmatically interact with your Airfocus projects
- Manage workspace groups and hierarchies
- Handle user permissions and roles

## Features

- **Simple API Client**: Easy-to-use client for Airfocus API
- **User Management**: List and filter users by activity, roles, and more
- **Workspace Access**: Access and manage workspace data
- **Command-line Tools**: Utility scripts for common tasks (like listing user activity)
- **Data Validation**: Comprehensive input validation using Pydantic
- **Error Handling**: Robust error handling with specific exception types
- **Logging**: Configurable logging throughout the library
- **Type Safety**: Full type hints and validation

## Requirements

- Python 3.8 or higher
- pip (Python package manager)
- An Airfocus account with API access

## Installation

### Prerequisites

- Python 3.11 or higher
- Git

### Clone the Repository

#### Windows

```powershell
git clone https://github.com/tibuski/pyAirfocus.git
cd pyAirfocus
python -m venv .
.\Scripts\activate
python -m pip install -r requirements.txt
```

#### macOS/Linux

```bash
git clone https://github.com/tibuski/pyAirfocus.git
cd pyAirfocus
python -m venv .
source ./bin/activate
python -m pip install -r requirements.txt
```

## Configuration

1. Create a `.env` file in the root directory with your Airfocus API credentials:

```
AIRFOCUS_API_KEY=your_api_key_here
VERIFY_SSL=true
```

2. Ensure your `.env` file is not tracked by git (it's already in the `.gitignore` file).

## Usage

### Using the API Client

```python
from airfocus.client import AirfocusClient

# Initialize the client
client = AirfocusClient()

# Get all users
users = client.team.get_users()

# Get all workspaces
workspaces = client.workspaces.get_workspaces()

# Create a new workspace with validation
try:
    new_workspace = client.workspaces.create_workspace(
        name="My New Workspace",
        description="A test workspace",
        order=1
    )
    print(f"Created workspace: {new_workspace.name}")
except ValueError as e:
    print(f"Validation error: {e}")
```

### Using the Command-line Tools

The package includes several utility scripts:

#### List Users by Last Login

```bash
python list_users_last_seen.py
```

This will display a table of all users with their names, roles, and last login times.

#### Print Workspace Hierarchy

```bash
python print_hierarchy.py
```

This script displays a visual tree representation of your workspace hierarchy with color formatting:
- Groups: Bold with different colors by level (purple, blue, cyan, green, yellow)
- Workspaces: Yellow italic text

The color-coded output makes it easy to distinguish between different levels of groups and workspaces.

#### Test Improvements

```bash
python test_improvements.py
```

This will run tests to demonstrate the validation and error handling improvements.

## Project Structure

```
pyAirfocus/
├── airfocus/                # Main package
│   ├── __init__.py
│   ├── client.py            # API client with improved error handling
│   ├── constants.py         # Centralized constants and configuration
│   ├── logging_config.py    # Logging configuration utilities
│   ├── endpoints/           # API endpoint implementations
│   │   ├── __init__.py
│   │   ├── team.py          # Team-related endpoints
│   │   └── workspaces.py    # Workspace-related endpoints
│   └── models/              # Data models with validation
│       ├── __init__.py
│       ├── team.py          # Team and user models
│       └── workspace.py     # Workspace and group models
├── list_users_last_seen.py  # CLI tool for listing users
├── print_hierarchy.py       # CLI tool for printing workspace hierarchy
├── test_improvements.py     # Test script for improvements
├── requirements.txt         # Project dependencies
└── .env                     # Environment variables (not in repo)
```

## Key Improvements

### 1. Input Validation
- All models now include comprehensive validation using Pydantic validators
- Email format validation for users
- Role validation against supported roles
- Name validation (non-empty strings)
- Order validation (non-negative integers)

### 2. Error Handling
- Specific exception types for different error conditions
- Graceful fallbacks when API calls fail
- Detailed error messages with context
- Proper HTTP status code handling

### 3. Logging
- Consistent logging throughout the library
- Configurable log levels and formats
- Structured logging with proper context
- Reduced noise from external libraries

### 4. Constants and Configuration
- Centralized constants for API endpoints, status codes, and error messages
- Environment variable management
- Consistent configuration across modules

### 5. Type Safety
- Comprehensive type hints throughout
- Pydantic models for data validation
- Better IDE support and code completion

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## License

[MIT License](LICENSE)

## Acknowledgements

- Built with [httpx](https://www.python-httpx.org/) for HTTP requests
- Environment variables managed with [python-dotenv](https://github.com/theskumar/python-dotenv)
- Uses [Pydantic](https://docs.pydantic.dev/) for data validation
- Logging configuration inspired by best practices