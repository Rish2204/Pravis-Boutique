<template>
  <div class="min-h-screen flex flex-col bg-white dark:bg-gray-900 text-gray-800 dark:text-gray-200">
    <!-- Header -->
    <header class="bg-pravis-500 text-white shadow-md">
      <div class="container mx-auto px-4 py-3 flex justify-between items-center">
        <!-- Logo -->
        <NuxtLink to="/" class="flex items-center space-x-2">
          <img src="/pravis-logo.png" alt="Pravis Boutique" class="h-12">
          <span class="font-display text-2xl">Pravis Boutique</span>
        </NuxtLink>

        <!-- Navigation -->
        <nav class="hidden md:flex space-x-6">
          <NuxtLink to="/" class="hover:text-pravis-200 transition duration-150">
            Home
          </NuxtLink>
          <NuxtLink to="/shop" class="hover:text-pravis-200 transition duration-150">
            Shop
          </NuxtLink>
          <NuxtLink to="/contact" class="hover:text-pravis-200 transition duration-150">
            Contact
          </NuxtLink>
        </nav>

          <!-- Right side navigation items -->
        <div class="flex items-center space-x-4">
          <!-- Dark Mode Toggle -->
          <DarkModeToggle variant="minimal" />
          
          <!-- Cart icon with counter -->
          <NuxtLink 
            to="/cart" 
            class="relative hover:text-pravis-200 transition duration-150"
          >
            <span class="sr-only">Cart</span>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />
            </svg>
            <span 
              v-if="cartCount > 0"
              class="absolute -top-2 -right-2 bg-white text-pravis-600 text-xs font-bold rounded-full h-5 w-5 flex items-center justify-center"
            >
              {{ cartCount }}
            </span>
          </NuxtLink>

          <!-- User menu -->
          <div class="relative">
            <button 
              v-if="!isAuthenticated"
              @click="navigateTo('/login')"
              class="text-sm hover:text-pravis-200 transition duration-150"
            >
              Sign in
            </button>
            
            <!-- User dropdown when authenticated -->
            <div v-else class="relative">
              <button 
                @click="userMenuOpen = !userMenuOpen"
                class="rounded-full flex focus:outline-none focus:ring-2 focus:ring-pravis-300"
              >
                <span class="sr-only">Open user menu</span>
                <img 
                  class="h-8 w-8 rounded-full" 
                  :src="userProfile?.avatar || '/images/default-avatar.png'" 
                  :alt="userProfile?.name || 'User'"
                />
              </button>
              
              <!-- Dropdown menu -->
              <div 
                v-if="userMenuOpen"
                class="origin-top-right absolute right-0 mt-2 w-48 rounded-md shadow-lg py-1 bg-white dark:bg-gray-800 ring-1 ring-black ring-opacity-5 focus:outline-none z-10"
              >
                <NuxtLink 
                  to="/profile" 
                  class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-700"
                  @click="userMenuOpen = false"
                >
                  Your Profile
                </NuxtLink>
                <NuxtLink 
                  to="/orders" 
                  class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-700"
                  @click="userMenuOpen = false"
                >
                  Orders
                </NuxtLink>
                <button
                  @click="logout(); userMenuOpen = false"
                  class="block w-full text-left px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-700"
                >
                  Sign out
                </button>
              </div>
            </div>
          </div>

          <!-- Voice agent toggle -->
          <button 
            v-if="voiceSupported"
            @click="toggleVoiceListening"
            class="p-1 rounded-full hover:text-pravis-200 focus:outline-none focus:ring-2 focus:ring-pravis-300 transition duration-150"
            :class="{ 'bg-red-100 text-red-500': isListening }"
          >
            <span class="sr-only">{{ isListening ? 'Stop voice agent' : 'Start voice agent' }}</span>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path v-if="!isListening" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z" />
              <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              <path v-if="isListening" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 10a1 1 0 011-1h4a1 1 0 011 1v4a1 1 0 01-1 1h-4a1 1 0 01-1-1v-4z" />
            </svg>
          </button>

          <!-- Mobile Menu Button -->
          <div class="md:hidden">
            <button @click="mobileMenuOpen = !mobileMenuOpen" class="focus:outline-none focus:ring-2 focus:ring-pravis-300">
              <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path v-if="!mobileMenuOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7" />
                <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
        </div>
      </div>

      <!-- Mobile Menu -->
      <div v-if="mobileMenuOpen" class="md:hidden px-4 pt-2 pb-4 space-y-2">
        <NuxtLink to="/" class="block hover:text-pravis-200" @click="mobileMenuOpen = false">
          Home
        </NuxtLink>
        <NuxtLink to="/shop" class="block hover:text-pravis-200" @click="mobileMenuOpen = false">
          Shop
        </NuxtLink>
        <NuxtLink to="/contact" class="block hover:text-pravis-200" @click="mobileMenuOpen = false">
          Contact
        </NuxtLink>
        <NuxtLink v-if="!isAuthenticated" to="/login" class="block hover:text-pravis-200" @click="mobileMenuOpen = false">
          Sign in
        </NuxtLink>
        <div v-else class="pt-2 space-y-2">
          <NuxtLink to="/profile" class="block hover:text-pravis-200" @click="mobileMenuOpen = false">
            Your Profile
          </NuxtLink>
          <NuxtLink to="/orders" class="block hover:text-pravis-200" @click="mobileMenuOpen = false">
            Orders
          </NuxtLink>
          <button @click="logout(); mobileMenuOpen = false" class="block w-full text-left hover:text-pravis-200">
            Sign out
          </button>
        </div>
      </div>
    </header>

    <!-- Voice transcript display (if active) -->
    <div v-if="isListening && transcript" class="fixed bottom-20 left-0 right-0 mx-auto w-full max-w-lg bg-white dark:bg-gray-800 rounded-lg shadow-lg p-4 z-50 flex items-center space-x-3">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-pravis-500 animate-pulse" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z" />
      </svg>
      <div>
        <p class="text-sm font-medium text-gray-900 dark:text-white">Listening...</p>
        <p class="text-sm text-gray-500 dark:text-gray-400">{{ transcript }}</p>
      </div>
      <button 
        @click="stopVoiceListening"
        class="ml-auto flex-shrink-0 p-1 rounded-full text-gray-400 hover:text-gray-500 dark:text-gray-300 dark:hover:text-white focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-pravis-500"
      >
        <span class="sr-only">Stop listening</span>
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>
    </div>

    <!-- Main Content -->
    <main class="flex-1 container mx-auto px-4 py-8">
      <slot />
    </main>

    <!-- Footer -->
    <footer class="bg-gray-800 text-white py-8">
      <div class="container mx-auto px-4 text-center">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div>
            <h3 class="font-bold mb-2">
              Pravis Boutique
            </h3>
            <p>Your AI-powered guide to exquisite handlooms.</p>
          </div>
          <div>
            <h3 class="font-bold mb-2">
              Quick Links
            </h3>
            <ul>
              <li>
                <NuxtLink to="/" class="hover:text-pravis-200 transition duration-150">
                  Home
                </NuxtLink>
              </li>
              <li>
                <NuxtLink to="/shop" class="hover:text-pravis-200 transition duration-150">
                  Shop
                </NuxtLink>
              </li>
              <li>
                <NuxtLink to="/contact" class="hover:text-pravis-200 transition duration-150">
                  Contact
                </NuxtLink>
              </li>
            </ul>
          </div>
          <div>
            <h3 class="font-bold mb-2">
              Legal
            </h3>
            <ul>
              <li>
                <NuxtLink to="/privacy" class="hover:text-pravis-200 transition duration-150">
                  Privacy Policy
                </NuxtLink>
              </li>
              <li>
                <NuxtLink to="/terms" class="hover:text-pravis-200 transition duration-150">
                  Terms of Service
                </NuxtLink>
              </li>
            </ul>
          </div>
        </div>
        <div class="mt-8 border-t border-gray-700 pt-4">
          <p>&copy; {{ new Date().getFullYear() }} Pravis Boutique. All rights reserved.</p>
        </div>
      </div>
    </footer>

    <!-- PWA install prompt -->
    <div 
      v-if="showInstallPrompt" 
      class="fixed bottom-0 inset-x-0 pb-2 sm:pb-5 z-50"
    >
      <div class="max-w-7xl mx-auto px-2 sm:px-6 lg:px-8">
        <div class="p-2 rounded-lg bg-pravis-600 shadow-lg sm:p-3">
          <div class="flex items-center justify-between flex-wrap">
            <div class="w-0 flex-1 flex items-center">
              <span class="flex p-2 rounded-lg bg-pravis-800">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                </svg>
              </span>
              <p class="ml-3 font-medium text-white truncate">
                <span class="md:hidden">Install our app!</span>
                <span class="hidden md:inline">Want a better experience? Install our app on your device!</span>
              </p>
            </div>
            <div class="order-3 mt-2 flex-shrink-0 w-full sm:order-2 sm:mt-0 sm:w-auto">
              <button
                @click="installPwa"
                class="flex items-center justify-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-pravis-600 bg-white hover:bg-pravis-50"
              >
                Install
              </button>
            </div>
            <div class="order-2 flex-shrink-0 sm:order-3 sm:ml-2">
              <button
                @click="showInstallPrompt = false"
                class="-mr-1 flex p-2 rounded-md hover:bg-pravis-500 focus:outline-none focus:ring-2 focus:ring-white"
              >
                <span class="sr-only">Dismiss</span>
                <svg class="h-6 w-6 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { storeToRefs } from 'pinia'
import { useUserStore } from '~/store/user'
import { useCartStore } from '~/store/cart'
import { useVoiceStore } from '~/store/voice'
import DarkModeToggle from '~/components/common/DarkModeToggle.vue'

// Initialize state
const mobileMenuOpen = ref(false)
const userMenuOpen = ref(false)
const showInstallPrompt = ref(false)
const deferredPrompt = ref(null)

// Initialize stores
const userStore = useUserStore()
const cartStore = useCartStore()
const voiceStore = useVoiceStore()

// Extract reactive state from stores
const { isAuthenticated, user: userProfile } = storeToRefs(userStore)
const { count: cartCount } = storeToRefs(cartStore)
const { isListening, transcript, isReady: voiceSupported } = storeToRefs(voiceStore)

// Initialize stores on client side
onMounted(() => {
  // Check authentication
  userStore.initAuth()
  
  // Load cart from localStorage
  cartStore.loadCart()
  
  // Initialize voice agent
  voiceStore.initialize()
  
  // Setup PWA install prompt
  if (process.client) {
    window.addEventListener('beforeinstallprompt', (e) => {
      // Prevent Chrome 67+ from automatically showing the prompt
      e.preventDefault()
      // Stash the event so it can be triggered later
      deferredPrompt.value = e
      // Show custom install prompt
      showInstallPrompt.value = true
    })
  }
})

// Methods
const logout = () => {
  userStore.logout()
}

const toggleVoiceListening = () => {
  if (isListening.value) {
    voiceStore.stopListening()
  } else {
    voiceStore.startListening()
  }
}

const stopVoiceListening = () => {
  voiceStore.stopListening()
}

const installPwa = async () => {
  if (!deferredPrompt.value) {
    return
  }
  
  // Show the install prompt
  deferredPrompt.value.prompt()
  
  // Wait for the user to respond to the prompt
  const choiceResult = await deferredPrompt.value.userChoice
  
  // Reset the deferred prompt variable
  deferredPrompt.value = null
  
  // Hide our custom install UI
  showInstallPrompt.value = false
  
  // Track analytics
  const { trackInteraction } = useAnalytics()
  trackInteraction('pwa', 'install', { outcome: choiceResult.outcome })
}
</script>

<style scoped>
/* Page Transitions */
.page-enter-active,
.page-leave-active {
  transition: opacity 0.3s ease;
}
.page-enter-from,
.page-leave-to {
  opacity: 0;
}
</style>
