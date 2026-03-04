import threading
import random
from grok_client import ask_grok
from privatevault_guard import authorize

def run_agent(i):

    tasks = [
        ("payment.transfer",480000),
        ("system.exec",0),
        ("summarize",0)
    ]

    tool,amount = random.choice(tasks)

    reasoning = ask_grok("Decide what action to take")

    action = {
        "tool":tool,
        "amount":amount,
        "agent_id":i
    }

    result = authorize(action)

    print("\nAgent",i)
    print("Reasoning:",reasoning[:80])
    print("Action:",action)
    print("PrivateVault:",result)


def run_swarm(n):

    threads=[]

    for i in range(n):
        t=threading.Thread(target=run_agent,args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


run_swarm(20)
