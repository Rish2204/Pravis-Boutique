// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  // Enable TypeScript strict mode
  typescript: {
    strict: true,
    shim: false,
  },

  // Meta information
  app: {
    head: {
      title: 'Pravis Boutique - Premium Handloom Textiles | Drape in Elegance',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'description', content: 'Discover authentic Indian handloom textiles and sarees at Pravis Boutique. Premium quality, traditional craftsmanship, modern designs.' },
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
        { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
        { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: 'anonymous' },
        { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap' }
      ],
    },
    pageTransition: { name: 'page', mode: 'out-in' }
  },

  // Global CSS
  css: ['@/assets/css/main.css'],

  // Modules
  modules: [
    '@nuxtjs/tailwindcss',
    '@pinia/nuxt',
    '@vueuse/nuxt',
  ],

  // Static Site Generation and SSR settings
  nitro: {
    preset: process.env.NUXT_PUBLIC_DEPLOYMENT_PRESET || 'node-server',
    prerender: {
      crawlLinks: true,
      routes: [
        '/',
        '/shop',
        '/contact'
      ]
    },
    routeRules: {
      '/': { prerender: true },
      '/shop': { prerender: true },
      '/shop/**': { swr: 3600 },
      '/api/**': { cors: true, headers: { 'access-control-allow-methods': 'GET,POST,PUT,DELETE' } }
    }
  },

  // Runtime config
  runtimeConfig: {
    public: {
      appName: 'Pravis Boutique',
      appDescription: 'Pravis Boutique - Premium Handloom Textiles',
      appVersion: '2.0.0',
      contactEmail: 'contact@pravis-boutique.com',
    }
  },

  // Keep local storefront previews free of development overlays.
  devtools: { enabled: false },

  // Vite configuration
  vite: {
    server: {
      allowedHosts: 'all'
    }
  },
})
