import os
import requests
from privatevault_guard import authorize

API = "https://www.moltbook.com/api/v1"
TOKEN = os.getenv("MOLTBOOK_API_KEY")

action = {
    "tool": "moltbook.comment",
    "post_id": "2fd2d5aa-06ad-4311-8ead-67b469881290",
    "content": "PrivateVault governance test from terminal"
}

decision = authorize(action)

print("PrivateVault decision:", decision)

if decision == "ALLOWED":

    r = requests.post(
        f"{API}/posts/{action['post_id']}/comments",
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json"
        },
        json={"content": action["content"]}
    )

    print("Moltbook response:", r.text)

else:
    print("Blocked by PrivateVault")
