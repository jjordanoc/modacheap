<template>
  <div class="row w-100"></div>
  <div
    src="@/assets/background.jpeg"
    id="main-banner"
    class="d-flex flex-column align-items-center justify-content-center"
  >
    <div
      class="fst-italic d-flex flex-column align-items-center justify-content-center"
    >
      <p id="search-description">
        Encuentra una prenda <strong>a tu medida</strong>
      </p>
      <form class="d-flex m-2" role="search" @submit.prevent="searchProducts()">
        <div class="input-group">
          <input
            class="form-control me-2"
            type="search"
            placeholder="Zapatos Adidas"
            aria-label="Search"
            name="buscar"
            v-model="query"
          />
          <input class="btn btn-outline-danger" type="submit" value="Buscar" />
        </div>
      </form>
      <div class="d-flex flex-row justify-content-center">
        <div
          class="dropdown-center m-4"
          v-for="filter in ['category', 'size', 'sex']"
          :key="filter"
        >
          <button
            class="btn btn-danger dropdown-toggle"
            type="button"
            id="menu-categoria"
            data-bs-toggle="dropdown"
            aria-expanded="false"
          >
            {{ dataName[filter][0] }}
          </button>
          <ul class="dropdown-menu" aria-labelledby="menu-categoria">
            <li>
              <h6 class="dropdown-header">
                Seleccione {{ dataName[filter][1] }}
              </h6>
            </li>
            <li><hr class="dropdown-divider" /></li>
            <li v-for="data in filterData[filter]" :key="data">
              <button class="dropdown-item" @click="filterBy(filter, data)">
                {{ data }}
              </button>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <div class="row w-100">
    <div class="col-2"></div>
    <div class="col-8">
      <div id="product-cards" class="d-flex justify-content-between">
        <strong
          >{{ productsData.products.length }} producto(s) disponibles</strong
        >
        <!-- Ordenar por -->
        <div class="dropdown">
          <button
            class="btn btn-secondary dropdown-toggle"
            type="button"
            id="dropdownMenuButton"
            data-bs-toggle="dropdown"
            aria-expanded="false"
          >
            <strong>Ordenar por</strong>
          </button>
          <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
            <li
              v-for="option in [
                'Menor Precio',
                'Mayor Precio',
                'Alfabeto (A-Z)',
                'Alfabeto (Z-A)',
              ]"
              :key="option"
            >
              <button class="dropdown-item" @click="orderBy(option)">
                {{ option }}
              </button>
            </li>
          </ul>
        </div>
      </div>
      <br />
      <!-- Productos -->
      <div
        class="row row-cols-1 row-cols-md-3 g-3"
        v-if="productsData.products.length"
      >
        <router-link
          v-for="product in productsData.products"
          :key="product.id"
          :to="{
            name: 'producto',
            params: {
              product_id: product.id,
            },
          }"
          style="text-decoration: none; color: var(--text-color)"
          class="col"
        >
          <div class="card">
            <img
              :src="
                product.images[0]
                  ? `http://127.0.0.1:5000/static/uploaded/${product.images[0].id}`
                  : require('@/assets/imagen_add.png')
              "
              class="card-img-top"
              width="15"
              height="280"
            />
            <div class="card-body">
              <h5 class="card-title">{{ product.name }}</h5>
              <div class="card-text1">
                Talla: {{ product.size }} <br />
                <div class="genero" v-if="product.sex === 'M'">
                  Género: Masculino
                </div>
                <div class="genero" v-if="product.sex === 'F'">
                  Género: Femenino
                </div>
                <div class="genero" v-if="product.sex === 'U'">
                  Género: Unisex
                </div>
                Distrito: {{ product.city }}
              </div>
              <br />
              <p class="card-text4">Precio: S./{{ product.price }}</p>
            </div>
          </div>
        </router-link>
      </div>
      <p class="fs-3" v-else>
        No se encontraron resultados. ¡Te animamos a vender productos de este
        tipo! <br />
      </p>
    </div>
    <div class="col-2"></div>
  </div>
</template>

<script>
import { store } from "@/store";

export default {
  name: "HomeView",
  data() {
    return {
      productsData: {
        count: 0,
        products: [],
        filtered: [],
        searched: [],
      },
      dataName: {
        category: ["Categoría", "la categoría"],
        size: ["Talla", "la talla"],
        sex: ["Género", "el género"],
      },
      filterData: {
        category: [
          "Abrigos",
          "Polos",
          "Pantalones",
          "Zapatos",
          "Accesorios",
          "Vestidos",
          "Blusas",
          "Invierno",
        ],
        size: ["XXS", "XS", "S", "M", "L", "XL", "XXL"],
        sex: ["F", "M", "U"],
      },
      query: "",
    };
  },
  methods: {
    getProducts() {
      fetch("http://127.0.0.1:5000/products", {
        method: "GET",
      })
        .then((res) => res.json())
        .then((resJson) => {
          if (resJson["success"]) {
            this.productsData = resJson;
            this.productsData.original = this.productsData.products;
          } else {
            store.displayNotification(resJson["message"], "danger");
          }
        });
    },
    searchProducts() {
      this.productsData.products = this.productsData.original;
      this.productsData.searched = [];
      for (
        let producto = 0;
        this.productsData.products[producto] !== undefined;
        producto++
      ) {
        if (
          this.productsData.products[producto]["name"]
            .toLowerCase()
            .search(this.query.toLowerCase()) !== -1
        ) {
          this.productsData.searched.push(this.productsData.products[producto]);
        }
        location.href = "#product-cards";
      }
      this.productsData.products = this.productsData.searched;
    },
    filterBy(attribute, category) {
      this.productsData.products = this.productsData.original;
      this.productsData.products = this.productsData.products.filter(function (
        product
      ) {
        return product[attribute] == category;
      });
    },
    orderBy(option) {
      this.productsData.products.sort((p1, p2) => {
        let fa, fb;
        if (option === "Menor Precio" || option === "Mayor Precio") {
          fa = p1.price;
          fb = p2.price;
        } else if (option === "Alfabeto (A-Z)" || option === "Alfabeto (Z-A)") {
          fa = p1.name.toLowerCase();
          fb = p2.name.toLowerCase();
        }
        if (option === "Menor Precio" || option === "Alfabeto (A-Z)") {
          if (fa < fb) {
            return -1;
          }
          if (fa > fb) {
            return 1;
          }
        } else if (option === "Mayor Precio" || option === "Alfabeto (Z-A)") {
          if (fa > fb) {
            return -1;
          }
          if (fa < fb) {
            return 1;
          }
        }
        return 0;
      });
    },
  },
  mounted() {
    this.getProducts();
  },
};
</script>
