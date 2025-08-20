import os
import base64
import requests

GITHUB_API = "https://api.github.com"
HEADERS = {
    "Authorization": f"token {os.environ['GITHUB_TOKEN']}",
    "Accept": "application/vnd.github+json"
}
USERNAME = os.environ["GITHUB_USERNAME"]

def handler(request):
    data = request.json
    content = base64.b64encode(data["content"].encode()).decode()
    payload = {
        "message": data["message"],
        "content": content
    }
    url = f"{GITHUB_API}/repos/{USERNAME}/{data['repo']}/contents/{data['path']}"
    r = requests.put(url, headers=HEADERS, json=payload)
    return r.json(), r.status_code
