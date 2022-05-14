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
            window.location.href = "/"
        }
        else {
            throw Error("Error de ingreso. Intente de nuevo.");
        }
    }).catch(function(e) {
        console.log(e);
    });
}