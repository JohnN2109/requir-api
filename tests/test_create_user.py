import json
import pytest
import requests
from pathlib import Path

users = json.loads(Path("data/users.json").read_text())

@pytest.mark.parametrize("user", users)
def test_create_user(user):
    response = requests.post("https://reqres.in/api/users", json=user)

    assert response.status_code == 201
    body = response.json()

    assert "id" in body
    assert "createdAt" in body
