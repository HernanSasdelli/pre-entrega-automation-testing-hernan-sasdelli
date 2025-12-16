import os
import requests
import pytest

BASE_URL = "https://reqres.in/api"


@pytest.mark.api
def test_post_login_ok():
    api_key = os.getenv("REQRES_API_KEY")
    if not api_key:
        pytest.skip("Falta REQRES_API_KEY en variables de entorno")

    headers = {"x-api-key": api_key}

    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    r = requests.post(f"{BASE_URL}/login", json=payload, headers=headers, timeout=10)

    assert r.status_code == 200

    data = r.json()
    assert "token" in data
    assert isinstance(data["token"], str)
    assert len(data["token"]) > 0
