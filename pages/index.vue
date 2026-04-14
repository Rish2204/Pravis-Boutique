<template>
  <div>
    <!-- Hero Section -->
    <section class="relative overflow-hidden py-16 md:py-24" style="background: linear-gradient(135deg, #fdf2f8 0%, #D4AF3720 50%, #A0001C10 100%)">
      <!-- Decorative overlays -->
      <div class="absolute inset-0 opacity-10">
        <div class="absolute top-0 left-1/4 w-96 h-96 rounded-full" style="background: radial-gradient(circle, #8B0000 0%, transparent 70%)"></div>
        <div class="absolute bottom-0 right-1/4 w-80 h-80 rounded-full" style="background: radial-gradient(circle, #D4AF37 0%, transparent 70%)"></div>
      </div>

      <div class="relative max-w-6xl mx-auto px-4">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <!-- Left: Text -->
          <div class="text-center lg:text-left">
            <h2 class="font-display text-pravis-800 text-4xl md:text-5xl lg:text-6xl leading-tight mb-6">
              Authentic Handloom<br />
              <span class="text-gold">Heritage</span>
            </h2>
            <p class="text-pravis-700 text-lg md:text-xl leading-relaxed mb-8 max-w-lg mx-auto lg:mx-0">
              Discover exquisite handwoven textiles from India's finest artisans. Each piece tells a story of tradition, craftsmanship, and timeless beauty.
            </p>
            <div class="flex flex-col sm:flex-row gap-4 justify-center lg:justify-start">
              <NuxtLink
                to="/shop"
                class="px-8 py-3 bg-pravis-500 hover:bg-pravis-600 text-white rounded-full font-semibold transition-all hover:scale-105 text-center"
              >
                Shop Now
              </NuxtLink>
              <a
                href="https://wa.me/?text=Hi!%20I%27d%20like%20to%20know%20more%20about%20Pravis%20Boutique%20products."
                target="_blank"
                rel="noopener noreferrer"
                class="px-8 py-3 border-2 border-pravis-500 text-pravis-500 hover:bg-pravis-500 hover:text-white rounded-full font-semibold transition-all text-center"
              >
                WhatsApp Inquiry
              </a>
            </div>
          </div>

          <!-- Right: Decorative SVG saree illustration -->
          <div class="hidden lg:flex justify-center">
            <svg width="360" height="440" viewBox="0 0 360 440" fill="none">
              <!-- Saree drape shape -->
              <defs>
                <pattern id="sareePattern" x="0" y="0" width="30" height="30" patternUnits="userSpaceOnUse">
                  <rect width="30" height="30" fill="#8B0000" />
                  <circle cx="15" cy="15" r="4" fill="#D4AF37" opacity="0.6" />
                  <rect x="12" y="12" width="6" height="6" rx="1" fill="#D4AF37" opacity="0.3" />
                </pattern>
                <linearGradient id="sareeGrad" x1="0" y1="0" x2="1" y2="1">
                  <stop offset="0%" stop-color="#8B0000" />
                  <stop offset="100%" stop-color="#5F0000" />
                </linearGradient>
              </defs>
              <!-- Main saree body -->
              <path
                d="M80 40 C80 40, 280 30, 300 60 C320 90, 310 180, 290 280 C270 380, 200 420, 160 430 C120 420, 60 380, 50 280 C40 180, 50 90, 80 40Z"
                fill="url(#sareePattern)"
                stroke="#D4AF37"
                stroke-width="2"
              />
              <!-- Gold border bars -->
              <rect x="60" y="100" width="240" height="6" rx="3" fill="#D4AF37" opacity="0.7" />
              <rect x="70" y="340" width="220" height="6" rx="3" fill="#D4AF37" opacity="0.7" />
              <!-- Decorative gold circles -->
              <circle cx="180" cy="200" r="40" fill="#D4AF37" opacity="0.1" />
              <circle cx="130" cy="260" r="25" fill="#D4AF37" opacity="0.15" />
              <circle cx="230" cy="160" r="30" fill="#D4AF37" opacity="0.12" />
              <!-- Pleat detail -->
              <path d="M140 370 Q160 360, 180 370 Q200 380, 220 370" stroke="#D4AF37" stroke-width="1.5" fill="none" opacity="0.5" />
              <path d="M130 385 Q160 375, 190 385 Q220 395, 240 385" stroke="#D4AF37" stroke-width="1" fill="none" opacity="0.3" />
            </svg>
          </div>
        </div>
      </div>
    </section>

    <!-- Featured Products -->
    <section class="bg-white py-16 md:py-20">
      <div class="max-w-6xl mx-auto px-4">
        <div class="text-center mb-12">
          <h2 class="font-display text-pravis-800 text-3xl md:text-4xl mb-3">Featured Collection</h2>
          <p class="text-pravis-600 text-lg">Handpicked pieces from India's finest looms</p>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 md:gap-8">
          <ProductCard
            v-for="product in featuredProducts"
            :key="product.id"
            :product="product"
          />
        </div>

        <div class="text-center mt-10">
          <NuxtLink
            to="/shop"
            class="inline-block px-8 py-3 bg-handloom-sage hover:bg-handloom-sage/90 text-white rounded-full font-semibold transition-colors"
          >
            View All Products
          </NuxtLink>
        </div>
      </div>
    </section>

    <!-- About / Heritage Section -->
    <section class="py-16 md:py-20" style="background: linear-gradient(180deg, #FDF2F8 0%, #F4F3EE 100%)">
      <div class="max-w-6xl mx-auto px-4">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <!-- Left: Story -->
          <div>
            <h2 class="font-display text-pravis-800 text-3xl md:text-4xl mb-6">Our Heritage Story</h2>
            <p class="text-pravis-700 leading-relaxed mb-4">
              Pravis Boutique was born from a deep appreciation for India's handloom traditions. We work directly with artisan communities across the country, bringing their extraordinary craftsmanship to those who value authentic, sustainable fashion.
            </p>
            <p class="text-pravis-700 leading-relaxed mb-8">
              Every thread tells a story — of generations of weavers who have perfected their art, of natural dyes sourced from the earth, and of patterns that carry centuries of cultural heritage.
            </p>

            <!-- Stats -->
            <div class="grid grid-cols-3 gap-4">
              <div class="text-center">
                <div class="text-pravis-600 font-bold text-2xl md:text-3xl">500+</div>
                <div class="text-pravis-500 text-sm mt-1">Artisan Partners</div>
              </div>
              <div class="text-center">
                <div class="text-pravis-600 font-bold text-2xl md:text-3xl">15+</div>
                <div class="text-pravis-500 text-sm mt-1">States</div>
              </div>
              <div class="text-center">
                <div class="text-pravis-600 font-bold text-2xl md:text-3xl">10K+</div>
                <div class="text-pravis-500 text-sm mt-1">Happy Customers</div>
              </div>
            </div>
          </div>

          <!-- Right: Values card -->
          <div class="bg-white rounded-2xl shadow-lg p-8">
            <h3 class="font-display text-pravis-800 text-2xl mb-6">Our Values</h3>
            <div class="space-y-5">
              <div class="flex items-start gap-4">
                <div class="w-10 h-10 rounded-full bg-gold/20 flex items-center justify-center flex-shrink-0">
                  <svg class="w-5 h-5 text-gold" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                  </svg>
                </div>
                <div>
                  <h4 class="font-semibold text-pravis-800 mb-1">Authentic Artisanship</h4>
                  <p class="text-pravis-600 text-sm">Every product is handcrafted by skilled artisans using traditional techniques passed down through generations.</p>
                </div>
              </div>
              <div class="flex items-start gap-4">
                <div class="w-10 h-10 rounded-full bg-gold/20 flex items-center justify-center flex-shrink-0">
                  <svg class="w-5 h-5 text-gold" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                  </svg>
                </div>
                <div>
                  <h4 class="font-semibold text-pravis-800 mb-1">Sustainable Practices</h4>
                  <p class="text-pravis-600 text-sm">We champion eco-friendly processes — natural dyes, organic fibers, and minimal waste production.</p>
                </div>
              </div>
              <div class="flex items-start gap-4">
                <div class="w-10 h-10 rounded-full bg-gold/20 flex items-center justify-center flex-shrink-0">
                  <svg class="w-5 h-5 text-gold" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                  </svg>
                </div>
                <div>
                  <h4 class="font-semibold text-pravis-800 mb-1">Fair Trade</h4>
                  <p class="text-pravis-600 text-sm">Artisans receive fair compensation, empowering communities and preserving handloom heritage.</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { products } from '~/data/products'

const featuredProducts = products.filter(p => p.featured)

useHead({
  title: 'Pravis Boutique — Drape in Elegance',
})
</script>
