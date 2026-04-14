<template>
  <div>
    <!-- Hero banner -->
    <section class="py-12 md:py-16 text-center" style="background: linear-gradient(135deg, #8B0000, #A0001C, #B7472A)">
      <h1 class="font-display text-white text-3xl md:text-4xl lg:text-5xl mb-2">Handloom Collection</h1>
      <p class="text-white/80 text-lg">Curated textiles from across India</p>
    </section>

    <!-- Filters + Grid -->
    <section class="max-w-6xl mx-auto px-4 py-10 md:py-14">
      <!-- Category filter -->
      <div class="flex flex-wrap items-center gap-3 mb-8">
        <span class="text-pravis-700 font-medium text-sm">Filter:</span>
        <button
          v-for="cat in categories"
          :key="cat"
          class="px-4 py-1.5 rounded-full text-sm font-medium transition-colors"
          :class="selectedCategory === cat
            ? 'bg-pravis-500 text-white'
            : 'bg-pravis-50 text-pravis-700 hover:bg-pravis-100'"
          @click="selectCategory(cat)"
        >
          {{ cat }}
        </button>
      </div>

      <!-- Product count -->
      <p class="text-pravis-500 text-sm mb-6">
        Showing {{ filteredProducts.length }} of {{ products.length }} products
      </p>

      <!-- Product grid -->
      <div v-if="filteredProducts.length" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
        <ProductCard
          v-for="product in filteredProducts"
          :key="product.id"
          :product="product"
        />
      </div>

      <!-- Empty state -->
      <div v-else class="text-center py-20">
        <div class="w-20 h-20 mx-auto mb-4 bg-gray-100 rounded-full flex items-center justify-center">
          <svg class="w-10 h-10 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4" />
          </svg>
        </div>
        <p class="text-gray-500 text-lg">No products found in this category</p>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { products, categories, type Category } from '~/data/products'

useHead({
  title: 'Shop — Pravis Boutique',
})

const route = useRoute()
const router = useRouter()

const selectedCategory = ref<Category>('All Products')

// Read category from URL query
watchEffect(() => {
  const urlCat = route.query.category as string | undefined
  if (urlCat && categories.includes(urlCat as Category)) {
    selectedCategory.value = urlCat as Category
  } else if (!urlCat) {
    selectedCategory.value = 'All Products'
  }
})

function selectCategory(cat: Category) {
  selectedCategory.value = cat
  if (cat === 'All Products') {
    router.replace({ query: {} })
  } else {
    router.replace({ query: { category: cat } })
  }
}

const filteredProducts = computed(() => {
  if (selectedCategory.value === 'All Products') return products
  return products.filter(p => {
    if (selectedCategory.value === 'Kurtas & Suits') {
      return p.category === 'Kurtas & Suits' || p.category === 'Suits'
    }
    if (selectedCategory.value === 'Stoles & Dupattas') {
      return p.category === 'Stoles & Dupattas' || p.category === 'Stoles' || p.category === 'Dupattas'
    }
    if (selectedCategory.value === 'Jackets & Tops') {
      return p.category === 'Jackets & Tops' || p.category === 'Jackets' || p.category === 'Shirts'
    }
    return p.category === selectedCategory.value
  })
})
</script>
