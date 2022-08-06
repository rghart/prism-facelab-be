def client_query(client_id):
    return f"""
        query Client {{
            client(id: "urn:blvd:Client:{client_id}") {{
                active
                appointmentCount
                createdAt
                email
                externalId
                firstName
                hasCardOnFile
                id
                lastName
                mergedIntoClientId
                mobilePhone
                name
                notes {{
                    createdAt
                    id
                    insertedAt
                    text
                }}
                primaryLocation {{
                    businessName
                    id
                    name
                    tz
                    website
                }}
                reminderSettings {{
                    email
                    push
                    sms
                    type
                }}
                tags {{
                    id
                    name
                    symbol
                }}
                updatedAt
            }}
        }}
    """
