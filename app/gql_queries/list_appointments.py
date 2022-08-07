from app.constants import BOULEVARD_LOCATION_ID


def list_appointments_query(
    client_id, query_str=None, location_id=BOULEVARD_LOCATION_ID, first_int=100
):
    return f"""
        query ListAppointments {{
          appointments(
            locationId: "urn:blvd:Location:{location_id}",
            first: {first_int},
            clientID: "urn:blvd:Client:{client_id}",
            query: "{query_str if query_str else ''}",
          ) {{
            edges {{
              node {{
                id
                notes
                createdAt
                cancellation {{
                    cancelledAt
                    notes
                    reason
                }}
                cancelled
                pendingFormCount
                state
                tags {{
                    id
                    name
                    symbol
                }}

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
