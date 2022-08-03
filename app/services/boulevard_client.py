# WIP - using for testing
import requests

from app.constants import BOULEVARD_LOCATION_ID
from app.services.boulevard_auth_constructor import construct_boulevard_auth

endpoint = "https://dashboard.boulevard.io/api/2020-01/admin"
gql_query = f"""
mutation {{
  createWebhook(
    input: {{
      locationId: "urn:blvd:Location:{BOULEVARD_LOCATION_ID}"
      url: "https://prism-be.herokuapp.com/blvd/client_created"
      name: "Prism Client Created"
      subscriptions: [{{ eventType: CLIENT_CREATED }}]
    }}
  ) {{
    webhook {{
      id
      subscriptions {{
        id
        enabled
        eventType
      }}
    }}
  }}
}}
"""
basic_auth = construct_boulevard_auth()
r = requests.post(
    endpoint,
    json={"query": gql_query},
    headers={
        'Authorization': basic_auth,
        'Accept': 'application/json',
    },
)
if r.status_code == 200:
    print(r.json())
else:
    raise Exception(f"Query failed to run with a {r.status_code}. {r.reason}.")