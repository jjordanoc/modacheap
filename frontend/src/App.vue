<template>
  <TheNavigation />
  <UserNotification
    :show="store.showNotification"
    :category="store.notificationCategory"
    :message="store.notificationMessage"
  />
  <router-view />
</template>

<script>
import TheNavigation from "./components/TheNavigation.vue";
import UserNotification from "./components/UserNotification.vue";
import { store } from "./store";
export default {
  name: "App",
  components: { TheNavigation, UserNotification },
  data() {
    return {
      store,
    };
  },
};
</script>

<style>
* {
  --title-color: #d40b0b;
  --main-background-color: #f6f6f8;
  --text-color: #242736;
  --title-font: "Caveat", cursive;
  --text-font: "Josefin Sans", sans-serif;
}

#main-navbar {
  background-color: transparent;
}

#main-background {
  width: 100%;
  height: 100vh;
  background: url("https://www.contreebute.com/hs-fs/hubfs/photo-1512436991641-6745cdb1723f.jpeg?width=800&name=photo-1512436991641-6745cdb1723f.jpeg")
    no-repeat center fixed;
  background-size: cover;
  background-blend-mode: multiply;
  background-color: rgb(120, 120, 120);
}

#main-banner {
  background: url("https://www.contreebute.com/hs-fs/hubfs/photo-1512436991641-6745cdb1723f.jpeg?width=800&name=photo-1512436991641-6745cdb1723f.jpeg")
    no-repeat center fixed;
  background-size: cover;
  background-blend-mode: multiply;
  background-color: rgb(120, 120, 120);
  padding: 0;
  height: 400px;
  margin-bottom: 40px;
}

#vender-form {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}

body {
  font-family: var(--text-font);
  color: var(--text-color);
  background-color: var(--main-background-color);
  margin: 0;
}

#main-title {
  color: var(--title-color);
  font-family: var(--title-font);
  font-size: 6em;
}

#main-description {
  color: white;
  font-size: 2em;
}

#search-description {
  color: white;
  font-size: 3em;
}

.producto-imagen {
  width: 40%;
}

.form-header h1 {
  font-size: 30px;
  text-align: center;
  color: black;
  padding: 20px 0;
  border-bottom: 2px solid black;
}

.top {
  background-color: var(--main-bg-color);
  color: var(--logo-color);
}

.box {
  padding: 10px 40px;
  color: black;
}
.box .subtitle {
  color: #90ba1b;
  font-size: 17px;
  font-weight: bold;
}

.form-bottom {
  background-color: blue;
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;
  padding: 10px 40px;
  text-align: right;
  border-top: 2px solid black;
}

.another {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.change {
  background-color: white;
  border: 2px solid black;
  padding: 5px 10px;
  text-align: center;
  display: inline-block;
  font-size: 20px;
  margin: 10px 30px;
  cursor: pointer;
}
.text-input {
  padding: 20px;
}

.submit-input {
  cursor: pointer;

  color: black;
  padding: 10px 25px;
  background-color: white;
  border: none;
}

/* Para slide de producto */
.slider {
  width: 500px;
  height: 400px;
  overflow: hidden;
}

.mid {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.navigation {
  display: flex;
  position: relative;
  top: -50px;
  left: 160px;
}

.bar {
  width: 50px;
  height: 10px;
  border: 1px solid var(--title-color);
  margin: 6px;
  cursor: pointer;
  transition: 0.4s;
}

.bar:hover {
  background: var(--title-color);
}

input[name="r"] {
  position: absolute;
  visibility: hidden;
}

.slides {
  width: 500%;
  height: 100%;
  display: flex;
}

.slide {
  width: 20%;
  transition: 0.6s;
}

.slide img {
  width: 100%;
  height: 100%;
}

#r1:checked ~ .s1 {
  margin-left: 0;
}

#r2:checked ~ .s1 {
  margin-left: -20%;
}

#r3:checked ~ .s1 {
  margin-left: -40%;
}

/* Para el pequeño banner */
.banner-box {
  font-size: 20px;
  font-weight: bold;
  opacity: 0;
  position: absolute;
  width: 100%;
  text-align: center;
}

.banner-text {
  background-color: black;
  color: white;
}

.b1 {
  animation: ani1 15s infinite;
}
.b2 {
  animation: ani2 15s infinite;
}
.b3 {
  animation: ani3 15s infinite;
}
.b4 {
  animation: ani4 15s infinite;
}
.b5 {
  animation: ani5 15s infinite;
}

@keyframes ani1 {
  0% {
    opacity: 0;
  }
  10% {
    opacity: 1;
  }
  20% {
    opacity: 0;
  }
}

@keyframes ani2 {
  20% {
    opacity: 0;
  }
  30% {
    opacity: 1;
  }
  40% {
    opacity: 0;
  }
}

@keyframes ani3 {
  40% {
    opacity: 0;
  }
  50% {
    opacity: 1;
  }
  60% {
    opacity: 0;
  }
}

@keyframes ani4 {
  60% {
    opacity: 0;
  }
  70% {
    opacity: 1;
  }
  80% {
    opacity: 0;
  }
}

@keyframes ani5 {
  80% {
    opacity: 0;
  }
  90% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}

/* Top page */

.inicio {
  background-color: whitesmoke;
}

.space {
  background-color: black;
  height: 20px;
}

.topButton {
  border-color: red;
  background-color: white;
  width: 200px;
  height: 40px;
}
.card-text3 {
  display: inline;
}

.card-text4 {
  text-align: right;
  color: red;
}

.card {
  font-family: "Josefin Sans", sans-serif;
}

.flex {
  font-family: "Josefin Sans", sans-serif;
  padding: 5%;
}

#button_crear {
  padding: 3%;
  background-color: #0f209e;
  width: 120px;
}

.producto-campo h2 {
  color: var(--title-color);
}

.producto-campo {
  width: 400px;
  margin: 10px;
  padding: 20px;
  border: 3px solid var(--text-color);
  box-shadow: 10px 5px 5px black;
  box-sizing: content-box;
}

a:link {
  text-decoration: none;
}

.whatsapp-logo {
  display: flex;
  flex-direction: row;
  align-items: center;
  height: 50px;
  background-color: #53ce60;
  color: black;
}

.whatsapp-logo img {
  width: 50px;
  height: 50px;
}

.whatsapp-logo p {
  margin: 0;
}

.hidden {
  display: none !important;
}

.imagen_add {
  border: none;
  margin: 0;
  padding: 0;
  height: 100%;
}

.imagen-bg {
  background-color: black;
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: center;
}

#message,
#alert {
  margin: 0;
  user-select: none;
}

.nav-link {
  user-select: none;
}

footer {
  color: white;
  background-color: #222;
  padding: 3rem;
  clear: both;
}

footer a {
  color: white;
  margin: 0;
  text-decoration: none;
  float: right;
}

footer a:hover {
  color: cornflowerblue;
}
</style>
