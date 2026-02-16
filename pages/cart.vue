<template>
  <div class="min-h-screen bg-gray-50 py-12">
    <div class="container mx-auto px-4">
      <h1 class="text-3xl font-bold text-gray-900 mb-8">Shopping Cart</h1>
      
      <!-- Empty Cart State -->
      <div class="text-center py-16">
        <div class="w-24 h-24 mx-auto mb-6 bg-gray-200 rounded-full flex items-center justify-center">
          <svg class="w-12 h-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4m0 0L7 13m0 0l-1.6 8H19M7 13v4a2 2 0 002 2h8a2 2 0 002-2v-4"/>
          </svg>
        </div>
        <h2 class="text-2xl font-semibold text-gray-900 mb-4">Shopping Cart</h2>
        <div class="bg-gold-100 border border-gold-300 rounded-lg p-4 mb-6 max-w-md mx-auto">
          <p class="text-pravis-700 font-semibold mb-1">🚧 Under Development</p>
          <p class="text-pravis-600 text-sm">Cart functionality is being built. Use WhatsApp inquiry for now.</p>
        </div>
        <p class="text-gray-600 mb-8">For immediate assistance, contact us directly</p>
        
        <div class="space-y-4">
          <NuxtLink 
            to="/shop" 
            class="inline-block bg-pravis-600 hover:bg-pravis-700 text-white px-8 py-3 rounded-lg font-semibold transition-colors"
          >
            Browse Products
          </NuxtLink>
          <br>
          <button 
            @click="openWhatsApp"
            class="inline-block bg-green-600 hover:bg-green-700 text-white px-8 py-3 rounded-lg font-semibold transition-colors mr-4"
          >
            WhatsApp Us
          </button>
          <NuxtLink 
            to="/" 
            class="inline-flex items-center text-pravis-600 hover:text-pravis-700 font-medium"
          >
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
            </svg>
            Continue Shopping
          </NuxtLink>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
// Page metadata
useHead({
  title: 'Shopping Cart - Pravis Boutique',
  meta: [
    { name: 'description', content: 'Your shopping cart at Pravis Boutique - handloom textiles and traditional clothing.' }
  ]
})

const openWhatsApp = () => {
  const phoneNumber = '916300208234'
  const message = 'Hi! I need assistance with shopping at Pravis Boutique.'
  const whatsappUrl = `https://wa.me/${phoneNumber}?text=${encodeURIComponent(message)}`
  window.open(whatsappUrl, '_blank')
}
</script>

<style scoped>
.container {
  max-width: 1200px;
}
</style>