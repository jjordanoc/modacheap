<!-- <template>
  <label class="imagen_add w-100">
    <img src="@/assets/imagen_add.png" ref="imageSource" />
    <input
      type="file"
      class="file"
      name="file"
      accept="image/*"
      required
      @change="addImage($event)"
    />
  </label>
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
export default {
  name: "ImageInput",
  props: {
    images: {
      type: Array,
      required: true,
    },
  },
  methods: {
    addImage(event) {
      console.log(event);
      console.log(event.target.files[0]);
      this.images.push(event.target.files[0]);
      this.$refs.imageSource.src = URL.createObjectURL(event.target.files[0]);
    },
  },
};
</script>

<style></style> -->
