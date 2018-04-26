'''
Manage Pagerduty using REST api directly
'''
import json
import os
import requests
import sys

# Lookup:
#   user
#       https://v2.developer.pagerduty.com/page/api-reference#!/Users/get_users
#       https://v2.developer.pagerduty.com/page/api-reference#!/Users/get_users_id
#   schedule
#       https://v2.developer.pagerduty.com/page/api-reference#!/Schedules/get_schedules
#       https://v2.developer.pagerduty.com/page/api-reference#!/Schedules/get_schedules_id
#   team
#       https://v2.developer.pagerduty.com/page/api-reference#!/Teams/get_teams
#       https://v2.developer.pagerduty.com/page/api-reference#!/Teams/get_teams_id
#   escalation policy ?
#       https://v2.developer.pagerduty.com/page/api-reference#!/Escalation_Policies/get_escalation_policies
#       https://v2.developer.pagerduty.com/page/api-reference#!/Escalation_Policies/get_escalation_policies_id
# Create:
#   service
#       https://v2.developer.pagerduty.com/page/api-reference#!/Services/post_services
#   Service integration and get Key
#       https://v2.developer.pagerduty.com/page/api-reference#!/Services/post_services_id_integrations
#   Service extension
#       https://v2.developer.pagerduty.com/page/api-reference#!/Extensions/post_extensions
#   Escalation policy
#       https://v2.developer.pagerduty.com/page/api-reference#!/Escalation_Policies/post_escalation_policies
# List:
#   services
#       https://v2.developer.pagerduty.com/page/api-reference#!/Services/get_services
#   Service integrations and keys
#       https://v2.developer.pagerduty.com/page/api-reference#!/Services/get_services_id_integrations_integration_id
#   service extensions
#       https://v2.developer.pagerduty.com/page/api-reference#!/Extensions/get_extensions
#   extension schemas: find Slack
#       https://v2.developer.pagerduty.com/page/api-reference#!/Extension_Schemas/get_extension_schemas
#   vendors
#       https://v2.developer.pagerduty.com/page/api-reference#!/Vendors/get_vendors
#       https://v2.developer.pagerduty.com/page/api-reference#!/Vendors/get_vendors_id
#       Only old Slack integration listed in vendors
# Get:
#   extension vendor by ID (make by name)
#       https://v2.developer.pagerduty.com/page/api-reference#!/Extension_Schemas/get_extension_schemas_id
#   extension
#       https://v2.developer.pagerduty.com/page/api-reference#!/Extensions/get_extensions_id
# Add:
#   escalation ploicy to team
#       https://v2.developer.pagerduty.com/page/api-reference#!/Teams/put_teams_id_escalation_policies_escalation_policy_id
#   user to team
#       https://v2.developer.pagerduty.com/page/api-reference#!/Teams/put_teams_id_users_user_id

# New slack uses webhook extension. List extension to see one as an example

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

# API uses: get (list, view, get), put(add,update), post(create), delete(delete,remove)
def get_request():
    print("placeholder")
    # Most/all of list_resources move here?

def list_resources(resource):
    # Works for:
    #   escalation_policies,
    #   extensions, extension_schemas,
    #   schedules, services, teams, users
    #   vendors,
    url = url_base + resource + "?limit=100"
    # Supports: ?query=XXX
    #   Claims name or email
    data = []
    offset = ""
    while True:
        result = requests.get(url + offset, headers=header)
        result_data = result.json()
        data = data + result_data[resource]
        if result_data["more"]:
            offset = "&offset={}".format(result_data["offset"] + result_data["limit"])
        else:
            break
        #print("Data: {}".format(json.dumps(data, indent=2)))
    return data

def get_user_by(users, key, value):
    id = ""
    for user in users:
        if user[key].lower() == value.lower():
            id = user["id"]
    return id

def statistics():
    resources = [
        "escalation_policies",
        "extension_schemas",
        "extensions",
        "schedules",
        "services",
        "teams",
        "users",
        "vendors",
    ]
    print("Pagerduty usage statistics:")
    for resource in resources:
        print("\t{}: {}".format(resource, len(list_resources(resource))))

users = list_resources("users")
print("Amar by name: {}".format(get_user_by(users,"name", "Amar kale")))
print("Amar by email: {}".format(get_user_by(users,"email", "akale@wiser.com")))

#statistics()
#teams = list_resources("teams")
#print(json.dumps(list_resources("users"), indent=2))
sys.exit(0)

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
