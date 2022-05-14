const usuarioLogin = function(e) {
    e.preventDefault();
    const correo = document.getElementById("correo");
    const clave = document.getElementById("clave");
    fetch("/login", {
        method: "POST",
        body: JSON.stringify({
            correo: correo.value,
            clave: clave.value
        }),
        headers: {
            "Content-Type": "application/json"
        },
        redirect: "follow"
    }).then(function(res) {
        console.log('Respuesta', res)
        return res.json();
    });
}

const usuarioRegistrar = function(e) {
    e.preventDefault();
    const correo = document.getElementById("correo");
    const clave = document.getElementById("clave");
    const nombre = document.getElementById("nombre");
    const celular = document.getElementById("celular");
    fetch("/login", {
        method: "POST",
        body: JSON.stringify({
            correo: correo.value,
            clave: clave.value,
            nombre: nombre.value,
            celular: celular.value,
        }),
        headers: {
            "Content-Type": "application/json"
        },
        redirect: "follow"
    }).then(function(res) {
        console.log('response=', res)
        return response.json();
    });
}