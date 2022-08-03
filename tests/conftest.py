import pytest

from app import prism


@pytest.fixture
def app():
    prism.app.config.update({
        "TESTING": True,
    })
    return prism.app


@pytest.fixture
def client(app):
    return app.test_client()
