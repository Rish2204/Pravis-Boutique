<template>
  <div class="group hover-lift bg-white rounded-2xl shadow-lg overflow-hidden border border-gray-100">
    <div class="h-64 relative overflow-hidden">
      <svg viewBox="0 0 200 250" class="w-full h-full">
        <defs>
          <pattern :id="product.patternId" x="0" y="0" width="25" height="25" patternUnits="userSpaceOnUse">
            <rect width="25" height="25" :fill="product.mainColor" />
            <circle cx="12.5" cy="12.5" r="2" :fill="product.accentColor" opacity="0.8" />
            <path d="M6 6 L19 6 L19 19 L6 19 Z" fill="none" :stroke="product.accentColor" stroke-width="0.3" />
          </pattern>
        </defs>
        <rect width="200" height="250" :fill="`url(#${product.patternId})`" />
        <rect x="0" y="0" width="200" height="15" :fill="product.accentColor" />
        <rect x="0" y="235" width="200" height="15" :fill="product.accentColor" />
        <!-- Decorative motif -->
        <g transform="translate(100, 125)">
          <circle cx="0" cy="0" r="20" :fill="product.accentColor" opacity="0.9" />
          <path d="M-12 -8 Q0 -18 12 -8 Q0 8 -12 -8" :fill="product.mainColor" />
        </g>
      </svg>
      <div class="absolute inset-0 bg-black bg-opacity-0 group-hover:bg-opacity-10 transition-all duration-300"></div>
    </div>
    <div class="p-6">
      <h5 class="font-playfair font-semibold text-handloom-deep mb-2 text-lg">{{ product.name }}</h5>
      <p class="text-sm text-gray-600 mb-3">{{ product.description }}</p>
      <div class="flex justify-between items-center mb-4">
        <span class="text-2xl font-bold text-handloom-rust">{{ product.price }}</span>
        <div class="flex text-yellow-400">
          <span v-for="n in 5" :key="n">
            {{ n <= product.rating ? '★' : '☆' }}
          </span>
        </div>
      </div>
      <div class="flex gap-2">
        <button 
          @click="addToCart(product)"
          class="flex-1 bg-handloom-rust text-white py-2 px-4 rounded-lg font-medium hover:bg-handloom-terracotta transition-colors"
        >
          Add to Cart
        </button>
        <a 
          :href="`https://wa.me/916300208234?text=${encodeURIComponent(product.whatsappText)}`"
          target="_blank"
          class="bg-green-500 text-white px-4 py-2 rounded-lg hover:bg-green-600 transition-colors flex items-center justify-center"
        >
          <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
            <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893A11.821 11.821 0 0020.465 3.516"/>
          </svg>
        </a>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  product: {
    type: Object,
    required: true
  }
})

const addToCart = (product) => {
  // Implement cart functionality
  console.log('Adding to cart:', product)
  // You can emit an event or use a store here
}
</script>

<style scoped>
.hover-lift {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.hover-lift:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 40px rgba(183, 71, 42, 0.15);
}
</style>