<template>
  <div>
    <!-- Show consent dialog first if no consent given -->
    <ConsentDialog v-if="showConsentDialog" @consent-decided="handleConsent" />

    <!-- Show main content only after consent -->
    <div v-else class="min-h-screen">
      <!-- Hero Section -->
      <div class="hero-section">
        <div class="container mx-auto px-4 py-20 text-center relative">
          <!-- Decorative elements -->
          <div class="golden-accent top-accent" />
          <div class="golden-accent bottom-accent" />

          <div class="logo-showcase mb-8">
            <img
              :src="logoSrc"
              alt="Pravis Handlooms"
              class="hero-logo"
              @error="handleLogoError"
              @load="handleLogoLoad"
            >
          </div>

          <h1 class="font-display text-6xl font-bold text-pravis-500 mb-6 hero-title">
            Pravis Handlooms
          </h1>
          <p class="text-2xl text-black mb-12 max-w-3xl mx-auto leading-relaxed">
            Discover the finest handwoven treasures with our AI-powered voice agent
            <span class="text-pravis-600 font-bold handloom-highlight">"Ask Pravi"</span>
            - Your personal handloom curator
          </p>

          <!-- Demo Buttons -->
          <div class="flex flex-col sm:flex-row gap-6 justify-center items-center">
            <button class="handloom-btn primary-btn px-10 py-4" @click="navigateToShop">
              🧵 Browse Handlooms
            </button>
            <button class="handloom-btn secondary-btn px-10 py-4">
              🗣️ Ask Pravi
            </button>
          </div>
        </div>
      </div>

      <!-- Features Section -->
      <div class="features-section bg-gradient-to-br from-pravis-50 to-white py-20">
        <div class="container mx-auto px-4">
          <h2 class="font-display text-4xl font-bold text-pravis-500 text-center mb-16">
            Handcrafted Excellence Meets AI Innovation
          </h2>
          <div class="grid md:grid-cols-3 gap-12">
            <div class="handloom-card text-center">
              <div class="handloom-icon-wrapper">
                <div class="text-5xl mb-6">
                  🧵
                </div>
              </div>
              <h3 class="font-display text-2xl font-bold mb-4 text-black">
                Artisan Curation
              </h3>
              <p class="text-black leading-relaxed">
                AI-powered recommendations featuring authentic handloom pieces from master artisans
              </p>
            </div>
            <div class="handloom-card text-center">
              <div class="handloom-icon-wrapper">
                <div class="text-5xl mb-6">
                  🎨
                </div>
              </div>
              <h3 class="font-display text-2xl font-bold mb-4 text-black">
                Voice Discovery
              </h3>
              <p class="text-black leading-relaxed">
                Describe your style to Ask Pravi and discover perfect handloom matches effortlessly
              </p>
            </div>
            <div class="handloom-card text-center">
              <div class="handloom-icon-wrapper">
                <div class="text-5xl mb-6">
                  ✨
                </div>
              </div>
              <h3 class="font-display text-2xl font-bold mb-4 text-black">
                Heritage & Modern
              </h3>
              <p class="text-black leading-relaxed">
                Traditional craftsmanship enhanced with modern shopping convenience
              </p>
            </div>
          </div>
        </div>
      </div>

      <!-- Voice Agent Floating Button -->
      <button class="voice-agent-button handloom-floating-btn" @click="activateVoiceAgent">
        <span class="btn-icon">🎤</span>
        <span class="btn-text">Ask Pravi</span>
      </button>
    </div>
  </div>
</template>

<script>
import ConsentDialog from '@/components/ConsentDialog.vue'

export default {
  components: {
    ConsentDialog
  },
  data () {
    return {
      showConsentDialog: true,
      logoSrc: '/pravis-logo.png',
      logoError: false
    }
  },
  mounted () {
    // Check if user has already given consent
    const existingConsent = localStorage.getItem('pravis-consent')
    if (existingConsent) {
      this.showConsentDialog = false
    }
  },
  methods: {
    handleConsent (consentData) {
      // Hide consent dialog and show main content
      this.showConsentDialog = false

      // Initialize analytics if user consented
      if (consentData.consent) {
        this.$router.push('/shop')
      } else {
        // User declined consent, do nothing
      }
    },
    navigateToShop () {
      this.$router.push('/shop')
    },
    activateVoiceAgent () {
      // Future: Launch voice agent functionality
      alert('🧵 Ask Pravi: "Namaste! I\'m here to help you discover beautiful handloom pieces. What style are you looking for today?"')
    },
    handleLogoError (event) {
      this.logoError = true
      // Set fallback or create a placeholder
      event.target.style.display = 'none'
      // Create a text-based fallback
      const logoContainer = event.target.parentElement
      if (!logoContainer.querySelector('.logo-fallback')) {
        const fallback = document.createElement('div')
        fallback.className = 'logo-fallback text-6xl font-bold text-white'
        fallback.textContent = 'P'
        fallback.style.cssText = `
          display: flex;
          align-items: center;
          justify-content: center;
          width: 100%;
          height: 100%;
        `
        logoContainer.appendChild(fallback)
      }
    },
    handleLogoLoad (event) {
      this.logoError = false
    }
  }
}
</script>

<style scoped>
body {
  font-family: 'Inter', sans-serif;
  background: #f6f6f6;
}
</style>
