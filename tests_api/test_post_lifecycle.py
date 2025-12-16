import pytest
import requests
from faker import Faker

fake = Faker()
# BASE_URL = "https://jsonplaceholder.typicode.com" 


@pytest.mark.e2e
def test_post_lifecycle(jsonplaceholder_base_url):#agrego el jsonplaceholder
    
    
    #POST /posts con Faker (title, body) y guardar id
    payload_create = {
        "title": fake.sentence(nb_words=4),
        "body": fake.paragraph(nb_sentences=2),
        "userId": 1
    }

    
    r_create = requests.post(f"{jsonplaceholder_base_url}/posts", json=payload_create, timeout=10)
    assert r_create.status_code in (200, 201)

    body_create = r_create.json()

    assert "id" in body_create and isinstance(body_create["id"], int)
    assert body_create["title"] == payload_create["title"]
    assert body_create["body"] == payload_create["body"]
    assert body_create["userId"] == payload_create["userId"]

    # Tiempo (performance, pregunta de cuestionario!)
    assert r_create.elapsed.total_seconds() < 1

    post_id = body_create["id"]

    #PATCH /posts/{id} actualizando título
    payload_patch = {"title": "Título actualizado por QA"}

   
    r_patch = requests.patch(f"{jsonplaceholder_base_url}/posts/{post_id}", json=payload_patch, timeout=10)
    assert r_patch.status_code == 200

    body_patch = r_patch.json()



    assert "title" in body_patch
    assert body_patch["title"] == "Título actualizado por QA"

  
    assert r_patch.elapsed.total_seconds() < 1

    #DELETE /posts/{id} y validar 200
    
    r_delete = requests.delete(f"{jsonplaceholder_base_url}/posts/{post_id}", timeout=10)
    assert r_delete.status_code == 200
    assert r_delete.elapsed.total_seconds() < 1

    # JSONPlaceholder suele devolver {} en DELETE
    if r_delete.text:
        body_delete = r_delete.json()
        assert body_delete == {} or "id" not in body_delete or body_delete.get("id") is None
