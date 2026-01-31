"""
Basic Policy Engine
"""

BLOCKED_COMMANDS = [
    "delete database",
    "drop table",
    "leak password",
    "send credentials",
    "wipe data"
]


def check_policy(command):

    cmd = command.lower()

    for bad in BLOCKED_COMMANDS:
        if bad in cmd:
            return False

    return True
