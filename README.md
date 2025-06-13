# pyAirfocus

A Python client library and CLI tools for interacting with the Airfocus API.

## Overview

pyAirfocus is a Python package that provides a simple and intuitive interface for working with the Airfocus API. With this library, you can:

- Access Airfocus workspaces and their data
- Retrieve user information and activity data
- Programmatically interact with your Airfocus projects

## Features

- **Simple API Client**: Easy-to-use client for Airfocus API
- **User Management**: List and filter users by activity, roles, and more
- **Workspace Access**: Access and manage workspace data
- **Command-line Tools**: Utility scripts for common tasks (like listing user activity)

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
git clone https://github.com/YOUR_USERNAME/pyAirfocus.git
cd pyAirfocus
python -m venv .
.\Scripts\activate
pip install -r requirements.txt
```

#### macOS/Linux

```bash
git clone https://github.com/YOUR_USERNAME/pyAirfocus.git
cd pyAirfocus
python3 -m venv .
source ./bin/activate
pip install -r requirements.txt
```


## Configuration

1. Create a `.env` file in the root directory with your Airfocus API credentials:

```
AIRFOCUS_API_KEY=your_api_key_here
AIRFOCUS_API_URL=https://api.airfocus.com/v1
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
```

### Using the Command-line Tools

The package includes several utility scripts:

#### List Users by Last Login

```bash
python list_users_last_seen.py
```

This will display a table of all users with their names, roles, and last login times.

## Project Structure

```
pyAirfocus/
├── airfocus/                # Main package
│   ├── __init__.py
│   ├── client.py            # API client
│   ├── endpoints/           # API endpoint implementations
│   └── models/              # Data models
├── list_users_last_seen.py  # CLI tool for listing users
├── requirements.txt         # Project dependencies
└── .env                     # Environment variables (not in repo)
```

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