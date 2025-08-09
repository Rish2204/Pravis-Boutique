<template>
  <section id="shop" class="py-20 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-16">
        <h3 class="text-4xl font-playfair font-bold text-handloom-deep mb-4">Featured Collection</h3>
        <p class="text-xl text-gray-600 max-w-2xl mx-auto">Handpicked selections showcasing the finest in Indian textile artistry</p>
      </div>
      
      <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
        <ProductCard
          v-for="product in products"
          :key="product.id"
          :product="product"
        />
      </div>
      
      <div class="text-center mt-12">
        <NuxtLink
          to="/shop"
          class="inline-block bg-handloom-sage text-white px-8 py-3 rounded-full font-semibold hover:bg-opacity-90 transition-colors"
        >
          View All Products
        </NuxtLink>
      </div>
    </div>
  </section>
</template>

<script setup>
import ProductCard from './ProductCard.vue'

const products = [
  {
    id: 1,
    name: 'Banarasi Silk Saree',
    description: 'Traditional zari work with intricate motifs',
    price: '₹12,500',
    rating: 5,
    patternId: 'product1',
    mainColor: '#8B0000',
    accentColor: '#FFD700',
    whatsappText: "Hi! I'm interested in the Banarasi Silk Saree (₹12,500)"
  },
  {
    id: 2,
    name: 'Chanderi Cotton',
    description: 'Lightweight handwoven elegance',
    price: '₹4,800',
    rating: 4,
    patternId: 'product2',
    mainColor: '#E07A5F',
    accentColor: '#F2CC8F',
    whatsappText: "Hi! I'm interested in the Chanderi Cotton saree (₹4,800)"
  },
  {
    id: 3,
    name: 'Anarkali Suit Set',
    description: 'Embroidered designer collection',
    price: '₹8,200',
    rating: 5,
    patternId: 'product3',
    mainColor: '#81B29A',
    accentColor: '#F2CC8F',
    whatsappText: "Hi! I'm interested in the Anarkali Suit Set (₹8,200)"
  },
  {
    id: 4,
    name: 'Kanjivaram Silk',
    description: 'Temple border traditional design',
    price: '₹15,600',
    rating: 5,
    patternId: 'product4',
    mainColor: '#3D405B',
    accentColor: '#F2CC8F',
    whatsappText: "Hi! I'm interested in the Kanjivaram Silk saree (₹15,600)"
  }
]
</script>

<style scoped>
/* Component specific styles if needed */
</style>