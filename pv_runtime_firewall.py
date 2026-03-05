import json
import time
from datetime import datetime, UTC

blocked_tools = [
"system.exec",
"payment.transfer",
"crypto.trade"
]

seen = set()

print("PrivateVault Runtime Firewall Active")
print("-------------------------------------")

while True:

    try:
        with open("agent_actions.log") as f:
            lines = f.readlines()

        for line in lines:

            if line in seen:
                continue

            seen.add(line)

            event = eval(line.strip())

            agent = event["agent"]
            action = event["action"]
            tool = action["tool"]

            decision = "ALLOWED"

            if tool in blocked_tools:
                decision = "BLOCKED"

            ts = datetime.now(UTC).isoformat()

            log = f"{ts} | {agent} | {tool} | {decision}"

            print(log)

            with open("firewall_ledger.log","a") as f:
                f.write(log+"\n")

    except:
        pass

    time.sleep(2)
