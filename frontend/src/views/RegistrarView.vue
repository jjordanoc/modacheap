<template>
  <div class="container">
    <div class="d-flex flex-column align-items-center">
      <div class="form-header">
        <h1>Registrar</h1>
      </div>
      <form id="login-form" @submit.prevent="register()">
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

          <div class="form-group mb-2">
            <label for="nombre" class="subtitle">Nombre</label>
            <input
              id="nombre"
              name="nombre"
              type="text"
              required
              class="form-control"
              v-model="name"
            />
          </div>

          <div class="form-group mb-2">
            <label for="celular" class="subtitle">Celular</label>
            <input
              id="celular"
              name="celular"
              type="text"
              required
              class="form-control"
              v-model="phone"
            />
          </div>

          <div class="d-flex justify-content-center">
            <div class="form-group d-grid gap-2 col-6 mx-auto mt-3 mb-5">
              <input
                type="submit"
                value="Registrar"
                class="btn btn-primary btn-lg"
              />
            </div>
          </div>
        </div>
      </form>

      <div class="d-flex mt-3 align-items-center">
        <div class="p-2">¿Ya tienes una cuenta de Moda Cheap?</div>
        <div class="p-2">
          <router-link to="/login">Login</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { store } from "@/store.js";
export default {
  name: "RegistrarView",
  data() {
    return {
      email: "",
      name: "",
      password: "",
      phone: "",
      store,
    };
  },
  methods: {
    register() {
      fetch("http://127.0.0.1:5000/register", {
        method: "POST",
        body: JSON.stringify({
          email: this.email,
          password: this.password,
          name: this.name,
          phone: this.phone,
        }),
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((res) => res.json())
        .then((resJson) => {
          if (resJson["success"]) {
            store.login(this.email, this.password);
          } else {
            // error handling
            console.log(resJson);
          }
        });
    },
  },
};
</script>
