from privatevault_bridge import authorize

class PrivateVaultPlugin:

    def before_tool_execution(self, action):

        print("\nPrivateVault Intercepted Tool Call")

        allowed, reason = authorize(action)

        print("Tool:", action.get("tool"))

        if not allowed:

            print("\n❌ BLOCKED")
            print("Policy violation:", reason)

            return {
                "status":"blocked",
                "reason":reason
            }

        print("\n✅ Allowed")

        return {
            "status":"allowed"
        }
