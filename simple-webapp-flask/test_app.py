import pytest
from app import app


@pytest.fixture
def client():
    app.testing = True
    return app.test_client()


def test_home(client):

    response = client.get("/")

    assert response.status_code == 200

    assert b"Welcome!" in response.data


def test_how_are_you(client):

    response = client.get("/how are you")

    assert response.status_code == 200

    assert b"I am good, how about you?" in response.data