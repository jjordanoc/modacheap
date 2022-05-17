def test_usuario_login_get(test_client):
    response = test_client.get("/usuario/login")
    assert response.status_code == 200

def test_usuario_login_post(test_client):
    response = test_client.post("/usuario/login")
    assert response.status_code == 200

def test_usuario_logout(test_client):
    response = test_client.get("/usuario/logout")
    assert response.status_code == 302

def test_index(test_client):
    response = test_client.get("/")
    assert response.status_code == 200

def test_usuario_registrar_get(test_client):
    response = test_client.get("/")
    assert response.status_code == 200

def test_usuario_registrar_post(test_client):
    response = test_client.post("/")
    assert response.status_code == 302

def test_producto_buscar(test_client):
    response = test_client.get("/producto/buscar/polo")
    assert response.status_code == 302

def test_producto_ver(test_client):
    response = test_client.get("/producto/ver/1")
    assert response.status_code == 200

def test_producto_categoria(test_client):
    response = test_client.get("/producto/categoria/Abrigos")
    assert response.status_code == 200

def test_producto_crear_get(test_client):
    response = test_client.get("/producto/crear")
    assert response.status_code == 302

def test_producto_crear_post(test_client):
    response = test_client.post("/producto/crear")
    assert response.status_code == 302

def test_borrar_producto(test_client):
    response = test_client.post("/producto/borrar")
    assert response.status_code == 302

def test_editar_producto(test_client):
    response = test_client.post("/producto/editar")
    assert response.status_code == 302

def test_usuario_comentar(test_client):
    response = test_client.post("/usuario/comentar")
    assert response.status_code == 302

def comentario_eliminar(test_client):
    response = test_client.post("/comentario/eliminar")
    assert response.status_code == 302

def imagen_crear(test_client):
    response = test_client.post("/imagen/crear")
    assert response.status_code == 302