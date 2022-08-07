import datetime

from freezegun import freeze_time

from app.webhooks.blvd.client_created import google_sheets


def test_client_created(client, mocker):
    # mocker.patch.object(google_sheets, 'append_to_sheet', return_value={'updates': {
    #   'spreadsheetId': '1UYkVD_gcvfdMUsPHFoZ2KQ1jpZ4aNdRwhL06OhcP5zE',
    #   'updatedRange': 'rebookings!A13:E13',
    #   'updatedRows': 1,
    #   'updatedColumns': 5,
    #   'updatedCells': 5
    # }})

    response = client.post(
        "/blvd/appointment_created",
        json={
            "data": {
                "node": {
                    "id": "urn:blvd:Appointment:6b0c90f8-d3da-4d71-ad6f-1b0810f9a0c1",
                    "startAt": "2019-10-02T12:55:00-07:00",
                    "endAt": "2019-10-02T14:35:00-07:00",
                    "notes": "",
                    "duration": 30,
                    "bookedByType": "STAFF",
                    "clientId": "urn:blvd:Client:66238350-db41-4684-b4cb-51d103ed01b0",
                    "client": {
                        "name": "John Doe",
                        "email": "john@gmail.com",
                        "mobilePhone": "+14805555555",
                        "id": "urn:blvd:Client:66238350-db41-4684-b4cb-51d103ed01b0",
                        "externalId": None,
                    },
                    "locationId": "urn:blvd:Location:3052ab0c-7e5d-4d36-8450-fd75a0d66811",
                    "location": {
                        "id": "urn:blvd:Location:3052ab0c-7e5d-4d36-8450-fd75a0d66811",
                        "name": "Santa Monica",
                        "tz": "America/Los_Angeles",
                        "businessName": "Jentleman Js",
                        "externalId": None,
                    },
                    "appointmentServices": [
                        {
                            "startTimeOffset": 0,
                            "startAt": "2019-10-02T12:55:00-07:00",
                            "staffRequested": False,
                            "staffId": "urn:blvd:Staff:88e7ac35-e9ce-4ada-8695-dd7c6fb33daf",
                            "staff": {
                                "lastName": "Backstedt",
                                "email": "backstedt@gmail.com",
                                "id": "urn:blvd:Staff:88e7ac35-e9ce-4ada-8695-dd7c6fb33daf",
                                "firstName": "Crystal",
                                "externalId": None,
                            },
                            "serviceId": "urn:blvd:Service:dda4ef5a-325c-4e80-b81a-e7da05e97fa0",
                            "service": {
                                "name": "(90 min) Arnica Deep Tissue Massage",
                                "id": "urn:blvd:Service:dda4ef5a-325c-4e80-b81a-e7da05e97fa0",
                                "externalId": None,
                            },
                            "id": "urn:blvd:AppointmentService:5efb757c-e79e-4912-a1e5-d50a3f4ffc79",
                        }
                    ],
                    "__typename": "Appointment",
                }
            },
            "businessId": "urn:blvd:Business:4d91175a-bf12-4420-be8a-4822a5093da3",
            "apiApplicationId": "urn:blvd:ApiApplication:60fb5218-dc1d-45da-ac85-1740b7b86e19",
            "webhookId": "urn:blvd:Webhook:bc5661b6-0e87-4a23-ad52-314b47308fa1",
            "event": "appointment.created",
            "eventType": "APPOINTMENT_CREATED",
            "resource": "Appointment",
        },
    )
    print(response.get_json())
    assert response.status_code == 200
    # assert response.get_json() == {
    #   'spreadsheetId': '1UYkVD_gcvfdMUsPHFoZ2KQ1jpZ4aNdRwhL06OhcP5zE',
    #   'updatedRange': 'rebookings!A13:E13',
    #   'updatedRows': 1,
    #   'updatedColumns': 5,
    #   'updatedCells': 5
    # }
