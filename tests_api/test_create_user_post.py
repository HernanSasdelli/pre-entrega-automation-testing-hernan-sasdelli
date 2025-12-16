import os
import requests
import pytest

BASE_URL = "https://reqres.in/api"

@pytest.mark.api
def test_post_create_user():
    api_key = os.getenv("REQRES_API_KEY")
    if not api_key:
        pytest.skip("Falta REQRES_API_KEY en variables de entorno")

    headers = {"x-api-key": api_key}

    payload = {"name": "morpheus", "job": "leader"}

    r = requests.post(f"{BASE_URL}/users", json=payload, headers=headers, timeout=10)

    assert r.status_code in (201, 200)
    data = r.json()
    assert "id" in data
    assert "createdAt" in data
