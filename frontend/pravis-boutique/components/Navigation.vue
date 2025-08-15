<template>
  <nav class="bg-white shadow-lg sticky top-0 z-40">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-16">
        <!-- Logo -->
        <div class="flex items-center space-x-3">
          <div class="w-10 h-10">
            <svg viewBox="0 0 100 100" class="w-full h-full">
              <defs>
                <linearGradient id="logoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" style="stop-color:#8B0000" />
                  <stop offset="50%" style="stop-color:#A0001C" />
                  <stop offset="100%" style="stop-color:#D4AF37" />
                </linearGradient>
              </defs>
              <!-- Stylized P with peacock elements -->
              <path d="M20 20 L20 80 L35 80 L35 55 L50 55 Q70 55 70 37.5 Q70 20 50 20 Z" fill="url(#logoGrad)" />
              <path d="M35 35 L50 35 Q55 35 55 37.5 Q55 40 50 40 L35 40 Z" fill="#F4F3EE" />
              <!-- Decorative elements -->
              <circle cx="75" cy="25" r="3" fill="#D4AF37" />
              <circle cx="80" cy="35" r="2" fill="#D4AF37" />
              <path d="M70 15 Q75 10 80 15 Q75 20 70 15" fill="#A0001C" opacity="0.7" />
            </svg>
          </div>
          <div>
            <h1 class="text-xl font-display font-bold text-pravis-800">Pravis Boutique</h1>
            <p class="text-xs text-pravis-600 font-medium">Drape in Elegance</p>
          </div>
        </div>

        <!-- Desktop Navigation -->
        <div class="hidden md:flex items-center space-x-8">
          <NuxtLink to="/shop" class="text-pravis-800 hover:text-pravis-600 transition-colors font-medium">Shop</NuxtLink>
          <a href="#about" class="text-pravis-800 hover:text-pravis-600 transition-colors font-medium">About</a>
          <a href="#contact" class="text-pravis-800 hover:text-pravis-600 transition-colors font-medium">Contact</a>
          
          <!-- AI Voice Assistant -->
          <button 
            @click="toggleVoiceAssistant" 
            class="flex items-center space-x-2 bg-pravis-600 text-white px-4 py-2 rounded-full hover:bg-pravis-700 transition-all duration-300 voice-pulse"
            id="voiceBtn"
          >
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z"></path>
            </svg>
            <span class="text-sm font-medium">Ask Pravi</span>
          </button>
        </div>

        <!-- Mobile menu button -->
        <button 
          class="md:hidden text-pravis-800" 
          @click="toggleMobileMenu"
        >
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
          </svg>
        </button>
      </div>
    </div>

    <!-- Mobile Navigation -->
    <div v-if="mobileMenuOpen" class="md:hidden bg-white border-t">
      <div class="px-4 py-4 space-y-3">
        <NuxtLink to="/shop" class="block text-pravis-800 hover:text-pravis-600 transition-colors font-medium">Shop</NuxtLink>
        <a href="#about" class="block text-pravis-800 hover:text-pravis-600 transition-colors font-medium">About</a>
        <a href="#contact" class="block text-pravis-800 hover:text-pravis-600 transition-colors font-medium">Contact</a>
        <button 
          @click="toggleVoiceAssistant" 
          class="flex items-center space-x-2 bg-pravis-600 text-white px-4 py-2 rounded-full w-full justify-center hover:bg-pravis-700 transition-colors"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z"></path>
          </svg>
          <span>Ask Pravi</span>
        </button>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue'

const mobileMenuOpen = ref(false)
const emit = defineEmits(['toggle-voice-assistant'])

const toggleMobileMenu = () => {
  mobileMenuOpen.value = !mobileMenuOpen.value
}

const toggleVoiceAssistant = () => {
  emit('toggle-voice-assistant')
}

// Navigation scroll effect
onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})

const handleScroll = () => {
  const nav = document.querySelector('nav')
  if (window.scrollY > 100) {
    nav?.classList.add('shadow-xl')
  } else {
    nav?.classList.remove('shadow-xl')
  }
}
</script>

<style scoped>
.voice-pulse {
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}
</style>