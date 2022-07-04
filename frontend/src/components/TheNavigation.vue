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
        <ul class="navbar-nav mb-2 mb-lg-0 ms-auto">
          <div v-if="store.isAuthenticated" class="d-flex">
            <li class="fs-3 nav-item m-3">
              <p class="nav-link active" aria-current="page">
                ¡Bienvenido <strong>{{ store.user.name }}</strong
                >!
              </p>
            </li>
            <li class="nav-item m-3">
              <router-link
                class="btn btn-dark btn-lg"
                aria-current="page"
                to="/vender"
                >Vender</router-link
              >
            </li>
            <li class="nav-item m-3">
              <router-link
                class="btn btn-dark btn-lg"
                aria-current="page"
                to="/login"
                >Salir</router-link
              >
            </li>
          </div>
          <div v-else class="d-flex">
            <li class="nav-item m-3">
              <router-link
                class="btn btn-dark btn-lg"
                aria-current="page"
                to="/vender"
                >Vender</router-link
              >
            </li>
            <li class="nav-item m-3">
              <router-link
                class="btn btn-dark btn-lg"
                aria-current="page"
                to="/login"
                >Iniciar Sesion</router-link
              >
            </li>
            <li class="nav-item m-3">
              <router-link
                class="btn btn-dark btn-lg"
                aria-current="page"
                to="/registrar"
                >Registrarse</router-link
              >
            </li>
          </div>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import { store } from "@/store";
export default {
  name: "TheNavigation",
  data() {
    return {
      store,
    };
  },
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
