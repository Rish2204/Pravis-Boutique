<template>
  <section id="about" class="py-20 handloom-pattern bg-handloom-cream">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid lg:grid-cols-2 gap-12 items-center">
        <div class="space-y-6">
          <h3 class="text-4xl font-playfair font-bold text-handloom-deep">Our Heritage Story</h3>
          <div class="space-y-4 text-lg text-gray-700 leading-relaxed">
            <p>
              Founded with a passion for preserving India's rich textile heritage, Pravis Boutique bridges the gap between traditional craftsmanship and contemporary fashion.
            </p>
            <p>
              Each piece in our collection is carefully sourced from master weavers across India, ensuring authenticity and supporting local artisan communities.
            </p>
            <p>
              We believe that every thread tells a story, every pattern holds history, and every garment carries the soul of its creator.
            </p>
          </div>
          
          <div class="grid grid-cols-3 gap-6 pt-6">
            <div class="text-center">
              <div class="text-3xl font-bold text-handloom-rust mb-2">500+</div>
              <div class="text-sm text-gray-600">Artisan Partners</div>
            </div>
            <div class="text-center">
              <div class="text-3xl font-bold text-handloom-rust mb-2">15+</div>
              <div class="text-sm text-gray-600">States Covered</div>
            </div>
            <div class="text-center">
              <div class="text-3xl font-bold text-handloom-rust mb-2">10K+</div>
              <div class="text-sm text-gray-600">Happy Customers</div>
            </div>
          </div>
        </div>
        
        <div class="relative">
          <div class="bg-white rounded-2xl p-8 shadow-xl">
            <h4 class="text-2xl font-playfair font-semibold text-handloom-deep mb-6">Our Values</h4>
            <div class="space-y-4">
              <div 
                v-for="value in values" 
                :key="value.title"
                class="flex items-start space-x-4"
              >
                <div class="w-8 h-8 bg-handloom-sage rounded-full flex items-center justify-center flex-shrink-0">
                  <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                  </svg>
                </div>
                <div>
                  <h5 class="font-semibold text-handloom-deep">{{ value.title }}</h5>
                  <p class="text-gray-600 text-sm">{{ value.description }}</p>
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
const values = [
  {
    title: 'Authentic Craftsmanship',
    description: 'Every piece is handwoven by skilled artisans using traditional techniques'
  },
  {
    title: 'Sustainable Fashion',
    description: 'Eco-friendly processes and natural materials for conscious fashion'
  },
  {
    title: 'Community Support',
    description: 'Empowering weaver communities through fair trade practices'
  }
]
</script>

<style scoped>
.handloom-pattern {
  background-image: 
    radial-gradient(circle at 25% 25%, rgba(183, 71, 42, 0.1) 0%, transparent 50%),
    radial-gradient(circle at 75% 75%, rgba(129, 178, 154, 0.1) 0%, transparent 50%);
}
</style>