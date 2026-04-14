<template>
  <div>
    <!-- Hero banner -->
    <section class="py-12 md:py-16 text-center" style="background: linear-gradient(135deg, #8B0000, #5F0000)">
      <h1 class="font-display text-white text-3xl md:text-4xl lg:text-5xl mb-2">Get in Touch</h1>
      <p class="text-white/80 text-lg">We'd love to hear from you</p>
    </section>

    <!-- Content -->
    <section class="max-w-6xl mx-auto px-4 py-10 md:py-16">
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-10 lg:gap-16">
        <!-- Left: Contact Info -->
        <div class="space-y-8">
          <div>
            <h2 class="font-display text-pravis-800 text-2xl md:text-3xl mb-6">Reach Out to Us</h2>
            <p class="text-pravis-600 leading-relaxed">
              Whether you have a question about our handloom textiles, need help with an order, or want to explore a custom weave, our team is here to help.
            </p>
          </div>

          <!-- Address -->
          <div class="flex items-start gap-4">
            <div class="w-12 h-12 rounded-lg bg-pravis-50 flex items-center justify-center flex-shrink-0">
              <svg class="w-6 h-6 text-pravis-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
              </svg>
            </div>
            <div>
              <h3 class="font-semibold text-pravis-800 mb-1">Visit Us</h3>
              <p class="text-pravis-600 text-sm leading-relaxed">
                Pravis Boutique<br />
                India
              </p>
            </div>
          </div>

          <!-- Phone -->
          <div class="flex items-start gap-4">
            <div class="w-12 h-12 rounded-lg bg-pravis-50 flex items-center justify-center flex-shrink-0">
              <svg class="w-6 h-6 text-pravis-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
              </svg>
            </div>
            <div>
              <h3 class="font-semibold text-pravis-800 mb-1">Call Us</h3>
              <p class="text-pravis-600 text-sm">+91 98765 43210</p>
            </div>
          </div>

          <!-- Email -->
          <div class="flex items-start gap-4">
            <div class="w-12 h-12 rounded-lg bg-pravis-50 flex items-center justify-center flex-shrink-0">
              <svg class="w-6 h-6 text-pravis-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
              </svg>
            </div>
            <div>
              <h3 class="font-semibold text-pravis-800 mb-1">Email Us</h3>
              <p class="text-pravis-600 text-sm">info@pravisboutique.com</p>
            </div>
          </div>

          <!-- WhatsApp -->
          <a
            href="https://wa.me/?text=Hi!%20I%27d%20like%20to%20get%20in%20touch%20with%20Pravis%20Boutique."
            target="_blank"
            rel="noopener noreferrer"
            class="inline-flex items-center gap-2 px-6 py-3 bg-green-600 hover:bg-green-700 text-white rounded-full font-semibold transition-colors"
          >
            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
              <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z" />
              <path d="M12 0C5.373 0 0 5.373 0 12c0 2.625.846 5.059 2.284 7.034L.789 23.492a.5.5 0 00.627.616l4.584-1.208A11.945 11.945 0 0012 24c6.627 0 12-5.373 12-12S18.627 0 12 0zm0 22c-2.239 0-4.332-.726-6.033-1.96l-.424-.312-2.715.715.728-2.66-.343-.546A9.935 9.935 0 012 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10z" />
            </svg>
            Chat on WhatsApp
          </a>
        </div>

        <!-- Right: Contact Form -->
        <div class="bg-white rounded-2xl shadow-lg p-6 md:p-8">
          <h3 class="font-display text-pravis-800 text-2xl mb-6">Send a Message</h3>

          <form @submit.prevent="handleSubmit" class="space-y-5">
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label for="firstName" class="block text-sm font-medium text-pravis-700 mb-1">First Name</label>
                <input
                  id="firstName"
                  v-model="form.firstName"
                  type="text"
                  required
                  class="w-full px-4 py-2.5 border border-pravis-200 rounded-lg text-pravis-800 focus:outline-none focus:border-pravis-500 focus:ring-1 focus:ring-pravis-500 transition-colors"
                  placeholder="Your first name"
                />
              </div>
              <div>
                <label for="lastName" class="block text-sm font-medium text-pravis-700 mb-1">Last Name</label>
                <input
                  id="lastName"
                  v-model="form.lastName"
                  type="text"
                  required
                  class="w-full px-4 py-2.5 border border-pravis-200 rounded-lg text-pravis-800 focus:outline-none focus:border-pravis-500 focus:ring-1 focus:ring-pravis-500 transition-colors"
                  placeholder="Your last name"
                />
              </div>
            </div>

            <div>
              <label for="email" class="block text-sm font-medium text-pravis-700 mb-1">Email</label>
              <input
                id="email"
                v-model="form.email"
                type="email"
                required
                class="w-full px-4 py-2.5 border border-pravis-200 rounded-lg text-pravis-800 focus:outline-none focus:border-pravis-500 focus:ring-1 focus:ring-pravis-500 transition-colors"
                placeholder="you@example.com"
              />
            </div>

            <div>
              <label for="subject" class="block text-sm font-medium text-pravis-700 mb-1">Subject</label>
              <input
                id="subject"
                v-model="form.subject"
                type="text"
                required
                class="w-full px-4 py-2.5 border border-pravis-200 rounded-lg text-pravis-800 focus:outline-none focus:border-pravis-500 focus:ring-1 focus:ring-pravis-500 transition-colors"
                placeholder="How can we help?"
              />
            </div>

            <div>
              <label for="message" class="block text-sm font-medium text-pravis-700 mb-1">Message</label>
              <textarea
                id="message"
                v-model="form.message"
                rows="5"
                required
                class="w-full px-4 py-2.5 border border-pravis-200 rounded-lg text-pravis-800 focus:outline-none focus:border-pravis-500 focus:ring-1 focus:ring-pravis-500 transition-colors resize-none"
                placeholder="Tell us more..."
              ></textarea>
            </div>

            <button
              type="submit"
              class="w-full px-6 py-3 bg-pravis-500 hover:bg-pravis-600 text-white rounded-lg font-semibold transition-colors"
            >
              Send Message
            </button>

            <p v-if="submitted" class="text-green-600 text-sm text-center font-medium">
              Thank you! We'll get back to you soon.
            </p>
          </form>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
useHead({
  title: 'Contact Us — Pravis Boutique',
})

const form = reactive({
  firstName: '',
  lastName: '',
  email: '',
  subject: '',
  message: '',
})

const submitted = ref(false)

function handleSubmit() {
  // Placeholder — no backend yet
  submitted.value = true
  setTimeout(() => {
    submitted.value = false
  }, 4000)
  form.firstName = ''
  form.lastName = ''
  form.email = ''
  form.subject = ''
  form.message = ''
}
</script>
