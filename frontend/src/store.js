import { reactive } from "vue";
import router from "./router";

export const store = reactive({
  user: {},
  isAuthenticated: false,
  login(email, password) {
    fetch("http://127.0.0.1:5000/login", {
      method: "POST",
      body: JSON.stringify({
        email: email,
        password: password,
      }),
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((res) => res.json())
      .then((resJson) => {
        if (resJson["success"]) {
          this.isAuthenticated = true;
          this.user = resJson["user"];
          console.log("Authenticated user");
          router.push("/");
        } else {
          console.log(resJson);
          this.displayNotification("A", "warning");
        }
      });
  },
  displayNotification(message, category) {
    this.showNotification = true;
    this.notificationMessage = message;
    this.notificationCategory = category;
  },
  hideNotification() {
    this.notificationMessage = "";
    this.notificationCategory = "";
    this.showNotification = false;
  },
  showNotification: false,
  notificationMessage: "",
  notificationCategory: "",
});
