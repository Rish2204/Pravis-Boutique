<template>
  <div>
    <!-- Redirect to shop index -->
    <NuxtPage />
  </div>
</template>

<script>
export default {
  mounted() {
    // Redirect to simple shop page
    this.$router.replace('/shop/simple')
  }
}
</script>
