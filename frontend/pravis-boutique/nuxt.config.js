export default defineNuxtConfig({
  // PWA Configuration
  modules: [
    '@vite-pwa/nuxt',
    '@nuxtjs/tailwindcss',
    '@vueuse/nuxt',
    '@pinia/nuxt'
  ],

  // PWA Settings
  pwa: {
    icon: {
      fileName: 'icon.png'
    },
    manifest: {
      name: 'Pravis Boutique',
      short_name: 'Pravis',
      description: 'AI-powered boutique shopping experience with voice agent',
      theme_color: '#3498db',
      background_color: '#ffffff',
      display: 'standalone',
      start_url: '/',
      icons: [
        {
          src: '/icon-192x192.png',
          sizes: '192x192',
          type: 'image/png'
        },
        {
          src: '/icon-512x512.png',
          sizes: '512x512',
          type: 'image/png'
        }
      ]
    },
    workbox: {
      globPatterns: ['**/*.{js,css,html,png,jpg,jpeg,svg,gif,webp}']
    }
  },

  // CSS Framework
  css: [
    '~/assets/css/main.css'
  ],

  // Head configuration
  app: {
    head: {
      title: 'Pravis Boutique - AI-Powered Fashion',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'description', content: 'Experience fashion with our AI voice agent Ask Pravi. Discover, shop, and get personalized recommendations.' },
        { name: 'keywords', content: 'boutique, fashion, AI, voice agent, shopping, Hyderabad' },
        { property: 'og:title', content: 'Pravis Boutique - AI-Powered Fashion' },
        { property: 'og:description', content: 'Experience fashion with our AI voice agent Ask Pravi' },
        { property: 'og:image', content: '/og-image.jpg' },
        { name: 'twitter:card', content: 'summary_large_image' }
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
        { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
        { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' },
        {
          href: 'https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap',
          rel: 'stylesheet'
        }
      ]
    }
  },

  // Runtime configuration
  runtimeConfig: {
    // Server-side environment variables
    backendUrl: process.env.BACKEND_URL || 'http://localhost:8000',
    openaiApiKey: process.env.OPENAI_API_KEY,

    // Client-side environment variables (exposed to frontend)
    public: {
      apiBase: process.env.NUXT_PUBLIC_API_BASE || '/api',
      voiceEnabled: process.env.NUXT_PUBLIC_VOICE_ENABLED || 'true',
      analyticsEnabled: process.env.NUXT_PUBLIC_ANALYTICS_ENABLED || 'true'
    }
  },

  // Nitro configuration for API routes
  nitro: {
    devProxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        prependPath: true
      }
    }
  },

  // Development configuration
  devtools: { enabled: true },

  // Enable network access for iPad testing
  devServer: {
    host: '0.0.0.0', // Allow external connections
    port: 3000
  },

  // Build configuration
  build: {
    transpile: ['@vueuse/core']
  },

  // Tailwind CSS configuration
  tailwindcss: {
    config: {
      theme: {
        extend: {
          fontFamily: {
            display: ['Playfair Display', 'serif'],
            body: ['Inter', 'sans-serif']
          },
          colors: {
            pravis: {
              50: '#fdf2f8',
              100: '#fce7f3',
              200: '#fbcfe8',
              300: '#f9a8d4',
              400: '#f472b6',
              500: '#8B0000', // Deep maroon red - primary
              600: '#A0001C', // Vibrant maroon red
              700: '#7F0000', // Dark maroon
              800: '#5F0000', // Darker maroon
              900: '#3F0000' // Darkest maroon
            },
            gold: {
              50: '#fffbeb',
              100: '#fef3c7',
              200: '#fde68a',
              300: '#fcd34d',
              400: '#fbbf24',
              500: '#D4AF37', // Golden color
              600: '#B8860B', // Dark golden rod
              700: '#996F00',
              800: '#7A5600',
              900: '#5B4000'
            }
          }
        }
      }
    }
  }
})
