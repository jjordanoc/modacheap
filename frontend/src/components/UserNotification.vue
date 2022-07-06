<template>
  <div
    v-show="show"
    class="alert alert-{{category}} alert-dismissible fade show d-flex justify-content-center"
    role="alert"
  >
    {{ message
    }}<button
      type="button"
      class="btn-close"
      data-bs-dismiss="alert"
      aria-label="Close"
    ></button>
  </div>
</template>

<script>
export default {
  name: "UserNotification",
  props: ["message", "category", "show"],
};
</script>
