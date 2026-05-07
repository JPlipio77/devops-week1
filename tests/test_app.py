import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_hello(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello from" in response.data


def test_health_endpoint_exists(clients):
    response = client.get('/health')
    assert response.status_code in (200, 503,)  # Depending on DB connection
