# flake8: noqa: E501
import json

import pytest
from freezegun import freeze_time

from app.constants import REBOOKINGS_SPREADSHEET_ID
from app.webhooks.blvd.client_created import google_sheets, logger
from tests.conftest import BLVD_RESOURCES_FILE_PATH, PING_JSON
from tests.helpers import load_test_json

CLIENT_CREATED_JSON = load_test_json(
    f"{BLVD_RESOURCES_FILE_PATH}/client_created_webhook_request"
)


@pytest.fixture
def mock_logger_info(mocker):
    return mocker.patch.object(logger, "info")


@freeze_time("2022-08-07 15:35:26.436324")
@pytest.mark.parametrize(
    "appointment_count, initial_appt_booked",
    [
        (0, False),
        (1, True),
    ],
)
def test_client_created(client, mocker, appointment_count, initial_appt_booked):
    mock_append_to_sheet = mocker.patch.object(
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
    CLIENT_CREATED_JSON["data"]["node"]["appointmentCount"] = appointment_count
    body_data = [
        [
            "urn:blvd:Client:ea9eea9f-df94-45ad-9d0b-88e1d33b2dd2",
            "Joseph Wellington",
            initial_appt_booked,
            False,
            appointment_count,
            "2022-08-07 15:35:26.436324",
            "2022-08-07T15:35:19.436324Z",
            "2022-08-07 15:35:26.436324",
        ]
    ]

    response = client.post("/blvd/client_created", json=CLIENT_CREATED_JSON)

    mock_append_to_sheet.assert_called_once_with(
        REBOOKINGS_SPREADSHEET_ID,
        "rebookings!A:A",
        body_data,
    )
    assert response.status_code == 200
    assert response.get_json() == {
        "spreadsheetId": "1UYkVD_gcvfdMUsPHFoZ2KQ1jpZ4aNdRwhL06OhcP5zE",
        "updatedRange": "rebookings!A13:E13",
        "updatedRows": 1,
        "updatedColumns": 5,
        "updatedCells": 5,
    }


def test_client_created_ping(client, mock_logger_info):
    response = client.post("/blvd/client_created", json=PING_JSON)
    assert response.get_json() == PING_JSON
    mock_logger_info.assert_called_once_with(
        "Received ping for https://my-domain/my-webhook-endpoint. "
        "ID: urn:blvd:Webhook:47ddad57-74bc-4f3f-b102-d42b0c918adb"
    )
