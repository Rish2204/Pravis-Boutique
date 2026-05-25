<template>
  <section class="hero-shell min-h-screen flex items-center overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 lg:py-28">
      <div class="grid lg:grid-cols-[1.02fr_0.98fr] gap-12 items-center">
        <div class="space-y-8 fade-in">
          <div class="inline-flex items-center gap-2 rounded-full border border-pravis-200 bg-white/80 px-4 py-2 text-sm font-semibold text-pravis-700 shadow-sm">
            <span class="h-2 w-2 rounded-full bg-pravis-600"></span>
            Indian attire boutique
          </div>

          <div class="space-y-6">
            <h2 class="text-5xl lg:text-7xl font-display font-bold text-pravis-950 leading-tight">
              Browse Indian
              <span class="text-pravis-600">attires</span>
              with ease
            </h2>
            <p class="text-xl text-pravis-800 leading-relaxed max-w-2xl">
              Explore sarees, suits, dupattas, lehengas, and handloom pieces curated for weddings, festive wear, and everyday elegance. Ask on WhatsApp, follow new drops on Instagram, or browse available listings on Amazon.
            </p>
          </div>

          <div class="grid sm:grid-cols-3 gap-3 max-w-2xl">
            <button
              @click="scrollToShop"
              class="inline-flex items-center justify-center rounded-full bg-pravis-700 px-6 py-4 font-semibold text-white shadow-lg transition hover:bg-pravis-800 hover:shadow-xl focus:outline-none focus:ring-2 focus:ring-pravis-500 focus:ring-offset-2"
            >
              Shop Collection
            </button>
            <a
              :href="whatsappUrl"
              target="_blank"
              rel="noopener noreferrer"
              class="inline-flex items-center justify-center rounded-full border-2 border-pravis-700 px-6 py-4 font-semibold text-pravis-700 transition hover:bg-pravis-700 hover:text-white focus:outline-none focus:ring-2 focus:ring-pravis-500 focus:ring-offset-2"
            >
              WhatsApp Us
            </a>
            <a
              :href="amazonUrl"
              target="_blank"
              rel="noopener noreferrer"
              class="inline-flex items-center justify-center rounded-full bg-[#232f3e] px-6 py-4 font-semibold text-white shadow-lg transition hover:bg-[#131921] hover:shadow-xl focus:outline-none focus:ring-2 focus:ring-pravis-500 focus:ring-offset-2"
            >
              Browse Amazon
            </a>
          </div>

          <div class="flex flex-wrap gap-3 text-sm font-medium text-pravis-800">
            <span class="rounded-full bg-white/80 px-4 py-2 shadow-sm">Sarees</span>
            <span class="rounded-full bg-white/80 px-4 py-2 shadow-sm">Suit sets</span>
            <span class="rounded-full bg-white/80 px-4 py-2 shadow-sm">Lehengas</span>
            <span class="rounded-full bg-white/80 px-4 py-2 shadow-sm">Dupattas</span>
          </div>
        </div>

        <div class="relative fade-in">
          <div class="absolute -left-5 top-10 hidden h-28 w-28 rounded-full bg-saffron-300/40 blur-2xl lg:block"></div>
          <div class="absolute -right-6 bottom-10 hidden h-36 w-36 rounded-full bg-pravis-300/40 blur-2xl lg:block"></div>

          <div class="relative rounded-[2rem] border border-white/70 bg-white/80 p-4 shadow-2xl backdrop-blur hover-lift">
            <div class="rounded-[1.5rem] bg-gradient-to-br from-pravis-800 via-pravis-700 to-saffron-500 p-6 text-white">
              <div class="mb-6 flex items-center justify-between">
                <div>
                  <p class="text-sm uppercase tracking-[0.24em] text-saffron-100">Featured drop</p>
                  <h3 class="mt-2 text-3xl font-display font-bold">Festive edit</h3>
                </div>
                <span class="rounded-full bg-white/15 px-3 py-1 text-sm">New</span>
              </div>

              <svg viewBox="0 0 420 470" class="w-full h-auto rounded-2xl bg-white/10">
                <defs>
                  <pattern id="heroSaree" x="0" y="0" width="30" height="30" patternUnits="userSpaceOnUse">
                    <rect width="30" height="30" fill="#7f0014" />
                    <circle cx="15" cy="15" r="2" fill="#D4AF37" opacity="0.85" />
                    <path d="M8 8 L22 8 L22 22 L8 22 Z" fill="none" stroke="#D4AF37" stroke-width="0.6" opacity="0.65" />
                  </pattern>
                </defs>
                <path d="M64 62 Q210 26 356 78 L348 420 Q210 455 72 420 Z" fill="url(#heroSaree)" />
                <rect x="58" y="68" width="304" height="10" rx="5" fill="#D4AF37" />
                <rect x="66" y="405" width="286" height="10" rx="5" fill="#D4AF37" />
                <path d="M112 130 Q210 102 304 136" fill="none" stroke="#F7D77A" stroke-width="5" opacity="0.9" />
                <path d="M120 356 Q148 342 176 356 Q204 342 232 356 Q260 342 288 356" fill="none" stroke="#F7D77A" stroke-width="4" opacity="0.8" />
                <g transform="translate(140 205)">
                  <circle r="28" fill="#D4AF37" opacity="0.95" />
                  <path d="M-16 -10 Q0 -28 16 -10 Q0 16 -16 -10" fill="#7f0014" />
                </g>
                <g transform="translate(245 260)">
                  <circle r="23" fill="#F2CC8F" opacity="0.95" />
                  <path d="M-13 -8 Q0 -23 13 -8 Q0 13 -13 -8" fill="#7f0014" />
                </g>
              </svg>

              <div class="mt-6 grid grid-cols-3 gap-3 text-center text-sm">
                <div class="rounded-2xl bg-white/15 px-3 py-3">
                  <p class="font-bold">WhatsApp</p>
                  <p class="text-saffron-100">fast inquiry</p>
                </div>
                <div class="rounded-2xl bg-white/15 px-3 py-3">
                  <p class="font-bold">Instagram</p>
                  <p class="text-saffron-100">new drops</p>
                </div>
                <div class="rounded-2xl bg-white/15 px-3 py-3">
                  <p class="font-bold">Amazon</p>
                  <p class="text-saffron-100">browse listings</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const whatsappUrl = 'https://wa.me/916300208234?text=Hi%20Pravis%20Boutique%2C%20I%20want%20to%20browse%20Indian%20attires.'
const amazonUrl = 'https://www.amazon.in/s?k=Pravis+Boutique+Indian+attire'

const scrollToShop = () => {
  const shopSection = document.getElementById('shop')
  if (shopSection) {
    shopSection.scrollIntoView({ behavior: 'smooth' })
  } else {
    navigateTo('/shop')
  }
}
</script>

<style scoped>
.hero-shell {
  background:
    radial-gradient(circle at 20% 20%, rgba(212, 175, 55, 0.28), transparent 32%),
    radial-gradient(circle at 85% 15%, rgba(139, 0, 0, 0.16), transparent 28%),
    linear-gradient(135deg, #fff7ed 0%, #fff1f2 48%, #fef3c7 100%);
}

.hover-lift {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.hover-lift:hover {
  transform: translateY(-8px);
  box-shadow: 0 24px 48px rgba(139, 0, 0, 0.18);
}

.fade-in {
  animation: fadeIn 0.6s ease-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>