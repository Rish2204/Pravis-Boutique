<template>
  <nav class="sticky top-0 z-40 border-b border-pravis-100 bg-white/95 shadow-sm backdrop-blur">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex h-16 items-center justify-between gap-4">
        <NuxtLink to="/" class="flex items-center space-x-3" aria-label="Pravis Boutique home">
          <div class="flex h-11 w-11 items-center justify-center rounded-full border border-pravis-200 bg-pravis-800 shadow-sm">
            <span class="font-display text-lg font-bold tracking-wide text-pravis-300">PB</span>
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
