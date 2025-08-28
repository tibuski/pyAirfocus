# pyAirfocus

Simple Python client to query airfocus workspaces and items using the airfocus API.

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
The script expects two things:
- An environment variable `AIRFOCUS_KEY` set to your API token
- A base URL in `constants.py` exposed as `URL`

Example `constants.py`:
```python
# constants.py
URL = "https://api.airfocus.com/"
```

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

## Run
```bash
python main.py
```

If the environment variable is not set, the script will exit with an error message.

## Notes
- The client uses a single `httpx.Client` with sensible timeouts.
- Logging is enabled; output appears at INFO level.