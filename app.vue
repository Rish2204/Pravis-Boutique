<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>

  <ClientOnly>
    <ConsentDialog @consentDecision="handleConsentDecision" />
  </ClientOnly>
</template>

<script setup lang="ts">
import ConsentDialog from '~/components/common/ConsentDialog.vue'

useHead({
  htmlAttrs: {
    lang: 'en'
  },
  bodyAttrs: {
    class: 'antialiased'
  },
  meta: [
    { charset: 'utf-8' },
    { name: 'viewport', content: 'width=device-width, initial-scale=1' },
    { name: 'description', content: 'Pravis Boutique - Premium handloom textiles and sarees' },
    { name: 'format-detection', content: 'telephone=no' },
    { name: 'theme-color', content: '#8B0000' },
  ],
  link: [
    { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
  ]
})

onErrorCaptured((err, _instance, info) => {
  console.error('Captured error:', err, info)
  return false
})

const handleConsentDecision = (decision: boolean) => {
  if (import.meta.client) {
    localStorage.setItem('pravis-consent', JSON.stringify({ consent: decision, timestamp: new Date().toISOString() }))
  }
}
</script>

<style>
:root {
  --pravis-primary: #8B0000;
  --pravis-gold: #D4AF37;
}

html {
  scroll-behavior: smooth;
  -webkit-tap-highlight-color: transparent;
}

body {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

*:focus-visible {
  outline: 2px solid var(--pravis-primary);
  outline-offset: 2px;
}
</style>
