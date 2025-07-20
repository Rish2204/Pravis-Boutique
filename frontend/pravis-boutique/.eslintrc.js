module.exports = {
  root: true,
  env: {
    browser: true,
    node: true
  },
  extends: [
    '@nuxtjs/eslint-config',
    'plugin:nuxt/recommended'
  ],
  rules: {
    'no-undef': 'off',
    'vue/multi-word-component-names': 'off'
  }
}
