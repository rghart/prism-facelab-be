import datetime
import logging

from flask import Blueprint, request

from app.constants import REBOOKINGS_SPREADSHEET_ID, SheetHeaderIndex
from app.services.google_sheets_client import google_sheets

logger = logging.getLogger(__name__)

blueprint = Blueprint('blvd_appointment_created', __name__, url_prefix='/blvd')


@blueprint.route('/appointment_created', methods=['POST'])
def appointment_created():
    request_json = request.get_json()

    if request_json.get('event') == "ping":
        logger.info(f"Received ping for {request_json.get('url')}. ID: {request_json.get('webhookId')}")
        return request_json

    client_data = request_json.get('data', {}).get('node')
    appt_client_id = client_data.get('clientId')

    sheet_client_ids = google_sheets.get_values_from_sheet(
        REBOOKINGS_SPREADSHEET_ID, 'rebookings!A2:A', major_dimension="COLUMNS"
    )[0]

    try:
        # Just checking if value exists for now - if it does not, a ValueError is raised
        sheet_client_ids.index(appt_client_id) + 2

        body_data = [[
            appt_client_id,
            str(datetime.datetime.now()),
            str(client_data),
        ]]

        updated_values_response = google_sheets.append_to_sheet(
            REBOOKINGS_SPREADSHEET_ID,
            'new_client_appointments!A:A',
            body_data,
        )

        updates = updated_values_response.get("updates")
        logger.info(f'Updated sheet with new Boulevard Appointment: {updates}')

        return updated_values_response

        # row_data = google_sheets.get_values_from_sheet(
        #     REBOOKINGS_SPREADSHEET_ID, f'rebookings!{row_index}:{row_index}'
        # )[0]
        # if row_data[SheetHeaderIndex.INITIAL_APPT_BOOKED.value] == 'FALSE':
        #     row_data[SheetHeaderIndex.INITIAL_APPT_BOOKED.value] = 'TRUE'
        # elif
        # print(row_data)
    except ValueError:
        logger.info(f'NOT FOUND: Attempted to find client_id {appt_client_id} in google sheet.')
        return request_json








