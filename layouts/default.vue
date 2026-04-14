<template>
  <div class="min-h-screen flex flex-col font-body">
    <!-- Header -->
    <header class="relative overflow-hidden" style="background: linear-gradient(135deg, #5d1a1a 0%, #7d2525 50%, #5d1a1a 100%)">
      <!-- Pattern overlay -->
      <div class="absolute inset-0 opacity-5">
        <svg width="100%" height="100%">
          <defs>
            <pattern id="headerPattern" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
              <path d="M10 0v20M0 10h20" stroke="white" stroke-width="0.5" fill="none" />
            </pattern>
          </defs>
          <rect width="100%" height="100%" fill="url(#headerPattern)" />
        </svg>
      </div>

      <div class="relative max-w-5xl mx-auto px-4 py-8 text-center">
        <!-- Logo area -->
        <div class="flex items-center justify-center gap-4 mb-2">
          <div class="w-20 h-20 md:w-24 md:h-24 rounded-full border-2 border-gold flex items-center justify-center bg-pravis-900/50" style="box-shadow: 0 0 20px rgba(212, 175, 55, 0.3)">
            <span class="text-gold font-display text-4xl md:text-5xl italic">P</span>
          </div>
        </div>
        <h1 class="font-display italic text-gold text-4xl md:text-5xl lg:text-6xl tracking-wide">
          pravis
        </h1>
        <p class="font-display italic text-gold/90 text-base md:text-lg mt-1 tracking-widest uppercase">
          Drape in Elegance
        </p>
      </div>
    </header>

    <!-- Navigation -->
    <nav
      class="bg-white sticky top-0 z-40 transition-shadow duration-300 no-print"
      :class="scrolled ? 'shadow-xl' : 'shadow-lg'"
    >
      <div class="max-w-6xl mx-auto px-4 h-16 flex items-center justify-between">
        <!-- Logo mark -->
        <NuxtLink to="/" class="flex items-center gap-2 group">
          <div class="w-10 h-10 rounded-full bg-gradient-to-br from-pravis-500 to-gold flex items-center justify-center">
            <span class="text-white font-display text-lg italic">P</span>
          </div>
          <span class="font-display italic text-pravis-800 text-lg hidden sm:inline">pravis</span>
        </NuxtLink>

        <!-- Desktop links -->
        <div class="hidden md:flex items-center gap-8">
          <NuxtLink to="/" class="text-pravis-800 hover:text-pravis-600 transition-colors font-medium">
            Home
          </NuxtLink>

          <!-- Shop dropdown -->
          <div class="relative" @mouseenter="shopOpen = true" @mouseleave="shopOpen = false">
            <NuxtLink
              to="/shop"
              class="text-pravis-800 hover:text-pravis-600 transition-colors font-medium flex items-center gap-1"
            >
              Shop
              <svg class="w-4 h-4 transition-transform" :class="{ 'rotate-180': shopOpen }" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
              </svg>
            </NuxtLink>
            <Transition name="dropdown">
              <div
                v-if="shopOpen"
                class="absolute top-full left-0 mt-1 w-52 bg-white rounded-lg shadow-xl border border-pravis-100 py-2 z-50"
              >
                <NuxtLink
                  v-for="cat in shopCategories"
                  :key="cat"
                  :to="`/shop?category=${encodeURIComponent(cat)}`"
                  class="block px-4 py-2 text-sm text-pravis-800 hover:bg-pravis-50 hover:text-pravis-600 transition-colors"
                >
                  {{ cat }}
                </NuxtLink>
              </div>
            </Transition>
          </div>

          <NuxtLink to="/contact" class="text-pravis-800 hover:text-pravis-600 transition-colors font-medium">
            Contact
          </NuxtLink>
        </div>

        <!-- Mobile hamburger -->
        <button
          class="md:hidden p-2 text-pravis-800 hover:text-pravis-600"
          aria-label="Toggle menu"
          @click="mobileOpen = !mobileOpen"
        >
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path
              v-if="!mobileOpen"
              stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M4 6h16M4 12h16M4 18h16"
            />
            <path
              v-else
              stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M6 18L18 6M6 6l12 12"
            />
          </svg>
        </button>
      </div>

      <!-- Mobile menu -->
      <Transition name="dropdown">
        <div v-if="mobileOpen" class="md:hidden bg-white border-t border-pravis-100 shadow-lg">
          <div class="px-4 py-3 space-y-1">
            <NuxtLink to="/" class="block py-2 text-pravis-800 hover:text-pravis-600 font-medium" @click="mobileOpen = false">
              Home
            </NuxtLink>
            <NuxtLink to="/shop" class="block py-2 text-pravis-800 hover:text-pravis-600 font-medium" @click="mobileOpen = false">
              Shop — All Products
            </NuxtLink>
            <NuxtLink
              v-for="cat in shopCategories.slice(1)"
              :key="cat"
              :to="`/shop?category=${encodeURIComponent(cat)}`"
              class="block py-2 pl-4 text-sm text-pravis-700 hover:text-pravis-600"
              @click="mobileOpen = false"
            >
              {{ cat }}
            </NuxtLink>
            <NuxtLink to="/contact" class="block py-2 text-pravis-800 hover:text-pravis-600 font-medium" @click="mobileOpen = false">
              Contact
            </NuxtLink>
          </div>
        </div>
      </Transition>
    </nav>

    <!-- Page Content -->
    <main class="flex-1">
      <slot />
    </main>

    <!-- Footer -->
    <footer class="bg-pravis-900 text-white no-print">
      <div class="max-w-7xl mx-auto px-4 py-12">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          <!-- Brand -->
          <div>
            <div class="flex items-center gap-3 mb-4">
              <div class="w-10 h-10 rounded-full border border-gold flex items-center justify-center">
                <span class="text-gold font-display text-xl italic">P</span>
              </div>
              <span class="font-display italic text-gold text-xl">pravis</span>
            </div>
            <p class="text-pravis-200 text-sm leading-relaxed">
              Premium Indian handloom textiles. Celebrating authentic artisanship and sustainable practices.
            </p>
          </div>

          <!-- Quick Links -->
          <div>
            <h3 class="font-display text-gold text-lg mb-4">Quick Links</h3>
            <ul class="space-y-2 text-sm">
              <li><NuxtLink to="/shop" class="text-pravis-200 hover:text-gold transition-colors">Shop</NuxtLink></li>
              <li><NuxtLink to="/contact" class="text-pravis-200 hover:text-gold transition-colors">Contact Us</NuxtLink></li>
              <li><span class="text-pravis-200/50">Size Guide (Coming Soon)</span></li>
              <li><span class="text-pravis-200/50">Care Instructions (Coming Soon)</span></li>
            </ul>
          </div>

          <!-- Contact -->
          <div>
            <h3 class="font-display text-gold text-lg mb-4">Contact</h3>
            <ul class="space-y-3 text-sm text-pravis-200">
              <li class="flex items-start gap-2">
                <svg class="w-4 h-4 mt-0.5 text-gold flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                </svg>
                info@pravisboutique.com
              </li>
              <li class="flex items-start gap-2">
                <svg class="w-4 h-4 mt-0.5 text-gold flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                </svg>
                +91 98765 43210
              </li>
            </ul>
          </div>

          <!-- Newsletter -->
          <div>
            <h3 class="font-display text-gold text-lg mb-4">Newsletter</h3>
            <p class="text-pravis-200 text-sm mb-3">Stay updated on new arrivals and artisan stories.</p>
            <div class="flex gap-2">
              <input
                type="email"
                placeholder="Your email"
                class="flex-1 px-3 py-2 rounded-lg bg-pravis-800 border border-pravis-700 text-white text-sm placeholder-pravis-400 focus:outline-none focus:border-gold"
              />
              <button class="px-4 py-2 bg-gold hover:bg-gold-dark text-pravis-900 rounded-lg text-sm font-semibold transition-colors">
                Join
              </button>
            </div>
          </div>
        </div>

        <!-- Bottom bar -->
        <div class="mt-10 pt-6 border-t border-pravis-800 flex flex-col sm:flex-row items-center justify-between gap-3 text-xs text-pravis-400">
          <span>&copy; {{ new Date().getFullYear() }} Pravis Boutique. All rights reserved.</span>
          <div class="flex gap-4">
            <span class="hover:text-gold cursor-default">Privacy Policy</span>
            <span class="hover:text-gold cursor-default">Terms of Service</span>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
import { categories } from '~/data/products'

const shopCategories = categories
const shopOpen = ref(false)
const mobileOpen = ref(false)
const scrolled = ref(false)

onMounted(() => {
  window.addEventListener('scroll', () => {
    scrolled.value = window.scrollY > 100
  })
})

const route = useRoute()
watch(() => route.path, () => {
  mobileOpen.value = false
  shopOpen.value = false
})
</script>

<style scoped>
.dropdown-enter-active,
.dropdown-leave-active {
  transition: opacity 0.2s ease, transform 0.2s ease;
}

.dropdown-enter-from,
.dropdown-leave-to {
  opacity: 0;
  transform: translateY(-8px);
}
</style>
