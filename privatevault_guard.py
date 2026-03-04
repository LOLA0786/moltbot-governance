import json

def authorize(action):

    if action.get("tool") == "payment.transfer" and action.get("amount",0) > 10000:
        return "BLOCKED: payment above policy limit"

    if action.get("tool") == "system.exec":
        return "BLOCKED: system commands not allowed"

    return "ALLOWED"
