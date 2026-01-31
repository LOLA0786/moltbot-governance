import json
import time
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "..", "mg_audit.log")


def log_event(run_id, event, data):

    record = {
        "run_id": run_id,
        "event": event,
        "data": data,
        "timestamp": time.time()
    }

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(record) + "\n")

