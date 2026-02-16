<template>
  <div class="hero-section">
    <!-- Main content -->
    <div class="container mx-auto px-4 py-16">
      <!-- Featured Product -->
      <div class="text-center mb-16">
        <h2 class="text-3xl md:text-4xl font-display text-pravis-800 mb-4">
          Exquisite Banaras Silk
        </h2>
        <p class="text-xl text-gray-700 mb-6">Handwoven Heritage</p>
        <div class="text-4xl font-bold text-pravis-700 mb-8">₹12,500</div>
        <button 
          class="bg-pravis-700 hover:bg-pravis-800 text-white px-12 py-4 rounded-full text-lg font-semibold transition-all duration-300 transform hover:scale-105 shadow-lg"
          @click="$router.push('/shop')"
        >
          Shop Collection
        </button>
      </div>

      <!-- Collections Grid -->
      <div class="mb-16">
        <h3 class="text-3xl font-display text-pravis-800 mb-8 text-center">Our Collections</h3>
        
        <div class="grid md:grid-cols-2 gap-6 max-w-3xl mx-auto">
          <div class="collection-item">
            <h4 class="font-semibold text-pravis-700">Sarees</h4>
            <p class="text-gray-600">Banaras | Kanchi | All Handlooms</p>
          </div>
          
          <div class="collection-item">
            <h4 class="font-semibold text-pravis-700">Accessories</h4>
            <p class="text-gray-600">Jewellery | Clutches</p>
          </div>
          
          <div class="collection-item">
            <h4 class="font-semibold text-pravis-700">Readymades</h4>
            <p class="text-gray-600">Blouses | Co-Ord Sets | Kurtis</p>
          </div>
          
          <div class="collection-item">
            <h4 class="font-semibold text-pravis-700">Suits</h4>
            <p class="text-gray-600">Traditional & Contemporary</p>
          </div>
        </div>
      </div>

      <!-- Contact Information -->
      <div class="bg-gradient-to-r from-pravis-700 to-pravis-800 text-white py-8 px-8 rounded-2xl shadow-xl max-w-2xl mx-auto">
        <div class="flex flex-col md:flex-row justify-between items-center gap-4">
          <div class="text-lg">
            <i class="fas fa-map-marker-alt mr-2"></i>
            2nd Floor, Mokila, 501203
          </div>
          <div class="text-lg">
            <i class="fas fa-phone mr-2"></i>
            6300208234
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
// Hero section component
</script>

<style scoped>
.hero-section {
  background: linear-gradient(to bottom, #faf8f5 0%, #ffffff 100%);
  min-height: calc(100vh - 200px);
  display: flex;
  align-items: center;
}

.collection-item {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.collection-item:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 12px rgba(0, 0, 0, 0.15);
}

.font-display {
  font-family: 'Playfair Display', serif;
}
</style>
