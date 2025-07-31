<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Hero Section -->
    <div class="bg-gradient-to-r from-pravis-600 to-saffron-600 text-white py-16">
      <div class="container mx-auto px-4 text-center">
        <h1 class="text-4xl font-bold mb-4">Handloom Collection</h1>
        <p class="text-xl text-pravis-100">
          Discover authentic handwoven treasures crafted by skilled artisans
        </p>
      </div>
    </div>

    <!-- Products Section -->
    <div class="container mx-auto px-4 py-12">
      <div class="mb-8">
        <h2 class="text-2xl font-bold text-gray-900 mb-4">Featured Products</h2>
        <p class="text-gray-600">Browse our collection of authentic handloom textiles</p>
      </div>

      <!-- Product Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
        <div 
          v-for="product in products" 
          :key="product.id"
          class="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow"
        >
          <!-- Product Image Placeholder -->
          <div class="h-48 bg-gradient-to-br from-pravis-100 to-saffron-100 flex items-center justify-center">
            <div class="text-center p-4">
              <div class="w-16 h-16 mx-auto mb-3 bg-pravis-200 rounded-full flex items-center justify-center">
                <svg class="w-8 h-8 text-pravis-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
                </svg>
              </div>
              <p class="text-xs text-pravis-600 font-medium">{{ product.fabric }}</p>
            </div>
          </div>

          <!-- Product Info -->
          <div class="p-4">
            <h3 class="font-semibold text-gray-900 mb-2 line-clamp-2">{{ product.name }}</h3>
            <p class="text-sm text-gray-600 mb-3 line-clamp-2">{{ product.description }}</p>
            
            <!-- Rating -->
            <div class="flex items-center mb-3">
              <div class="flex">
                <svg 
                  v-for="star in 5" 
                  :key="star"
                  :class="star <= Math.round(product.rating) ? 'text-yellow-400' : 'text-gray-300'"
                  class="w-4 h-4"
                  fill="currentColor" 
                  viewBox="0 0 20 20"
                >
                  <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/>
                </svg>
              </div>
              <span class="ml-2 text-sm text-gray-500">({{ product.reviews }})</span>
            </div>

            <!-- Price and Origin -->
            <div class="flex items-center justify-between mb-4">
              <div>
                <span class="text-xl font-bold text-pravis-600">₹{{ product.price }}</span>
                <span v-if="product.originalPrice > product.price" class="ml-2 text-sm text-gray-500 line-through">
                  ₹{{ product.originalPrice }}
                </span>
              </div>
              <span class="text-xs text-gray-500 bg-gray-100 px-2 py-1 rounded">
                {{ product.origin }}
              </span>
            </div>

            <!-- Add to Cart Button -->
            <button 
              @click="addToCart(product)"
              class="w-full px-4 py-2 text-sm font-medium rounded-md transition-colors bg-pravis-600 hover:bg-pravis-700 text-white"
            >
              Inquire on WhatsApp
            </button>
          </div>
        </div>
      </div>

      <!-- Empty State -->
      <div v-if="products.length === 0" class="text-center py-16">
        <div class="w-24 h-24 mx-auto mb-6 bg-gray-200 rounded-full flex items-center justify-center">
          <svg class="w-12 h-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"/>
          </svg>
        </div>
        <h3 class="text-xl font-semibold text-gray-900 mb-2">No products found</h3>
        <p class="text-gray-600">Check back soon for new arrivals!</p>
      </div>
    </div>

    <!-- Back to Home -->
    <div class="text-center pb-12">
      <NuxtLink to="/" class="inline-flex items-center text-pravis-600 hover:text-pravis-700 font-medium">
        <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
        </svg>
        Back to Home
      </NuxtLink>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

// Page metadata
useHead({
  title: 'Shop - Pravis Boutique',
  meta: [
    { name: 'description', content: 'Browse our collection of authentic handloom textiles and handwoven treasures.' }
  ]
})

// Dummy product data
const products = ref([
  {
    id: 1,
    name: "Banarasi Silk Saree - Golden Thread",
    price: 15999,
    originalPrice: 18999,
    category: "sarees",
    fabric: "Pure Silk",
    origin: "Varanasi, UP",
    rating: 4.8,
    reviews: 124,
    inStock: true,
    description: "Exquisite Banarasi silk saree with intricate golden thread work and traditional motifs."
  },
  {
    id: 2,
    name: "Handwoven Cotton Kurta Set",
    price: 3499,
    originalPrice: 3499,
    category: "kurtas",
    fabric: "Pure Cotton",
    origin: "Lucknow, UP",
    rating: 4.6,
    reviews: 89,
    inStock: true,
    description: "Comfortable handwoven cotton kurta with traditional embroidery and matching dupatta."
  },
  {
    id: 3,
    name: "Kashmiri Pashmina Shawl",
    price: 8999,
    originalPrice: 10999,
    category: "shawls",
    fabric: "Pashmina",
    origin: "Kashmir",
    rating: 4.9,
    reviews: 56,
    inStock: true,
    description: "Luxurious Kashmiri pashmina shawl with delicate hand-embroidered patterns."
  },
  {
    id: 4,
    name: "Chanderi Silk Dupatta",
    price: 2799,
    originalPrice: 2799,
    category: "dupatta",
    fabric: "Chanderi Silk",
    origin: "Chanderi, MP",
    rating: 4.7,
    reviews: 78,
    inStock: true,
    description: "Elegant Chanderi silk dupatta with traditional zari work and floral motifs."
  },
  {
    id: 5,
    name: "Handloom Linen Saree",
    price: 4999,
    originalPrice: 5999,
    category: "sarees",
    fabric: "Pure Linen",
    origin: "Kerala",
    rating: 4.5,
    reviews: 92,
    inStock: true,
    description: "Breathable handloom linen saree perfect for everyday wear with subtle border designs."
  },
  {
    id: 6,
    name: "Rajasthani Block Print Lehenga",
    price: 12999,
    originalPrice: 15999,
    category: "lehenga",
    fabric: "Cotton Silk",
    origin: "Jaipur, Rajasthan",
    rating: 4.8,
    reviews: 67,
    inStock: true,
    description: "Vibrant Rajasthani block print lehenga with mirror work and traditional patterns."
  }
])

// Methods
const addToCart = (product) => {
  console.log('Add to cart clicked for:', product.name)
  
  const phoneNumber = '916300208234'
  const message = `Hi! I'm interested in ${product.name} from Pravis Boutique. Price: ₹${product.price}`
  const whatsappUrl = `https://wa.me/${phoneNumber}?text=${encodeURIComponent(message)}`
  
  console.log('WhatsApp URL:', whatsappUrl)
  
  // Simple direct navigation
  window.open(whatsappUrl, '_blank')
}
</script>

<style scoped>
.container {
  max-width: 1200px;
}

.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>