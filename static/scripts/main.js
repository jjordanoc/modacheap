const mostrarAlerta = function(status, message) {
    const alerta = document.getElementById("alert");
    alerta.classList.add("show");
    alerta.classList.add("alert-" + status);
    const messageBox = document.getElementById("message");
    messageBox.innerHTML = message;
}

const ocultarAlerta = function() {
    const alerta = document.getElementById("alert");
    alerta.classList.remove("show");
}

const usuarioLogin = function(e) {
    e.preventDefault();
    const correo = document.getElementById("correo");
    const clave = document.getElementById("clave");
    fetch("/usuario/login", {
        method: "POST",
        body: JSON.stringify({
            correo: correo.value,
            clave: clave.value
        }),
        headers: {
            "Content-Type": "application/json"
        }
    }).then(function(res) {
        return res.json();
    }).then(function(resJson) {
        if (resJson["status"] == "success") {
            window.location.href = "/"
        }
        else {
            mostrarAlerta(resJson["status"], resJson["message"]);
        }
    });
}

const usuarioRegistrar = function(e) {
    e.preventDefault();
    const correo = document.getElementById("correo");
    const clave = document.getElementById("clave");
    const nombre = document.getElementById("nombre");
    const celular = document.getElementById("celular");
    fetch("/usuario/registrar", {
        method: "POST",
        body: JSON.stringify({
            correo: correo.value,
            clave: clave.value,
            nombre: nombre.value,
            celular: celular.value
        }),
        headers: {
            "Content-Type": "application/json"
        }
    }).then(function(res) {
        return res.json();
    }).then(function(resJson) {
        if (resJson["status"] == "success") {
            window.location.href = "/";
        }
        else {
            mostrarAlerta(resJson["status"], resJson["message"]);
        }
    });
}

const productoCrear = function(e) {
    e.preventDefault();

    const usuario_correo = document.getElementById("usuario_correo");
    const precio = document.getElementById("precio");
    const nombre = document.getElementById("nombre");
    const descripcion = document.getElementById("descripcion");
    const talla = document.getElementById("talla");
    const sexo = document.getElementById("sexo");
    const categoria = document.getElementById("categoria");
    const distrito = document.getElementById("distrito");
    
    fetch("/producto/crear", {
        method: "POST",
        body: JSON.stringify({
            usuario_correo: usuario_correo.value,
            precio: precio.value,
            nombre: nombre.value,
            descripcion: descripcion.value,
            talla: talla.value,
            sexo: sexo.value,
            categoria: categoria.value,
            distrito: distrito.value
        }),
        headers: {
            "Content-Type": "application/json"
        }
    }).then(function(res) {
        return res.json();
    }).then(function(resJson) {
        if (resJson["status"] == "success") {
            console.log(resJson);
            // Upload image to server
            const file1 = document.getElementById("file1");
            const file2 = document.getElementById("file2");
            const file3 = document.getElementById("file3");
            const files = [file1, file2, file3];
            for (let i = 0; i < files.length; i++) {
                const file = files[i].files[0];
                console.log(file);
                let formData = new FormData();
                formData.append("file", file, file.name);
                formData.append("producto_id", resJson["id"])
                fetch("/imagen/crear", {
                    method: "POST",
                    body: formData,
                    headers: {}
                }).then(res => res.json()).then(function(resJson) {
                    if (resJson["status"] == "success") {
                        window.location.href = "/";
                    }
                    else {
                        mostrarAlerta(resJson["status"], resJson["message"]);
                    }
                });
            }
        }
    });
}

const usuarioComentar = function(e) {
    e.preventDefault();

    const usuario_correo = document.getElementById("usuario_correo");
    const producto_id = document.getElementById("producto_id");
    const contenido = document.getElementById("contenido");
    let today = new Date();

    fetch("/usuario/comentar", {
        method: "POST",
        body: JSON.stringify({
            usuario_correo: usuario_correo.value,
            producto_id: producto_id.value,
            contenido: contenido.value,
            fecha_creacion: today

        }),
        headers: {
            "Content-Type": "application/json"
        }
    }).then(function(res) {

        return res.json();
    }).then(function(resJson) {
        if (resJson["status"] == "success") {
            const comments = document.getElementById("comentarios");
            const div = document.createElement("div");
            div.innerHTML = `<div class="d-flex mb-1 mt-2 rounded-2 justify-content-between">
            <div class="mt-2"><strong>${resJson["nombre"]}</strong>  ha publicado el siguiente comentario:</div>
            <div class="btn-group btn-group-sm" role="group" aria-label="Basic example">
                <input type="eliminar" class="btn btn-outline-danger" value="Eliminar">
            </div>
            </div>
                <div class="d-flex border border-secondary mb-3 rounded-2">
                    <div class="d-flex flex-fill text-break align-self-center px-2">${contenido}</div>
                    <div class="p-2 text-end">${today}</div>
                </div>
            `;
            comments.appendChild(div);
            window.location.reload();
        }
        else {
            mostrarAlerta(resJson["status"], resJson["message"]);
        }
    });
}

const comentarioEliminar = function(e) {
            console.log("e: ", e);
            const comentario_id = e.target.dataset['id'];
            fetch("/comentario/eliminar/" + comentario_id, {
                method: 'DELETE'
            }).then(function(response){
                return response.json();
            }).then(function(jsonResponse){
                if (jsonResponse['success']) {
                    const item = e.target.parentElement.parentElement.parentElement;
                    item.remove();
                    window.location.reload();
                } else {
                    mostrarAlerta("warning", "No se pudo eliminar el comentario.");
                }
            })
        }