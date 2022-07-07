<template>
  <div class="d-flex flex-row justify-content-center mt-4" v-if="product">
    <div class="m-3 d-flex flex-column producto-imagen">
      <div class="imagen-bg">
        <div class="slider">
          <div class="slides" v-if="product.images">
            <input type="radio" name="r" id="r3" checked />
            <input type="radio" name="r" id="r2" checked />
            <input type="radio" name="r" id="r1" checked />
            <div class="slide s1" v-if="product.images[0]">
              <img
                :src="`http://127.0.0.1:5000/static/uploaded/${product.images[0].id}`"
              />
            </div>
            <div class="slide" v-if="product.images[1]">
              <img
                :src="`http://127.0.0.1:5000/static/uploaded/${product.images[1].id}`"
              />
            </div>

            <div class="slide" v-if="product.images[2]">
              <img
                :src="`http://127.0.0.1:5000/static/uploaded/${product.images[2].id}`"
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
        <h4 class="border-bottom">Publique su comentario</h4>
        <form id="comentario-form" @submit.prevent="createComment()">
          <div
            class="d-flex border border-2 rounded-2 border-primary justify-content-center"
          >
            <div class="form-group mb-3 me-auto p-2 flex-fill">
              <label for="contenido" class="subtitle">Comentario</label>
              <p><small>Ingrese un máximo de 255 caracteres.</small></p>
              <textarea
                id="contenido"
                name="contenido"
                required
                class="form-control border-primary"
                v-model="content"
              ></textarea>
            </div>
            <div
              class="d-flex justify-content-center"
              v-if="store.isAuthenticated"
            >
              <div class="form-group d-grid gap-2 p-2">
                <input
                  type="submit"
                  value="Añadir comentario"
                  class="btn btn-primary btn-lg"
                />
              </div>
            </div>
            <div class="d-flex justify-content-center" v-else>
              <div class="form-group d-grid gap-2 p-2">
                <router-link
                  to="/login"
                  class="btn btn-primary btn-lg align-self-center"
                  >Inicia sesión</router-link
                >
              </div>
            </div>
          </div>
        </form>
      </div>
      <div>
        <h3 class="border-bottom">Comentarios</h3>
        <div class="fw-lighter" v-if="product.comments">
          Hay {{ product.comments.length }} comentario(s).
        </div>
        <div class="d-flex flex-column mb-3">
          <div id="comentarios" v-if="product.comments">
            <p class="mt-3 mb-3 fs-3" v-if="product.comments.length == 0">
              No se encontraron resultados. ¡Sé el primero en comentar! <br />
            </p>
            <div v-else v-for="comment in product.comments" :key="comment.id">
              <div class="d-flex mb-1 mt-2 rounded-2 justify-content-between">
                <div class="mt-2">
                  <strong>{{ comment.user.name }}</strong> ha publicado el
                  siguiente comentario:
                </div>
                <div
                  class="btn-group btn-group-sm"
                  role="group"
                  aria-label="Basic example"
                >
                  <button
                    class="btn btn-outline-danger btn-sm delete-button"
                    @click="deleteComment(comment.id)"
                  >
                    Eliminar
                  </button>
                </div>
              </div>
              <div class="d-flex border border-secondary mb-3 rounded-2">
                <div class="d-flex flex-fill text-break align-self-center px-2">
                  {{ comment.content }}
                </div>
                <div class="p-2 text-end">
                  {{ comment.creation_date }}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
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
            <img src="@/assets/whatsapp_logo.png" />
            <p>Contactar con el vendedor</p>
          </div>
        </a>
      </div>

      <div class="producto-campo" v-if="store.user.id == user.id">
        <div class="d-grid gap-2">
          <router-link
            class="btn btn-warning"
            :to="{
              name: 'editar',
              params: {
                product_id: product_id,
              },
            }"
            >Editar producto</router-link
          >
          <button class="btn btn-danger" @click="deleteProduct()">
            Eliminar producto
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import router from "@/router";
import { store } from "@/store";

export default {
  name: "ProductoView",
  props: {
    product_id: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      product: {},
      user: {},
      content: "",
      store,
    };
  },
  methods: {
    getProduct() {
      console.log(this.product_id);
      fetch("http://127.0.0.1:5000/products/" + this.product_id, {
        method: "GET",
      })
        .then((res) => res.json())
        .then((resJson) => {
          console.log(resJson);
          this.product = resJson.product;
          this.user = resJson.user;
        });
    },
    deleteProduct() {
      fetch("http://127.0.0.1:5000/products/" + this.product_id, {
        method: "DELETE",
      })
        .then((res) => res.json())
        .then((resJson) => {
          console.log(resJson);
          if (resJson["success"]) {
            router.push("/");
          } else {
            // error handling
          }
        });
    },
    createComment() {
      fetch(`http://127.0.0.1:5000/products/${this.product_id}/comments`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          creation_date: new Date().toLocaleString(),
          content: this.content,
          user_id: this.user.id,
        }),
      })
        .then((res) => res.json())
        .then((resJson) => {
          console.log(resJson);
        });
    },
    deleteComment(id) {
      fetch(`http://127.0.0.1:5000/comments/${id}`, {
        method: "DELETE",
      })
        .then((res) => res.json())
        .then((resJson) => {
          console.log(resJson);
        });
    },
  },
  mounted() {
    this.getProduct();
  },
};
</script>
