import hashlib
import json
import time

def record(action,status):

    record = {
        "action":action,
        "status":status,
        "time":time.time()
    }

    h = hashlib.sha256(json.dumps(record).encode()).hexdigest()

    print("Decision hash:",h)

    return h
