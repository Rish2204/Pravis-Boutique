<template>
  <div class="min-h-screen">
    <!-- Hero Carousel -->
    <HeroCarousel />
    
    <!-- Categories Section -->
    <div class="bg-gradient-to-br from-pravis-50 to-gold-50 py-16">
      <div class="container mx-auto px-4">
        <h2 class="text-4xl font-display text-center text-pravis-900 mb-12">
          Our Collections
        </h2>
        
        <div class="text-center max-w-4xl mx-auto mb-12">
          <p class="text-xl text-pravis-700 leading-relaxed">
            <span class="handloom-highlight font-semibold">Six yards of pure grace</span>, rooted in culture, styled with elegance.
          </p>
          <div class="mt-6 space-y-2">
            <p class="text-lg text-pravis-600">
              <span class="font-semibold">Sarees:</span> Banaras | Kanchi | All Handlooms
            </p>
            <p class="text-lg text-pravis-600">
              <span class="font-semibold">Accessories:</span> Jewellery | Clutches
            </p>
            <p class="text-lg text-pravis-600">
              <span class="font-semibold">Readymades:</span> Blouses | Co-Ord Sets | Kurtis | Suits
            </p>
          </div>
        </div>

      <!-- Featured Products Section -->
      <div class="grid md:grid-cols-3 gap-8 max-w-6xl mx-auto">
        <!-- Product Card 1 -->
        <div class="handloom-card bg-white rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 overflow-hidden">
          <div class="h-64 bg-gradient-to-br from-pravis-100 to-gold-100 flex items-center justify-center">
            <span class="text-6xl">🥻</span>
          </div>
          <div class="p-6">
            <h3 class="text-xl font-display font-bold mb-2 text-pravis-900">Banaras Silk Saree</h3>
            <p class="text-gray-600 mb-4">Pure silk with traditional zari work</p>
            <div class="flex justify-between items-center">
              <span class="text-2xl font-bold text-gold-600">₹12,500</span>
              <button class="bg-pravis-500 hover:bg-pravis-600 text-white px-4 py-2 rounded-full text-sm font-semibold transition-colors">
                View Details
              </button>
            </div>
          </div>
        </div>
        
        <!-- Product Card 2 -->
        <div class="handloom-card bg-white rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 overflow-hidden">
          <div class="h-64 bg-gradient-to-br from-gold-100 to-pravis-100 flex items-center justify-center">
            <span class="text-6xl">👗</span>
          </div>
          <div class="p-6">
            <h3 class="text-xl font-display font-bold mb-2 text-pravis-900">Designer Blouse</h3>
            <p class="text-gray-600 mb-4">Contemporary designs with traditional touch</p>
            <div class="flex justify-between items-center">
              <span class="text-2xl font-bold text-gold-600">₹3,500</span>
              <button class="bg-pravis-500 hover:bg-pravis-600 text-white px-4 py-2 rounded-full text-sm font-semibold transition-colors">
                View Details
              </button>
            </div>
          </div>
        </div>
        
        <!-- Product Card 3 -->
        <div class="handloom-card bg-white rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 overflow-hidden">
          <div class="h-64 bg-gradient-to-br from-pravis-100 to-gold-100 flex items-center justify-center">
            <span class="text-6xl">💍</span>
          </div>
          <div class="p-6">
            <h3 class="text-xl font-display font-bold mb-2 text-pravis-900">Traditional Jewellery</h3>
            <p class="text-gray-600 mb-4">Handcrafted temple jewellery sets</p>
            <div class="flex justify-between items-center">
              <span class="text-2xl font-bold text-gold-600">₹15,000</span>
              <button class="bg-pravis-500 hover:bg-pravis-600 text-white px-4 py-2 rounded-full text-sm font-semibold transition-colors">
                View Details
              </button>
            </div>
          </div>
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