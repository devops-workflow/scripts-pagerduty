'''
Manage Pagerduty using REST api directly
'''
import json
import os
import requests
import sys

# Create service
# Create Service integration and get Key
# Create Service extension
# Create Escalation policy
# List services
# List Service integrations and keys
# List service extensions
# Lookup escalation policy
# List extension schemas: find Slack
# Get extension vendor by ID (make by name)

url_base = "https://api.pagerduty.com/"
if "TF_VAR_pagerduty_token" in os.environ:
    pagerduty_api_key = os.environ["TF_VAR_pagerduty_token"]
else:
    print("ERROR: Environment variable TF_VAR_pagerduty_token is required")
    sys.exit(1)
header = {
  "Accept": "application/vnd.pagerduty+json;version=2",
  "Authorization": "Token token=" + pagerduty_api_key
}
#url = url_base + "extension_schemas"
#result = requests.get(url, headers=header)
#print(json.dumps(result.json(), indent=2))
## No slack

#url = url_base + "vendors"
#result = requests.get(url, headers=header)
#print(json.dumps(result.json(), indent=2))
# Has Slack to Pagerduty. Create incident from in Slack

url = url_base + "services"
result = requests.get(url, headers=header)
print(json.dumps(result.json(), indent=2))

#Extension type = SLack How to find via API????

sys.exit(0)
