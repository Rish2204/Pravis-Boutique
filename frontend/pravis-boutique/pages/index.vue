<template>
  <div class="min-h-screen bg-gradient-to-br from-pravis-50 to-saffron-50">
    <!-- Hero Section -->
    <div class="hero-section mt-4 md:mt-8">
    <div class="container mx-auto px-4 py-20 text-center">
      <div class="mb-12">
        <div class="w-32 h-32 mx-auto mb-8">
          <img src="/pravis-logo.svg" alt="Pravis Logo" class="h-full w-full object-contain drop-shadow-lg" />
        </div>
      </div>

      <h1 class="hero-title text-5xl md:text-6xl font-display font-bold text-pravis-900 mb-4 leading-tight">
        Pravis
      </h1>
      <h2 class="text-3xl md:text-4xl font-display italic text-pravis-600 mb-8 tracking-wide">
        Drape in Elegance
      </h2>
      
      <p class="text-xl text-pravis-700 mb-16 max-w-3xl mx-auto leading-relaxed">
        <span class="handloom-highlight font-semibold">Six yards of pure grace</span>, rooted in culture, styled with elegance.
        <br>
        <span class="text-pravis-600 mt-2 block">Sarees • Banaras • Kanchi • All Handlooms</span>
        <span class="text-pravis-600">Accessories • Jewellery • Clutches</span>
        <br>
        <span class="text-pravis-600">Readymades • Blouses • Co-Ord Sets • Kurtis • Suits</span>
      </p>

      <!-- Action Buttons -->
      <div class="flex flex-col sm:flex-row gap-6 justify-center items-center mb-24">
        <button 
          class="handloom-btn primary-btn bg-pravis-500 hover:bg-pravis-600 text-white px-10 py-4 rounded-full text-lg font-semibold transition-all duration-300 shadow-lg border-2 border-gold-500"
          @click="navigateToShop"
        >
          🧵 Browse Collection
        </button>
        <button 
          class="handloom-btn secondary-btn bg-gold-500 hover:bg-gold-600 text-pravis-900 px-10 py-4 rounded-full text-lg font-semibold transition-all duration-300 shadow-lg"
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