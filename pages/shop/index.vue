<template>
  <div class="min-h-screen bg-pravis-50">
    <section class="bg-gradient-to-br from-pravis-800 via-pravis-700 to-saffron-600 text-white">
      <div class="container mx-auto px-4 py-16 lg:py-20">
        <div class="max-w-3xl">
          <p class="mb-4 text-sm font-bold uppercase tracking-[0.24em] text-saffron-100">Pravis Boutique catalog</p>
          <h1 class="text-4xl font-bold leading-tight lg:text-6xl">Browse Indian attires for every occasion</h1>
          <p class="mt-5 text-lg leading-8 text-pravis-100">
            Sarees, suit sets, dupattas, lehengas, shawls, and handloom-inspired pieces. Use WhatsApp for real-time availability, Instagram for latest looks, and Amazon for marketplace browsing.
          </p>
          <div class="mt-8 flex flex-col gap-3 sm:flex-row">
            <a
              :href="whatsappCatalogUrl"
              target="_blank"
              rel="noopener noreferrer"
              class="inline-flex items-center justify-center rounded-full bg-white px-7 py-3 font-semibold text-pravis-800 transition hover:bg-saffron-100"
            >
              Ask on WhatsApp
            </a>
            <a
              :href="instagramUrl"
              target="_blank"
              rel="noopener noreferrer"
              class="inline-flex items-center justify-center rounded-full border border-white/70 px-7 py-3 font-semibold text-white transition hover:bg-white/10"
            >
              View Instagram
            </a>
            <a
              :href="amazonCatalogUrl"
              target="_blank"
              rel="noopener noreferrer"
              class="inline-flex items-center justify-center rounded-full bg-[#232f3e] px-7 py-3 font-semibold text-white transition hover:bg-[#131921]"
            >
              Browse Amazon
            </a>
          </div>
        </div>
      </div>
    </section>

    <section class="container mx-auto px-4 py-10">
      <div class="mb-8 flex flex-col gap-4 lg:flex-row lg:items-end lg:justify-between">
        <div>
          <h2 class="text-2xl font-bold text-gray-950">Shop by style</h2>
          <p class="mt-2 text-gray-600">Filter visually by the categories customers usually ask for first.</p>
        </div>
        <div class="flex flex-wrap gap-2">
          <button
            v-for="category in categories"
            :key="category"
            @click="activeCategory = category"
            class="rounded-full border px-4 py-2 text-sm font-semibold transition"
            :class="activeCategory === category ? 'border-pravis-700 bg-pravis-700 text-white' : 'border-pravis-200 bg-white text-pravis-700 hover:bg-pravis-50'"
          >
            {{ category }}
          </button>
        </div>
      </div>

      <div class="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
        <article
          v-for="product in filteredProducts"
          :key="product.id"
          class="overflow-hidden rounded-2xl border border-pravis-100 bg-white shadow-sm transition hover:-translate-y-1 hover:shadow-xl"
        >
          <div class="relative h-56 overflow-hidden" :style="{ background: product.background }">
            <div class="absolute inset-0 opacity-30" :style="{ backgroundImage: product.pattern }"></div>
            <div class="absolute left-4 top-4 rounded-full bg-white/90 px-3 py-1 text-xs font-bold text-pravis-700 shadow-sm">
              {{ product.category }}
            </div>
            <div class="absolute right-4 top-4 rounded-full bg-pravis-900/80 px-3 py-1 text-xs font-bold text-white">
              {{ product.availability }}
            </div>
            <div class="absolute inset-x-5 bottom-5 rounded-2xl bg-white/90 p-4 shadow-lg backdrop-blur">
              <p class="text-sm font-semibold text-pravis-700">{{ product.fabric }}</p>
              <p class="mt-1 text-xs text-gray-600">{{ product.origin }}</p>
            </div>
          </div>

          <div class="p-5">
            <div class="mb-4 min-h-[132px]">
              <h3 class="text-lg font-bold text-gray-950">{{ product.name }}</h3>
              <p class="mt-2 text-sm leading-6 text-gray-600">{{ product.description }}</p>
            </div>

            <div class="mb-5 flex items-center justify-between gap-3">
              <div>
                <p class="text-xl font-bold text-pravis-700">Rs. {{ product.price.toLocaleString('en-IN') }}</p>
                <p v-if="product.originalPrice > product.price" class="text-sm text-gray-500 line-through">Rs. {{ product.originalPrice.toLocaleString('en-IN') }}</p>
              </div>
              <span class="rounded-full bg-saffron-100 px-3 py-1 text-xs font-bold text-pravis-800">{{ product.tag }}</span>
            </div>

            <div class="grid gap-2">
              <a
                :href="buildWhatsappUrl(product)"
                target="_blank"
                rel="noopener noreferrer"
                class="inline-flex items-center justify-center rounded-xl bg-pravis-700 px-4 py-3 text-sm font-semibold text-white transition hover:bg-pravis-800"
              >
                WhatsApp Inquiry
              </a>
              <div class="grid grid-cols-2 gap-2">
                <a
                  :href="instagramUrl"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="inline-flex items-center justify-center rounded-xl border border-pravis-200 px-4 py-3 text-sm font-semibold text-pravis-700 transition hover:bg-pravis-50"
                >
                  Instagram
                </a>
                <a
                  :href="product.amazonUrl"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="inline-flex items-center justify-center rounded-xl bg-[#232f3e] px-4 py-3 text-sm font-semibold text-white transition hover:bg-[#131921]"
                >
                  Amazon
                </a>
              </div>
            </div>
          </div>
        </article>
      </div>

      <div v-if="filteredProducts.length === 0" class="rounded-2xl bg-white py-16 text-center shadow-sm">
        <h3 class="text-xl font-semibold text-gray-900">No products found</h3>
        <p class="mt-2 text-gray-600">Try another category.</p>
      </div>
    </section>
  </div>
</template>

<script setup>
import { computed, ref } from 'vue'

useHead({
  title: 'Shop Indian Attires - Pravis Boutique',
  meta: [
    { name: 'description', content: 'Browse Pravis Boutique Indian attire collections with WhatsApp, Instagram, and Amazon shopping links.' }
  ]
})

const whatsappPhone = '916300208234'
const instagramUrl = 'https://www.instagram.com/pravis.handlooms/?hl=en'
const amazonCatalogUrl = 'https://www.amazon.in/s?k=Pravis+Boutique+Indian+attire'
const whatsappCatalogUrl = `https://wa.me/${whatsappPhone}?text=${encodeURIComponent('Hi Pravis Boutique, I want to browse your Indian attire catalog.')}`

const categories = ['All', 'Sarees', 'Suit sets', 'Dupattas', 'Lehengas', 'Shawls']
const activeCategory = ref('All')

const products = ref([
  {
    id: 1,
    name: 'Banarasi Silk Saree - Golden Thread',
    price: 15999,
    originalPrice: 18999,
    category: 'Sarees',
    fabric: 'Pure Silk',
    origin: 'Varanasi, UP',
    tag: 'Wedding pick',
    availability: 'Ask for colors',
    description: 'Rich Banarasi-inspired saree with golden thread work and traditional motifs.',
    background: 'linear-gradient(135deg, #8B0000, #D4AF37)',
    pattern: 'radial-gradient(circle at 24px 24px, rgba(255,255,255,.55) 2px, transparent 3px)',
    amazonUrl: 'https://www.amazon.in/s?k=Pravis+Boutique+Banarasi+Silk+Saree'
  },
  {
    id: 2,
    name: 'Handwoven Cotton Kurta Set',
    price: 3499,
    originalPrice: 3499,
    category: 'Suit sets',
    fabric: 'Pure Cotton',
    origin: 'Lucknow, UP',
    tag: 'Daily wear',
    availability: 'Sizes vary',
    description: 'Comfortable cotton kurta set with easy styling for office, home, and casual outings.',
    background: 'linear-gradient(135deg, #81B29A, #F2CC8F)',
    pattern: 'radial-gradient(circle at 30px 30px, rgba(255,255,255,.45) 5px, transparent 6px)',
    amazonUrl: 'https://www.amazon.in/s?k=Pravis+Boutique+Cotton+Kurta+Set'
  },
  {
    id: 3,
    name: 'Kashmiri Pashmina Shawl',
    price: 8999,
    originalPrice: 10999,
    category: 'Shawls',
    fabric: 'Pashmina',
    origin: 'Kashmir',
    tag: 'Gift edit',
    availability: 'Limited',
    description: 'Soft shawl with delicate embroidery-inspired detailing for gifting and winter styling.',
    background: 'linear-gradient(135deg, #3D405B, #F2CC8F)',
    pattern: 'repeating-linear-gradient(90deg, rgba(255,255,255,.28) 0 2px, transparent 2px 18px)',
    amazonUrl: 'https://www.amazon.in/s?k=Pravis+Boutique+Pashmina+Shawl'
  },
  {
    id: 4,
    name: 'Chanderi Silk Dupatta',
    price: 2799,
    originalPrice: 2799,
    category: 'Dupattas',
    fabric: 'Chanderi Silk',
    origin: 'Chanderi, MP',
    tag: 'Lightweight',
    availability: 'Inquire',
    description: 'Elegant dupatta with festive shine that pairs with plain kurtas and suit sets.',
    background: 'linear-gradient(135deg, #E07A5F, #F2CC8F)',
    pattern: 'linear-gradient(45deg, rgba(255,255,255,.32) 25%, transparent 25%, transparent 50%, rgba(255,255,255,.32) 50%, rgba(255,255,255,.32) 75%, transparent 75%)',
    amazonUrl: 'https://www.amazon.in/s?k=Pravis+Boutique+Chanderi+Silk+Dupatta'
  },
  {
    id: 5,
    name: 'Handloom Linen Saree',
    price: 4999,
    originalPrice: 5999,
    category: 'Sarees',
    fabric: 'Pure Linen',
    origin: 'Kerala',
    tag: 'Everyday saree',
    availability: 'Ask for stock',
    description: 'Breathable handloom-style linen saree with subtle border details.',
    background: 'linear-gradient(135deg, #6B705C, #DDBEA9)',
    pattern: 'repeating-linear-gradient(0deg, rgba(255,255,255,.22) 0 3px, transparent 3px 16px)',
    amazonUrl: 'https://www.amazon.in/s?k=Pravis+Boutique+Handloom+Linen+Saree'
  },
  {
    id: 6,
    name: 'Rajasthani Block Print Lehenga',
    price: 12999,
    originalPrice: 15999,
    category: 'Lehengas',
    fabric: 'Cotton Silk',
    origin: 'Jaipur, Rajasthan',
    tag: 'Event wear',
    availability: 'Pre-order',
    description: 'Vibrant block-print inspired lehenga with festive mirror-work styling.',
    background: 'linear-gradient(135deg, #BC4749, #F2E8CF)',
    pattern: 'radial-gradient(circle at 28px 28px, rgba(255,255,255,.45) 4px, transparent 5px)',
    amazonUrl: 'https://www.amazon.in/s?k=Pravis+Boutique+Rajasthani+Block+Print+Lehenga'
  },
  {
    id: 7,
    name: 'Floral Print Cotton Suit Set',
    price: 4999,
    originalPrice: 5999,
    category: 'Suit sets',
    fabric: 'Pure Cotton',
    origin: 'Handcrafted edit',
    tag: 'Fresh arrival',
    availability: 'Ask for sizes',
    description: 'Three-piece cotton suit set with floral print, pants, and matching dupatta.',
    background: 'linear-gradient(135deg, #F4A7B9, #F8EDEB)',
    pattern: 'radial-gradient(circle at 22px 22px, rgba(139,0,0,.22) 3px, transparent 4px)',
    amazonUrl: 'https://www.amazon.in/s?k=Pravis+Boutique+Floral+Cotton+Suit+Set'
  }
])

const filteredProducts = computed(() => {
  if (activeCategory.value === 'All') return products.value
  return products.value.filter(product => product.category === activeCategory.value)
})

const buildWhatsappUrl = (product) => {
  const message = `Hi Pravis Boutique, I am interested in ${product.name}. Price: Rs. ${product.price.toLocaleString('en-IN')}. Can you share photos, availability, sizing, and order details?`
  return `https://wa.me/${whatsappPhone}?text=${encodeURIComponent(message)}`
}
</script>

<style scoped>
.container {
  max-width: 1200px;
}
</style>
