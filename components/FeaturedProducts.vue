<template>
  <section id="shop" class="bg-white py-20">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="mb-12 flex flex-col gap-6 lg:flex-row lg:items-end lg:justify-between">
        <div>
          <p class="mb-3 text-sm font-bold uppercase tracking-[0.24em] text-pravis-600">Featured collection</p>
          <h3 class="text-4xl font-display font-bold text-pravis-950">Indian attires ready to browse</h3>
          <p class="mt-4 max-w-2xl text-lg text-gray-600">
            Start with the most requested pieces, then use WhatsApp for availability, Instagram for fresh styling posts, or Amazon for marketplace browsing.
          </p>
        </div>
        <NuxtLink
          to="/shop"
          class="inline-flex items-center justify-center rounded-full bg-pravis-700 px-7 py-3 font-semibold text-white shadow-lg transition hover:bg-pravis-800 hover:shadow-xl"
        >
          View Full Catalog
        </NuxtLink>
      </div>

      <div class="grid gap-6 md:grid-cols-2 lg:grid-cols-4">
        <article
          v-for="product in products"
          :key="product.id"
          class="group overflow-hidden rounded-2xl border border-pravis-100 bg-white shadow-sm transition hover:-translate-y-1 hover:shadow-xl"
        >
          <div class="relative h-56 overflow-hidden" :style="{ background: product.background }">
            <div class="absolute inset-0 opacity-30" :style="{ backgroundImage: product.pattern }"></div>
            <div class="absolute left-4 top-4 rounded-full bg-white/90 px-3 py-1 text-xs font-bold text-pravis-700 shadow-sm">
              {{ product.category }}
            </div>
            <div class="absolute inset-x-6 bottom-6 rounded-2xl bg-white/85 p-4 shadow-lg backdrop-blur">
              <p class="text-sm font-semibold text-pravis-700">{{ product.fabric }}</p>
              <p class="mt-1 text-xs text-gray-600">{{ product.origin }}</p>
            </div>
          </div>

          <div class="p-5">
            <div class="mb-4 min-h-[104px]">
              <h4 class="text-lg font-bold text-gray-950">{{ product.name }}</h4>
              <p class="mt-2 text-sm leading-6 text-gray-600">{{ product.description }}</p>
            </div>

            <div class="mb-5 flex items-center justify-between">
              <p class="text-xl font-bold text-pravis-700">{{ product.price }}</p>
              <p class="text-sm font-medium text-gray-500">{{ product.badge }}</p>
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
    </div>
  </section>
</template>

<script setup>
const whatsappPhone = '916300208234'
const instagramUrl = 'https://www.instagram.com/pravis.handlooms/?hl=en'

const products = [
  {
    id: 1,
    name: 'Banarasi Silk Saree',
    description: 'Traditional zari work for weddings, pujas, and festive occasions.',
    price: 'Rs. 12,500',
    category: 'Saree',
    fabric: 'Silk with zari border',
    origin: 'Banarasi inspired',
    badge: 'Festive pick',
    background: 'linear-gradient(135deg, #8B0000, #D4AF37)',
    pattern: 'radial-gradient(circle at 24px 24px, rgba(255,255,255,.55) 2px, transparent 3px)',
    amazonUrl: 'https://www.amazon.in/s?k=Pravis+Boutique+Banarasi+Silk+Saree'
  },
  {
    id: 2,
    name: 'Chanderi Cotton Saree',
    description: 'Lightweight drape with a soft finish for day events and gifting.',
    price: 'Rs. 4,800',
    category: 'Saree',
    fabric: 'Chanderi cotton',
    origin: 'Handloom edit',
    badge: 'Easy drape',
    background: 'linear-gradient(135deg, #E07A5F, #F2CC8F)',
    pattern: 'linear-gradient(45deg, rgba(255,255,255,.32) 25%, transparent 25%, transparent 50%, rgba(255,255,255,.32) 50%, rgba(255,255,255,.32) 75%, transparent 75%)',
    amazonUrl: 'https://www.amazon.in/s?k=Pravis+Boutique+Chanderi+Cotton+Saree'
  },
  {
    id: 3,
    name: 'Anarkali Suit Set',
    description: 'Embroidered set for celebrations, family gatherings, and portraits.',
    price: 'Rs. 8,200',
    category: 'Suit set',
    fabric: 'Embroidered blend',
    origin: 'Designer collection',
    badge: 'Occasion wear',
    background: 'linear-gradient(135deg, #81B29A, #F2CC8F)',
    pattern: 'radial-gradient(circle at 30px 30px, rgba(255,255,255,.45) 5px, transparent 6px)',
    amazonUrl: 'https://www.amazon.in/s?k=Pravis+Boutique+Anarkali+Suit+Set'
  },
  {
    id: 4,
    name: 'Kanjivaram Silk Saree',
    description: 'Temple-border statement piece with rich contrast and classic shine.',
    price: 'Rs. 15,600',
    category: 'Saree',
    fabric: 'Kanjivaram silk',
    origin: 'South Indian edit',
    badge: 'Premium',
    background: 'linear-gradient(135deg, #3D405B, #D4AF37)',
    pattern: 'repeating-linear-gradient(90deg, rgba(255,255,255,.28) 0 2px, transparent 2px 18px)',
    amazonUrl: 'https://www.amazon.in/s?k=Pravis+Boutique+Kanjivaram+Silk+Saree'
  }
]

const buildWhatsappUrl = (product) => {
  const message = `Hi Pravis Boutique, I am interested in ${product.name} (${product.price}). Can you share availability, photos, and ordering details?`
  return `https://wa.me/${whatsappPhone}?text=${encodeURIComponent(message)}`
}
</script>
