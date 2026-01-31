# 🔐 MoltBot Governance

Governance, audit logs, and kill-switches for AI agents — turn MoltBot into a production system.

MoltBot is powerful.  
Without control, agents can duplicate actions, leak data, or run wild.

This project adds:

✅ Audit trails  
✅ Policy enforcement  
✅ Retry limits  
✅ Kill-switch  
✅ Execution control  

---

## 🚀 Features

- Transaction-style runs
- Full execution logs
- Cost & retry limits
- Policy checks
- Replayable traces

---

## 📦 Install

```bash
pip install moltbot-governance
⚡ Quick Start
from mg import wrap_agent

agent = wrap_agent(moltbot_agent)
agent.run("Generate report")
💰 Pricing
Plan	Price
Free	₹0
Pro	₹4,444 / month
Team	$199 / month
Why This Exists
Built after multiple real production failures.

Agents need control, not just prompts.

License
MIT
