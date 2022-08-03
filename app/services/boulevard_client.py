# WIP - using for testing
import requests

from app.constants import BOULEVARD_CLIENT_CREATED_WEBHOOK_ID
from app.services.boulevard_auth_constructor import construct_boulevard_auth

endpoint = "https://dashboard.boulevard.io/api/2020-01/admin"
gql_query = f"""
mutation {{
  pingWebhook(input: {{ id: "{BOULEVARD_CLIENT_CREATED_WEBHOOK_ID}" }}) {{
    webhook {{
      id
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