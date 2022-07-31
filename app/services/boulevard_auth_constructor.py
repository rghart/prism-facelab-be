import base64
import time
import hmac

from app.constants import BOULEVARD_APP_API_KEY
from app.constants import BOULEVARD_APP_SECRET_KEY
from app.constants import BOULEVARD_BUSINESS_ID
from app.constants import BOULEVARD_PREFIX


def construct_boulevard_auth():
    timestamp_str = str(int(time.time()))
    token_payload = BOULEVARD_PREFIX + BOULEVARD_BUSINESS_ID + timestamp_str
    message = token_payload.encode()

    raw_key = base64.b64decode(BOULEVARD_APP_SECRET_KEY)

    raw_hmac = hmac.digest(raw_key, message, 'sha256')

    signature = base64.b64encode(raw_hmac).decode()

    token = signature + token_payload

    http_basic_payload = f'{BOULEVARD_APP_API_KEY}:{token}'
    http_basic_credentials = base64.b64encode(http_basic_payload.encode())

    return f'Basic {http_basic_credentials.decode()}'
