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
    }).then(res => res.json()).then(function(resJson) {
        if (resJson["status"] == "success") {
            window.location.href = "/"
        }
        else {
            throw Error("Error de ingreso. Intente de nuevo.");
        }
    }).catch(function(e) {
        console.log(e);
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
    }).then(res => res.json()).then(function(resJson) {
        if (resJson["status"] == "success") {
            console.log(resJson);
            window.location.href = "/";
        }
    }).catch(function(e) {
        console.log(e);
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
    const imagenes = document.getElementById("imagenes");
    
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
            const files = imagenes.files;
            for (let i = 0; i < files.length; i++) {
                const file = files[i];
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
                });
            }
        }
    }).catch(function() {
        
    });

   
}

const imagenCrear = function(e) {
    
}