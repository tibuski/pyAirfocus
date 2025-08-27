import os
import httpx

URL = 'https://app.airfocus.com/api/'

def airfocusApi(URL,endpoint):
    r = httpx.get(f"{URL}{endpoint}")
    print(r.status_code)

def main():
    airfocusApi(URL,'workspaces')

if __name__ == "__main__":
    main()