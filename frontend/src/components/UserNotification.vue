<template>
  <div
    v-if="show"
    :class="`alert alert-${category} d-flex justify-content-center`"
    role="alert"
  >
    <p v-show="show">{{ message }}</p>
  </div>
</template>

<script>
import { store } from "@/store";

export default {
  name: "UserNotification",
  props: ["message", "category", "show"],
  watch: {
    show() {
      setTimeout(() => {
        store.showNotification = false;
        store.notificationMessage = "";
        store.notificationCategory = "";
      }, 5000);
    },
  },
};
</script>
