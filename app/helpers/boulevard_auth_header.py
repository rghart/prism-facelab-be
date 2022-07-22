import base64
import math
import time
import hashlib
import hmac

from app.constants import BOULEVARD_APP_API_KEY
from app.constants import BOULEVARD_APP_SECRET_KEY
from app.constants import BOULEVARD_BUSINESS_ID
from app.constants import BOULEVARD_PREFIX


def construct_boulevard_auth():
    seconds_since_epoch = time.time()
    timestamp_str = str(math.floor(seconds_since_epoch))

    token_payload = BOULEVARD_PREFIX + BOULEVARD_BUSINESS_ID + timestamp_str
    message = token_payload.encode('utf8')

    raw_key = base64.b64decode(BOULEVARD_APP_SECRET_KEY)

    raw_hmac = hmac.new(raw_key, message, hashlib.sha256).digest()

    signature = base64.b64encode(raw_hmac)

    token = signature.decode("utf8") + token_payload

    http_basic_payload = BOULEVARD_APP_API_KEY + ":" + token
    http_basic_credentials = base64.b64encode(http_basic_payload.encode('utf8'))
    http_basic_header = "Authorization: Basic " + http_basic_credentials.decode("utf8")

    return http_basic_header
