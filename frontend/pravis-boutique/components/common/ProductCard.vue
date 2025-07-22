<template>
  <div class="group relative bg-white dark:bg-gray-800 rounded-lg shadow-sm overflow-hidden transition transform hover:-translate-y-1 hover:shadow-md" role="article" aria-labelledby="product-name-{{product.id}}" tabindex="0">
    <!-- Product image with loading state -->
    <div class="relative aspect-w-3 aspect-h-4 bg-gray-100 dark:bg-gray-700">
      <NuxtLink :to="`/shop/product/${product.id}`" aria-label="View details of {{product.name}}">
        <div v-if="loading" class="absolute inset-0 flex items-center justify-center" role="status" aria-label="Loading product image">
          <svg class="animate-spin h-8 w-8 text-pravis-500" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" aria-hidden="true">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
          <span class="sr-only">Loading</span>
        </div>
        <img 
          :src="product.image" 
          :alt="product.name"
          class="w-full h-full object-center object-cover"
          @load="loading = false"
          :class="{ 'opacity-0': loading }"
        />
      </NuxtLink>
      
      <!-- Badge (if on sale or new) -->
      <div v-if="product.onSale || product.isNew" class="absolute top-2 left-2">
        <span 
          v-if="product.onSale" 
          class="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-red-100 text-red-800 dark:bg-red-800 dark:text-red-100"
          role="status"
          aria-label="This product is on sale"
        >
          Sale
        </span>
        <span 
          v-else-if="product.isNew" 
          class="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-green-100 text-green-800 dark:bg-green-800 dark:text-green-100"
          role="status"
          aria-label="This is a new product"
        >
          New
        </span>
      </div>
      
      <!-- Quick actions -->
      <div class="absolute inset-0 bg-black bg-opacity-20 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity">
        <div class="flex space-x-2">
          <!-- Quick view -->
          <button 
            @click="quickView"
            class="p-2 rounded-full bg-white text-gray-900 hover:bg-pravis-500 hover:text-white transition-colors focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-pravis-500"
            aria-label="Quick view of {{product.name}}"
          >
            <span class="sr-only">Quick view</span>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
            </svg>
          </button>
          
          <!-- Add to cart -->
          <button 
            @click="addToCart"
            class="p-2 rounded-full bg-white text-gray-900 hover:bg-pravis-500 hover:text-white transition-colors focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-pravis-500"
            aria-label="Add {{product.name}} to cart"
          >
            <span class="sr-only">Add to cart</span>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />
            </svg>
          </button>
          
          <!-- Wishlist -->
          <button 
            @click="toggleWishlist"
            class="p-2 rounded-full bg-white text-gray-900 hover:bg-pravis-500 hover:text-white transition-colors focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-pravis-500"
            :class="{ 'bg-red-500 text-white': inWishlist }"
            :aria-label="inWishlist ? `Remove ${product.name} from wishlist` : `Add ${product.name} to wishlist`"
            :aria-pressed="inWishlist ? 'true' : 'false'"
          >
            <span class="sr-only">{{ inWishlist ? 'Remove from wishlist' : 'Add to wishlist' }}</span>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" :class="{ 'fill-current': inWishlist }" aria-hidden="true">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
            </svg>
          </button>
        </div>
      </div>
    </div>
    
    <!-- Product info -->
    <div class="p-4">
      <h3 class="text-sm font-medium text-gray-900 dark:text-white" :id="`product-name-${product.id}`">
        <NuxtLink :to="`/shop/product/${product.id}`" class="hover:text-pravis-600 dark:hover:text-pravis-400" aria-label="View details of {{product.name}}">
          {{ product.name }}
        </NuxtLink>
      </h3>
      
      <!-- Category -->
      <p v-if="product.category" class="mt-1 text-sm text-gray-500 dark:text-gray-400">
        {{ product.category }}
      </p>
      
      <!-- Price -->
      <div class="mt-2 flex justify-between items-center">
        <div>
          <span v-if="product.originalPrice && product.onSale" class="text-sm text-gray-500 line-through mr-2">
            {{ formatPrice(product.originalPrice) }}
          </span>
          <span class="text-sm font-medium text-gray-900 dark:text-white">
            {{ formatPrice(product.price) }}
          </span>
        </div>
        
        <!-- Rating stars -->
        <div v-if="product.rating" class="flex items-center">
          <div class="flex items-center" role="img" :aria-label="`Rated ${product.rating} out of 5 stars`">
            <svg 
              v-for="i in 5" 
              :key="i"
              :class="[
                i <= Math.round(product.rating) ? 'text-yellow-400' : 'text-gray-300 dark:text-gray-600',
                'h-4 w-4'
              ]"
              xmlns="http://www.w3.org/2000/svg" 
              viewBox="0 0 20 20" 
              fill="currentColor" 
              aria-hidden="true"
            >
              <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118l-2.8-2.034c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
            </svg>
          </div>
          <span class="ml-1 text-xs text-gray-500 dark:text-gray-400" aria-label="{{product.reviewCount || 0}} reviews">
            ({{ product.reviewCount || 0 }})
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useCartStore } from '~/store/cart'
import { announceToScreenReader, playAudioFeedback } from '~/utils/accessibility'

// Props
const props = defineProps({
  product: {
    type: Object,
    required: true
  }
})

// Emits
const emit = defineEmits(['quick-view', 'wishlist-toggle', 'add-to-cart'])

// State
const loading = ref(true)
const inWishlist = ref(false) // This would be connected to a wishlist store in a real app

// Cart store
const cartStore = useCartStore()

// Methods
const formatPrice = (price) => {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
  }).format(price)
}

const addToCart = () => {
  cartStore.addItem(props.product)
  emit('add-to-cart', props.product)
  
  // Play audio feedback
  playAudioFeedback('addToCart')
  
  // Announce to screen reader
  announceToScreenReader(`${props.product.name} added to cart`, 'polite')
  
  // Analytics tracking
  const { trackInteraction } = useAnalytics()
  trackInteraction('product', 'add_to_cart', {
    product_id: props.product.id,
    product_name: props.product.name,
    price: props.product.price
  })
}

const toggleWishlist = () => {
  inWishlist.value = !inWishlist.value
  emit('wishlist-toggle', {
    product: props.product,
    inWishlist: inWishlist.value
  })
  
  // Play audio feedback
  playAudioFeedback(inWishlist.value ? 'success' : 'click')
  
  // Announce to screen reader
  announceToScreenReader(
    inWishlist.value 
      ? `${props.product.name} added to wishlist` 
      : `${props.product.name} removed from wishlist`, 
    'polite'
  )
  
  // Analytics tracking
  const { trackInteraction } = useAnalytics()
  trackInteraction('product', inWishlist.value ? 'add_to_wishlist' : 'remove_from_wishlist', {
    product_id: props.product.id,
    product_name: props.product.name
  })
}

// Quick view handler
const quickView = () => {
  emit('quick-view', props.product)
  
  // Play audio feedback
  playAudioFeedback('click')
  
  // Announce to screen reader
  announceToScreenReader(`Quick view of ${props.product.name} opened`, 'polite')
}
</script>
