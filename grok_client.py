import os
import requests

API_KEY = os.getenv("GROK_API_KEY")

def ask_grok(prompt):

    url = "https://api.x.ai/v1/chat/completions"

    headers = {
        "Authorization": "Bearer " + API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "model": "grok-4-latest",
        "temperature": 0,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    r = requests.post(url, headers=headers, json=payload)

    try:
        data = r.json()
    except:
        return r.text

    if "choices" not in data:
        return str(data)

    return data["choices"][0]["message"]["content"]
