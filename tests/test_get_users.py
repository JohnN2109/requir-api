import requests

def test_get_list_users():
    response = requests.get("https://reqres.in/api/users?page=2")
    assert response.status_code == 200
    body = response.json()

    assert "total" in body
    assert body["data"][0]["last_name"]
    assert body["data"][1]["last_name"]

    assert len(body["data"]) == body["per_page"]
