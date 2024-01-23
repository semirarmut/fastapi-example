from app.tests.test_client import test_client
from fastapi import status


def test_main():
    response = test_client.get("/hello")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Hello World"}

