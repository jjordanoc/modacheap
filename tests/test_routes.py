def test_usuario_login_get(test_client):
    response = test_client.get("/usuario/login")
    assert response.status_code == 200


def test_usuario_login_post(test_client):
    response = test_client.post("/usuario/login")
    assert response.status_code != 500