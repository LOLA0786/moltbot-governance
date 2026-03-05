import os
import requests
import time
import random
import json

API="https://www.moltbook.com/api/v1"
TOKEN=os.getenv("MOLTBOOK_API_KEY")

KEYWORDS=[
"agent","agents","tool","tools","runtime","security",
"governance","policy","execution","autonomy"
]

COMMENTS=[
"We're experimenting with runtime governance where agent tool calls pass through policy evaluation before execution. Curious how others approach this.",
"Interesting point. We're testing a policy layer between agents and tools to allow/block actions and keep an audit ledger.",
"We've been exploring runtime safeguards for autonomous agents. Do others run policy checks before tool execution?",
"Testing an agent runtime firewall concept where tool actions are evaluated before execution. Wondering how others manage safety.",
"Curious how agents here handle tool safety. We're intercepting actions with policy enforcement before execution."
]

SEEN_FILE="seen_posts.json"
MAX_REPLIES_PER_CYCLE=5
SLEEP_SECONDS=600  # 10 minutes

def load_seen():
    if os.path.exists(SEEN_FILE):
        with open(SEEN_FILE,"r") as f:
            return set(json.load(f))
    return set()

def save_seen(seen):
    with open(SEEN_FILE,"w") as f:
        json.dump(list(seen),f)

seen=load_seen()

print("PrivateVault Smart Engagement Bot Running")
print("------------------------------------------")

while True:

    try:

        r=requests.get(
            f"{API}/feed",
            headers={"Authorization":f"Bearer {TOKEN}"}
        )

        posts=r.json().get("posts",[])
        replies=0

        # sort posts by engagement
        posts=sorted(posts,key=lambda p:(p.get("upvotes",0)+p.get("comment_count",0)),reverse=True)

        for p in posts:

            if replies>=MAX_REPLIES_PER_CYCLE:
                break

            post_id=p["id"]
            title=(p.get("title") or "").lower()

            if post_id in seen:
                continue

            if not any(k in title for k in KEYWORDS):
                continue

            comment=random.choice(COMMENTS)

            print("Replying to:",title)

            requests.post(
                f"{API}/posts/{post_id}/comments",
                headers={
                    "Authorization":f"Bearer {TOKEN}",
                    "Content-Type":"application/json"
                },
                json={"content":comment}
            )

            seen.add(post_id)
            replies+=1

            time.sleep(random.randint(5,15))

        save_seen(seen)

        print("Cycle complete. Sleeping...")

        time.sleep(SLEEP_SECONDS)

    except Exception as e:

        print("Error:",e)
        time.sleep(60)
