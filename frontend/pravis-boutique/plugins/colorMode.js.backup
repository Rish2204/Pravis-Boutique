export default defineNuxtPlugin(nuxtApp => {
  // Skip on server side
  if (!process.client) return
  
  // Add color mode to app
  const colorMode = {
    preference: null,
    
    // Set to 'dark', 'light' or 'system'
    get value() {
      return this.preference || this.getSystemPreference()
    },
    
    // Get system color preference
    getSystemPreference() {
      if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        return 'dark'
      }
      return 'light'
    },
    
    // Set preferred color mode
    set(value) {
      if (value === 'system') {
        this.preference = null
        localStorage.removeItem('color-mode')
        this.apply(this.getSystemPreference())
      } else if (value === 'dark' || value === 'light') {
        this.preference = value
        localStorage.setItem('color-mode', value)
        this.apply(value)
      }
    },
    
    // Apply color mode to document
    apply(value) {
      if (value === 'dark') {
        document.documentElement.classList.add('dark')
      } else {
        document.documentElement.classList.remove('dark')
      }
    },
    
    // Initialize color mode
    init() {
      const storedMode = localStorage.getItem('color-mode')
      
      if (storedMode) {
        this.preference = storedMode
      }
      
      this.apply(this.value)
      
      // Watch for system preference changes
      if (window.matchMedia) {
        window
          .matchMedia('(prefers-color-scheme: dark)')
          .addEventListener('change', e => {
            if (!this.preference) {
              this.apply(e.matches ? 'dark' : 'light')
            }
          })
      }
    }
  }
  
  // Initialize on plugin load
  colorMode.init()
  
  // Make available to components
  nuxtApp.provide('colorMode', colorMode)
})
