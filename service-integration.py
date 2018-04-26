'''
Manage Pagerduty via pypd
'''
import json
import os
import pypd
import sys

config_file = "config.json"

if "TF_VAR_pagerduty_token" in os.environ:
    pypd.api_key = os.environ["TF_VAR_pagerduty_token"]
else:
    print("ERROR: Environment variable TF_VAR_pagerduty_token is required")
    sys.exit(1)

try:
    with open(config_file) as f:
        config = json.load(f)
except IOError:
    print("ERROR: File not found")
    sys.exit(2)

for service in config["services"]:
    print("Service: {}".format(service))
    service_obj = pypd.Service.find_one(name=config["services"][service]["pagerduty_service"])
    service_id = service_obj.id
    print("\tID: {}".format(service_id))
    #print(json.dumps(service_obj.json, indent=2))
    # NO print(json.dumps(json.loads(j), indent=2))
    integrations = pypd.Service.get(service_obj, "integrations")
    for integration in integrations:
        print("\tIntegration: {} ID: {}".format(integration["summary"],integration["id"]))
        #print(integration)
        # Key is in here
        i = pypd.Service.get_integration(service_obj, integration["id"]).json
        #print(json.dumps(pypd.Service.get_integration(service_obj, integration["id"]).json, indent=2))
        print("Integration key: {}".format(i["integration_key"]))
        # Get integration key? In server object in [integrations][0][integration_key]
        #   Not is this
        #if integration["summary"] == "lambda":
        #    # This creates v1.
        #   # How to create v2? type = events_api_v2_inbound_integration_reference
        #    # Will create multiple with same name
        #    data = {
        #        "type": "generic_events_api_inbound_integration",
        #        "name": "Service Monitor"
        #    }
        #    result = pypd.Integration.create(service=service_id, data=data)
        #    print(result)
    #print(service_obj) # Only id & name
    #print(pypd.Integration.find_one(service=service_id))

sys.exit(0)

policies = pypd.EscalationPolicy.find()
print(policies)

policy = pypd.EscalationPolicy.fetch(policies[0].id)
print(policy)
print(policy.json)
ep = pypd.EscalationPolicy.create(data=ep_data)
service = pypd.Service.create(data=service_data)
eps = pypd.EscalationPolicy.find(user_ids=[user.id])
users = pypd.User.find(exclude=("jdc+drumpf@pagerduty.com",))
service = pypd.Service.find_one()
escalation_policy = pypd.EscalationPolicy.find_one()
# pypd.Integration.
# pypd.
# Create service integration
# POST /services/{id}/intergrations
'''
{
  "integration": {
    "id": "string",
    "summary": "string",
    "type": "aws_cloudwatch_inbound_integration",
    "self": "string",
    "html_url": "string",
    "name": "string",
    "service": {
      "id": "string",
      "summary": "string",
      "type": "service",
      "self": "string",
      "html_url": "string"
    },
    "created_at": "2018-04-25T18:30:35.082Z",
    "vendor": {
      "id": "string",
      "summary": "string",
      "type": "vendor",
      "self": "string",
      "html_url": "string"
    }
  }
}
'''

# List vendors, search to find one

    # Create extension
    # POST /extensions
