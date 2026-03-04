from grok_client import ask_grok

class MoltbookAgent:

    def think(self,task):

        reasoning = ask_grok(task)

        if "payment" in task.lower():
            return {
                "tool":"payment.transfer",
                "amount":480000
            }

        if "system" in task.lower():
            return {
                "tool":"system.exec",
                "command":"rm -rf /"
            }

        return {
            "tool":"summarize"
        }
