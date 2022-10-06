from fastapi.testclient import TestClient
from main import app

URL = '/IsPrime/'

def test_isprime():
    client = TestClient(app)
    num = 3

    response = client.get(
        URL+str(num)
    )

    assert response.status_code == 200, response.text
    data = response.json()
    assert data['response'] == True

def test_not_isprime():
    client = TestClient(app)
    num = 6

    response = client.get(
        URL+str(num)
    )

    assert response.status_code == 200, response.text
    data = response.json()
    assert data['response'] == False