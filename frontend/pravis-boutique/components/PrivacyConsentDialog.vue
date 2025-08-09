<template>
  <Transition name="slide-in">
    <div 
      v-if="showDialog" 
      class="fixed inset-0 bg-black bg-opacity-50 z-50 flex items-center justify-center p-4"
    >
      <div class="bg-white rounded-2xl max-w-md w-full p-6 shadow-2xl">
        <div class="flex items-center mb-4">
          <svg class="w-6 h-6 text-handloom-sage mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path>
          </svg>
          <h3 class="text-lg font-semibold text-handloom-deep">Privacy First Analytics</h3>
        </div>
        <p class="text-gray-600 mb-6 text-sm leading-relaxed">
          We use privacy-first analytics to improve your shopping experience. Your data stays anonymous and is never shared with third parties.
        </p>
        <div class="flex flex-col sm:flex-row gap-3">
          <button 
            @click="acceptAnalytics" 
            class="flex-1 bg-handloom-sage text-white px-4 py-2 rounded-lg font-medium hover:bg-opacity-90 transition-colors"
          >
            Accept Analytics
          </button>
          <button 
            @click="declineAnalytics" 
            class="flex-1 border border-gray-300 text-gray-700 px-4 py-2 rounded-lg font-medium hover:bg-gray-50 transition-colors"
          >
            Essential Only
          </button>
        </div>
      </div>
    </div>
  </Transition>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const showDialog = ref(false)

const acceptAnalytics = () => {
  localStorage.setItem('analyticsConsent', 'accepted')
  showDialog.value = false
  // Initialize analytics here
  console.log('Analytics initialized')
}

const declineAnalytics = () => {
  localStorage.setItem('analyticsConsent', 'declined')
  showDialog.value = false
  console.log('Analytics declined')
}

onMounted(() => {
  // Check if user has already made a choice
  if (!localStorage.getItem('analyticsConsent')) {
    // Show dialog after a short delay for better UX
    setTimeout(() => {
      showDialog.value = true
    }, 1000)
  }
})
</script>

<style scoped>
.slide-in-enter-active,
.slide-in-leave-active {
  transition: all 0.5s ease-out;
}

.slide-in-enter-from {
  transform: translateY(100%);
  opacity: 0;
}

.slide-in-enter-to {
  transform: translateY(0);
  opacity: 1;
}

.slide-in-leave-from {
  transform: translateY(0);
  opacity: 1;
}

.slide-in-leave-to {
  transform: translateY(100%);
  opacity: 0;
}
</style>