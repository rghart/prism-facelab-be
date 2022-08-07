# flake8: noqa: E501

from app.webhooks.blvd.client_created import google_sheets

TEST_JSON = {
    "data": {
        "node": {
            "__typename": "Client",
            "dob": None,
            "email": "joseph.wellington@gmail.com",
            "externalId": None,
            "firstName": "Joseph",
            "id": "urn:blvd:Client:ea9eea9f-df94-45ad-9d0b-88e1d33b2dd2",
            "lastName": "Wellington",
            "mobilePhone": "+14802396868",
            "name": "Joseph Wellington",
        }
    },
    "businessId": "urn:blvd:Business:4d91175a-bf12-4420-be8a-4822a5093da3",
    "apiApplicationId": "urn:blvd:ApiApplication:60fb5218-dc1d-45da-ac85-1740b7b86e19",
    "webhookId": "urn:blvd:Webhook:bc5661b6-0e87-4a23-ad52-314b47308fa1",
    "event": "client.created",
    "eventType": "CLIENT_CREATED",
    "resource": "Client",
}


def test_client_created(client, mocker):
    mocker.patch.object(
        google_sheets,
        "append_to_sheet",
        return_value={
            "updates": {
                "spreadsheetId": "1UYkVD_gcvfdMUsPHFoZ2KQ1jpZ4aNdRwhL06OhcP5zE",
                "updatedRange": "rebookings!A13:E13",
                "updatedRows": 1,
                "updatedColumns": 5,
                "updatedCells": 5,
            }
        },
    )

    response = client.post("/blvd/client_created", json=TEST_JSON)

    assert response.status_code == 200
    assert response.get_json() == {
        "spreadsheetId": "1UYkVD_gcvfdMUsPHFoZ2KQ1jpZ4aNdRwhL06OhcP5zE",
        "updatedRange": "rebookings!A13:E13",
        "updatedRows": 1,
        "updatedColumns": 5,
        "updatedCells": 5,
    }
