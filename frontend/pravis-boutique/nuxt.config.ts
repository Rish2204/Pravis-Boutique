// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  // Meta information
  app: {
    head: {
      title: process.env.NUXT_PUBLIC_APP_NAME || 'Pravis Boutique',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'description', content: process.env.NUXT_PUBLIC_APP_DESCRIPTION || 'Pravis Boutique E-commerce Platform' },
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
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
    '@vite-pwa/nuxt',
  ],
  
  // Static Site Generation and SSR settings
  nitro: {
    preset: process.env.NUXT_PUBLIC_DEPLOYMENT_PRESET || 'azure-static',
    prerender: {
      crawlLinks: true,
      routes: [
        '/',
        '/about',
        '/products',
        '/contact'
      ]
    },
    routeRules: {
      // Static generation for better SEO
      '/': { prerender: true },
      '/about': { prerender: true },
      '/products': { swr: 3600 },  // Regenerate every hour
      '/products/**': { swr: 3600 },
      '/api/**': { cors: true, headers: { 'access-control-allow-methods': 'GET,POST,PUT,DELETE' } }
    }
  },
  
  // Runtime config
  runtimeConfig: {
    // Private keys (server-side only)
    apiSecret: process.env.API_SECRET || '',
    
    // Public keys (exposed to client)
    public: {
      apiBaseUrl: process.env.NUXT_PUBLIC_API_BASE_URL || 'http://localhost:8000',
      apiVersion: process.env.NUXT_PUBLIC_API_VERSION || '/api/v1',
      appName: process.env.NUXT_PUBLIC_APP_NAME || 'Pravis Boutique',
      appDescription: process.env.NUXT_PUBLIC_APP_DESCRIPTION || 'Pravis Boutique E-commerce Platform',
      appVersion: process.env.NUXT_PUBLIC_APP_VERSION || '1.0.0',
      contactEmail: process.env.NUXT_PUBLIC_CONTACT_EMAIL || 'contact@pravis-boutique.com',
      enableVoiceAgent: process.env.NUXT_PUBLIC_ENABLE_VOICE_AGENT === 'true',
      enableAnalytics: process.env.NUXT_PUBLIC_ENABLE_ANALYTICS === 'true',
      authEnabled: process.env.NUXT_PUBLIC_AUTH_ENABLED === 'true',
    }
  },
  
  // PWA configuration
  pwa: {
    registerType: 'autoUpdate',
    manifest: {
      name: process.env.NUXT_PUBLIC_APP_NAME || 'Pravis Boutique',
      short_name: 'Pravis',
      description: process.env.NUXT_PUBLIC_APP_DESCRIPTION || 'Pravis Boutique E-commerce Platform',
      theme_color: '#ffffff',
      background_color: '#ffffff',
      display: 'standalone',
      orientation: 'portrait',
      scope: '/',
      start_url: '/',
      lang: 'en',
      dir: 'ltr',
      categories: ['shopping', 'lifestyle', 'e-commerce'],
      icons: [
        {
          src: 'icons/icon-64x64.png',
          sizes: '64x64',
          type: 'image/png'
        },
        {
          src: 'icons/icon-192x192.png',
          sizes: '192x192',
          type: 'image/png'
        },
        {
          src: 'icons/icon-512x512.png',
          sizes: '512x512',
          type: 'image/png',
          purpose: 'any'
        },
        {
          src: 'icons/maskable-icon-512x512.png',
          sizes: '512x512',
          type: 'image/png',
          purpose: 'maskable'
        }
      ]
    },
    workbox: {
      navigateFallback: '/',
      globPatterns: ['**/*.{js,css,html,png,svg,ico,webp,woff,woff2,ttf,eot}'],
      runtimeCaching: [
        {
          urlPattern: /^https:\/\/fonts\.googleapis\.com\/.*/i,
          handler: 'CacheFirst',
          options: {
            cacheName: 'google-fonts-cache',
            expiration: {
              maxEntries: 10,
              maxAgeSeconds: 60 * 60 * 24 * 365 // 1 year
            },
            cacheableResponse: {
              statuses: [0, 200]
            }
          }
        },
        {
          urlPattern: /^https:\/\/fonts\.gstatic\.com\/.*/i,
          handler: 'CacheFirst',
          options: {
            cacheName: 'google-fonts-cache',
            expiration: {
              maxEntries: 10,
              maxAgeSeconds: 60 * 60 * 24 * 365 // 1 year
            },
            cacheableResponse: {
              statuses: [0, 200]
            }
          }
        },
        {
          urlPattern: /\.(?:png|jpg|jpeg|svg|webp)$/i,
          handler: 'CacheFirst',
          options: {
            cacheName: 'images-cache',
            expiration: {
              maxEntries: 60,
              maxAgeSeconds: 60 * 60 * 24 * 30 // 30 days
            }
          }
        },
        {
          urlPattern: new RegExp('^' + process.env.NUXT_PUBLIC_API_BASE_URL || 'http://localhost:8000'),
          handler: 'NetworkFirst',
          options: {
            cacheName: 'api-cache',
            expiration: {
              maxEntries: 100,
              maxAgeSeconds: 60 * 60 * 24 // 1 day
            },
            networkTimeoutSeconds: 10,
            cacheableResponse: {
              statuses: [0, 200]
            }
          }
        }
      ],
      offlineAnalytics: true,
      skipWaiting: true,
      clientsClaim: true
    },
    devOptions: {
      enabled: true,
      type: 'module',
    },
  },
  
  // Development tools
  devtools: { enabled: true },
  
  // Vite configuration for allowing tunnel hosts
  vite: {
    server: {
      allowedHosts: 'all'  // Disable host checking for tunnels
    }
  },
})
