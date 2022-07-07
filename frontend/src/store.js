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
          router.push("/");
        } else {
          this.displayNotification(resJson["message"], "danger");
        }
      });
  },
  displayNotification(message, category) {
    this.showNotification = true;
    this.notificationMessage = message;
    this.notificationCategory = category;
  },
  showNotification: false,
  notificationMessage: "",
  notificationCategory: "",
});
