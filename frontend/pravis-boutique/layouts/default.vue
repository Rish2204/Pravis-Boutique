<template>
  <div class="min-h-screen flex flex-col bg-white dark:bg-gray-900 text-gray-800 dark:text-gray-200">
    <!-- Header -->
    <header class="bg-pravis-600 text-white shadow-md">
      <div class="container mx-auto px-4 py-4 flex justify-between items-center">
        <!-- Logo -->
        <NuxtLink to="/" class="flex items-center space-x-3">
          <div class="w-10 h-10 bg-white rounded-full flex items-center justify-center">
            <span class="text-2xl font-bold text-pravis-600">P</span>
          </div>
          <span class="text-2xl font-bold">Pravis Boutique</span>
        </NuxtLink>

        <!-- Navigation -->
        <nav class="hidden md:flex space-x-6">
          <NuxtLink 
            to="/" 
            class="hover:text-pravis-200 transition duration-150 px-3 py-2 rounded-md"
            :class="{ 'bg-pravis-700': $route.path === '/' }"
          >
            Home
          </NuxtLink>
          <NuxtLink 
            to="/shop" 
            class="hover:text-pravis-200 transition duration-150 px-3 py-2 rounded-md"
            :class="{ 'bg-pravis-700': $route.path.startsWith('/shop') }"
          >
            Shop
          </NuxtLink>
          <NuxtLink 
            to="/contact" 
            class="hover:text-pravis-200 transition duration-150 px-3 py-2 rounded-md"
            :class="{ 'bg-pravis-700': $route.path === '/contact' }"
          >
            Contact
          </NuxtLink>
        </nav>

        <!-- Mobile menu and cart -->
        <div class="flex items-center space-x-4">
          <!-- Cart -->
          <NuxtLink to="/cart" class="relative p-2 hover:bg-pravis-700 rounded-full transition">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4m0 0L7 13m0 0l-1.6 8H19M7 13v4a2 2 0 002 2h8a2 2 0 002-2v-4"/>
            </svg>
            <span v-if="cartCount > 0" class="absolute -top-1 -right-1 bg-red-500 text-white text-xs rounded-full w-5 h-5 flex items-center justify-center">
              {{ cartCount }}
            </span>
          </NuxtLink>

          <!-- Mobile menu button -->
          <button 
            @click="mobileMenuOpen = !mobileMenuOpen"
            class="md:hidden p-2 hover:bg-pravis-700 rounded-md transition"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
            </svg>
          </button>
        </div>
      </div>

      <!-- Mobile menu -->
      <div v-if="mobileMenuOpen" class="md:hidden bg-pravis-700">
        <div class="px-4 py-2 space-y-2">
          <NuxtLink 
            to="/" 
            class="block px-3 py-2 rounded-md hover:bg-pravis-800 transition"
            @click="mobileMenuOpen = false"
          >
            Home
          </NuxtLink>
          <NuxtLink 
            to="/shop" 
            class="block px-3 py-2 rounded-md hover:bg-pravis-800 transition"
            @click="mobileMenuOpen = false"
          >
            Shop
          </NuxtLink>
          <NuxtLink 
            to="/contact" 
            class="block px-3 py-2 rounded-md hover:bg-pravis-800 transition"
            @click="mobileMenuOpen = false"
          >
            Contact
          </NuxtLink>
        </div>
      </div>
    </header>

    <!-- Main Content -->
    <main class="flex-1">
      <slot />
    </main>

    <!-- Footer -->
    <footer class="bg-pravis-800 text-white py-8">
      <div class="container mx-auto px-4">
        <div class="grid md:grid-cols-3 gap-8">
          <div>
            <h3 class="text-lg font-semibold mb-4">Pravis Boutique</h3>
            <p class="text-pravis-200">
              Authentic handloom textiles crafted with tradition and care.
            </p>
          </div>
          <div>
            <h3 class="text-lg font-semibold mb-4">Quick Links</h3>
            <div class="space-y-2">
              <NuxtLink to="/" class="block text-pravis-200 hover:text-white transition">Home</NuxtLink>
              <NuxtLink to="/shop" class="block text-pravis-200 hover:text-white transition">Shop</NuxtLink>
              <NuxtLink to="/contact" class="block text-pravis-200 hover:text-white transition">Contact</NuxtLink>
            </div>
          </div>
          <div>
            <h3 class="text-lg font-semibold mb-4">Contact Info</h3>
            <div class="text-pravis-200 space-y-2">
              <p>📧 info@pravisboutique.com</p>
              <p>📞 +91 98765 43210</p>
              <p>📍 Handloom District, India</p>
            </div>
          </div>
        </div>
        <div class="border-t border-pravis-700 mt-8 pt-8 text-center text-pravis-200">
          <p>&copy; 2024 Pravis Boutique. All rights reserved.</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

// Simple state management
const mobileMenuOpen = ref(false)

// Simple cart count (can be replaced with actual store later)
const cartCount = computed(() => {
  // For now, return 0. This can be connected to actual cart store later
  return 0
})
</script>

<style scoped>
.container {
  max-width: 1200px;
}
</style>