from app.constants import BOULEVARD_LOCATION_ID


def create_webhook(
    url: str, name: str, event_type: str, location_id: str = BOULEVARD_LOCATION_ID
):
    return f"""
        mutation {{
          createWebhook(
            input: {{
              locationId: "urn:blvd:Location:{location_id}"
              url: {url}
              name: {name}
              subscriptions: [{{ eventType: {event_type} }}]
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
