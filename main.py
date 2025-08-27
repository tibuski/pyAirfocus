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
    response = postApi('workspaces/search', data)
    return response.json()['items']

def getFields():
    # data = {"archived": False}
    data = {}
    response = postApi('fields/search', data)
    return response.json()['items']

def getItemsByWorkspaceID(workspaceId):
    data = {}
    response = postApi(f"workspaces/{workspaceId}/items/search", data)
    return response.json()['items']

def main():

    allWorkspaces = getWorkspaces()
    for workspace in allWorkspaces:
        print(workspace['name'])
        items=getItemsByWorkspaceID(workspace['id'])
        for item in items:
            print(f"-- {item['name']}")
            for k,v in item['fields'].items():
                for k,v in v.items():
                    print(f"---- {k} : {v}")

if __name__ == "__main__":
    main()

