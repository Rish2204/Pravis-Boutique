<template>
  <!-- Contact Us box to be displayed on the home page -->
  <div class="bg-white dark:bg-gray-800 rounded-2xl shadow-xl p-8 max-w-3xl mx-auto">
    <h2 class="text-3xl font-bold text-pravis-700 dark:text-pravis-300 mb-4 text-center">
      Contact Us
    </h2>
    <p class="text-gray-700 dark:text-gray-300 text-center mb-6">
      Have questions about our handloom collections or need help placing an order?  We’re here to assist you.
    </p>
    <div class="flex flex-col sm:flex-row justify-around items-start sm:items-center gap-6 mb-6">
      <!-- Phone Information -->
      <div class="flex items-start">
        <div class="mr-4 mt-1">
          <svg class="w-6 h-6 text-pravis-600 dark:text-pravis-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
          </svg>
        </div>
        <div>
          <h3 class="text-lg font-medium text-gray-900 dark:text-white">Phone</h3>
          <p class="text-gray-600 dark:text-gray-300">+91 63002 08234</p>
          <p class="text-sm text-gray-500 dark:text-gray-400">Mon–Sat 9:00 AM – 6:00 PM IST</p>
        </div>
      </div>
      <!-- Email Information -->
      <div class="flex items-start">
        <div class="mr-4 mt-1">
          <svg class="w-6 h-6 text-pravis-600 dark:text-pravis-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
          </svg>
        </div>
        <div>
          <h3 class="text-lg font-medium text-gray-900 dark:text-white">Email</h3>
          <p class="text-gray-600 dark:text-gray-300">info@pravishandlooms.com</p>
          <p class="text-gray-600 dark:text-gray-300">orders@pravishandlooms.com</p>
        </div>
      </div>
    </div>
    <!-- Call to Action -->
    <div class="text-center">
      <nuxt-link to="/contact" class="inline-flex items-center bg-pravis-600 hover:bg-pravis-700 text-white font-semibold px-6 py-3 rounded-lg transition-colors">
        Send Us a Message
      </nuxt-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ContactUsBox',
};
</script>

<style scoped>
/* Styles specific to the Contact Us box can be extended here if needed */
</style>
