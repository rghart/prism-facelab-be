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
        # Checking if value exists - if it does not, a ValueError is raised
        row_number = sheet_client_ids.index(appt_client_id) + 2

        row_data = google_sheets.get_values_from_sheet(
            REBOOKINGS_SPREADSHEET_ID, f'rebookings!{row_number}:{row_number}'
        )[0]
        current_time = datetime.datetime.now()
        sheet_input_datetime = datetime.datetime.fromisoformat(row_data[SheetHeaderIndex.INPUT_TIME.value])

        if row_data[SheetHeaderIndex.INITIAL_APPT_BOOKED.value] == 'FALSE':
            row_data[SheetHeaderIndex.INITIAL_APPT_BOOKED.value] = 'TRUE'
        elif sheet_input_datetime <= current_time <= (sheet_input_datetime + datetime.timedelta(seconds=15)):
            logger.info(f"Initial appt already booked: {row_data}")
            return {'row_data': row_data}
        elif row_data[SheetHeaderIndex.REBOOKED.value] == 'FALSE':
            row_data[SheetHeaderIndex.REBOOKED.value] = 'TRUE'
        else:
            return {'row_data': row_data}

        row_data[SheetHeaderIndex.ROW_LAST_UPDATED_TIME.value] = str(current_time)

        body_data = [[
            appt_client_id,
            str(current_time),
            str(client_data),
        ]]

        rebookings_update_response = google_sheets.update_sheet(
            REBOOKINGS_SPREADSHEET_ID,
            f'rebookings!{row_number}:{row_number}',
            [row_data],
        )
        google_sheets.append_to_sheet(
            REBOOKINGS_SPREADSHEET_ID,
            'new_client_appointments!A:A',
            body_data,
        )

        logger.info(f'Updated sheet with new Boulevard Appointment: {rebookings_update_response}')

        return rebookings_update_response

    except ValueError:
        logger.info(f'NOT FOUND: Attempted to find client_id {appt_client_id} in google sheet.')
        return request_json








