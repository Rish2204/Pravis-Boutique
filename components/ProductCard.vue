<template>
  <div class="bg-white rounded-lg shadow-sm hover-lift overflow-hidden group">
    <!-- Image placeholder -->
    <div
      class="relative h-64 flex items-center justify-center"
      :style="{ background: `linear-gradient(135deg, ${product.color}15, ${product.color}30)` }"
    >
      <!-- Coming Soon overlay -->
      <div class="text-center px-4">
        <div
          class="w-16 h-16 mx-auto mb-3 rounded-full flex items-center justify-center"
          :style="{ backgroundColor: `${product.color}20` }"
        >
          <svg class="w-8 h-8" :style="{ color: product.color }" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
          </svg>
        </div>
        <span class="text-xs font-medium tracking-wider uppercase" :style="{ color: product.color }">
          Coming Soon
        </span>
      </div>

      <!-- Sale badge -->
      <span
        v-if="product.originalPrice > product.price"
        class="absolute top-3 left-3 bg-red-600 text-white text-xs font-semibold px-2 py-1 rounded-full"
      >
        Sale
      </span>

      <!-- Fabric badge -->
      <span class="absolute top-3 right-3 bg-white/90 text-pravis-700 text-xs px-2 py-1 rounded-full">
        {{ product.fabric }}
      </span>
    </div>

    <!-- Product info -->
    <div class="p-4">
      <h3 class="font-display text-pravis-800 text-lg leading-tight mb-1 line-clamp-2">
        {{ product.name }}
      </h3>
      <p class="text-pravis-500 text-sm mb-2 line-clamp-2">
        {{ product.description }}
      </p>

      <!-- Origin -->
      <span class="inline-block bg-pravis-50 text-pravis-700 text-xs px-2 py-0.5 rounded-full mb-3">
        {{ product.origin }}
      </span>

      <!-- Price -->
      <div class="flex items-baseline gap-2 mb-3">
        <span class="text-pravis-600 font-bold text-lg">{{ formatPrice(product.price) }}</span>
        <span v-if="product.originalPrice > product.price" class="text-gray-400 text-sm line-through">
          {{ formatPrice(product.originalPrice) }}
        </span>
      </div>

      <!-- WhatsApp CTA -->
      <a
        :href="getWhatsAppLink(product.name)"
        target="_blank"
        rel="noopener noreferrer"
        class="block w-full text-center px-4 py-2.5 bg-pravis-500 hover:bg-pravis-600 text-white rounded-lg text-sm font-semibold transition-colors"
      >
        Inquire on WhatsApp
      </a>
    </div>
  </div>
</template>

<script setup lang="ts">
import { formatPrice, getWhatsAppLink, type Product } from '~/data/products'

defineProps<{
  product: Product
}>()
</script>
