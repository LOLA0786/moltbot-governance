import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.wrapper import wrap_agent


class FakeMoltBot:

    def run(self, cmd):
        return "Executed: " + cmd


bot = FakeMoltBot()

safe_bot = wrap_agent(bot)

# First run
print(safe_bot.run("Generate report"))

# Duplicate run (should block)
print(safe_bot.run("Generate report"))
