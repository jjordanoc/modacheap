<template>
  <div class="container">
    <div class="d-flex flex-column align-items-center">
      <div class="form-header">
        <h1>Login</h1>
      </div>
      <form id="login-form" @submit.prevent="store.login(email, password)">
        <div class="d-flex flex-column">
          <div class="form-group mb-2">
            <label for="correo" class="subtitle">Correo</label>
            <input
              id="correo"
              name="correo"
              type="email"
              required
              class="form-control"
              v-model="email"
            />
          </div>

          <div class="form-group mb-3">
            <label for="clave" class="subtitle">Clave</label>
            <input
              id="clave"
              name="clave"
              type="password"
              required
              class="form-control"
              v-model="password"
            />
          </div>

          <div class="d-flex justify-content-center">
            <div class="form-group d-grid gap-2 col-6 mx-auto mt-3 mb-5">
              <input
                type="submit"
                value="Login"
                class="btn btn-primary btn-lg"
              />
            </div>
          </div>
        </div>
      </form>

      <div class="d-flex mt-3 align-items-center">
        <div class="p-2">¿No tienes una cuenta de Moda Cheap?</div>
        <div class="p-2">
          <router-link to="/registrar">Regístrate</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { store } from "@/store.js";
export default {
  name: "LoginView",
  data() {
    return {
      email: "",
      password: "",
      store,
    };
  },
};
</script>
