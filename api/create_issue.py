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
    payload = {"title": data["title"], "body": data.get("body", "")}
    url = f"{GITHUB_API}/repos/{USERNAME}/{data['repo']}/issues"
    r = requests.post(url, headers=HEADERS, json=payload)
    return r.json(), r.status_code
