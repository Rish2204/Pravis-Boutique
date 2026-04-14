import type { Config } from 'tailwindcss'

export default <Config>{
  content: [
    './components/**/*.{vue,ts}',
    './layouts/**/*.vue',
    './pages/**/*.vue',
    './app.vue',
  ],
  theme: {
    extend: {
      colors: {
        pravis: {
          50: '#FDF2F8',
          100: '#F8E8EC',
          200: '#E8BAC2',
          300: '#D4AF37',
          400: '#B8860B',
          500: '#8B0000',
          600: '#A0001C',
          700: '#7F0000',
          800: '#5F0000',
          900: '#3F0000',
          950: '#1F0000',
        },
        gold: {
          DEFAULT: '#D4AF37',
          dark: '#B8860B',
        },
        handloom: {
          rust: '#B7472A',
          terracotta: '#E07A5F',
          sage: '#81B29A',
          gold: '#F2CC8F',
          deep: '#3D405B',
          cream: '#F4F3EE',
        },
      },
      fontFamily: {
        display: ['Playfair Display', 'serif'],
        body: ['Inter', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
