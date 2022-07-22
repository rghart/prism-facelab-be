from dotenv import load_dotenv
import os

load_dotenv()

BOULEVARD_APP_SECRET_KEY = os.environ.get('BOULEVARD_APP_SECRET_KEY')
BOULEVARD_APP_API_KEY = os.environ.get('BOULEVARD_APP_API_KEY')
BOULEVARD_BUSINESS_ID = os.environ.get('BOULEVARD_BUSINESS_ID')
BOULEVARD_PREFIX = os.environ.get('BOULEVARD_PREFIX')
GOOGLE_SERVICE_ACCOUNT_CREDENTIALS = os.environ.get('GOOGLE_SERVICE_ACCOUNT_CREDENTIALS')
REBOOKINGS_SPREADSHEET_ID = os.environ.get('REBOOKINGS_SPREADSHEET_ID')
