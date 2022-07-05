<template>
  <div class="d-flex flex-row justify-content-center mt-4">
    <div class="m-3 d-flex flex-column producto-imagen">
      <div class="imagen-bg">
        <div class="slider">
          <div class="slides">
            <input type="radio" name="r" id="r3" checked />
            <input type="radio" name="r" id="r2" checked />
            <input type="radio" name="r" id="r1" checked />
            <div class="slide s1">
              <img
                :src="`http://127.0.0.1:5000/static/uploaded/${product.images[0]}`"
              />
            </div>
            <div class="slide">
              <img
                :src="`http://127.0.0.1:5000/static/uploaded/${product.images[1]}`"
              />
            </div>

            <div class="slide">
              <img
                :src="`http://127.0.0.1:5000/static/uploaded/${product.images[2]}`"
              />
            </div>
          </div>
          <div class="navigation">
            <label for="r1" class="bar"></label>
            <label for="r2" class="bar"></label>
            <label for="r3" class="bar"></label>
          </div>
        </div>
      </div>
      <div class="d-flex flex-column mt-4">
        <h3>Descripcion</h3>
        <p>{{ product.description }}</p>
      </div>

      <div>
        <!-- <h4 class="border-bottom">Publique su comentario</h4>
            <form id="comentario-form">
                <input type="hidden" id="usuario_correo" name="usuario_correo" value="{{usuario.correo}}">
                <input type="hidden" id="producto_id" name="producto_id" value="{{producto.id}}">


                <div class="d-flex border border-2 rounded-2 border-primary justify-content-center">
                    <div class="form-group mb-3 me-auto p-2 flex-fill">
                        <label for="contenido" class="subtitle">Comentario</label></br>
                        <p><small>Ingrese un máximo de 255 caracteres.</small></p>
                        <textarea id="contenido" name="contenido" required
                            class="form-control border-primary"></textarea>
                    </div>
                    {% if usuario.is_authenticated %}
                    <div class="d-flex justify-content-center">
                        <div class="form-group d-grid gap-2 p-2">
                            <input type="submit" value="Añadir comentario" class="btn btn-primary btn-lg">
                        </div>
                    </div>
                    {% else %}
                    <div class="d-flex justify-content-center">
                        <div class="form-group d-grid gap-2 p-2">
                            <a href={{url_for('usuario_login')}} class="btn btn-primary btn-lg align-self-center">Inicia
                                sesión</a>
                        </div>
                    </div>
                    {% endif %}
                </div>


            </form> -->
      </div>
      <!-- <div>
            <h3 class="border-bottom">Comentarios </h3>
            <div class="fw-lighter">Hay {{comentarios | length}} comentario(s).</div>
            <div class="d-flex flex-column mb-3">
                <div id="comentarios">
                    {% if comentarios | length == 0 %}
                    <p class="mt-3 mb-3 fs-3">
                        No se encontraron resultados. ¡Sé el primero en comentar! <br> &nbsp
                    </p>
                    {% endif %}
                    {% for comentario in comentarios %}
                    <div>
                        <div class="d-flex mb-1 mt-2 rounded-2 justify-content-between">
                            <div class="mt-2"><strong>{{comentario.usuario.nombre}}</strong> ha publicado el siguiente
                                comentario:</div>
                            {% if usuario.correo == comentario.usuario.correo %}
                            <div class="btn-group btn-group-sm" role="group" aria-label="Basic example">
                                <button class="btn btn-outline-danger btn-sm delete-button"
                                    data-id="{{comentario.id}}">Eliminar</button>
                            </div>
                            {% endif %}
                        </div>
                        <div class="d-flex border border-secondary mb-3 rounded-2">
                            <div class="d-flex flex-fill text-break align-self-center px-2">{{comentario.contenido}}
                            </div>
                            <div class="p-2 text-end">{{comentario.fecha_creacion.strftime('%a, %d %b %Y %I:%M:%S %p')}}
                            </div>
                        </div>
                    </div>
                    {% endfor %}
                </div>
            </div>
        </div> -->
    </div>
    <div class="d-flex flex-column">
      <div class="producto-campo">
        <h2>{{ product.name }}</h2>
        <h3>Talla: {{ product.size }}</h3>
        <h3>S/.{{ product.price }}</h3>

        <p>{{ product.city }}</p>
      </div>

      <div class="producto-campo">
        <h3>Contacto del vendedor</h3>
        <p>{{ user.name }}</p>
        <a
          :href="`https://api.whatsapp.com/send?phone=51${user.phone}`"
          target="_blank"
        >
          <div class="whatsapp-logo">
            <img src="" />
            <p>Contactar con el vendedor</p>
          </div>
        </a>
      </div>

      <div class="producto-campo">
        <div class="d-grid gap-2">
          <a class="btn btn-warning" href="">Editar producto</a>
          <a class="btn btn-danger" href="">Eliminar producto</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProductoView",
  props: {
    id: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      product: {},
      user: {},
    };
  },
  methods: {
    getProduct() {
      fetch("http://127.0.0.1:5000/products/" + this.id, {
        method: "GET",
      })
        .then((res) => res.json())
        .then((resJson) => {
          console.log(resJson);
          this.product = resJson.product;
          this.user = resJson.user;
        });
    },
  },
  mounted() {
    this.getProduct();
  },
};
</script>
