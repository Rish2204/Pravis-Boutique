/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './components/**/*.{js,vue,ts}',
    './layouts/**/*.vue',
    './pages/**/*.vue',
    './plugins/**/*.{js,ts}',
    './app.vue',
    './error.vue'
  ],
  theme: {
    extend: {
      colors: {
        // Pravis Brand Colors - Handloom Maroon & Gold Theme
        pravis: {
          50: '#FDF2F8',   // Light rosy background
          100: '#F8E8EC',  // Very light pink
          200: '#E8BAC2',  // Light gold-pink accent for hover states
          300: '#D4AF37',  // Gold accent color
          400: '#B8860B',  // Dark gold
          500: '#8B0000',  // Primary maroon color (brand main)
          600: '#A0001C',  // Slightly brighter maroon for hover/emphasis
          700: '#7F0000',  // Deep maroon
          800: '#5F0000',  // Dark maroon for accents
          900: '#3F0000',  // Very dark maroon
          950: '#1F0000',  // Almost black maroon
        },
        // Additional handloom colors
        indigo: {
          50: '#f0f4ff',
          100: '#e0e9ff',
          200: '#c7d6fe',
          300: '#a5b8fc',
          400: '#8b94f8',
          500: '#6366f1',   // Traditional indigo
          600: '#4f46e5',
          700: '#4338ca',
          800: '#3730a3',
          900: '#312e81',
        },
        saffron: {
          50: '#fffbf5',
          100: '#fff4e6',
          200: '#ffe4b8',
          300: '#ffce7a',
          400: '#ffb347',
          500: '#ff9500',   // Saffron orange
          600: '#e6850e',
          700: '#cc7a00',
          800: '#996600',
          900: '#664400',
        },
        // Social media colors for sharing buttons
        facebook: '#1877f2',
        twitter: '#1da1f2',
        pinterest: '#e60023',
        instagram: '#e1306c',
      },
      fontFamily: {
        // Font families - add your own custom fonts
        sans: [
          'Inter',
          'ui-sans-serif',
          'system-ui',
          '-apple-system',
          'BlinkMacSystemFont',
          'Segoe UI',
          'Roboto',
          'Helvetica Neue',
          'Arial',
          'sans-serif',
        ],
        display: [
          'Playfair Display',
          'ui-serif',
          'Georgia',
          'Cambria',
          'Times New Roman',
          'serif',
        ],
      },
      spacing: {
        // Custom spacing for consistent design
        '128': '32rem',
        '144': '36rem',
      },
      borderRadius: {
        // Custom border radius
        '4xl': '2rem',
      },
      typography: (theme) => ({
        DEFAULT: {
          css: {
            maxWidth: 'none',
            color: theme('colors.gray.700'),
            a: {
              color: theme('colors.pravis.600'),
              '&:hover': {
                color: theme('colors.pravis.700'),
              },
            },
            'h1, h2, h3, h4': {
              color: theme('colors.gray.900'),
              fontWeight: theme('fontWeight.bold'),
            },
            // Dark mode adjustments
            '.dark &': {
              color: theme('colors.gray.300'),
              'h1, h2, h3, h4': {
                color: theme('colors.white'),
              },
              a: {
                color: theme('colors.pravis.400'),
                '&:hover': {
                  color: theme('colors.pravis.300'),
                },
              },
            },
          },
        },
      }),
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('@tailwindcss/forms'),
    require('@tailwindcss/aspect-ratio'),
  ],
  // Support dark mode
  darkMode: 'class',
};
