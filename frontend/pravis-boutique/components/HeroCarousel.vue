<template>
  <div class="relative w-full min-h-screen overflow-hidden">
    <!-- Background with texture -->
    <div class="absolute inset-0 bg-gradient-to-br from-pravis-800 via-pravis-700 to-pravis-900"></div>
    
    <!-- Decorative pattern overlay -->
    <div class="absolute inset-0 opacity-10">
      <div class="w-full h-full decorative-pattern"></div>
    </div>
    
    <!-- Main content centered -->
    <div class="relative h-full flex flex-col items-center justify-center text-center py-20">
      <div class="container mx-auto px-4 max-w-4xl">
        
        <!-- Animated Logo and Main Branding -->
        <div class="mb-12">
          <!-- Animated Blouse Logo -->
          <div class="flex items-center justify-center mb-8">
            <AnimatedLogo />
            <div class="ml-6">
              <h1 class="text-6xl md:text-8xl lg:text-9xl font-display text-gold-500 mb-2" style="font-family: 'Playfair Display', serif; font-style: italic; font-weight: 400;">
                pravis
              </h1>
              <p class="text-2xl md:text-3xl text-gold-400 tracking-wider" style="font-family: 'Playfair Display', serif; font-style: italic;">
                Drape in Elegance
              </p>
            </div>
          </div>
        </div>

        <!-- Featured Product Section -->
        <div class="mb-16">
          <div class="text-center mb-8">
            <h2 class="text-4xl md:text-5xl font-display text-gold-500 mb-4" style="font-family: 'Playfair Display', serif;">
              pravis
            </h2>
            <p class="text-xl md:text-2xl text-gold-400 mb-6" style="font-family: 'Playfair Display', serif; font-style: italic;">
              Drape in Elegance
            </p>
            <p class="text-lg md:text-xl text-pravis-100 mb-8">
              Exquisite Banaras Silk - Handwoven Heritage
            </p>
            <div class="text-4xl md:text-5xl font-bold text-gold-500 mb-8">
              ₹12,500
            </div>
            <button 
              class="bg-gold-500 hover:bg-gold-600 text-pravis-900 px-12 py-4 rounded-full text-xl font-semibold transition-all duration-300 shadow-2xl transform hover:scale-105"
              @click="$router.push('/shop')"
            >
              Shop Collection
            </button>
          </div>
        </div>

        <!-- Collections Section -->
        <div class="mb-16">
          <h3 class="text-4xl md:text-5xl font-display text-gold-500 mb-12" style="font-family: 'Playfair Display', serif;">
            Our Collections
          </h3>
          
          <div class="space-y-6 text-left max-w-2xl mx-auto">
            <div class="flex items-center text-lg md:text-xl text-pravis-100">
              <span class="w-4 h-4 bg-gold-500 rounded-full mr-4"></span>
              <span class="font-semibold text-gold-400">Sarees:</span>
              <span class="ml-2">Banaras | Kanchi | All Handlooms</span>
            </div>
            <div class="flex items-center text-lg md:text-xl text-pravis-100">
              <span class="w-4 h-4 bg-gold-500 rounded-full mr-4"></span>
              <span class="font-semibold text-gold-400">Accessories:</span>
              <span class="ml-2">Jewellery | Clutches</span>
            </div>
            <div class="flex items-center text-lg md:text-xl text-pravis-100">
              <span class="w-4 h-4 bg-gold-500 rounded-full mr-4"></span>
              <span class="font-semibold text-gold-400">Readymades:</span>
              <span class="ml-2">Blouses | Co-Ord Sets | Kurtis</span>
            </div>
            <div class="flex items-center text-lg md:text-xl text-pravis-100">
              <span class="w-4 h-4 bg-gold-500 rounded-full mr-4"></span>
              <span class="font-semibold text-gold-400">Suits</span>
            </div>
          </div>
        </div>

        <!-- Contact Information -->
        <div class="bg-gold-500 text-pravis-900 py-8 px-12 rounded-2xl shadow-2xl">
          <div class="flex flex-col md:flex-row justify-between items-center space-y-4 md:space-y-0">
            <div class="text-lg md:text-xl font-semibold">
              2nd Floor, Mokila, 501203.
            </div>
            <div class="text-lg md:text-xl font-semibold">
              Cell: 6300208234
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
// Static hero section - no carousel functionality needed
</script>

<style scoped>
/* Clean, centered layout styles */
</style>