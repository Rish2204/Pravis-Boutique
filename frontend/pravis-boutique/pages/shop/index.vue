<template>
  <div>
    <!-- Hero section -->
    <section class="bg-gray-100 dark:bg-gray-800 py-12">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center">
          <h1 class="text-3xl font-extrabold text-gray-900 dark:text-white sm:text-4xl">
            Discover Our Collection
          </h1>
          <p class="mt-4 text-lg text-gray-500 dark:text-gray-300">
            Browse our curated selection of handcrafted, luxury boutique items.
          </p>
        </div>
      </div>
    </section>
    
    <!-- Filters and sort section -->
    <section class="border-b border-gray-200 dark:border-gray-700">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="py-6 flex items-center justify-between">
          <!-- Filter button (mobile) -->
          <button 
            @click="showFilters = !showFilters"
            class="inline-flex items-center lg:hidden px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm text-sm font-medium text-gray-700 dark:text-gray-300 bg-white dark:bg-gray-800 hover:bg-gray-50 dark:hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-pravis-500"
          >
            <svg class="-ml-1 mr-2 h-5 w-5 text-gray-400" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z" />
            </svg>
            Filters
          </button>
          
          <!-- Active filters (desktop) -->
          <div class="hidden lg:flex lg:items-center">
            <span class="mr-3 text-sm font-medium text-gray-700 dark:text-gray-300">Filters:</span>
            <div class="flex flex-wrap gap-2">
              <div 
                v-for="(value, key) in activeFilters" 
                :key="key"
                class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-pravis-100 text-pravis-800 dark:bg-pravis-800 dark:text-pravis-100"
              >
                {{ key }}: {{ value }}
                <button 
                  @click="removeFilter(key)"
                  class="ml-1.5 inline-flex items-center justify-center w-4 h-4 rounded-full text-pravis-400 hover:text-pravis-600 dark:text-pravis-300 dark:hover:text-pravis-100 focus:outline-none"
                >
                  <span class="sr-only">Remove filter for {{ key }}</span>
                  <svg class="h-3 w-3" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                  </svg>
                </button>
              </div>
              
              <button 
                v-if="Object.keys(activeFilters).length > 0"
                @click="clearFilters"
                class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-gray-100 text-gray-800 hover:bg-gray-200 dark:bg-gray-700 dark:text-gray-300 dark:hover:bg-gray-600"
              >
                Clear all
              </button>
            </div>
          </div>
          
          <!-- Sort options -->
          <div class="flex items-center">
            <label for="sort-by" class="mr-2 text-sm font-medium text-gray-700 dark:text-gray-300">Sort by:</label>
            <select 
              id="sort-by" 
              v-model="sortOption"
              @change="sortProducts"
              class="block pl-3 pr-10 py-2 text-base border-gray-300 dark:border-gray-600 focus:outline-none focus:ring-pravis-500 focus:border-pravis-500 sm:text-sm rounded-md bg-white dark:bg-gray-800 text-gray-900 dark:text-white"
            >
              <option value="newest">Newest</option>
              <option value="price-low">Price: Low to High</option>
              <option value="price-high">Price: High to Low</option>
              <option value="popular">Most Popular</option>
              <option value="rating">Highest Rated</option>
            </select>
          </div>
        </div>
      </div>
    </section>
    
    <!-- Mobile filters panel -->
    <div 
      v-if="showFilters" 
      class="fixed inset-0 z-40 overflow-hidden lg:hidden"
    >
      <div class="absolute inset-0 bg-black bg-opacity-25" @click="showFilters = false"></div>
      
      <div class="fixed inset-y-0 left-0 max-w-xs w-full bg-white dark:bg-gray-800 shadow-xl flex flex-col">
        <div class="flex items-center justify-between px-4 py-3 border-b border-gray-200 dark:border-gray-700">
          <h2 class="text-lg font-medium text-gray-900 dark:text-white">Filters</h2>
          <button 
            @click="showFilters = false"
            class="text-gray-400 hover:text-gray-500 dark:text-gray-300 dark:hover:text-white focus:outline-none focus:ring-2 focus:ring-pravis-500"
          >
            <span class="sr-only">Close filters</span>
            <svg class="h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        
        <div class="flex-1 overflow-auto py-4 px-4">
          <!-- Category filter -->
          <div class="border-b border-gray-200 dark:border-gray-700 pb-6">
            <h3 class="text-sm font-medium text-gray-900 dark:text-white">Categories</h3>
            <div class="mt-3 space-y-3">
              <div 
                v-for="category in categories" 
                :key="category.id"
                class="flex items-center"
              >
                <input 
                  :id="`category-${category.id}`" 
                  :value="category.id"
                  v-model="selectedCategories"
                  type="checkbox" 
                  class="h-4 w-4 border-gray-300 rounded text-pravis-600 focus:ring-pravis-500"
                />
                <label :for="`category-${category.id}`" class="ml-3 text-sm text-gray-600 dark:text-gray-400">
                  {{ category.name }}
                </label>
              </div>
            </div>
          </div>
          
          <!-- Price range filter -->
          <div class="border-b border-gray-200 dark:border-gray-700 py-6">
            <h3 class="text-sm font-medium text-gray-900 dark:text-white">Price Range</h3>
            <div class="mt-3">
              <div class="flex items-center justify-between">
                <div class="w-1/2 pr-2">
                  <label for="min-price" class="sr-only">Minimum Price</label>
                  <input 
                    id="min-price" 
                    v-model.number="priceRange[0]"
                    type="number" 
                    placeholder="Min" 
                    class="block w-full border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:ring-pravis-500 focus:border-pravis-500 sm:text-sm bg-white dark:bg-gray-800 text-gray-900 dark:text-white"
                  />
                </div>
                <div class="w-1/2 pl-2">
                  <label for="max-price" class="sr-only">Maximum Price</label>
                  <input 
                    id="max-price" 
                    v-model.number="priceRange[1]"
                    type="number" 
                    placeholder="Max" 
                    class="block w-full border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:ring-pravis-500 focus:border-pravis-500 sm:text-sm bg-white dark:bg-gray-800 text-gray-900 dark:text-white"
                  />
                </div>
              </div>
            </div>
          </div>
          
          <!-- More filters can be added here -->
        </div>
        
        <div class="border-t border-gray-200 dark:border-gray-700 py-4 px-4">
          <Button 
            variant="primary" 
            block 
            @click="applyFilters"
          >
            Apply Filters
          </Button>
          <Button 
            variant="light" 
            block 
            class="mt-3"
            @click="clearFilters"
          >
            Clear All
          </Button>
        </div>
      </div>
    </div>
    
    <!-- Main content -->
    <section class="py-8">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex flex-col lg:flex-row -mx-4">
          <!-- Sidebar filters (desktop) -->
          <div class="hidden lg:block lg:w-1/4 px-4">
            <div class="sticky top-24">
              <!-- Category filter -->
              <div class="border-b border-gray-200 dark:border-gray-700 pb-6">
                <h3 class="text-sm font-medium text-gray-900 dark:text-white">Categories</h3>
                <div class="mt-3 space-y-3">
                  <div 
                    v-for="category in categories" 
                    :key="category.id"
                    class="flex items-center"
                  >
                    <input 
                      :id="`category-desktop-${category.id}`" 
                      :value="category.id"
                      v-model="selectedCategories"
                      type="checkbox" 
                      class="h-4 w-4 border-gray-300 rounded text-pravis-600 focus:ring-pravis-500"
                    />
                    <label :for="`category-desktop-${category.id}`" class="ml-3 text-sm text-gray-600 dark:text-gray-400">
                      {{ category.name }}
                    </label>
                  </div>
                </div>
              </div>
              
              <!-- Price range filter -->
              <div class="border-b border-gray-200 dark:border-gray-700 py-6">
                <h3 class="text-sm font-medium text-gray-900 dark:text-white">Price Range</h3>
                <div class="mt-3">
                  <div class="flex items-center justify-between">
                    <div class="w-1/2 pr-2">
                      <label for="min-price-desktop" class="sr-only">Minimum Price</label>
                      <input 
                        id="min-price-desktop" 
                        v-model.number="priceRange[0]"
                        type="number" 
                        placeholder="Min" 
                        class="block w-full border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:ring-pravis-500 focus:border-pravis-500 sm:text-sm bg-white dark:bg-gray-800 text-gray-900 dark:text-white"
                      />
                    </div>
                    <div class="w-1/2 pl-2">
                      <label for="max-price-desktop" class="sr-only">Maximum Price</label>
                      <input 
                        id="max-price-desktop" 
                        v-model.number="priceRange[1]"
                        type="number" 
                        placeholder="Max" 
                        class="block w-full border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:ring-pravis-500 focus:border-pravis-500 sm:text-sm bg-white dark:bg-gray-800 text-gray-900 dark:text-white"
                      />
                    </div>
                  </div>
                  <Button 
                    variant="primary" 
                    size="sm"
                    block 
                    class="mt-3"
                    @click="applyFilters"
                  >
                    Apply
                  </Button>
                </div>
              </div>
              
              <!-- More filters can be added here -->
            </div>
          </div>
          
          <!-- Product grid -->
          <div class="w-full lg:w-3/4 px-4">
            <!-- Loading state -->
            <div v-if="loading" class="flex justify-center py-12">
              <svg class="animate-spin h-10 w-10 text-pravis-500" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
            </div>
            
            <!-- No results state -->
            <div v-else-if="!loading && filteredProducts.length === 0" class="flex flex-col items-center justify-center py-12">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-16 w-16 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <h3 class="mt-4 text-lg font-medium text-gray-900 dark:text-white">No products found</h3>
              <p class="mt-2 text-gray-500 dark:text-gray-400">Try adjusting your filters or search term.</p>
              <Button 
                variant="outline-primary" 
                class="mt-6"
                @click="clearFilters"
              >
                Clear Filters
              </Button>
            </div>
            
            <!-- Product grid -->
            <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
              <div 
                v-for="product in filteredProducts" 
                :key="product.id"
                class="transition-all duration-200 ease-in-out"
              >
                <ProductCard 
                  :product="product" 
                  @quick-view="openQuickView"
                  @add-to-cart="handleAddToCart"
                  @wishlist-toggle="handleWishlistToggle"
                />
              </div>
            </div>
            
            <!-- Pagination -->
            <div v-if="totalPages > 1" class="mt-12 flex justify-center">
              <nav class="relative z-0 inline-flex rounded-md shadow-sm -space-x-px" aria-label="Pagination">
                <!-- Previous button -->
                <button
                  @click="currentPage > 1 && (currentPage--)"
                  :disabled="currentPage <= 1"
                  class="relative inline-flex items-center px-2 py-2 rounded-l-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 text-sm font-medium text-gray-500 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-700 disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  <span class="sr-only">Previous</span>
                  <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                    <path fill-rule="evenodd" d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z" clip-rule="evenodd" />
                  </svg>
                </button>
                
                <!-- Page numbers -->
                <template v-for="page in paginationPages">
                  <button
                    v-if="page !== '...'"
                    :key="page"
                    @click="currentPage = page"
                    :class="[
                      'relative inline-flex items-center px-4 py-2 border text-sm font-medium',
                      currentPage === page
                        ? 'z-10 bg-pravis-50 dark:bg-pravis-900 border-pravis-500 dark:border-pravis-400 text-pravis-600 dark:text-pravis-200'
                        : 'bg-white dark:bg-gray-800 border-gray-300 dark:border-gray-600 text-gray-500 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-700'
                    ]"
                  >
                    {{ page }}
                  </button>
                  <span
                    v-else
                    :key="`ellipsis-${page}`"
                    class="relative inline-flex items-center px-4 py-2 border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 text-sm font-medium text-gray-700 dark:text-gray-300"
                  >
                    ...
                  </span>
                </template>
                
                <!-- Next button -->
                <button
                  @click="currentPage < totalPages && (currentPage++)"
                  :disabled="currentPage >= totalPages"
                  class="relative inline-flex items-center px-2 py-2 rounded-r-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 text-sm font-medium text-gray-500 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-700 disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  <span class="sr-only">Next</span>
                  <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                    <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" />
                  </svg>
                </button>
              </nav>
            </div>
          </div>
        </div>
      </div>
    </section>
    
    <!-- Quick view modal -->
    <div 
      v-if="quickViewProduct"
      class="fixed z-50 inset-0 overflow-y-auto"
    >
      <div class="flex items-center justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
        <div class="fixed inset-0 bg-black bg-opacity-50 transition-opacity" @click="closeQuickView"></div>
        
        <div class="inline-block align-bottom bg-white dark:bg-gray-800 rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-3xl sm:w-full">
          <div class="absolute top-0 right-0 pt-4 pr-4">
            <button 
              @click="closeQuickView"
              class="text-gray-400 hover:text-gray-500 dark:text-gray-300 dark:hover:text-white focus:outline-none focus:ring-2 focus:ring-pravis-500"
            >
              <span class="sr-only">Close</span>
              <svg class="h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
          
          <div class="flex flex-col md:flex-row">
            <!-- Product image -->
            <div class="md:w-1/2 p-6">
              <div class="aspect-w-3 aspect-h-4 bg-gray-100 dark:bg-gray-700 rounded-lg overflow-hidden">
                <img 
                  :src="quickViewProduct.image" 
                  :alt="quickViewProduct.name"
                  class="w-full h-full object-center object-cover"
                />
              </div>
            </div>
            
            <!-- Product info -->
            <div class="md:w-1/2 p-6">
              <h3 class="text-xl font-medium text-gray-900 dark:text-white">{{ quickViewProduct.name }}</h3>
              
              <p v-if="quickViewProduct.category" class="mt-1 text-sm text-gray-500 dark:text-gray-400">
                {{ quickViewProduct.category }}
              </p>
              
              <!-- Rating -->
              <div v-if="quickViewProduct.rating" class="mt-2 flex items-center">
                <div class="flex items-center">
                  <svg 
                    v-for="i in 5" 
                    :key="i"
                    :class="[
                      i <= Math.round(quickViewProduct.rating) ? 'text-yellow-400' : 'text-gray-300 dark:text-gray-600',
                      'h-5 w-5'
                    ]"
                    xmlns="http://www.w3.org/2000/svg" 
                    viewBox="0 0 20 20" 
                    fill="currentColor" 
                    aria-hidden="true"
                  >
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118l-2.8-2.034c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                </div>
                <span class="ml-2 text-sm text-gray-500 dark:text-gray-400">
                  {{ quickViewProduct.rating }} ({{ quickViewProduct.reviewCount || 0 }} reviews)
                </span>
              </div>
              
              <!-- Price -->
              <div class="mt-4">
                <span v-if="quickViewProduct.originalPrice && quickViewProduct.onSale" class="text-gray-500 line-through mr-2">
                  {{ formatPrice(quickViewProduct.originalPrice) }}
                </span>
                <span class="text-xl font-medium text-gray-900 dark:text-white">
                  {{ formatPrice(quickViewProduct.price) }}
                </span>
              </div>
              
              <!-- Description -->
              <div class="mt-4">
                <p class="text-base text-gray-700 dark:text-gray-300">
                  {{ quickViewProduct.description }}
                </p>
              </div>
              
              <!-- Add to cart -->
              <div class="mt-6">
                <div class="flex items-center space-x-3">
                  <div class="flex items-center border border-gray-300 dark:border-gray-600 rounded-md">
                    <button 
                      @click="quickViewQuantity > 1 && quickViewQuantity--"
                      class="p-2 text-gray-500 dark:text-gray-400 hover:text-gray-600 dark:hover:text-gray-300 focus:outline-none focus:ring-2 focus:ring-pravis-500"
                    >
                      <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H4" />
                      </svg>
                    </button>
                    <input 
                      v-model="quickViewQuantity"
                      type="number" 
                      min="1" 
                      class="w-12 text-center border-0 focus:ring-0 p-1 text-gray-900 dark:text-white bg-white dark:bg-gray-800"
                    />
                    <button 
                      @click="quickViewQuantity++"
                      class="p-2 text-gray-500 dark:text-gray-400 hover:text-gray-600 dark:hover:text-gray-300 focus:outline-none focus:ring-2 focus:ring-pravis-500"
                    >
                      <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
                      </svg>
                    </button>
                  </div>
                  
                  <Button 
                    variant="primary"
                    class="flex-1"
                    @click="addToCartFromQuickView"
                  >
                    Add to Cart
                  </Button>
                </div>
              </div>
              
              <!-- View details link -->
              <div class="mt-6">
                <NuxtLink 
                  :to="`/shop/product/${quickViewProduct.id}`"
                  class="text-pravis-600 hover:text-pravis-500 dark:text-pravis-400 dark:hover:text-pravis-300 font-medium"
                >
                  View full details
                  <span aria-hidden="true"> &rarr;</span>
                </NuxtLink>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Voice assistant -->
    <VoiceAssistant />
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted, watch } from 'vue'
import ProductCard from '~/components/common/ProductCard.vue'
import Button from '~/components/common/Button.vue'
import VoiceAssistant from '~/components/common/VoiceAssistant.vue'
import { useProducts } from '~/composables/useProducts'
import { useCartStore } from '~/store/cart'

// Setup composables and stores
const { getProducts, getCategories } = useProducts()
const cartStore = useCartStore()
const route = useRoute()
const router = useRouter()

// Initialize state
const products = ref([])
const categories = ref([])
const loading = ref(true)
const error = ref(null)
const showFilters = ref(false)
const currentPage = ref(1)
const itemsPerPage = ref(12)
const totalItems = ref(0)
const sortOption = ref('newest')
const selectedCategories = ref([])
const priceRange = ref([0, 5000])
const activeFilters = reactive({})
const quickViewProduct = ref(null)
const quickViewQuantity = ref(1)

// Get query params on load
onMounted(async () => {
  try {
    // Get initial query params
    const query = route.query
    
    if (query.category) {
      selectedCategories.value = Array.isArray(query.category) 
        ? query.category 
        : [query.category]
      activeFilters.category = selectedCategories.value.join(', ')
    }
    
    if (query.minPrice) {
      priceRange.value[0] = Number(query.minPrice)
      activeFilters['min price'] = `$${priceRange.value[0]}`
    }
    
    if (query.maxPrice) {
      priceRange.value[1] = Number(query.maxPrice)
      activeFilters['max price'] = `$${priceRange.value[1]}`
    }
    
    if (query.sort) {
      sortOption.value = query.sort
    }
    
    if (query.page) {
      currentPage.value = Number(query.page)
    }
    
    // Load categories
    const categoriesData = await getCategories()
    categories.value = categoriesData
    
    // Load products
    await loadProducts()
    
    // Track page view
    const { trackPageView } = useAnalytics()
    trackPageView('shop', { 
      filters: activeFilters, 
      sort: sortOption.value,
      page: currentPage.value
    })
  } catch (err) {
    error.value = err.message || 'Failed to load shop page'
  } finally {
    loading.value = false
  }
})

// Watch for changes in pagination or sorting
watch([currentPage, sortOption], () => {
  loadProducts()
  updateQueryParams()
})

// Load products with current filters and sorting
async function loadProducts() {
  loading.value = true
  
  try {
    // Prepare filter options
    const options = {
      page: currentPage.value,
      limit: itemsPerPage.value,
      sort: sortOption.value
    }
    
    if (selectedCategories.value.length > 0) {
      options.category = selectedCategories.value.join(',')
    }
    
    if (priceRange.value[0] > 0) {
      options.minPrice = priceRange.value[0]
    }
    
    if (priceRange.value[1] < 5000) {
      options.maxPrice = priceRange.value[1]
    }
    
    // Get products
    const result = await getProducts(options)
    
    // Mock pagination data for demo purposes
    // In a real app, this would come from the API
    products.value = result
    totalItems.value = 100 // Mock total for demo
  } catch (err) {
    error.value = err.message || 'Failed to load products'
  } finally {
    loading.value = false
  }
}

// Apply filters and reload products
function applyFilters() {
  // Update active filters
  activeFilters = {}
  
  if (selectedCategories.value.length > 0) {
    const categoryNames = selectedCategories.value.map(id => {
      const category = categories.value.find(c => c.id === id)
      return category ? category.name : id
    })
    activeFilters.category = categoryNames.join(', ')
  }
  
  if (priceRange.value[0] > 0) {
    activeFilters['min price'] = `$${priceRange.value[0]}`
  }
  
  if (priceRange.value[1] < 5000) {
    activeFilters['max price'] = `$${priceRange.value[1]}`
  }
  
  // Reset to first page
  currentPage.value = 1
  
  // Close mobile filters
  showFilters.value = false
  
  // Reload products
  loadProducts()
  
  // Update URL
  updateQueryParams()
}

// Clear all filters
function clearFilters() {
  selectedCategories.value = []
  priceRange.value = [0, 5000]
  activeFilters = {}
  currentPage.value = 1
  
  // Close mobile filters
  showFilters.value = false
  
  // Reload products
  loadProducts()
  
  // Update URL
  updateQueryParams()
}

// Remove a specific filter
function removeFilter(key) {
  if (key === 'category') {
    selectedCategories.value = []
  } else if (key === 'min price') {
    priceRange.value[0] = 0
  } else if (key === 'max price') {
    priceRange.value[1] = 5000
  }
  
  delete activeFilters[key]
  
  // Reload products
  loadProducts()
  
  // Update URL
  updateQueryParams()
}

// Sort products
function sortProducts() {
  loadProducts()
  updateQueryParams()
}

// Update URL query parameters
function updateQueryParams() {
  const query = {}
  
  if (selectedCategories.value.length > 0) {
    query.category = selectedCategories.value
  }
  
  if (priceRange.value[0] > 0) {
    query.minPrice = priceRange.value[0]
  }
  
  if (priceRange.value[1] < 5000) {
    query.maxPrice = priceRange.value[1]
  }
  
  if (sortOption.value !== 'newest') {
    query.sort = sortOption.value
  }
  
  if (currentPage.value > 1) {
    query.page = currentPage.value
  }
  
  router.push({ query })
}

// Format price for display
function formatPrice(price) {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
  }).format(price)
}

// Quick view product
function openQuickView(product) {
  quickViewProduct.value = product
  quickViewQuantity.value = 1
  
  // Track analytics
  const { trackInteraction } = useAnalytics()
  trackInteraction('product', 'quick_view', {
    product_id: product.id,
    product_name: product.name
  })
}

function closeQuickView() {
  quickViewProduct.value = null
}

// Add to cart from quick view
function addToCartFromQuickView() {
  if (!quickViewProduct.value) return
  
  const product = { ...quickViewProduct.value }
  cartStore.addItem(product, quickViewQuantity.value)
  
  // Show success message
  // (In a real app, you'd use a toast or notification system)
  alert(`Added ${quickViewQuantity.value} ${product.name} to cart!`)
  
  // Close quick view
  closeQuickView()
  
  // Track analytics
  const { trackInteraction } = useAnalytics()
  trackInteraction('product', 'add_to_cart', {
    product_id: product.id,
    product_name: product.name,
    price: product.price,
    quantity: quickViewQuantity.value
  })
}

// Add to cart from product card
function handleAddToCart(product) {
  // Show success message
  // (In a real app, you'd use a toast or notification system)
  alert(`Added ${product.name} to cart!`)
}

// Handle wishlist toggle
function handleWishlistToggle(data) {
  const { product, inWishlist } = data
  // In a real app, you'd update a wishlist store here
  
  // Show success message
  // (In a real app, you'd use a toast or notification system)
  if (inWishlist) {
    alert(`Added ${product.name} to your wishlist!`)
  } else {
    alert(`Removed ${product.name} from your wishlist!`)
  }
}

// Computed properties
const totalPages = computed(() => Math.ceil(totalItems.value / itemsPerPage.value))

const filteredProducts = computed(() => {
  // In a real app, filtering would be done on the server
  // This is just for demo purposes
  return products.value
})

// Generate pagination pages array
const paginationPages = computed(() => {
  const pages = []
  
  if (totalPages.value <= 7) {
    // Show all pages if 7 or fewer
    for (let i = 1; i <= totalPages.value; i++) {
      pages.push(i)
    }
  } else {
    // Complex pagination with ellipsis
    pages.push(1)
    
    if (currentPage.value > 3) {
      pages.push('...')
    }
    
    // Pages around current page
    const start = Math.max(2, currentPage.value - 1)
    const end = Math.min(totalPages.value - 1, currentPage.value + 1)
    
    for (let i = start; i <= end; i++) {
      pages.push(i)
    }
    
    if (currentPage.value < totalPages.value - 2) {
      pages.push('...')
    }
    
    pages.push(totalPages.value)
  }
  
  return pages
})
</script>
