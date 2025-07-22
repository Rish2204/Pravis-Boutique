<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
  
  <!-- Consent Dialog shown on first visit -->
  <ClientOnly>
    <ConsentDialog @consentDecision="handleConsentDecision" />
  </ClientOnly>
</template>

<script setup>
import { useAnalyticsStore } from '~/store/analytics'
import ConsentDialog from '~/components/common/ConsentDialog.vue'

// Global app configuration
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
    { name: 'description', content: 'Pravis Boutique - Your AI-powered guide to exquisite handlooms' },
    { name: 'format-detection', content: 'telephone=no' },
    { name: 'theme-color', content: '#0ea5e9' }, // PWA theme color
    { name: 'apple-mobile-web-app-capable', content: 'yes' }, // iOS fullscreen PWA
    { name: 'apple-mobile-web-app-status-bar-style', content: 'black-translucent' } // iOS status bar style
  ],
  link: [
    { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
    { rel: 'apple-touch-icon', sizes: '180x180', href: '/icons/apple-touch-icon.png' }
  ]
})

// Set up global error handling
onErrorCaptured((err, instance, info) => {
  console.error('Captured error:', err)
  
// Report to analytics if consent is given
  if (process.client && analyticsStore.hasConsent) {
    analyticsStore.trackInteraction('error', 'error_occurred', {
      error: err.message || String(err),
      component: instance?.$options?.name || 'unknown',
      info,
      url: window.location.href
    })
  }
  
  // Let error propagate to be caught by the Nuxt error page
  return false
})

// Initialize analytics on app start
const analyticsStore = useAnalyticsStore()

onMounted(() => {
  if (process.client) {
    // Initialize analytics store
    analyticsStore.initialize()
  }
})

// Handle consent decision from dialog
const handleConsentDecision = (decision) => {
  console.log('Consent decision:', decision)
}
</script>

<style>
/* Global styles are handled in assets/css/main.css */
:root {
  --pravis-primary: #0ea5e9;
  --pravis-primary-dark: #0369a1;
}

html {
  scroll-behavior: smooth;
  -webkit-tap-highlight-color: transparent;
}

body {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* Focus styles for keyboard navigation */
*:focus-visible {
  outline: 2px solid var(--pravis-primary);
  outline-offset: 2px;
}
</style>
