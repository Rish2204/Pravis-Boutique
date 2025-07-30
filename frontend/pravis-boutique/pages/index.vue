<template>
  <div class="min-h-screen bg-gradient-to-br from-pravis-50 to-saffron-50">
    <!-- Hero Section -->
    <div class="container mx-auto px-4 py-20 text-center">
      <div class="mb-8">
        <div class="w-24 h-24 mx-auto mb-6 bg-pravis-600 rounded-full flex items-center justify-center">
          <span class="text-4xl font-bold text-white">P</span>
        </div>
      </div>

      <h1 class="text-6xl font-bold text-pravis-900 mb-6">
        Pravis Handlooms
      </h1>
      
      <p class="text-xl text-pravis-700 mb-12 max-w-3xl mx-auto">
        Discover the finest handwoven treasures crafted with tradition and elegance.
        <span class="text-pravis-800 font-semibold">Premium Quality</span> - Authentic handloom textiles
      </p>

      <!-- Action Buttons -->
      <div class="flex flex-col sm:flex-row gap-6 justify-center items-center mb-20">
        <button 
          class="bg-pravis-600 hover:bg-pravis-700 text-white px-8 py-4 rounded-lg text-lg font-semibold transition-colors"
          @click="navigateToShop"
        >
          🧵 Browse Collection
        </button>
        <button 
          class="bg-saffron-600 hover:bg-saffron-700 text-white px-8 py-4 rounded-lg text-lg font-semibold transition-colors"
          @click="navigateToContact"
        >
          📞 Contact Us
        </button>
      </div>

      <!-- Features Section -->
      <div class="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto">
        <div class="bg-white p-8 rounded-lg shadow-md">
          <div class="text-4xl mb-4">🧵</div>
          <h3 class="text-xl font-bold mb-3 text-pravis-900">Artisan Crafted</h3>
          <p class="text-gray-600">
            Authentic handloom pieces from master artisans across India
          </p>
        </div>
        
        <div class="bg-white p-8 rounded-lg shadow-md">
          <div class="text-4xl mb-4">🎨</div>
          <h3 class="text-xl font-bold mb-3 text-pravis-900">Style Collection</h3>
          <p class="text-gray-600">
            Browse our curated collection of traditional and contemporary designs
          </p>
        </div>
        
        <div class="bg-white p-8 rounded-lg shadow-md">
          <div class="text-4xl mb-4">✨</div>
          <h3 class="text-xl font-bold mb-3 text-pravis-900">Heritage & Quality</h3>
          <p class="text-gray-600">
            Traditional craftsmanship with modern shopping convenience
          </p>
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