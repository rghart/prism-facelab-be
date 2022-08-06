# WIP - using for testing
import datetime

import pytz
import requests

from app.constants import BOULEVARD_CLIENT_CREATED_WEBHOOK_ID, BOULEVARD_LOCATION_ID
from app.gql_queries.client import client_query
from app.gql_queries.list_appointments import list_appointments_query
from app.services.boulevard_auth_constructor import construct_boulevard_auth

endpoint = "https://dashboard.boulevard.io/api/2020-01/admin"
dttz = datetime.datetime.now(pytz.timezone('US/Central'))
dttz_new = dttz.replace(microsecond=0)
gql_query = list_appointments_query()
print(gql_query)

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