<template>
  <div class="min-h-screen bg-gradient-to-br from-pravis-50 to-saffron-50">
    <!-- Hero Section -->
    <div class="hero-section mt-4 md:mt-8">
    <div class="container mx-auto px-4 py-20 text-center">
      <div class="mb-12">
        <div class="w-24 h-24 mx-auto mb-8 bg-pravis-500 rounded-full flex items-center justify-center shadow-lg">
          <span class="text-4xl font-bold text-white">P</span>
        </div>
      </div>

      <h1 class="hero-title text-5xl md:text-6xl font-display font-bold text-pravis-900 mb-8 leading-tight">
        Pravis Handlooms
      </h1>
      
      <p class="text-xl text-pravis-700 mb-16 max-w-3xl mx-auto leading-relaxed">
        <span class="handloom-highlight">Six yards of pure grace</span>, rooted in culture, styled with elegance.
        Discover authentic handwoven treasures from master artisans across India.
      </p>

      <!-- Action Buttons -->
      <div class="flex flex-col sm:flex-row gap-6 justify-center items-center mb-24">
        <button 
          class="handloom-btn primary-btn bg-pravis-500 hover:bg-pravis-600 text-white px-10 py-4 rounded-full text-lg font-semibold transition-all duration-300 shadow-lg"
          @click="navigateToShop"
        >
          🧵 Browse Collection
        </button>
        <button 
          class="handloom-btn secondary-btn bg-white hover:bg-pravis-50 text-pravis-500 border-2 border-pravis-300 px-10 py-4 rounded-full text-lg font-semibold transition-all duration-300 shadow-lg"
          @click="navigateToContact"
        >
          📞 Contact Us
        </button>
      </div>

      <!-- Features Section -->
      <div class="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto">
        <div class="handloom-card bg-white p-8 rounded-xl shadow-lg hover:shadow-xl transition-all duration-300">
          <div class="handloom-icon-wrapper mb-6">
            <div class="text-3xl text-pravis-500">🧵</div>
          </div>
          <h3 class="text-xl font-display font-bold mb-4 text-pravis-900">Artisan Crafted</h3>
          <p class="text-gray-600 leading-relaxed">
            Authentic handloom pieces from master artisans across India
          </p>
        </div>
        
        <div class="handloom-card bg-white p-8 rounded-xl shadow-lg hover:shadow-xl transition-all duration-300">
          <div class="handloom-icon-wrapper mb-6">
            <div class="text-3xl text-pravis-500">🎨</div>
          </div>
          <h3 class="text-xl font-display font-bold mb-4 text-pravis-900">Style Collection</h3>
          <p class="text-gray-600 leading-relaxed">
            Browse our curated collection of traditional and contemporary designs
          </p>
        </div>
        
        <div class="handloom-card bg-white p-8 rounded-xl shadow-lg hover:shadow-xl transition-all duration-300">
          <div class="handloom-icon-wrapper mb-6">
            <div class="text-3xl text-pravis-500">✨</div>
          </div>
          <h3 class="text-xl font-display font-bold mb-4 text-pravis-900">Heritage & Quality</h3>
          <p class="text-gray-600 leading-relaxed">
            Traditional craftsmanship with modern shopping convenience
          </p>
        </div>
      </div>
    </div>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    navigateToShop() {
      this.$router.push('/shop')
    },
    navigateToContact() {
      this.$router.push('/contact')
    }
  }
}
</script>

<style scoped>
.container {
  max-width: 1200px;
}
</style>