<template>
  <section class="gradient-bg min-h-screen flex items-center handloom-pattern">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
      <div class="grid lg:grid-cols-2 gap-12 items-center">
        <div class="space-y-8 fade-in">
          <div class="space-y-6">
            <h2 class="text-5xl lg:text-7xl font-display font-bold text-pravis-900 leading-tight">
              Authentic
              <span class="text-pravis-600">Handloom</span>
              Heritage
            </h2>
            <p class="text-xl text-pravis-800 leading-relaxed opacity-90">
              Discover the timeless beauty of Indian textiles. Each piece tells a story of tradition, craftsmanship, and elegance passed down through generations.
            </p>
          </div>
          <div class="flex flex-col sm:flex-row gap-4">
            <button 
              @click="scrollToShop" 
              class="bg-pravis-600 text-white px-8 py-4 rounded-full font-semibold hover:bg-pravis-700 transition-all duration-300 transform hover:scale-105 shadow-lg"
            >
              Shop Now
            </button>
            <a 
              href="https://wa.me/916300208234" 
              class="border-2 border-pravis-600 text-pravis-600 px-8 py-4 rounded-full font-semibold hover:bg-pravis-600 hover:text-white transition-all duration-300 text-center"
            >
              WhatsApp Inquiry
            </a>
          </div>
        </div>
        
        <!-- Hero Image -->
        <div class="relative fade-in">
          <div class="relative rounded-2xl overflow-hidden shadow-2xl hover-lift">
            <svg viewBox="0 0 400 500" class="w-full h-auto">
              <defs>
                <pattern id="heroSaree" x="0" y="0" width="30" height="30" patternUnits="userSpaceOnUse">
                  <rect width="30" height="30" fill="#8B0000" />
                  <circle cx="15" cy="15" r="2" fill="#D4AF37" opacity="0.8" />
                  <path d="M8 8 L22 8 L22 22 L8 22 Z" fill="none" stroke="#D4AF37" stroke-width="0.5" opacity="0.6" />
                </pattern>
                <linearGradient id="heroGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" style="stop-color:#8B0000" />
                  <stop offset="50%" style="stop-color:#A0001C" />
                  <stop offset="100%" style="stop-color:#D4AF37" />
                </linearGradient>
              </defs>
              
              <!-- Main saree drape -->
              <path d="M60 80 Q200 60 340 100 L340 450 Q200 480 60 450 Z" fill="url(#heroSaree)" />
              
              <!-- Golden border -->
              <rect x="55" y="75" width="290" height="8" fill="#D4AF37" />
              <rect x="55" y="445" width="290" height="8" fill="#D4AF37" />
              
              <!-- Decorative motifs -->
              <g transform="translate(120, 180)">
                <circle cx="0" cy="0" r="18" fill="#D4AF37" opacity="0.9" />
                <path d="M-12 -8 Q0 -20 12 -8 Q0 8 -12 -8" fill="#8B0000" />
                <circle cx="0" cy="-5" r="3" fill="#D4AF37" />
              </g>
              <g transform="translate(200, 280)">
                <circle cx="0" cy="0" r="15" fill="#D4AF37" opacity="0.8" />
                <path d="M-10 -6 Q0 -16 10 -6 Q0 6 -10 -6" fill="#8B0000" />
              </g>
              <g transform="translate(280, 220)">
                <circle cx="0" cy="0" r="12" fill="#D4AF37" opacity="0.7" />
                <path d="M-8 -5 Q0 -13 8 -5 Q0 5 -8 -5" fill="#8B0000" />
              </g>
              
              <!-- Pleats detail -->
              <path d="M60 400 Q80 390 100 400 Q120 390 140 400 Q160 390 180 400" fill="none" stroke="#D4AF37" stroke-width="2" opacity="0.8" />
            </svg>
          </div>
          
          <!-- Floating decorative elements -->
          <div class="absolute -top-6 -right-6 w-24 h-24 bg-pravis-300 rounded-full opacity-20 animate-pulse"></div>
          <div class="absolute -bottom-6 -left-6 w-20 h-20 bg-pravis-600 rounded-full opacity-20 animate-pulse" style="animation-delay: 1s;"></div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const scrollToShop = () => {
  const shopSection = document.getElementById('shop')
  if (shopSection) {
    shopSection.scrollIntoView({ behavior: 'smooth' })
  } else {
    // Navigate to shop page if not on home page
    navigateTo('/shop')
  }
}
</script>

<style scoped>
.gradient-bg {
  background: linear-gradient(135deg, #fdf2f8 0%, #D4AF37 50%, #A0001C 100%);
}

.handloom-pattern {
  background-image: 
    radial-gradient(circle at 25% 25%, rgba(139, 0, 0, 0.1) 0%, transparent 50%),
    radial-gradient(circle at 75% 75%, rgba(212, 175, 55, 0.1) 0%, transparent 50%);
}

.hover-lift {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.hover-lift:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 40px rgba(139, 0, 0, 0.15);
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