<template>
  <div class="min-h-screen flex flex-col bg-white">
    <!-- Simple Header for non-home pages -->
    <header v-if="$route.path !== '/'" class="maroon-pattern text-white shadow-lg relative">
      <div class="container mx-auto px-6 py-4">
        <div class="flex justify-between items-center">
          <!-- Pravis Peacock Logo -->
          <NuxtLink to="/" class="flex items-center space-x-3 z-10">
            <div class="w-12 h-12 md:w-14 md:h-14">
              <img src="/pravis-peacock-logo.svg" alt="Pravis Logo" class="h-full w-full object-contain drop-shadow-lg" />
            </div>
            <div class="hidden lg:flex flex-col items-start ml-2">
              <span class="font-display text-3xl text-gold-500 tracking-wider" style="font-family: 'Playfair Display', serif; font-style: italic;">
                pravis
              </span>
              <span class="text-sm text-pravis-200 tracking-widest -mt-1" style="font-family: 'Georgia', serif; font-style: italic;">
                Drape in Elegance
              </span>
            </div>
          </NuxtLink>

          <!-- Streamlined Navigation -->
          <nav class="hidden md:flex items-center space-x-8 text-lg">
            <NuxtLink 
              to="/shop" 
              class="text-white hover:text-pravis-200 transition duration-200 font-medium"
              :class="{ 'text-pravis-200 border-b-2 border-pravis-200 pb-1': $route.path.startsWith('/shop') }"
            >
              Shop
            </NuxtLink>
            <NuxtLink 
              to="/contact" 
              class="text-white hover:text-pravis-200 transition duration-200 font-medium"
              :class="{ 'text-pravis-200 border-b-2 border-pravis-200 pb-1': $route.path === '/contact' }"
            >
              Contact
            </NuxtLink>
          </nav>

          <!-- Essential Actions -->
          <div class="flex items-center space-x-4">
            <!-- Cart Icon -->
            <NuxtLink to="/cart" class="relative hover:bg-pravis-600 p-2 rounded-full transition duration-200">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4m0 0L7 13m0 0l-1.6 8H19M7 13v4a2 2 0 002 2h8a2 2 0 002-2v-4"/>
              </svg>
              <span v-if="cartCount > 0" class="absolute -top-1 -right-1 bg-pravis-300 text-pravis-800 text-xs font-bold rounded-full w-5 h-5 flex items-center justify-center">
                {{ cartCount }}
              </span>
            </NuxtLink>

            <!-- Mobile menu button -->
            <button 
              @click="mobileMenuOpen = !mobileMenuOpen"
              class="md:hidden p-2 hover:bg-pravis-600 rounded-md transition duration-200"
            >
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path v-if="!mobileMenuOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
                <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
              </svg>
            </button>
          </div>
        </div>
      </div>

      <!-- Mobile Navigation -->
      <div v-if="mobileMenuOpen" class="md:hidden bg-pravis-800 border-t border-pravis-600">
        <div class="px-6 py-4 space-y-3">
          <NuxtLink 
            to="/shop" 
            class="block text-white hover:text-pravis-200 py-2 transition duration-200"
            @click="mobileMenuOpen = false"
          >
            Shop
          </NuxtLink>
          <NuxtLink 
            to="/contact" 
            class="block text-white hover:text-pravis-200 py-2 transition duration-200"
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
    <footer class="bg-pravis-800 text-white py-12">
      <div class="container mx-auto px-6">
        <div class="grid md:grid-cols-3 gap-8">
          <div>
            <h3 class="text-lg font-display font-semibold mb-4">Pravis Handlooms</h3>
            <p class="text-pravis-200 leading-relaxed">
              Six yards of pure grace, rooted in culture, styled with elegance.
            </p>
          </div>
          <div>
            <h3 class="text-lg font-display font-semibold mb-4">Our Collections</h3>
            <div class="space-y-2">
              <NuxtLink to="/shop" class="block text-pravis-200 hover:text-pravis-300 transition">All Products</NuxtLink>
              <NuxtLink to="/shop?category=sarees" class="block text-pravis-200 hover:text-pravis-300 transition">Sarees: Banaras | Kanchi</NuxtLink>
              <NuxtLink to="/shop?category=accessories" class="block text-pravis-200 hover:text-pravis-300 transition">Accessories: Jewellery | Clutches</NuxtLink>
              <NuxtLink to="/shop?category=readymades" class="block text-pravis-200 hover:text-pravis-300 transition">Readymades: Blouses | Kurtis | Suits</NuxtLink>
              <NuxtLink to="/contact" class="block text-pravis-200 hover:text-pravis-300 transition mt-4">Contact Us</NuxtLink>
            </div>
          </div>
          <div>
            <h3 class="text-lg font-display font-semibold mb-4">Connect</h3>
            <div class="text-pravis-200 space-y-2">
              <p>📧 info@pravishandlooms.com</p>
              <p>📞 +91 63002 08234</p>
              <p>📍 2nd Floor, Mokila, 501203</p>
              <a 
                href="https://www.instagram.com/pravis.handlooms/?hl=en" 
                target="_blank" 
                rel="noopener noreferrer"
                class="inline-flex items-center text-pravis-200 hover:text-pravis-300 transition-colors duration-200 mt-3"
              >
                <svg class="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
                </svg>
                Follow us on Instagram
              </a>
            </div>
          </div>
        </div>
        <div class="border-t border-pravis-700 mt-8 pt-8 text-center text-pravis-200">
          <p>&copy; 2025 Pravis Handlooms. Crafted with tradition, styled with love.</p>
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