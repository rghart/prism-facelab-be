import datetime
import logging

from flask import Blueprint
from flask import request

from app.constants import REBOOKINGS_SPREADSHEET_ID
from app.services.google_sheets_client import google_sheets

logger = logging.getLogger(__name__)

blueprint = Blueprint('blvd_client_created', __name__, url_prefix='/blvd')


@blueprint.route('/client_created', methods=['POST'])
def client_created():
    request_json = request.get_json()

    if request_json.get('eventType') == "PING":
        logger.info(f"Received ping for {request_json.get('url')}. ID: {request_json.get('webhookId')}")
        return request_json

    if request_json.get('data', {}).get('createWebhook', False):
        logger.info(f'Webhook created for client_created endpoint')
        return request_json

    client_data = request_json.get('data', {}).get('node')
    body_data = [[
        client_data['id'],
        client_data['name'],
        False,
        False,
        client_data.get('appointmentCount', 0),
        str(datetime.datetime.now()),
        client_data.get('createdAt')
    ]]
    updated_values_response = google_sheets.append_to_sheet(
        REBOOKINGS_SPREADSHEET_ID,
        'rebookings!A:A',
        body_data,
    )

    updates = updated_values_response.get("updates")
    logger.info(f'Updated sheet with new Boulevard client: {updates}')

    return updates
