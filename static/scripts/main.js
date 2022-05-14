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
        },
        redirect: "follow"
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
<<<<<<< HEAD
    fetch("/login", {
=======
    fetch("/usuario/registrar", {
>>>>>>> 7e1b53fdee9fd84db745a7ca99d5dd007ba30174
        method: "POST",
        body: JSON.stringify({
            correo: correo.value,
            clave: clave.value,
            nombre: nombre.value,
<<<<<<< HEAD
            celular: celular.value,
=======
            celular: celular.value
>>>>>>> 7e1b53fdee9fd84db745a7ca99d5dd007ba30174
        }),
        headers: {
            "Content-Type": "application/json"
        },
        redirect: "follow"
<<<<<<< HEAD
    }).then(function(res) {
        console.log('response=', res)
        return response.json();
=======
    }).then(res => res.json()).then(function(resJson) {
        if (resJson["status"] == "success") {
            window.location.href = "/"
        }
        else {
            throw Error("Error de ingreso. Intente de nuevo.");
        }
    }).catch(function(e) {
        console.log(e);
>>>>>>> 7e1b53fdee9fd84db745a7ca99d5dd007ba30174
    });
}