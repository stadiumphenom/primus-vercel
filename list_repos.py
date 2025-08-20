import os
import requests
from fastapi import FastAPI, HTTPException

app = FastAPI()

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
API_URL = "https://api.github.com"

@app.get("/list_repos")
def list_repos():
    if not GITHUB_TOKEN:
        raise HTTPException(status_code=401, detail="GitHub token not set")
    headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}
    r = requests.get(f"{API_URL}/user/repos", headers=headers)
    if r.status_code == 200:
        repos = [repo["name"] for repo in r.json()]
        return {"repositories": repos}
    else:
        raise HTTPException(status_code=r.status_code, detail=r.json().get("message", "Unknown error"))
