<template>
  <nav class="navbar navbar-expand-lg bg-light" id="main-navbar">
    <div class="container-fluid">
      <router-link class="navbar-brand" to="/" id="main-title">
        Moda Cheap
      </router-link>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <!-- {% if usuario %} -->
        <ul class="navbar-nav mb-2 mb-lg-0 ms-auto">
          <!-- {% if usuario.is_authenticated %}
          <li class="fs-3 nav-item m-3">
            <p class="nav-link active" aria-current="page">
              ¡Bienvenido <strong>{{ usuario.nombre }}</strong
              >!
            </p>
          </li>
          <li class="nav-item m-3">
            <router-link
              class="btn btn-dark btn-lg"
              aria-current="page"
              href="{{url_for('producto_crear')}}"
              >Vender</a
            >
          </li>
          <li class="nav-item m-3">
            <router-link
              class="btn btn-dark btn-lg"
              aria-current="page"
              href="{{url_for('usuario_logout')}}"
              >Salir</a
            >
          </li>
          {% else %} -->
          <li class="nav-item m-3">
            <router-link class="btn btn-dark btn-lg" aria-current="page" to="/"
              >Vender</router-link
            >
          </li>
          <li class="nav-item m-3">
            <router-link class="btn btn-dark btn-lg" aria-current="page" to="/"
              >Iniciar Sesion</router-link
            >
          </li>
          <li class="nav-item m-3">
            <router-link class="btn btn-dark btn-lg" aria-current="page" to="/"
              >Registrarse</router-link
            >
          </li>
          <!-- {% endif %} -->
        </ul>
        <!-- {% endif %} -->
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "TheNavigation",
};
</script>

<style>
#main-navbar {
  background-color: transparent;
}

#main-title {
  color: var(--title-color);
  font-family: var(--title-font);
  font-size: 6em;
}
li {
  list-style: none;
}
</style>
