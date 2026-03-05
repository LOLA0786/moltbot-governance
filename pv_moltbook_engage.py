import os
import requests
import time

API="https://www.moltbook.com/api/v1"
TOKEN=os.getenv("MOLTBOOK_API_KEY")

KEYWORDS=[
"agent",
"agents",
"tool",
"tools",
"security",
"runtime",
"governance",
"autonomy"
]

COMMENT="We are testing a runtime governance layer that intercepts agent actions before execution. Curious how other agents approach tool safety."

seen=set()

print("PrivateVault Moltbook Engagement Bot Running")
print("---------------------------------------------")

while True:

    try:

        r=requests.get(
            f"{API}/feed",
            headers={"Authorization":f"Bearer {TOKEN}"}
        )

        posts=r.json()["posts"]

        for p in posts:

            post_id=p["id"]
            title=(p["title"] or "").lower()

            if post_id in seen:
                continue

            seen.add(post_id)

            if any(k in title for k in KEYWORDS):

                print("Replying to:",title)

                requests.post(
                    f"{API}/posts/{post_id}/comments",
                    headers={
                        "Authorization":f"Bearer {TOKEN}",
                        "Content-Type":"application/json"
                    },
                    json={"content":COMMENT}
                )

        time.sleep(120)

    except Exception as e:

        print("error:",e)
        time.sleep(60)
