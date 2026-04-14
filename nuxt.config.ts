export default defineNuxtConfig({
  devtools: { enabled: false },
  compatibilityDate: '2024-11-01',

  modules: [
    '@nuxtjs/tailwindcss',
    '@nuxtjs/google-fonts',
    '@pinia/nuxt',
  ],

  app: {
    head: {
      title: 'Pravis Boutique — Drape in Elegance',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'description', content: 'Premium Indian handloom textiles and sarees. Authentic artisanship, sustainable practices, fair trade.' },
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      ],
    },
    pageTransition: { name: 'page', mode: 'out-in' },
  },

  googleFonts: {
    families: {
      'Playfair+Display': {
        wght: [400, 700],
        ital: [400],
      },
      Inter: [300, 400, 500, 600, 700],
    },
    display: 'swap',
  },

  tailwindcss: {
    configPath: 'tailwind.config.ts',
  },

  css: ['~/assets/css/main.css'],
})
