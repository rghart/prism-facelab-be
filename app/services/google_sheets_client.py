import json
import logging

from google.oauth2 import service_account
from googleapiclient import discovery
from googleapiclient.errors import HttpError

from app.constants import GOOGLE_SERVICE_ACCOUNT_CREDENTIALS

logger = logging.getLogger(__name__)


class GoogleSheets:
    def __init__(self):
        self.service = discovery.build(
            "sheets", "v4", credentials=self._construct_credentials()
        )
        self.sheet = self.service.spreadsheets()

    def append_to_sheet(
        self,
        spreadsheet_id,
        spreadsheet_range,
        body_data,
        value_input_option="RAW",
        insert_data_option="INSERT_ROWS",
    ):
        try:
            request = self.sheet.values().append(
                spreadsheetId=spreadsheet_id,
                range=spreadsheet_range,
                valueInputOption=value_input_option,
                insertDataOption=insert_data_option,
                body={"values": body_data},
            )
            response = request.execute()
            return response
        except HttpError as err:
            logger.error(
                f"HttpError: {err.status_code}, {err.reason}. Details: {err.error_details}"
            )
            raise HttpError

    def update_sheet(
        self,
        spreadsheet_id,
        spreadsheet_range,
        body_data,
        value_input_option="RAW",
    ):
        try:
            request = self.sheet.values().update(
                spreadsheetId=spreadsheet_id,
                range=spreadsheet_range,
                valueInputOption=value_input_option,
                includeValuesInResponse=True,
                body={"values": body_data},
            )
            response = request.execute()
            return response
        except HttpError as err:
            logger.error(
                f"HttpError: {err.status_code}, {err.reason}. Details: {err.error_details}"
            )
            raise HttpError

    def get_values_from_sheet(
        self,
        spreadsheet_id,
        spreadsheet_range,
        major_dimension="ROWS",
        value_render_option="FORMATTED_VALUE",
    ):
        try:
            result = (
                self.sheet.values()
                .get(
                    spreadsheetId=spreadsheet_id,
                    range=spreadsheet_range,
                    majorDimension=major_dimension,
                    valueRenderOption=value_render_option,
                )
                .execute()
            )

            return result.get("values", [])

        except HttpError as err:
            logger.error(
                f"HttpError: {err.status_code}, {err.reason}. Details: {err.error_details}"
            )
            raise HttpError

    @staticmethod
    def _construct_credentials():
        json_data = json.loads(GOOGLE_SERVICE_ACCOUNT_CREDENTIALS)
        json_data["private_key"] = json_data["private_key"].replace("\\n", "\n")

        return service_account.Credentials.from_service_account_info(json_data)


google_sheets = GoogleSheets()
