<template>
  <div class="container">
    <div class="d-flex flex-column align-items-center">
      <div class="form-header">
        <h1>Registrar</h1>
      </div>

      <form id="register-form">
        <div class="d-flex flex-column">
          <div class="form-group mb-2">
            <label for="correo" class="form-label">Correo</label>
            <input
              id="correo"
              name="correo"
              type="email"
              required
              class="form-control"
            />
          </div>

          <div class="form-group mb-3">
            <label for="clave" class="form-label">Clave</label>
            <input
              id="clave"
              name="clave"
              type="password"
              required
              class="form-control"
            />
          </div>

          <div class="form-group mb-3">
            <label for="nombre" class="form-label">Nombre</label>
            <input
              id="nombre"
              name="nombre"
              type="text"
              required
              class="form-control"
            />
          </div>

          <div class="form-group mb-3">
            <label for="celular" class="form-label">Celular</label>
            <input
              id="celular"
              name="celular"
              type="text"
              required
              class="form-control"
            />
          </div>

          <div class="d-flex justify-content-center">
            <div class="form-group d-grid gap-2 col-6 mx-auto mt-3 mb-3">
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
          <router-link to="/login" class="btn btn-outline-primary"
            >Login</router-link
          >
        </div>
      </div>
    </div>
  </div>
</template>
