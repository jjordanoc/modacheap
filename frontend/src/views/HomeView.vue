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
      <form
        class="d-flex m-2"
        role="search"
        action="/producto/buscar"
        method="GET"
      >
        <div class="input-group">
          <input
            class="form-control me-2"
            type="search"
            placeholder="Zapatos Adidas"
            aria-label="Search"
            name="buscar"
          />
          <input class="btn btn-outline-danger" type="submit" value="Buscar" />
        </div>
      </form>
      <div class="d-flex flex-row justify-content-center">
        <div class="dropdown-center m-4">
          <button
            class="btn btn-danger dropdown-toggle"
            type="button"
            id="menu-categoria"
            data-bs-toggle="dropdown"
            aria-expanded="false"
          ></button>
          <!-- <ul class="dropdown-menu",aria-labelledby="menu-categoria">
            <li><h6 class="dropdown-header">Seleccione la categoría</h6></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href={{url_for('producto_categoria', nombre_categoria='Abrigos' )}}>Abrigos</a>
            </li>
            <li><a class="dropdown-item" href={{url_for('producto_categoria', nombre_categoria='Polos' )}}>Polos</a>
            </li>
            <li><a class="dropdown-item" href={{url_for('producto_categoria', nombre_categoria='Pantalones'
                )}}>Pantalones</a></li>
            <li><a class="dropdown-item" href={{url_for('producto_categoria', nombre_categoria='Zapatos' )}}>Zapatos</a>
            </li>
            <li><a class="dropdown-item" href={{url_for('producto_categoria', nombre_categoria='Accesorios'
                )}}>Accesorios</a></li>
            <li><a class="dropdown-item" href={{url_for('producto_categoria', nombre_categoria='Vestidos' )}}>Vestidos</a>
            </li>
            <li><a class="dropdown-item" href={{url_for('producto_categoria', nombre_categoria='Blusas' )}}>Blusas</a>
            </li>
            <li><a class="dropdown-item" href={{url_for('producto_categoria', nombre_categoria='Invierno' )}}>Ropa de
                invierno</a></li>
        </ul> -->
        </div>

        <div class="dropdown-center m-4">
          <button
            class="btn btn-danger dropdown-toggle"
            type="button"
            id="menu-talla"
            data-bs-toggle="dropdown"
            aria-expanded="false"
          >
            Tipo
          </button>
          <!-- <ul class="dropdown-menu dropdown-menu-start",aria-labelledby="menu-talla">
            <li><h6 class="dropdown-header">Seleccione la talla</h6></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" type="button" href={{url_for('producto_talla', nombre_talla="XXS")}}>XXS</a></li>
            <li><a class="dropdown-item" type="button" href={{url_for('producto_talla', nombre_talla="XS")}}>XS</a></li>
            <li><a class="dropdown-item" type="button" href={{url_for('producto_talla', nombre_talla="S")}}>S</a></li>
            <li><a class="dropdown-item" type="button" href={{url_for('producto_talla', nombre_talla="M")}}>M</a></li>
            <li><a class="dropdown-item" type="button" href={{url_for('producto_talla', nombre_talla="L")}}>L</a></li>
            <li><a class="dropdown-item" type="button" href={{url_for('producto_talla', nombre_talla="XL")}}>XL</a></li>
            <li><a class="dropdown-item" type="button" href={{url_for('producto_talla', nombre_talla="XXL")}}>XXL</a></li>
        </ul> -->
        </div>

        <div class="dropdown-center m-4">
          <button
            class="btn btn-danger dropdown-toggle"
            type="button"
            id="menu-genero"
            data-bs-toggle="dropdown"
            aria-expanded="false"
          >
            Género
          </button>
          <!-- <ul class="dropdown-menu dropdown-menu-start",aria-labelledby="menu-genero">
            <li><h6 class="dropdown-header">Seleccione el género</h6></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" type="button" href={{url_for('producto_genero', nombre_genero="M")}}>Hombre</a></li>
            <li><a class="dropdown-item" type="button" href={{url_for('producto_genero', nombre_genero="F")}}>Mujer</a></li>
            <li><a class="dropdown-item" type="button" href={{url_for('producto_genero', nombre_genero="U")}}>Unisex</a></li>
        </ul> -->
        </div>
      </div>
    </div>
  </div>

  <div class="row w-100">
    <div class="col-2"></div>
    <div class="col-8" ,style="background-color:#;">
      <div class="d-flex justify-content-between">
        <strong>{{ productos }} producto(s) disponibles</strong>
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
          <!-- <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
          <li><a class="dropdown-item" href="{{url_for('ordenar_criterio' , criterio='precio', orden='desc')}}">Menor Precio</a></li>
          <li><a class="dropdown-item" href="{{url_for('ordenar_criterio' , criterio='precio', orden='asc')}}">Mayor Precio</a></li>
          <li><a class="dropdown-item" href="{{url_for('ordenar_criterio' , criterio='nombre', orden='asc')}}">Alfabeto (Ascendente)</a></li>
          <li><a class="dropdown-item" href="{{url_for('ordenar_criterio' , criterio='nombre', orden='desc')}}">Alfabeto (Descendente)</a></li>
        </ul> -->
        </div>
      </div>
      <br />
      <!-- Productos -->
      <!-- {% if productos %} -->
      <div class="row row-cols-1 row-cols-md-3 g-3">
        <!-- {% for producto in productos %} -->
        <a
          href="/"
          style="text-decoration: none; color: var(--text-color)"
          class="col"
        >
          <div class="card">
            <img src="" class="card-img-top" width="15" height="280" />
            <div class="card-body">
              <h5 class="card-title">{{ producto.nombre }}</h5>
              <p class="card-text1">
                <!-- Talla: {{ producto.talla }} <br />
                {% if producto.sexo == "M" %} Género: Hombre <br />
                {% elif producto.sexo == "F" %} Género: Mujer <br />
                {% else %} Género: Unisex <br />
                {% endif %} Distrito: {{ producto.distrito }} -->
              </p>
              <p class="card-text4">Precio: S./{{ producto.precio }}</p>
            </div>
          </div>
        </a>
        <!-- {% endfor %} -->
      </div>
      <!-- {% else %} -->
      <p class="fs-3">
        No se encontraron resultados. ¡Te animamos a vender productos de este
        tipo! <br />
      </p>
      <!-- {% endif %} -->
    </div>
    <div class="col-2"></div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: "HomeView",
  methods: {
    getProducts() {
      fetch("http://127.0.0.1:5000/products", {
        method: "GET",
      })
        .then((res) => res.json())
        .then((resJson) => {
          console.log(resJson);
        });
    },
  },
  mounted() {
    this.getProducts();
  },
};
</script>