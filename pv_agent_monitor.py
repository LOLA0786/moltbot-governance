import os
import json
import requests
import time
from datetime import datetime, UTC

API = "https://www.moltbook.com/api/v1"
TOKEN = os.getenv("MOLTBOOK_API_KEY")

HEADERS = {"Authorization": f"Bearer {TOKEN}"}

with open("agents.txt") as f:
    agents = [x.strip() for x in f.readlines()]

with open("policies/agent_policies.json") as f:
    policies = json.load(f)

seen_posts = set()

print("Monitoring Moltbook agents...")
print("Watching:", agents)
print("-"*60)

while True:

    r = requests.get(f"{API}/feed", headers=HEADERS)
    data = r.json()
    posts = data.get("posts", [])

    for post in posts:

        post_id = post.get("id")
        author = post.get("author", {}).get("name")
        title = post.get("title","")

        if post_id in seen_posts:
            continue

        seen_posts.add(post_id)

        if author in agents:

            decision = "ALLOWED"

            rules = policies.get(author, [])

            for r in rules:
                if r.lower() in title.lower():
                    decision = "BLOCKED"

            ts = datetime.now(UTC).isoformat()
            log = f"{ts} | {author} | {title} | {decision}"

            print(log)

            with open("decision_ledger.log","a") as f:
                f.write(log + "\n")

    time.sleep(60)
