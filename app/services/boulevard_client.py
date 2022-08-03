# WIP - using for testing
import requests

from app.constants import BOULEVARD_LOCATION_ID
from app.services.boulevard_auth_constructor import construct_boulevard_auth

endpoint = "https://dashboard.boulevard.io/api/2020-01/admin"
gql_query = f"""
query ListAppointments {{
  appointments(
    locationId: "urn:blvd:Location:{BOULEVARD_LOCATION_ID}",
    first: 100,
  ) {{
    edges {{
      node {{
        id
        notes

        client {{
          firstName
          lastName
          email
          mobilePhone
        }}

        appointmentServices {{
          id
          startAt
          price
          duration
          service {{
            name
            category {{
              name
            }}
          }}

          staffRequested
          staff {{
            firstName
            lastName
            email
            mobilePhone

            role {{
              name
            }}
          }}
        }}
      }}
    }}

    pageInfo {{
      endCursor
      hasNextPage
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