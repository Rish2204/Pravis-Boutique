<template>
  <div>
    <!-- Loading state -->
    <div v-if="loading" class="py-16 flex justify-center">
      <svg class="animate-spin h-10 w-10 text-pravis-500" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
        <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
        <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
      </svg>
    </div>
    
    <!-- Error state -->
    <div v-else-if="error" class="py-16 flex flex-col items-center justify-center">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-16 w-16 text-red-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
      </svg>
      <h2 class="mt-4 text-xl font-medium text-gray-900 dark:text-white">Error loading product</h2>
      <p class="mt-2 text-gray-500 dark:text-gray-400">{{ error }}</p>
      <Button 
        variant="primary" 
        class="mt-6"
        @click="reloadProduct"
      >
        Try Again
      </Button>
    </div>
    
    <!-- Product details -->
    <div v-else-if="product" class="py-12">
      <!-- Breadcrumbs -->
      <nav class="mb-10 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto">
        <ol class="flex items-center space-x-2 text-sm text-gray-500 dark:text-gray-400">
          <li>
            <NuxtLink to="/" class="hover:text-pravis-600 dark:hover:text-pravis-400">
              Home
            </NuxtLink>
          </li>
          <li class="flex items-center">
            <svg class="h-4 w-4 text-gray-400" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
            </svg>
          </li>
          <li>
            <NuxtLink to="/shop" class="hover:text-pravis-600 dark:hover:text-pravis-400">
              Shop
            </NuxtLink>
          </li>
          <li class="flex items-center">
            <svg class="h-4 w-4 text-gray-400" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
            </svg>
          </li>
          <li v-if="product.category">
            <NuxtLink :to="`/shop?category=${product.categoryId}`" class="hover:text-pravis-600 dark:hover:text-pravis-400">
              {{ product.category }}
            </NuxtLink>
          </li>
          <li v-if="product.category" class="flex items-center">
            <svg class="h-4 w-4 text-gray-400" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
            </svg>
          </li>
          <li class="font-medium text-gray-900 dark:text-white">
            {{ product.name }}
          </li>
        </ol>
      </nav>
      
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="lg:grid lg:grid-cols-2 lg:gap-x-8">
          <!-- Product images -->
          <div class="lg:max-w-lg lg:self-start">
            <!-- Main image -->
            <div class="aspect-w-1 aspect-h-1 rounded-lg overflow-hidden">
              <img 
                :src="currentImage" 
                :alt="product.name"
                class="w-full h-full object-center object-cover"
              />
            </div>
            
            <!-- Image thumbnails -->
            <div v-if="product.images && product.images.length > 1" class="mt-4 grid grid-cols-4 gap-4">
              <button
                v-for="(image, index) in product.images"
                :key="index"
                @click="currentImage = image"
                class="relative rounded-md overflow-hidden focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-pravis-500"
                :class="{ 'ring-2 ring-pravis-500': currentImage === image }"
              >
                <img 
                  :src="image" 
                  alt=""
                  class="w-full h-full object-center object-cover"
                />
                <div 
                  class="absolute inset-0 rounded-md ring-1 ring-inset"
                  :class="currentImage === image ? 'ring-pravis-500' : 'ring-transparent'"
                ></div>
              </button>
            </div>
          </div>
          
          <!-- Product details -->
          <div class="mt-10 lg:mt-0">
            <!-- Badge (if on sale or new) -->
            <div v-if="product.onSale || product.isNew" class="mb-4">
              <span 
                v-if="product.onSale" 
                class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-red-100 text-red-800 dark:bg-red-800 dark:text-red-100"
              >
                Sale
              </span>
              <span 
                v-else-if="product.isNew" 
                class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-green-100 text-green-800 dark:bg-green-800 dark:text-green-100"
              >
                New
              </span>
            </div>
            
            <h1 class="text-3xl font-extrabold text-gray-900 dark:text-white">
              {{ product.name }}
            </h1>
            
            <!-- Rating -->
            <div v-if="product.rating" class="mt-3 flex items-center">
              <div class="flex items-center">
                <svg 
                  v-for="i in 5" 
                  :key="i"
                  :class="[
                    i <= Math.round(product.rating) ? 'text-yellow-400' : 'text-gray-300 dark:text-gray-600',
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
                {{ product.rating }} ({{ product.reviewCount || 0 }} reviews)
              </span>
            </div>
            
            <!-- Price -->
            <div class="mt-4">
              <span v-if="product.originalPrice && product.onSale" class="text-gray-500 line-through mr-2">
                {{ formatPrice(product.originalPrice) }}
              </span>
              <span class="text-2xl font-medium text-gray-900 dark:text-white">
                {{ formatPrice(product.price) }}
              </span>
              <span v-if="product.originalPrice && product.onSale" class="ml-2 text-red-600 dark:text-red-400">
                Save {{ formatDiscountPercentage(product.originalPrice, product.price) }}%
              </span>
            </div>
            
            <!-- Availability -->
            <div class="mt-4">
              <p class="text-base text-gray-700 dark:text-gray-300">
                <span v-if="product.inStock" class="text-green-600 dark:text-green-400 font-medium">In Stock</span>
                <span v-else class="text-red-600 dark:text-red-400 font-medium">Out of Stock</span>
                <span v-if="product.stockCount" class="ml-2 text-sm text-gray-500 dark:text-gray-400">
                  ({{ product.stockCount }} available)
                </span>
              </p>
            </div>
            
            <!-- Description -->
            <div class="mt-6">
              <h3 class="text-sm font-medium text-gray-900 dark:text-white">Description</h3>
              <div class="mt-2 prose prose-sm text-gray-700 dark:text-gray-300">
                <p>{{ product.description }}</p>
                <div v-if="product.descriptionHtml" v-html="product.descriptionHtml"></div>
              </div>
            </div>
            
            <!-- Attributes -->
            <div v-if="product.attributes && Object.keys(product.attributes).length > 0" class="mt-6">
              <h3 class="text-sm font-medium text-gray-900 dark:text-white">Details</h3>
              <div class="mt-2">
                <ul class="list-disc list-inside text-sm text-gray-700 dark:text-gray-300 space-y-1">
                  <li v-for="(value, key) in product.attributes" :key="key">
                    <span class="font-medium">{{ formatAttributeName(key) }}:</span> {{ value }}
                  </li>
                </ul>
              </div>
            </div>
            
            <!-- Variants -->
            <div v-if="product.variants && product.variants.length > 0" class="mt-6">
              <h3 class="text-sm font-medium text-gray-900 dark:text-white">Options</h3>
              <div v-for="(variant, index) in product.variantGroups" :key="index" class="mt-4">
                <h4 class="text-sm text-gray-600 dark:text-gray-400">{{ variant.name }}</h4>
                <div class="mt-2 flex flex-wrap gap-2">
                  <button
                    v-for="option in variant.options"
                    :key="option.id"
                    @click="selectVariantOption(variant.id, option.id)"
                    class="px-3 py-1 rounded-md text-sm font-medium focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-pravis-500"
                    :class="isVariantOptionSelected(variant.id, option.id) 
                      ? 'bg-pravis-600 text-white' 
                      : 'bg-gray-100 text-gray-800 dark:bg-gray-700 dark:text-gray-200 hover:bg-gray-200 dark:hover:bg-gray-600'"
                  >
                    {{ option.name }}
                  </button>
                </div>
              </div>
            </div>
            
            <!-- Add to cart -->
            <div class="mt-8">
              <div class="flex items-center space-x-4">
                <div class="flex items-center border border-gray-300 dark:border-gray-600 rounded-md">
                  <button 
                    @click="quantity > 1 && quantity--"
                    class="p-2 text-gray-500 dark:text-gray-400 hover:text-gray-600 dark:hover:text-gray-300 focus:outline-none focus:ring-2 focus:ring-pravis-500"
                    :disabled="!product.inStock"
                  >
                    <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H4" />
                    </svg>
                  </button>
                  <input 
                    v-model="quantity"
                    type="number" 
                    min="1" 
                    :max="product.stockCount || 99"
                    class="w-16 text-center border-0 focus:ring-0 p-2 text-gray-900 dark:text-white bg-white dark:bg-gray-800"
                    :disabled="!product.inStock"
                  />
                  <button 
                    @click="quantity++"
                    class="p-2 text-gray-500 dark:text-gray-400 hover:text-gray-600 dark:hover:text-gray-300 focus:outline-none focus:ring-2 focus:ring-pravis-500"
                    :disabled="!product.inStock || (product.stockCount && quantity >= product.stockCount)"
                  >
                    <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
                    </svg>
                  </button>
                </div>
                
                <Button 
                  variant="primary"
                  size="lg"
                  class="flex-1"
                  :disabled="!product.inStock"
                  @click="addToCart"
                >
                  <template #icon>
                    <svg class="-ml-1 mr-2 h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z" />
                    </svg>
                  </template>
                  {{ product.inStock ? 'Add to Cart' : 'Out of Stock' }}
                </Button>
                
                <button 
                  @click="toggleWishlist"
                  class="p-3 rounded-full border border-gray-300 dark:border-gray-600 text-gray-700 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-pravis-500"
                  :class="{ 'bg-red-50 text-red-600 border-red-300 dark:bg-red-900 dark:text-red-300 dark:border-red-700': inWishlist }"
                >
                  <span class="sr-only">{{ inWishlist ? 'Remove from wishlist' : 'Add to wishlist' }}</span>
                  <svg class="h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" :class="{ 'fill-current': inWishlist }">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
                  </svg>
                </button>
              </div>
            </div>
            
            <!-- Social sharing -->
            <div class="mt-8 border-t border-gray-200 dark:border-gray-700 pt-8">
              <h3 class="text-sm font-medium text-gray-900 dark:text-white">Share</h3>
              <div class="mt-2 flex space-x-3">
                <button 
                  @click="shareProduct('facebook')"
                  class="text-gray-400 hover:text-facebook focus:outline-none"
                >
                  <span class="sr-only">Share on Facebook</span>
                  <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                    <path fill-rule="evenodd" d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z" clip-rule="evenodd" />
                  </svg>
                </button>
                <button 
                  @click="shareProduct('twitter')"
                  class="text-gray-400 hover:text-twitter focus:outline-none"
                >
                  <span class="sr-only">Share on Twitter</span>
                  <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                    <path d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84" />
                  </svg>
                </button>
                <button 
                  @click="shareProduct('pinterest')"
                  class="text-gray-400 hover:text-pinterest focus:outline-none"
                >
                  <span class="sr-only">Share on Pinterest</span>
                  <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                    <path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd" />
                  </svg>
                </button>
                <button 
                  @click="shareProduct('email')"
                  class="text-gray-400 hover:text-gray-600 dark:hover:text-gray-300 focus:outline-none"
                >
                  <span class="sr-only">Share via Email</span>
                  <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                  </svg>
                </button>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Product tabs -->
        <div class="mt-16 border-t border-gray-200 dark:border-gray-700">
          <div class="border-b border-gray-200 dark:border-gray-700">
            <nav class="-mb-px flex space-x-8">
              <button
                v-for="tab in tabs"
                :key="tab.id"
                @click="activeTab = tab.id"
                class="whitespace-nowrap py-6 border-b-2 font-medium text-sm focus:outline-none"
                :class="[
                  activeTab === tab.id
                    ? 'border-pravis-600 text-pravis-600 dark:border-pravis-400 dark:text-pravis-400'
                    : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300 dark:text-gray-400 dark:hover:text-gray-300 dark:hover:border-gray-600'
                ]"
              >
                {{ tab.name }}
              </button>
            </nav>
          </div>
          
          <!-- Description tab -->
          <div v-if="activeTab === 'description'" class="py-6">
            <div class="prose prose-sm max-w-none text-gray-700 dark:text-gray-300">
              <p v-if="!product.fullDescription">{{ product.description }}</p>
              <div v-else v-html="product.fullDescription"></div>
            </div>
          </div>
          
          <!-- Specifications tab -->
          <div v-if="activeTab === 'specifications'" class="py-6">
            <div v-if="product.specifications && product.specifications.length > 0">
              <div class="border-t border-gray-200 dark:border-gray-700">
                <dl>
                  <template v-for="(spec, index) in product.specifications" :key="spec.name">
                    <div class="px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6" :class="index % 2 === 0 ? 'bg-gray-50 dark:bg-gray-800' : 'bg-white dark:bg-gray-900'">
                      <dt class="text-sm font-medium text-gray-700 dark:text-gray-300">
                        {{ spec.name }}
                      </dt>
                      <dd class="mt-1 text-sm text-gray-900 dark:text-gray-100 sm:mt-0 sm:col-span-2">
                        {{ spec.value }}
                      </dd>
                    </div>
                  </template>
                </dl>
              </div>
            </div>
            <div v-else class="text-center py-8 text-gray-500 dark:text-gray-400">
              <p>No specifications available for this product.</p>
            </div>
          </div>
          
          <!-- Reviews tab -->
          <div v-if="activeTab === 'reviews'" class="py-6">
            <div v-if="product.reviews && product.reviews.length > 0">
              <!-- Reviews summary -->
              <div class="mb-8">
                <h3 class="text-lg font-medium text-gray-900 dark:text-white">Customer Reviews</h3>
                <div class="mt-3 flex items-center">
                  <div class="flex items-center">
                    <svg 
                      v-for="i in 5" 
                      :key="i"
                      :class="[
                        i <= Math.round(product.rating) ? 'text-yellow-400' : 'text-gray-300 dark:text-gray-600',
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
                  <p class="ml-2 text-sm text-gray-700 dark:text-gray-300">
                    {{ product.rating }} out of 5 stars ({{ product.reviews.length }} reviews)
                  </p>
                </div>
              </div>
              
              <!-- Reviews list -->
              <div class="space-y-8">
                <div 
                  v-for="(review, index) in product.reviews" 
                  :key="index"
                  class="border-b border-gray-200 dark:border-gray-700 pb-8"
                >
                  <div class="flex items-center">
                    <img
                      v-if="review.avatar"
                      :src="review.avatar"
                      :alt="review.author"
                      class="h-8 w-8 rounded-full mr-4"
                    />
                    <div v-else class="h-8 w-8 rounded-full bg-gray-200 dark:bg-gray-700 flex items-center justify-center mr-4">
                      <svg class="h-5 w-5 text-gray-400 dark:text-gray-500" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                      </svg>
                    </div>
                    <div>
                      <h4 class="text-sm font-medium text-gray-900 dark:text-white">{{ review.author }}</h4>
                      <div class="mt-1 flex items-center">
                        <div class="flex items-center">
                          <svg 
                            v-for="i in 5" 
                            :key="i"
                            :class="[
                              i <= review.rating ? 'text-yellow-400' : 'text-gray-300 dark:text-gray-600',
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
                        <p class="ml-2 text-xs text-gray-500 dark:text-gray-400">
                          {{ formatDate(review.date) }}
                        </p>
                      </div>
                    </div>
                  </div>
                  <div class="mt-4">
                    <h5 v-if="review.title" class="text-sm font-medium text-gray-900 dark:text-white">{{ review.title }}</h5>
                    <p class="mt-1 text-sm text-gray-700 dark:text-gray-300">{{ review.content }}</p>
                  </div>
                </div>
              </div>
              
              <!-- Write a review -->
              <div class="mt-8">
                <Button 
                  variant="outline-primary"
                  @click="showReviewForm = !showReviewForm"
                >
                  {{ showReviewForm ? 'Cancel' : 'Write a Review' }}
                </Button>
                
                <div v-if="showReviewForm" class="mt-6 bg-gray-50 dark:bg-gray-800 p-6 rounded-lg">
                  <h3 class="text-lg font-medium text-gray-900 dark:text-white">Write a Review</h3>
                  <form @submit.prevent="submitReview" class="mt-4">
                    <div class="space-y-4">
                      <div>
                        <label for="review-name" class="block text-sm font-medium text-gray-700 dark:text-gray-300">Your Name</label>
                        <input 
                          id="review-name"
                          v-model="reviewForm.name"
                          type="text"
                          required
                          class="mt-1 block w-full border border-gray-300 dark:border-gray-600 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-pravis-500 focus:border-pravis-500 sm:text-sm bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                        />
                      </div>
                      <div>
                        <label for="review-email" class="block text-sm font-medium text-gray-700 dark:text-gray-300">Email Address</label>
                        <input 
                          id="review-email"
                          v-model="reviewForm.email"
                          type="email"
                          required
                          class="mt-1 block w-full border border-gray-300 dark:border-gray-600 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-pravis-500 focus:border-pravis-500 sm:text-sm bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                        />
                      </div>
                      <div>
                        <label for="review-rating" class="block text-sm font-medium text-gray-700 dark:text-gray-300">Rating</label>
                        <div class="mt-1 flex items-center">
                          <button 
                            v-for="i in 5" 
                            :key="i"
                            type="button"
                            @click="reviewForm.rating = i"
                            class="p-1 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-pravis-500"
                          >
                            <svg 
                              class="h-5 w-5"
                              :class="i <= reviewForm.rating ? 'text-yellow-400' : 'text-gray-300 dark:text-gray-600'"
                              xmlns="http://www.w3.org/2000/svg" 
                              viewBox="0 0 20 20" 
                              fill="currentColor" 
                              aria-hidden="true"
                            >
                              <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118l-2.8-2.034c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                            </svg>
                          </button>
                        </div>
                      </div>
                      <div>
                        <label for="review-title" class="block text-sm font-medium text-gray-700 dark:text-gray-300">Review Title</label>
                        <input 
                          id="review-title"
                          v-model="reviewForm.title"
                          type="text"
                          class="mt-1 block w-full border border-gray-300 dark:border-gray-600 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-pravis-500 focus:border-pravis-500 sm:text-sm bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                        />
                      </div>
                      <div>
                        <label for="review-content" class="block text-sm font-medium text-gray-700 dark:text-gray-300">Review</label>
                        <textarea 
                          id="review-content"
                          v-model="reviewForm.content"
                          rows="4"
                          required
                          class="mt-1 block w-full border border-gray-300 dark:border-gray-600 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-pravis-500 focus:border-pravis-500 sm:text-sm bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                        ></textarea>
                      </div>
                      <div class="flex justify-end">
                        <Button 
                          type="submit"
                          variant="primary"
                          :loading="reviewSubmitting"
                        >
                          Submit Review
                        </Button>
                      </div>
                    </div>
                  </form>
                </div>
              </div>
            </div>
            <div v-else class="text-center py-8 text-gray-500 dark:text-gray-400">
              <p>No reviews yet. Be the first to review this product!</p>
              <Button 
                variant="outline-primary"
                class="mt-4"
                @click="showReviewForm = !showReviewForm"
              >
                {{ showReviewForm ? 'Cancel' : 'Write a Review' }}
              </Button>
              
              <div v-if="showReviewForm" class="mt-6 bg-gray-50 dark:bg-gray-800 p-6 rounded-lg">
                <h3 class="text-lg font-medium text-gray-900 dark:text-white">Write a Review</h3>
                <form @submit.prevent="submitReview" class="mt-4">
                  <div class="space-y-4">
                    <div>
                      <label for="review-name" class="block text-sm font-medium text-gray-700 dark:text-gray-300">Your Name</label>
                      <input 
                        id="review-name"
                        v-model="reviewForm.name"
                        type="text"
                        required
                        class="mt-1 block w-full border border-gray-300 dark:border-gray-600 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-pravis-500 focus:border-pravis-500 sm:text-sm bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                      />
                    </div>
                    <div>
                      <label for="review-email" class="block text-sm font-medium text-gray-700 dark:text-gray-300">Email Address</label>
                      <input 
                        id="review-email"
                        v-model="reviewForm.email"
                        type="email"
                        required
                        class="mt-1 block w-full border border-gray-300 dark:border-gray-600 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-pravis-500 focus:border-pravis-500 sm:text-sm bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                      />
                    </div>
                    <div>
                      <label for="review-rating" class="block text-sm font-medium text-gray-700 dark:text-gray-300">Rating</label>
                      <div class="mt-1 flex items-center">
                        <button 
                          v-for="i in 5" 
                          :key="i"
                          type="button"
                          @click="reviewForm.rating = i"
                          class="p-1 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-pravis-500"
                        >
                          <svg 
                            class="h-5 w-5"
                            :class="i <= reviewForm.rating ? 'text-yellow-400' : 'text-gray-300 dark:text-gray-600'"
                            xmlns="http://www.w3.org/2000/svg" 
                            viewBox="0 0 20 20" 
                            fill="currentColor" 
                            aria-hidden="true"
                          >
                            <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118l-2.8-2.034c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                          </svg>
                        </button>
                      </div>
                    </div>
                    <div>
                      <label for="review-title" class="block text-sm font-medium text-gray-700 dark:text-gray-300">Review Title</label>
                      <input 
                        id="review-title"
                        v-model="reviewForm.title"
                        type="text"
                        class="mt-1 block w-full border border-gray-300 dark:border-gray-600 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-pravis-500 focus:border-pravis-500 sm:text-sm bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                      />
                    </div>
                    <div>
                      <label for="review-content" class="block text-sm font-medium text-gray-700 dark:text-gray-300">Review</label>
                      <textarea 
                        id="review-content"
                        v-model="reviewForm.content"
                        rows="4"
                        required
                        class="mt-1 block w-full border border-gray-300 dark:border-gray-600 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-pravis-500 focus:border-pravis-500 sm:text-sm bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                      ></textarea>
                    </div>
                    <div class="flex justify-end">
                      <Button 
                        type="submit"
                        variant="primary"
                        :loading="reviewSubmitting"
                      >
                        Submit Review
                      </Button>
                    </div>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Related products -->
        <div v-if="relatedProducts.length > 0" class="mt-16">
          <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-6">Related Products</h2>
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            <div 
              v-for="relatedProduct in relatedProducts" 
              :key="relatedProduct.id"
              class="transition-all duration-200 ease-in-out"
            >
              <ProductCard 
                :product="relatedProduct" 
                @quick-view="openQuickView"
                @add-to-cart="handleAddToCart"
                @wishlist-toggle="handleWishlistToggle"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Voice assistant -->
    <VoiceAssistant />
    
    <!-- Quick view modal for related products -->
    <div 
      v-if="quickViewProduct"
      class="fixed z-50 inset-0 overflow-y-auto"
    >
      <div class="flex items-center justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
        <div class="fixed inset-0 bg-black bg-opacity-50 transition-opacity" @click="closeQuickView"></div>
        
        <div class="inline-block align-bottom bg-white dark:bg-gray-800 rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-3xl sm:w-full">
          <!-- Similar to the quick view in the shop page -->
          <!-- Content omitted for brevity -->
          <div class="p-6">
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
            <div class="text-center">
              <h3 class="text-lg font-medium text-gray-900 dark:text-white">
                {{ quickViewProduct.name }}
              </h3>
              <Button 
                variant="primary"
                class="mt-4"
                @click="navigateTo(`/shop/product/${quickViewProduct.id}`)"
              >
                View Details
              </Button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from 'vue'
import ProductCard from '~/components/common/ProductCard.vue'
import Button from '~/components/common/Button.vue'
import VoiceAssistant from '~/components/common/VoiceAssistant.vue'
import { useProducts } from '~/composables/useProducts'
import { useCartStore } from '~/store/cart'

// Route params
const route = useRoute()
const productId = route.params.id

// Setup composables and stores
const { getProduct, getRelatedProducts, submitReview: submitProductReview } = useProducts()
const cartStore = useCartStore()

// State
const product = ref(null)
const loading = ref(true)
const error = ref(null)
const quantity = ref(1)
const inWishlist = ref(false) // This would be connected to a wishlist store in a real app
const currentImage = ref('')
const activeTab = ref('description')
const relatedProducts = ref([])
const selectedVariants = reactive({})
const quickViewProduct = ref(null)
const showReviewForm = ref(false)
const reviewSubmitting = ref(false)
const reviewForm = reactive({
  name: '',
  email: '',
  rating: 5,
  title: '',
  content: ''
})

// Tabs for product details
const tabs = [
  { id: 'description', name: 'Description' },
  { id: 'specifications', name: 'Specifications' },
  { id: 'reviews', name: 'Reviews' }
]

// Fetch product data
async function fetchProduct() {
  loading.value = true
  error.value = null
  
  try {
    const data = await getProduct(productId)
    product.value = data
    
    // Set current image to main image
    if (product.value.image) {
      currentImage.value = product.value.image
    } else if (product.value.images && product.value.images.length > 0) {
      currentImage.value = product.value.images[0]
    }
    
    // Track product view
    const { trackProductInteraction } = useAnalytics()
    trackProductInteraction(product.value.id, 'view', {
      product_name: product.value.name,
      price: product.value.price,
      category: product.value.category
    })
    
    // Fetch related products
    fetchRelatedProducts()
  } catch (err) {
    error.value = err.message || 'Failed to load product'
  } finally {
    loading.value = false
  }
}

// Fetch related products
async function fetchRelatedProducts() {
  try {
    const data = await getRelatedProducts(productId, 4)
    relatedProducts.value = data
  } catch (err) {
    console.error('Failed to load related products:', err)
  }
}

// Reload product data
function reloadProduct() {
  fetchProduct()
}

// Format price for display
function formatPrice(price) {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
  }).format(price)
}

// Format discount percentage
function formatDiscountPercentage(originalPrice, salePrice) {
  if (!originalPrice || !salePrice) return 0
  const discount = ((originalPrice - salePrice) / originalPrice) * 100
  return Math.round(discount)
}

// Format date for reviews
function formatDate(dateString) {
  const date = new Date(dateString)
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}

// Format attribute name
function formatAttributeName(name) {
  return name
    .replace(/([A-Z])/g, ' $1')
    .replace(/^./, str => str.toUpperCase())
    .replace(/_/g, ' ')
}

// Add to cart
function addToCart() {
  if (!product.value || !product.value.inStock) return
  
  cartStore.addItem(product.value, quantity.value)
  
  // Show success message
  // (In a real app, you'd use a toast or notification system)
  alert(`Added ${quantity.value} ${product.value.name} to cart!`)
  
  // Track analytics
  const { trackProductInteraction } = useAnalytics()
  trackProductInteraction(product.value.id, 'add_to_cart', {
    product_name: product.value.name,
    price: product.value.price,
    quantity: quantity.value,
    category: product.value.category
  })
}

// Toggle wishlist
function toggleWishlist() {
  inWishlist.value = !inWishlist.value
  
  // Track analytics
  const { trackProductInteraction } = useAnalytics()
  trackProductInteraction(
    product.value.id, 
    inWishlist.value ? 'add_to_wishlist' : 'remove_from_wishlist',
    {
      product_name: product.value.name,
      price: product.value.price,
      category: product.value.category
    }
  )
  
  // Show success message
  // (In a real app, you'd use a toast or notification system)
  alert(`${inWishlist.value ? 'Added to' : 'Removed from'} wishlist!`)
}

// Select variant option
function selectVariantOption(variantId, optionId) {
  selectedVariants[variantId] = optionId
}

// Check if variant option is selected
function isVariantOptionSelected(variantId, optionId) {
  return selectedVariants[variantId] === optionId
}

// Social sharing
function shareProduct(platform) {
  if (!process.client) return
  
  const url = window.location.href
  const title = product.value.name
  const description = product.value.description
  
  let shareUrl = ''
  
  switch (platform) {
    case 'facebook':
      shareUrl = `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}`
      break
    case 'twitter':
      shareUrl = `https://twitter.com/intent/tweet?url=${encodeURIComponent(url)}&text=${encodeURIComponent(title)}`
      break
    case 'pinterest':
      shareUrl = `https://pinterest.com/pin/create/button/?url=${encodeURIComponent(url)}&description=${encodeURIComponent(description)}&media=${encodeURIComponent(product.value.image)}`
      break
    case 'email':
      shareUrl = `mailto:?subject=${encodeURIComponent(title)}&body=${encodeURIComponent(`Check out this product: ${url}`)}`
      break
  }
  
  if (shareUrl) {
    window.open(shareUrl, '_blank')
    
    // Track analytics
    const { trackInteraction } = useAnalytics()
    trackInteraction('product', 'share', {
      product_id: product.value.id,
      product_name: product.value.name,
      platform
    })
  }
}

// Submit review
async function submitReview() {
  if (reviewSubmitting.value) return
  
  reviewSubmitting.value = true
  
  try {
    const reviewData = {
      productId: product.value.id,
      name: reviewForm.name,
      email: reviewForm.email,
      rating: reviewForm.rating,
      title: reviewForm.title,
      content: reviewForm.content
    }
    
    await submitProductReview(product.value.id, reviewData)
    
    // In a real app, you'd refresh the reviews here
    // For demo purposes, we'll just add it to the UI
    if (!product.value.reviews) {
      product.value.reviews = []
    }
    
    product.value.reviews.unshift({
      author: reviewForm.name,
      rating: reviewForm.rating,
      title: reviewForm.title,
      content: reviewForm.content,
      date: new Date().toISOString()
    })
    
    // Update average rating
    const totalRating = product.value.reviews.reduce((sum, review) => sum + review.rating, 0)
    product.value.rating = totalRating / product.value.reviews.length
    product.value.reviewCount = product.value.reviews.length
    
    // Reset form
    reviewForm.name = ''
    reviewForm.email = ''
    reviewForm.rating = 5
    reviewForm.title = ''
    reviewForm.content = ''
    
    // Hide form
    showReviewForm.value = false
    
    // Show success message
    alert('Thank you for your review!')
  } catch (err) {
    alert('Failed to submit review. Please try again.')
  } finally {
    reviewSubmitting.value = false
  }
}

// Quick view for related products
function openQuickView(product) {
  quickViewProduct.value = product
}

function closeQuickView() {
  quickViewProduct.value = null
}

// Handle actions from product cards
function handleAddToCart(product) {
  cartStore.addItem(product)
  alert(`Added ${product.name} to cart!`)
}

function handleWishlistToggle(data) {
  const { product, inWishlist } = data
  alert(`${inWishlist ? 'Added to' : 'Removed from'} wishlist!`)
}

// Load product on mount
onMounted(() => {
  fetchProduct()
})
</script>

<style>
/* Additional styles for the product detail page */
.prose img {
  border-radius: 0.375rem;
}

/* Fix for Safari aspect ratio issues */
@supports not (aspect-ratio: 1 / 1) {
  .aspect-w-1.aspect-h-1 {
    position: relative;
    padding-bottom: 100%;
  }
  .aspect-w-1.aspect-h-1 img {
    position: absolute;
    height: 100%;
    width: 100%;
    top: 0;
    left: 0;
    object-fit: cover;
  }
}
</style>
