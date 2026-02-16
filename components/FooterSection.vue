<template>
  <footer id="contact" class="bg-pravis-900 text-white py-16">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid md:grid-cols-4 gap-8 mb-12">
        <!-- Brand -->
        <div class="space-y-4">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10">
              <svg viewBox="0 0 100 100" class="w-full h-full">
                <defs>
                  <linearGradient id="footerLogo" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" style="stop-color:#D4AF37" />
                    <stop offset="100%" style="stop-color:#B8860B" />
                  </linearGradient>
                </defs>
                <path d="M20 20 L20 80 L35 80 L35 55 L50 55 Q70 55 70 37.5 Q70 20 50 20 Z" fill="url(#footerLogo)" />
                <path d="M35 35 L50 35 Q55 35 55 37.5 Q55 40 50 40 L35 40 Z" fill="#F4F3EE" />
                <circle cx="75" cy="25" r="3" fill="#D4AF37" />
                <circle cx="80" cy="35" r="2" fill="#D4AF37" />
              </svg>
            </div>
            <div>
              <h4 class="font-display font-bold text-lg">Pravis Boutique</h4>
              <p class="text-pravis-300 text-sm">Drape in Elegance</p>
            </div>
          </div>
          <p class="text-gray-300 text-sm leading-relaxed">
            Authentic handloom textiles celebrating India's rich heritage of craftsmanship and artistry.
          </p>
          
          <!-- Social Media -->
          <div class="flex space-x-4 pt-4">
            <a 
              v-for="social in socialLinks" 
              :key="social.name"
              :href="social.url" 
              target="_blank"
              rel="noopener noreferrer"
              class="w-10 h-10 bg-pravis-600 rounded-full flex items-center justify-center hover:bg-pravis-700 transition-colors"
            >
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                <path :d="social.icon" />
              </svg>
            </a>
          </div>
        </div>
        
        <!-- Quick Links -->
        <div>
          <h5 class="font-semibold mb-6 text-pravis-300">Quick Links</h5>
          <ul class="space-y-3 text-sm">
            <li v-for="link in quickLinks" :key="link.text">
              <a :href="link.href" class="text-gray-300 hover:text-pravis-300 transition-colors">
                {{ link.text }}
              </a>
            </li>
          </ul>
        </div>
        
        <!-- Contact Info -->
        <div>
          <h5 class="font-semibold mb-6 text-pravis-300">Contact Us</h5>
          <div class="space-y-3 text-sm text-gray-300">
            <div class="flex items-center space-x-3">
              <svg class="w-4 h-4 text-pravis-300 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path>
              </svg>
              <span>+91 6300208234</span>
            </div>
            <div class="flex items-center space-x-3">
              <svg class="w-4 h-4 text-pravis-300 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
              </svg>
              <span>hello@pravisboutique.com</span>
            </div>
            <div class="flex items-start space-x-3">
              <svg class="w-4 h-4 text-pravis-300 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
              </svg>
              <span>Hyderabad, Telangana<br>India</span>
            </div>
          </div>
        </div>
        
        <!-- Newsletter -->
        <div>
          <h5 class="font-semibold mb-6 text-pravis-300">Stay Updated</h5>
          <p class="text-sm text-gray-300 mb-4">Subscribe to get updates on new collections and exclusive offers.</p>
          <form @submit.prevent="handleSubscribe" class="space-y-3">
            <input 
              v-model="email"
              type="email" 
              placeholder="Enter your email" 
              required
              class="w-full px-4 py-2 bg-white bg-opacity-10 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:border-pravis-300 transition-colors"
            >
            <button 
              type="submit" 
              class="w-full bg-pravis-600 text-white py-2 rounded-lg font-medium hover:bg-pravis-700 transition-colors"
            >
              Subscribe
            </button>
          </form>
        </div>
      </div>
      
      <!-- Bottom Bar -->
      <div class="border-t border-gray-600 pt-8 flex flex-col md:flex-row justify-between items-center">
        <p class="text-sm text-gray-400 mb-4 md:mb-0">
          © 2024 Pravis Boutique. All rights reserved. | Handcrafted with ❤️ for textile lovers
        </p>
        <div class="flex space-x-6 text-sm text-gray-400">
          <a href="/privacy" class="hover:text-pravis-300 transition-colors">Privacy Policy</a>
          <a href="/terms" class="hover:text-pravis-300 transition-colors">Terms of Service</a>
          <a href="#" class="hover:text-pravis-300 transition-colors">Shipping Policy</a>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { ref } from 'vue'

const email = ref('')

const socialLinks = [
  {
    name: 'Twitter',
    url: '#',
    icon: 'M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z'
  },
  {
    name: 'Pinterest',
    url: '#',
    icon: 'M12.017 0C5.396 0 .029 5.367.029 11.987c0 5.079 3.158 9.417 7.618 11.174-.105-.949-.199-2.403.041-3.439.219-.937 1.406-5.957 1.406-5.957s-.359-.72-.359-1.781c0-1.663.967-2.911 2.168-2.911 1.024 0 1.518.769 1.518 1.688 0 1.029-.653 2.567-.992 3.992-.285 1.193.6 2.165 1.775 2.165 2.128 0 3.768-2.245 3.768-5.487 0-2.861-2.063-4.869-5.008-4.869-3.41 0-5.409 2.562-5.409 5.199 0 1.033.394 2.143.889 2.741.099.12.112.225.085.345-.09.375-.293 1.199-.334 1.363-.053.225-.172.271-.402.165-1.495-.69-2.433-2.878-2.433-4.646 0-3.776 2.748-7.252 7.92-7.252 4.158 0 7.392 2.967 7.392 6.923 0 4.135-2.607 7.462-6.233 7.462-1.214 0-2.357-.629-2.75-1.378l-.748 2.853c-.271 1.043-1.002 2.35-1.492 3.146C9.57 23.812 10.763 24.009 12.017 24.009c6.624 0 11.99-5.367 11.99-11.988C24.007 5.367 18.641.001.012.001z'
  },
  {
    name: 'Instagram',
    url: 'https://www.instagram.com/pravis.handlooms/?hl=en',
    icon: 'M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z'
  }
]

const quickLinks = [
  { text: 'Shop Collection', href: '/shop' },
  { text: 'Our Story', href: '#about' },
  { text: 'Size Guide', href: '#' },
  { text: 'Care Instructions', href: '#' },
  { text: 'Return Policy', href: '#' }
]

const handleSubscribe = () => {
  if (email.value) {
    alert('Thank you for subscribing! You\'ll receive updates about our latest collections.')
    email.value = ''
  }
}
</script>

<style scoped>
/* Component specific styles if needed */
</style>