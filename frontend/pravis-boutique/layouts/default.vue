<template>
  <div class="bg-white text-gray-800">
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
          <NuxtLink to="/" class="hover:text-pravis-200">
            Home
          </NuxtLink>
          <NuxtLink to="/shop" class="hover:text-pravis-200">
            Shop
          </NuxtLink>
          <NuxtLink to="/contact" class="hover:text-pravis-200">
            Contact
          </NuxtLink>
        </nav>

        <!-- Mobile Menu Button -->
        <div class="md:hidden">
          <button @click="isMenuOpen = !isMenuOpen">
            <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7" />
            </svg>
          </button>
        </div>
      </div>

      <!-- Mobile Menu -->
      <div v-if="isMenuOpen" class="md:hidden px-4 pt-2 pb-4 space-y-2">
        <NuxtLink to="/" class="block hover:text-pravis-200">
          Home
        </NuxtLink>
        <NuxtLink to="/shop" class="block hover:text-pravis-200">
          Shop
        </NuxtLink>
        <NuxtLink to="/contact" class="block hover:text-pravis-200">
          Contact
        </NuxtLink>
      </div>
    </header>

    <!-- Main Content -->
    <main class="container mx-auto px-4 py-8">
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
                <NuxtLink to="/" class="hover:text-pravis-200">
                  Home
                </NuxtLink>
              </li>
              <li>
                <NuxtLink to="/shop" class="hover:text-pravis-200">
                  Shop
                </NuxtLink>
              </li>
              <li>
                <NuxtLink to="/contact" class="hover:text-pravis-200">
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
                <NuxtLink to="/privacy" class="hover:text-pravis-200">
                  Privacy Policy
                </NuxtLink>
              </li>
              <li>
                <NuxtLink to="/terms" class="hover:text-pravis-200">
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
  </div>
</template>

<script>
export default {
  data () {
    return {
      isMenuOpen: false
    }
  }
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
