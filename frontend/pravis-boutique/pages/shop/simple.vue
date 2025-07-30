<template>
  <div class="min-h-screen bg-gray-50 dark:bg-gray-900">
    <!-- Hero section -->
    <section class="bg-gradient-to-r from-pravis-50 to-saffron-50 dark:from-pravis-900 dark:to-pravis-800 py-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center">
          <h1 class="text-4xl md:text-5xl font-extrabold text-pravis-900 dark:text-pravis-50 font-display">
            Handloom Heritage Collection
          </h1>
          <p class="mt-6 text-xl text-pravis-700 dark:text-pravis-200 max-w-3xl mx-auto">
            Discover authentic handwoven treasures crafted by skilled artisans across India. 
            Each piece tells a story of tradition, elegance, and timeless beauty.
          </p>
          <div class="mt-8 flex flex-wrap justify-center items-center gap-4 text-sm text-pravis-600 dark:text-pravis-300">
            <span class="flex items-center">
              <svg class="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 20 20">
                <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
              Authentic Handloom
            </span>
            <span class="flex items-center">
              <svg class="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 20 20">
                <path d="M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z"/>
              </svg>
              Ethically Sourced
            </span>
            <span class="flex items-center">
              <svg class="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 20 20">
                <path d="M13 6a3 3 0 11-6 0 3 3 0 016 0zM18 8a2 2 0 11-4 0 2 2 0 014 0zM14 15a4 4 0 00-8 0v3h8v-3z"/>
              </svg>
              Supporting Artisans
            </span>
          </div>
        </div>
      </div>
    </section>

    <!-- Main content -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div class="lg:grid lg:grid-cols-4 lg:gap-8">
        
        <!-- Sidebar filters -->
        <div class="hidden lg:block">
          <div class="bg-white dark:bg-gray-800 rounded-lg shadow-sm p-6">
            <h2 class="text-lg font-semibold text-gray-900 dark:text-white mb-6">Filter Products</h2>
            
            <!-- Categories -->
            <div class="mb-8">
              <h3 class="text-sm font-medium text-gray-900 dark:text-white mb-4">Categories</h3>
              <div class="space-y-3">
                <button 
                  v-for="category in categories" 
                  :key="category.id"
                  @click="selectedCategory = category.id"
                  :class="[
                    'w-full text-left px-3 py-2 rounded-md text-sm transition-colors',
                    selectedCategory === category.id 
                      ? 'bg-pravis-100 text-pravis-800 font-medium dark:bg-pravis-800 dark:text-pravis-200' 
                      : 'text-gray-600 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-700'
                  ]"
                >
                  {{ category.name }} ({{ category.count }})
                </button>
              </div>
            </div>

            <!-- Price Range -->
            <div class="mb-8">
              <h3 class="text-sm font-medium text-gray-900 dark:text-white mb-4">Price Range</h3>
              <div class="space-y-2">
                <button 
                  v-for="range in priceRanges" 
                  :key="range.label"
                  @click="selectedPriceRange = range"
                  :class="[
                    'w-full text-left px-3 py-2 rounded-md text-sm transition-colors',
                    selectedPriceRange?.label === range.label 
                      ? 'bg-pravis-100 text-pravis-800 font-medium dark:bg-pravis-800 dark:text-pravis-200' 
                      : 'text-gray-600 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-700'
                  ]"
                >
                  {{ range.label }}
                </button>
              </div>
            </div>

            <!-- Clear filters -->
            <button 
              @click="clearFilters"
              class="w-full px-4 py-2 text-sm font-medium text-pravis-600 bg-pravis-50 hover:bg-pravis-100 rounded-md transition-colors dark:bg-pravis-900 dark:text-pravis-300 dark:hover:bg-pravis-800"
            >
              Clear All Filters
            </button>
          </div>
        </div>

        <!-- Product grid -->
        <div class="lg:col-span-3">
          <!-- Search and sort -->
          <div class="mb-8 flex flex-col sm:flex-row gap-4 justify-between items-start sm:items-center">
            <div class="flex-1 max-w-md">
              <input 
                v-model="searchQuery"
                type="text" 
                placeholder="Search handloom products..."
                class="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-pravis-500 focus:border-transparent dark:bg-gray-800 dark:text-white"
              >
            </div>
            <div class="flex items-center space-x-4">
              <span class="text-sm text-gray-500 dark:text-gray-400">
                {{ filteredProducts.length }} products
              </span>
              <select 
                v-model="sortBy"
                class="px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md text-sm bg-white dark:bg-gray-800 text-gray-900 dark:text-white focus:ring-2 focus:ring-pravis-500"
              >
                <option value="featured">Featured</option>
                <option value="price-low">Price: Low to High</option>
                <option value="price-high">Price: High to Low</option>
                <option value="rating">Rating</option>
              </select>
            </div>
          </div>

          <!-- Products grid -->
          <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
            <div 
              v-for="product in sortedProducts" 
              :key="product.id"
              class="bg-white dark:bg-gray-800 rounded-lg shadow-sm hover:shadow-md transition-shadow duration-200 overflow-hidden group"
            >
              <!-- Product image -->
              <div class="aspect-w-4 aspect-h-3 bg-gray-200 dark:bg-gray-700 relative overflow-hidden">
                <div class="w-full h-64 bg-gradient-to-br from-pravis-100 to-saffron-100 dark:from-pravis-800 dark:to-pravis-700 flex items-center justify-center">
                  <div class="text-center p-4">
                    <div class="w-16 h-16 mx-auto mb-3 bg-pravis-200 dark:bg-pravis-600 rounded-full flex items-center justify-center">
                      <svg class="w-8 h-8 text-pravis-600 dark:text-pravis-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
                      </svg>
                    </div>
                    <p class="text-xs text-pravis-600 dark:text-pravis-300 font-medium">{{ product.fabric }}</p>
                  </div>
                </div>
                <!-- Sale badge -->
                <div v-if="product.originalPrice > product.price" class="absolute top-3 left-3">
                  <span class="bg-red-500 text-white text-xs font-bold px-2 py-1 rounded">
                    SALE
                  </span>
                </div>
                <!-- Out of stock overlay -->
                <div v-if="!product.inStock" class="absolute inset-0 bg-black bg-opacity-50 flex items-center justify-center">
                  <span class="bg-gray-900 text-white px-4 py-2 rounded-md text-sm font-medium">
                    Out of Stock
                  </span>
                </div>
              </div>

              <!-- Product info -->
              <div class="p-6">
                <div class="mb-3">
                  <h3 class="text-lg font-medium text-gray-900 dark:text-white mb-1 line-clamp-2">
                    {{ product.name }}
                  </h3>
                  <p class="text-sm text-gray-500 dark:text-gray-400 line-clamp-2">
                    {{ product.description }}
                  </p>
                </div>

                <!-- Rating and reviews -->
                <div class="flex items-center mb-3">
                  <div class="flex items-center">
                    <div class="flex">
                      <svg 
                        v-for="star in 5" 
                        :key="star"
                        :class="[
                          'w-4 h-4',
                          star <= Math.round(product.rating) ? 'text-yellow-400' : 'text-gray-300 dark:text-gray-600'
                        ]"
                        fill="currentColor" 
                        viewBox="0 0 20 20"
                      >
                        <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/>
                      </svg>
                    </div>
                    <span class="ml-2 text-sm text-gray-500 dark:text-gray-400">
                      ({{ product.reviews }})
                    </span>
                  </div>
                </div>

                <!-- Price and origin -->
                <div class="flex items-center justify-between mb-4">
                  <div>
                    <span class="text-xl font-bold text-pravis-600 dark:text-pravis-400">
                      {{ formatPrice(product.price) }}
                    </span>
                    <span v-if="product.originalPrice > product.price" class="ml-2 text-sm text-gray-500 line-through">
                      {{ formatPrice(product.originalPrice) }}
                    </span>
                  </div>
                  <span class="text-xs text-gray-500 dark:text-gray-400 bg-gray-100 dark:bg-gray-700 px-2 py-1 rounded">
                    {{ product.origin }}
                  </span>
                </div>

                <!-- Tags -->
                <div class="flex flex-wrap gap-1 mb-4">
                  <span 
                    v-for="tag in product.tags.slice(0, 3)" 
                    :key="tag"
                    class="text-xs bg-pravis-100 text-pravis-700 dark:bg-pravis-800 dark:text-pravis-300 px-2 py-1 rounded-full"
                  >
                    {{ tag }}
                  </span>
                </div>

                <!-- Add to cart button -->
                <button 
                  @click="addToCart(product)"
                  :disabled="!product.inStock"
                  :class="[
                    'w-full px-4 py-2 text-sm font-medium rounded-md transition-colors',
                    product.inStock 
                      ? 'bg-pravis-600 hover:bg-pravis-700 text-white' 
                      : 'bg-gray-300 text-gray-500 cursor-not-allowed dark:bg-gray-600 dark:text-gray-400'
                  ]"
                >
                  {{ product.inStock ? 'Add to Cart' : 'Out of Stock' }}
                </button>
              </div>
            </div>
          </div>

          <!-- Empty state -->
          <div v-if="filteredProducts.length === 0" class="text-center py-12">
            <svg class="w-16 h-16 mx-auto text-gray-400 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.172 16.172a4 4 0 015.656 0M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
            <h3 class="text-lg font-medium text-gray-900 dark:text-white mb-2">No products found</h3>
            <p class="text-gray-500 dark:text-gray-400 mb-4">Try adjusting your search or filter criteria</p>
            <button 
              @click="clearFilters"
              class="px-4 py-2 bg-pravis-600 text-white rounded-md hover:bg-pravis-700 transition-colors"
            >
              Clear Filters
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Back to home -->
    <div class="text-center py-8">
      <nuxt-link to="/" class="inline-flex items-center text-pravis-600 hover:text-pravis-700 font-medium">
        <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
        </svg>
        Back to Home
      </nuxt-link>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { useProductData } from '~/composables/useProductData'
import { useCartStore } from '~/store/cart'

// Page metadata
useHead({
  title: 'Handloom Collection - Pravis Handlooms',
  meta: [
    { name: 'description', content: 'Discover authentic handwoven treasures crafted by skilled artisans across India. Premium handloom sarees, kurtas, and textiles.' }
  ]
})

// Setup composables and stores
const { 
  getAllProducts, 
  getCategories, 
  getFilters,
  searchProducts,
  filterProducts,
  formatPrice 
} = useProductData()

const cartStore = useCartStore()
const { trackProduct, trackCart, logInteraction } = useAnalytics()

// Reactive data
const searchQuery = ref('')
const selectedCategory = ref('all')
const selectedPriceRange = ref(null)
const sortBy = ref('featured')

// Get data
const allProducts = getAllProducts()
const categories = getCategories()
const filters = getFilters()
const priceRanges = filters.priceRange

// Computed properties
const filteredProducts = computed(() => {
  let products = [...allProducts]
  
  // Filter by search query
  if (searchQuery.value) {
    products = searchProducts(searchQuery.value)
  }
  
  // Filter by category
  if (selectedCategory.value !== 'all') {
    products = products.filter(p => p.category === selectedCategory.value)
  }
  
  // Filter by price range
  if (selectedPriceRange.value) {
    products = products.filter(p => 
      p.price >= selectedPriceRange.value.min && 
      p.price <= selectedPriceRange.value.max
    )
  }
  
  return products
})

const sortedProducts = computed(() => {
  const products = [...filteredProducts.value]
  
  switch (sortBy.value) {
    case 'price-low':
      return products.sort((a, b) => a.price - b.price)
    case 'price-high':
      return products.sort((a, b) => b.price - a.price)
    case 'rating':
      return products.sort((a, b) => b.rating - a.rating)
    case 'featured':
    default:
      return products.sort((a, b) => (b.featured ? 1 : 0) - (a.featured ? 1 : 0))
  }
})

// Methods
const clearFilters = () => {
  searchQuery.value = ''
  selectedCategory.value = 'all'
  selectedPriceRange.value = null
  sortBy.value = 'featured'
}

const addToCart = (product) => {
  const cartItem = {
    id: product.id,
    name: product.name,
    price: product.price,
    image: product.images[0],
    quantity: 1
  }
  
  cartStore.addItem(cartItem)
  
  // Track e-commerce analytics
  trackProduct('add_to_cart', product, {
    source: 'shop_page',
    category: product.category,
    fabric: product.fabric,
    origin: product.origin
  })
  
  trackCart('add', cartItem, {
    totalItems: cartStore.count + 1,
    source: 'shop_page'
  })
  
  logInteraction('add_to_cart', 'button', {
    productId: product.id,
    productName: product.name,
    price: product.price,
    category: product.category
  })
  
  console.log(`Added ${product.name} to cart`)
}
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>