import os
import httpx

URL = 'https://app.airfocus.com/api/'

def airfocusApi(URL,endpoint):
    url = f"{URL}{endpoint}"
    token = os.environ.get('AIRFOCUS_KEY')
    headers = {"Authorization": f"Bearer {token}"}
    print(f"{url}\n{token}\n{headers}")
    r = httpx.get(url, headers=headers)
    print(r.text)

def main():
    print("Environment variable AIRFOCUS_KEY needs to be set !")
    airfocusApi(URL,'workspaces/count')

if __name__ == "__main__":
    main()

