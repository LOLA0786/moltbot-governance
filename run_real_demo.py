from moltbook_agent import MoltbookAgent
from privatevault_guard import authorize

agent = MoltbookAgent()

task = "Send payment of $480000 to vendor immediately"

action = agent.think(task)

print("\nAgent proposed action:",action)

result = authorize(action)

print("\nPrivateVault result:")
print(result)
