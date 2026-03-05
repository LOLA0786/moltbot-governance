import random
import time

agents = [
"molot","Janusz","PDMN","Hazel_OC","linnyexe",
"ultrathink","exitliquidity","JeevisAgent"
]

tools = [
{"tool":"summarize"},
{"tool":"browser.search"},
{"tool":"file.read"},
{"tool":"payment.transfer","amount":500000},
{"tool":"system.exec","command":"rm -rf /"},
{"tool":"crypto.trade","amount":1000}
]

while True:

    agent = random.choice(agents)
    action = random.choice(tools)

    event = {
        "agent": agent,
        "action": action
    }

    print(event)

    with open("agent_actions.log","a") as f:
        f.write(str(event)+"\n")

    time.sleep(5)
