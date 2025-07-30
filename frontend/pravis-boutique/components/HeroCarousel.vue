<template>
  <div class="relative w-full h-[400px] md:h-[500px] lg:h-[600px] overflow-hidden">
    <!-- Background with texture -->
    <div class="absolute inset-0 bg-gradient-to-br from-pravis-800 via-pravis-700 to-pravis-900"></div>
    
    <!-- Decorative pattern overlay -->
    <div class="absolute inset-0 opacity-10">
      <div class="w-full h-full" style="background-image: url('data:image/svg+xml,%3Csvg width="40" height="40" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"%3E%3Cg fill="%23D4AF37" fill-opacity="0.3"%3E%3Cpath d="M20 20c0-5.5-4.5-10-10-10s-10 4.5-10 10 4.5 10 10 10 10-4.5 10-10zm10 0c0-5.5-4.5-10-10-10s-10 4.5-10 10 4.5 10 10 10 10-4.5 10-10z"/%3E%3C/g%3E%3C/svg%3E'); background-size: 40px 40px;"></div>
    </div>
    
    <!-- Carousel images -->
    <div class="relative h-full">
      <transition-group
        name="carousel"
        tag="div"
        class="relative h-full"
      >
        <div
          v-for="(image, index) in images"
          v-show="currentIndex === index"
          :key="image.id"
          class="absolute inset-0 flex items-center justify-center"
        >
          <div class="container mx-auto px-4 grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
            <!-- Text content -->
            <div class="text-white text-center md:text-left order-2 md:order-1">
              <h1 class="text-5xl md:text-6xl lg:text-7xl font-display mb-4" style="font-family: 'Playfair Display', serif; font-style: italic;">
                <span class="text-gold-500">pravis</span>
              </h1>
              <p class="text-2xl md:text-3xl mb-2 text-pravis-200" style="font-family: 'Georgia', serif; font-style: italic;">
                Drape in Elegance
              </p>
              <p class="text-lg md:text-xl mb-8 text-pravis-100">
                {{ image.caption }}
              </p>
              <div class="text-3xl md:text-4xl font-bold text-gold-500 mb-8">
                {{ image.price }}
              </div>
              <button 
                class="bg-gold-500 hover:bg-gold-600 text-pravis-900 px-8 py-3 rounded-full font-semibold transition-all duration-300 shadow-lg"
                @click="$router.push('/shop')"
              >
                Shop Collection
              </button>
            </div>
            
            <!-- Image -->
            <div class="order-1 md:order-2">
              <div class="relative">
                <div class="absolute -inset-4 bg-gold-500 opacity-20 blur-xl rounded-full"></div>
                <img 
                  :src="image.src" 
                  :alt="image.alt"
                  class="relative w-full max-w-md mx-auto rounded-lg shadow-2xl"
                />
              </div>
            </div>
          </div>
        </div>
      </transition-group>
    </div>
    
    <!-- Navigation dots -->
    <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 flex space-x-2">
      <button
        v-for="(image, index) in images"
        :key="index"
        @click="currentIndex = index"
        class="w-3 h-3 rounded-full transition-all duration-300"
        :class="currentIndex === index ? 'bg-gold-500 w-8' : 'bg-white opacity-50 hover:opacity-75'"
      ></button>
    </div>
    
    <!-- Navigation arrows -->
    <button
      @click="prev"
      class="absolute left-4 top-1/2 transform -translate-y-1/2 bg-white bg-opacity-20 hover:bg-opacity-30 text-white p-3 rounded-full transition-all duration-300"
    >
      <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
      </svg>
    </button>
    <button
      @click="next"
      class="absolute right-4 top-1/2 transform -translate-y-1/2 bg-white bg-opacity-20 hover:bg-opacity-30 text-white p-3 rounded-full transition-all duration-300"
    >
      <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
      </svg>
    </button>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const currentIndex = ref(0)
let intervalId = null

// Product images with captions and prices
const images = ref([
  {
    id: 1,
    src: '/images/product-1.jpg',
    alt: 'Banaras Silk Saree',
    caption: 'Exquisite Banaras Silk - Handwoven Heritage',
    price: '₹12,500'
  },
  {
    id: 2,
    src: '/images/product-2.jpg',
    alt: 'Kanchi Cotton Saree',
    caption: 'Pure Kanchi Cotton - Traditional Elegance',
    price: '₹8,500'
  },
  {
    id: 3,
    src: '/images/product-3.jpg',
    alt: 'Designer Blouse',
    caption: 'Designer Blouses - Contemporary Style',
    price: '₹3,500'
  },
  {
    id: 4,
    src: '/images/product-4.jpg',
    alt: 'Handloom Kurta Set',
    caption: 'Handloom Kurta Sets - Modern Comfort',
    price: '₹5,500'
  },
  {
    id: 5,
    src: '/images/product-5.jpg',
    alt: 'Traditional Jewellery',
    caption: 'Traditional Jewellery - Timeless Beauty',
    price: '₹15,000'
  }
])

const next = () => {
  currentIndex.value = (currentIndex.value + 1) % images.value.length
}

const prev = () => {
  currentIndex.value = currentIndex.value === 0 ? images.value.length - 1 : currentIndex.value - 1
}

// Auto-rotate carousel
onMounted(() => {
  intervalId = setInterval(next, 5000) // Change slide every 5 seconds
})

onUnmounted(() => {
  if (intervalId) clearInterval(intervalId)
})
</script>

<style scoped>
.carousel-enter-active,
.carousel-leave-active {
  transition: opacity 1s ease-in-out, transform 1s ease-in-out;
}

.carousel-enter-from {
  opacity: 0;
  transform: translateX(100px);
}

.carousel-leave-to {
  opacity: 0;
  transform: translateX(-100px);
}
</style>