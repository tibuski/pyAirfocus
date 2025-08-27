import httpx
import json

from constants import URL
from os import environ

# Retrieve API key from Environment variable
if environ.get('AIRFOCUS_KEY') is not None:
    token = environ.get('AIRFOCUS_KEY')
else:
    print("!!! Environment variable AIRFOCUS_KEY needs to be set !!!")
    exit()

def getApi(endpoint):
    url = f"{URL}{endpoint}"
    headers = {"Authorization": f"Bearer {token}"}
    return httpx.get(url, headers=headers)

def postApi(endpoint,data):
    url = f"{URL}{endpoint}"
    headers = {"Authorization": f"Bearer {token}","accept": "application/json", "Content-Type": "application/json"}
    return httpx.post(url, headers=headers, json=data)

def getWorkspaces():
    # data = {"archived": False}
    data = {}
    return postApi('workspaces/search', data)

def main():

    response=getWorkspaces().json()
    allWorkspaces= response['items']
    for workspace in allWorkspaces:
        print(workspace['name'])

if __name__ == "__main__":
    main()