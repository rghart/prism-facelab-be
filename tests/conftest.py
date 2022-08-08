import pytest

from app import prism
from tests.helpers import load_test_json

RESOURCES_FILE_PATH = "tests/resources"
BLVD_RESOURCES_FILE_PATH = f"{RESOURCES_FILE_PATH}/blvd"

PING_JSON = load_test_json(f"{BLVD_RESOURCES_FILE_PATH}/ping_request")


@pytest.fixture
def app():
    prism.app.config.update(
        {
            "TESTING": True,
        }
    )
    return prism.app


@pytest.fixture
def client(app):
    return app.test_client()
