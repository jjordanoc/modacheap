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
            window.location.href = "/";
        }
        else {
            mostrarAlerta(resJson["status"], resJson["message"]);
        }
    });
}
