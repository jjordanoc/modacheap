<template>
  <form @submit.prevent="updateProduct()">
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
          <textarea
            id="descripcion"
            name="descripcion"
            required
            class="form-control border-primary"
            cols="50"
            v-model="product.description"
          ></textarea>
        </div>
      </div>
      <div class="d-flex flex-column">
        <div class="producto-campo">
          <div class="form-group mb-3">
            <h2>Nombre del producto:</h2>
            <input
              type="text"
              id="nombre"
              name="nombre"
              required
              class="form-control"
              minlength="5"
              maxlength="80"
              v-model="product.name"
            />
          </div>
          <div class="form-group mb-3">
            <h3>Talla:</h3>
            <select
              name="talla"
              id="talla"
              required
              class="form-select"
              v-model="product.size"
            >
              <option disabled value="">Seleccionar</option>
              <option value="XXS">XXS</option>
              <option value="XS">XS</option>
              <option value="S">S</option>
              <option value="M">M</option>
              <option value="L">L</option>
              <option value="XL">XL</option>
              <option value="XXL">XXL</option>
            </select>
          </div>
          <div class="from-group mb-3">
            <h3>Género:</h3>
            <select
              name="sexo"
              id="sexo"
              required
              class="form-select"
              v-model="product.sex"
            >
              <option disabled value="">Seleccionar</option>
              <option value="M">Hombre</option>
              <option value="F">Mujer</option>
              <option value="U">Unisex</option>
            </select>
          </div>
          <div class="form-group mb-3">
            <h3>Categoría:</h3>
            <select
              name="categoria"
              id="categoria"
              required
              class="form-select"
              v-model="product.category"
            >
              <option disabled value="">Seleccionar</option>
              <option value="Abrigos">Abrigos</option>
              <option value="Polos">Polos</option>
              <option value="Pantalones">Pantalones</option>
              <option value="Zapatos">Zapatos</option>
              <option value="Accesorios">Accesorios</option>
              <option value="Vestidos">Vestidos</option>
              <option value="Blusas">Blusas</option>
              <option value="Invierno">Ropa de invierno</option>
            </select>
          </div>
          <div class="form-group mb-3">
            <h3>Precio (S/.):</h3>
            <input
              type="number"
              min="0"
              max="99999"
              id="precio"
              name="precio"
              step="any"
              required
              class="form-control"
              v-model="product.price"
            />
          </div>
          <div class="form-group mb-3">
            <h3>Distrito:</h3>
            <select
              name="distrito"
              id="distrito"
              required
              class="form-select"
              v-model="product.city"
            >
              <option disabled value="">Seleccionar</option>
              <option value="ANCON">ANCON</option>
              <option value="ATE">ATE</option>
              <option value="BARRANCO">BARRANCO</option>
              <option value="BREÑA">BREÑA</option>
              <option value="CARABAYLLO">CARABAYLLO</option>
              <option value="CHACLACAYO">CHACLACAYO</option>
              <option value="CHORRILLOS">CHORRILLOS</option>
              <option value="CIENEGUILLA">CIENEGUILLA</option>
              <option value="COMAS">COMAS</option>
              <option value="EL AGUSTINO">EL AGUSTINO</option>
              <option value="INDEPENDENCIA">INDEPENDENCIA</option>
              <option value="JESUS MARIA">JESUS MARIA</option>
              <option value="LA MOLINA">LA MOLINA</option>
              <option value="LA VICTORIA">LA VICTORIA</option>
              <option value="LIMA">LIMA</option>
              <option value="LINCE">LINCE</option>
              <option value="LOS OLIVOS">LOS OLIVOS</option>
              <option value="LURIGANCHO">LURIGANCHO</option>
              <option value="LURIN">LURIN</option>
              <option value="MAGDALENA DEL MAR">MAGDALENA DEL MAR</option>
              <option value="MIRAFLORES">MIRAFLORES</option>
              <option value="PACHACAMAC">PACHACAMAC</option>
              <option value="PUCUSANA">PUCUSANA</option>
              <option value="PUEBLO LIBRE">PUEBLO LIBRE</option>
              <option value="PUENTE PIEDRA">PUENTE PIEDRA</option>
              <option value="PUNTA HERMOSA">PUNTA HERMOSA</option>
              <option value="PUNTA NEGRA">PUNTA NEGRA</option>
              <option value="RIMAC">RIMAC</option>
              <option value="SAN BARTOLO">SAN BARTOLO</option>
              <option value="SAN BORJA">SAN BORJA</option>
              <option value="SAN ISIDRO">SAN ISIDRO</option>
              <option value="SAN JUAN DE LURIGANCHO">
                SAN JUAN DE LURIGANCHO
              </option>
              <option value="SAN JUAN DE MIRAFLORES">
                SAN JUAN DE MIRAFLORES
              </option>
              <option value="SAN LUIS">SAN LUIS</option>
              <option value="SAN MARTIN DE PORRES">SAN MARTIN DE PORRES</option>
              <option value="SAN MIGUEL">SAN MIGUEL</option>
              <option value="SANTA ANITA">SANTA ANITA</option>
              <option value="SANTA MARIA DEL MAR">SANTA MARIA DEL MAR</option>
              <option value="SANTA ROSA">SANTA ROSA</option>
              <option value="SANTIAGO DE SURCO">SANTIAGO DE SURCO</option>
              <option value="SURQUILLO">SURQUILLO</option>
              <option value="VILLA EL SALVADOR">VILLA EL SALVADOR</option>
              <option value="VILLA MARIA DEL TRIUNFO">
                VILLA MARIA DEL TRIUNFO
              </option>
            </select>
          </div>
        </div>

        <!-- <div class="producto-campo">
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
        </div> -->
        <div class="d-flex justify-content-center">
          <input
            class="btn btn-danger btn-lg"
            type="submit"
            value="Actualizar"
          />
        </div>
      </div>
    </div>
  </form>
</template>

<script>
import router from "@/router";
import { store } from "@/store";

export default {
  name: "EditarProductoView",
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
    updateProduct() {
      console.log(this.product_id);
      fetch("http://127.0.0.1:5000/products/" + this.product_id, {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name: this.product.name,
          price: this.product.price,
          description: this.product.description,
          size: this.product.size,
          sex: this.product.sex,
          category: this.product.category,
          city: this.product.city,
        }),
      })
        .then((res) => res.json())
        .then((resJson) => {
          console.log(resJson);
          router.push("/producto/" + this.product_id);
        });
    },
  },
  mounted() {
    this.getProduct();
  },
};
</script>
