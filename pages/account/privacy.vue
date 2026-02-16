<template>
  <div class="container mx-auto px-4 py-8">
    <div class="max-w-4xl mx-auto">
      <h1 class="text-3xl font-bold mb-8 text-gray-800 dark:text-white">
        Privacy Settings
      </h1>

      <div class="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6 mb-8">
        <h2 class="text-2xl font-semibold mb-6 text-gray-800 dark:text-white">
          Data & Privacy Controls
        </h2>

        <div class="mb-8">
          <p class="text-gray-700 dark:text-gray-300 mb-4">
            Manage how your data is collected and used while shopping at Pravis Boutique.
            You can change these settings at any time.
          </p>
        </div>

        <PrivacyControls />
      </div>

      <div class="mt-8 flex justify-between">
        <button
          @click="goBack"
          class="inline-flex items-center px-4 py-2 bg-gray-200 dark:bg-gray-700 text-gray-800 dark:text-white rounded-md hover:bg-gray-300 dark:hover:bg-gray-600"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M9.707 14.707a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 1.414L7.414 9H15a1 1 0 110 2H7.414l2.293 2.293a1 1 0 010 1.414z" clip-rule="evenodd" />
          </svg>
          Back to Account
        </button>

        <NuxtLink
          to="/privacy"
          class="inline-flex items-center px-4 py-2 bg-pravis-100 dark:bg-pravis-900 text-pravis-800 dark:text-pravis-100 rounded-md hover:bg-pravis-200 dark:hover:bg-pravis-800"
        >
          View Privacy Policy
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-2" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M10.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L12.586 11H5a1 1 0 110-2h7.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
          </svg>
        </NuxtLink>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import PrivacyControls from '@/components/common/PrivacyControls.vue'

useHead({
  title: 'Privacy Settings - Pravis Boutique',
  meta: [
    { name: 'description', content: 'Manage your privacy settings and data preferences' }
  ]
})

const goBack = () => {
  navigateTo('/account')
}
</script>
