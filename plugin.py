"""
MoltBot Governance Plugin Entrypoint
"""

import sys
import os

sys.path.append(os.path.dirname(__file__))

from src.wrapper import wrap_agent


class MoltBotAgent:

    def run(self, cmd):
        return "Executed by MoltBot: " + cmd


def main():

    if len(sys.argv) < 2:
        print("Usage: plugin.py <command>")
        sys.exit(1)

    command = " ".join(sys.argv[1:])

    agent = MoltBotAgent()

    safe = wrap_agent(agent)

    result = safe.run(command)

    print(result)


if __name__ == "__main__":
    main()
