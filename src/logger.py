"""
Audit Logger for MoltBot Governance
"""

import json
import time


LOG_FILE = "mg_audit.log"


def log_event(run_id, event, data):

    record = {
        "run_id": run_id,
        "event": event,
        "data": str(data),
        "timestamp": time.time()
    }

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(record) + "\n")
