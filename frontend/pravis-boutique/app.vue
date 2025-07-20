<template>
  <div id="app">
    <NuxtPage />
  </div>
</template>

<script setup>
// Global app configuration
useHead({
  htmlAttrs: {
    lang: 'en'
  },
  bodyAttrs: {
    class: 'antialiased'
  }
})

// Initialize analytics on app start
const { init: initAnalytics } = useAnalytics()
onMounted(() => {
  initAnalytics()
})
</script>

<style>
/* Global styles are handled in assets/css/main.css */
</style>
