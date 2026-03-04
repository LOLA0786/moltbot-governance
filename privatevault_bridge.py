import yaml
import os

POLICY_PATH = os.getenv("PRIVATEVAULT_POLICY","../PrivateVault-Mega-Repo/policies.yaml")

with open(POLICY_PATH,"r") as f:
    policies = yaml.safe_load(f)["rules"]

def authorize(action):

    for rule in policies:

        if action.get("tool") == rule.get("tool"):

            if "condition" in rule:

                if action.get("amount",0) > 10000:
                    return False, rule.get("reason","policy violation")

            if rule.get("action") == "block":
                return False, rule.get("reason","blocked")

    return True,"allowed"
