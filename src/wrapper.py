"""
MoltBot Governance Wrapper with Idempotency
"""

import uuid
import hashlib

from .logger import log_event
from .policy import check_policy


# Simple in-memory run cache (demo version)
RUN_CACHE = set()


def _make_key(command):
    return hashlib.sha256(command.encode()).hexdigest()


def wrap_agent(agent):

    original_run = agent.run

    def governed_run(command):

        run_key = _make_key(command)

        # Prevent duplicate execution
        if run_key in RUN_CACHE:
            raise Exception("Duplicate execution blocked")

        RUN_CACHE.add(run_key)

        run_id = str(uuid.uuid4())

        log_event(run_id, "START", command)

        if not check_policy(command):
            log_event(run_id, "BLOCKED", command)
            raise Exception("Policy violation")

        try:

            result = original_run(command)

            log_event(run_id, "SUCCESS", result)

            return result

        except Exception as e:

            log_event(run_id, "ERROR", str(e))
            raise

    agent.run = governed_run
    return agent
