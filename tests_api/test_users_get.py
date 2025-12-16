import os
import requests
import pytest

BASE_URL = "https://reqres.in/api"


@pytest.mark.api
def test_get_users_pagina_2():
    api_key = os.getenv("REQRES_API_KEY")
    if not api_key:
        pytest.skip("Falta REQRES_API_KEY en variables de entorno")

    headers = {"x-api-key": api_key}

    r = requests.get(
        f"{BASE_URL}/users",
        params={"page": 2},
        headers=headers,
        timeout=10
    )

    assert r.status_code == 200

    data = r.json()
    assert data["page"] == 2
    assert isinstance(data["data"], list)

def test_get_users_pagina_2(logger):
    logger.info("API - GET users page=2")
    ...
