<template>
  <nav class="sticky top-0 z-40 border-b border-pravis-100 bg-white/95 shadow-sm backdrop-blur">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex h-16 items-center justify-between gap-4">
        <NuxtLink to="/" class="flex items-center space-x-3" aria-label="Pravis Boutique home">
          <div class="w-10 h-10">
            <svg viewBox="0 0 100 100" class="w-full h-full">
              <defs>
                <linearGradient id="logoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" style="stop-color:#8B0000" />
                  <stop offset="50%" style="stop-color:#A0001C" />
                  <stop offset="100%" style="stop-color:#D4AF37" />
                </linearGradient>
              </defs>
              <path d="M20 20 L20 80 L35 80 L35 55 L50 55 Q70 55 70 37.5 Q70 20 50 20 Z" fill="url(#logoGrad)" />
              <path d="M35 35 L50 35 Q55 35 55 37.5 Q55 40 50 40 L35 40 Z" fill="#F4F3EE" />
              <circle cx="75" cy="25" r="3" fill="#D4AF37" />
              <circle cx="80" cy="35" r="2" fill="#D4AF37" />
              <path d="M70 15 Q75 10 80 15 Q75 20 70 15" fill="#A0001C" opacity="0.7" />
            </svg>
          </div>
          <div>
            <h1 class="text-xl font-display font-bold text-pravis-800">Pravis Boutique</h1>
            <p class="text-xs text-pravis-600 font-medium">Indian attire catalog</p>
          </div>
        </NuxtLink>

        <div class="hidden md:flex items-center space-x-7">
          <NuxtLink to="/shop" class="text-pravis-800 hover:text-pravis-600 transition-colors font-medium">Shop</NuxtLink>
          <a href="/#about" class="text-pravis-800 hover:text-pravis-600 transition-colors font-medium">About</a>
          <a href="/#contact" class="text-pravis-800 hover:text-pravis-600 transition-colors font-medium">Contact</a>
          <a
            href="https://www.instagram.com/pravis.handlooms/?hl=en"
            target="_blank"
            rel="noopener noreferrer"
            class="text-pravis-800 hover:text-pravis-600 transition-colors font-medium"
          >
            Instagram
          </a>
          <a
            href="https://www.amazon.in/s?k=Pravis+Boutique+Indian+attire"
            target="_blank"
            rel="noopener noreferrer"
            class="rounded-full bg-[#232f3e] px-4 py-2 text-sm font-semibold text-white transition hover:bg-[#131921]"
          >
            Amazon
          </a>
          <a
            href="https://wa.me/916300208234?text=Hi%20Pravis%20Boutique%2C%20I%20want%20to%20browse%20Indian%20attires."
            target="_blank"
            rel="noopener noreferrer"
            class="rounded-full bg-pravis-700 px-4 py-2 text-sm font-semibold text-white transition hover:bg-pravis-800"
          >
            WhatsApp
          </a>
        </div>

        <button
          class="md:hidden rounded-lg p-2 text-pravis-800 hover:bg-pravis-50"
          @click="toggleMobileMenu"
          aria-label="Open navigation menu"
        >
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
          </svg>
        </button>
      </div>
    </div>

    <div v-if="mobileMenuOpen" class="md:hidden border-t border-pravis-100 bg-white">
      <div class="px-4 py-4 space-y-3">
        <NuxtLink to="/shop" class="block text-pravis-800 hover:text-pravis-600 transition-colors font-medium">Shop</NuxtLink>
        <a href="/#about" class="block text-pravis-800 hover:text-pravis-600 transition-colors font-medium">About</a>
        <a href="/#contact" class="block text-pravis-800 hover:text-pravis-600 transition-colors font-medium">Contact</a>
        <a href="https://www.instagram.com/pravis.handlooms/?hl=en" target="_blank" rel="noopener noreferrer" class="block text-pravis-800 hover:text-pravis-600 transition-colors font-medium">Instagram</a>
        <a href="https://www.amazon.in/s?k=Pravis+Boutique+Indian+attire" target="_blank" rel="noopener noreferrer" class="block rounded-lg bg-[#232f3e] px-4 py-3 text-center font-semibold text-white">Browse Amazon</a>
        <a href="https://wa.me/916300208234?text=Hi%20Pravis%20Boutique%2C%20I%20want%20to%20browse%20Indian%20attires." target="_blank" rel="noopener noreferrer" class="block rounded-lg bg-pravis-700 px-4 py-3 text-center font-semibold text-white">WhatsApp Inquiry</a>
      </div>
    </div>
  </nav>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

const mobileMenuOpen = ref(false)

const toggleMobileMenu = () => {
  mobileMenuOpen.value = !mobileMenuOpen.value
}

const handleScroll = () => {
  const nav = document.querySelector('nav')
  if (window.scrollY > 100) {
    nav?.classList.add('shadow-xl')
  } else {
    nav?.classList.remove('shadow-xl')
  }
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>
