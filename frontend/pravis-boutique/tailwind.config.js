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
        // Brand colors - customize these to match your brand
        pravis: {
          50: '#f0f9ff',
          100: '#e0f2fe',
          200: '#bae6fd',
          300: '#7dd3fc',
          400: '#38bdf8',
          500: '#0ea5e9',
          600: '#0284c7',
          700: '#0369a1',
          800: '#075985',
          900: '#0c4a6e',
          950: '#082f49',
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
