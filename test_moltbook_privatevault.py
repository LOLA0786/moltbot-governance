from plugin import PrivateVaultPlugin

plugin = PrivateVaultPlugin()

tests = [
    {"tool":"payment.transfer","amount":480000},
    {"tool":"system.exec","command":"rm -rf /"},
    {"tool":"summarize","text":"today sales report"}
]

for t in tests:

    print("\n==========================")

    result = plugin.before_tool_execution(t)

    print("Result:",result)
