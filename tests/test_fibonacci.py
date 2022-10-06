from fastapi.testclient import TestClient
from main import app

URL = '/fibonacci'

def test_fibonnaci_1():
    client = TestClient(app)
    num = {
        "index":1
    }

    response = client.post(
        URL,
        json=num
    )

    assert response.status_code == 200, response.text
    data = response.json()
    assert data['response'] == 1

def test_fibonnaci_2():
    client = TestClient(app)
    num = {
        "index":2
    }

    response = client.post(
        URL,
        json=num
    )

    assert response.status_code == 200, response.text
    data = response.json()
    assert data['response'] == 1

def test_fibonnaci_12():
    client = TestClient(app)
    num = {
        "index":12
    }

    response = client.post(
        URL,
        json=num
    )

    assert response.status_code == 200, response.text
    data = response.json()
    assert data['response'] == 144

def test_fibonnaci_text():
    client = TestClient(app)
    num = {
        "index":"dasdas"
    }

    response = client.post(
        URL,
        json=num
    )

    assert response.status_code == 422, response.text
    data = response.json()
    assert data['detail']
