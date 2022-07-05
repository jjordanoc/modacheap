<template>
  <div class="d-flex flex-column align-items-center">
    <h1 class="mt-4">Vende un producto</h1>
    <form id="vender-form" class="flex-wrap" @submit.prevent="createProduct()">
      <div class="d-flex flex-row justify-content-center mt-4">
        <div class="m-3 d-flex flex-column producto-imagen">
          <div class="imagen-bg">
            <div class="slider">
              <div class="slides">
                <input type="radio" name="r" id="r3" checked />
                <input type="radio" name="r" id="r2" checked />
                <input type="radio" name="r" id="r1" checked />
                <div class="slide s1">
                  <label class="imagen_add w-100">
                    <img
                      src="@/assets/imagen_add.png"
                      id="imagen_1"
                      ref="imageSource1"
                    />
                    <input
                      class="file"
                      type="file"
                      id="file1"
                      name="file1"
                      accept="image/*"
                      required
                      @change="addImage(1, $event)"
                    />
                  </label>
                </div>
                <div class="slide">
                  <label class="imagen_add w-100">
                    <img
                      src="@/assets/imagen_add.png"
                      id="imagen_2"
                      ref="imageSource2"
                    />
                    <input
                      class="file"
                      type="file"
                      id="file2"
                      name="file2"
                      accept="image/*"
                      required
                      @change="addImage(2, $event)"
                    />
                  </label>
                </div>

                <div class="slide">
                  <label class="imagen_add w-100">
                    <img
                      src="@/assets/imagen_add.png"
                      id="imagen_3"
                      ref="imageSource3"
                    />
                    <input
                      class="file"
                      type="file"
                      id="file3"
                      name="file3"
                      accept="image/*"
                      required
                      @change="addImage(3, $event)"
                    />
                  </label>
                </div>
              </div>
              <div class="d-flex navigation">
                <label for="r1" class="bar"></label>
                <label for="r2" class="bar"></label>
                <label for="r3" class="bar"></label>
              </div>
            </div>
          </div>

          <!-- <input
            type="file"
            id="file2"
            name="file2"
            accept="image/*"
            required
            @change="addImage($event)"
          />
          <input
            type="file"
            id="file3"
            name="file3"
            accept="image/*"
            required
            @change="addImage($event)"
          /> -->
          <p>Incluye 3 imágenes del producto.</p>

          <div class="d-flex flex-column mt-4">
            <h3>Descripción</h3>

            <div class="form-group mb-3 me-auto p-2 flex-fill">
              <label for="descripcion" class="form-label"
                >Incluye una descripción breve:</label
              >
              <textarea
                id="descripcion"
                name="descripcion"
                required
                class="form-control border-primary"
                cols="50"
                v-model="description"
              ></textarea>
            </div>
          </div>
        </div>
        <div class="d-flex flex-column">
          <div class="producto-campo">
            <div class="form-group mb-3">
              <label for="nombre" class="form-label"
                >Nombre del producto:</label
              >
              <input
                type="text"
                id="nombre"
                name="nombre"
                required
                class="form-control"
                minlength="5"
                maxlength="80"
                v-model="name"
              />
            </div>

            <div class="form-group mb-3">
              <label for="precio" class="form-label">Precio:</label>
              <input
                type="number"
                min="0"
                max="99999"
                id="precio"
                name="precio"
                step="any"
                required
                class="form-control"
                v-model="price"
              />
            </div>

            <div class="form-group mb-3">
              <label for="talla">Talla de la prenda:</label>
              <select
                name="talla"
                id="talla"
                required
                class="form-select"
                v-model="size"
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
              <label for="sexo">Género de la prenda:</label>
              <select
                name="sexo"
                id="sexo"
                required
                class="form-select"
                v-model="sex"
              >
                <option disabled value="">Seleccionar</option>
                <option value="M">Hombre</option>
                <option value="F">Mujer</option>
                <option value="U">Unisex</option>
              </select>
            </div>

            <div class="form-group mb-3">
              <label for="categoria">Categoría de la prenda:</label>
              <select
                name="categoria"
                id="categoria"
                required
                class="form-select"
                v-model="category"
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
              <label for="distrito">Distrito en el que se encuentra:</label>
              <select
                name="distrito"
                id="distrito"
                required
                class="form-select"
                v-model="city"
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
                <option value="SAN MARTIN DE PORRES">
                  SAN MARTIN DE PORRES
                </option>
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
            <input type="submit" value="Crear" class="btn btn-danger w-100" />
          </div>
        </div>
      </div>
    </form>
  </div>
</template>

<style>
.file {
  display: none;
}
.imagen_add:hover {
  cursor: pointer;
}
</style>

<script>
import router from "@/router";
import { store } from "@/store";

export default {
  name: "VenderView",
  data() {
    return {
      description: "",
      name: "",
      price: 0,
      size: "",
      sex: "",
      city: "",
      category: "",
      images: [],
      store,
    };
  },
  methods: {
    createProduct() {
      fetch("http://127.0.0.1:5000/products", {
        method: "POST",
        body: JSON.stringify({
          description: this.description,
          name: this.name,
          price: this.price,
          size: this.size,
          sex: this.sex,
          city: this.city,
          category: this.category,
          user_id: this.store.user.id,
        }),
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((res) => res.json())
        .then((resJson) => {
          if (resJson["success"]) {
            // add images to server
            this.images.forEach((file) => {
              console.log(file);
              let formData = new FormData();
              formData.append("file", file, file.name);
              formData.append("product_id", resJson["product_id"]);
              console.log(resJson);
              fetch(
                `http://127.0.0.1:5000/products/${resJson["product_id"]}/images`,
                {
                  method: "POST",
                  body: formData,
                  headers: {},
                }
              );
            });
            console.log(resJson);
            router.push("/");
          } else {
            console.log(resJson);
          }
        });
    },
    addImage(num, event) {
      console.log(event);
      console.log(event.target.files[0]);
      this.images.push(event.target.files[0]);
      console.log(this.$refs, "imageSource" + num);
      this.$refs["imageSource" + num].src = URL.createObjectURL(
        event.target.files[0]
      );
    },
  },
};
</script>
