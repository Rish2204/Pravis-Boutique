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
        
        <!-- Privacy Controls Component -->
        <PrivacyControls />
      </div>
      
      <div class="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6">
        <h2 class="text-2xl font-semibold mb-6 text-gray-800 dark:text-white">
          Voice Assistant Privacy
        </h2>
        
        <div class="mb-6">
          <p class="text-gray-700 dark:text-gray-300 mb-4">
            Our "Ask Pravi" voice assistant helps you shop and find products with voice commands.
            Control how your voice data is processed below.
          </p>
        </div>
        
        <div class="space-y-6">
          <!-- Voice Data Storage -->
          <div class="flex items-center justify-between">
            <div>
              <h3 class="text-lg font-medium text-gray-800 dark:text-white">Voice Data Storage</h3>
              <p class="text-sm text-gray-600 dark:text-gray-400">
                Store voice transcripts to improve voice recognition
              </p>
            </div>
            <label class="toggle-switch">
              <input 
                type="checkbox" 
                v-model="voiceDataStorage"
                @change="updateVoiceSettings"
              />
              <span class="toggle-slider"></span>
            </label>
          </div>
          
          <!-- Voice Recognition Training -->
          <div class="flex items-center justify-between">
            <div>
              <h3 class="text-lg font-medium text-gray-800 dark:text-white">Voice Recognition Training</h3>
              <p class="text-sm text-gray-600 dark:text-gray-400">
                Help improve our voice recognition with your voice data
              </p>
            </div>
            <label class="toggle-switch">
              <input 
                type="checkbox" 
                v-model="voiceTraining"
                @change="updateVoiceSettings"
              />
              <span class="toggle-slider"></span>
            </label>
          </div>
          
          <!-- Clear Voice History -->
          <div class="mt-8 pt-6 border-t border-gray-200 dark:border-gray-700">
            <button 
              @click="clearVoiceHistory"
              class="bg-red-600 hover:bg-red-700 text-white px-4 py-2 rounded-md"
            >
              Clear Voice History
            </button>
            <p class="text-sm text-gray-600 dark:text-gray-400 mt-2">
              Permanently delete all stored voice data and transcripts
            </p>
          </div>
        </div>
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

<script setup>
import { ref } from 'vue';
import PrivacyControls from '@/components/common/PrivacyControls.vue';
import { useVoiceStore } from '~/store/voice';

// Set page metadata
useHead({
  title: 'Privacy Settings - Pravis Boutique',
  meta: [
    { name: 'description', content: 'Manage your privacy settings and data preferences' }
  ]
});

// Voice privacy settings
const voiceStore = useVoiceStore();
const voiceDataStorage = ref(localStorage.getItem('voice-data-storage') === 'true');
const voiceTraining = ref(localStorage.getItem('voice-training') === 'true');

// Update voice settings
const updateVoiceSettings = () => {
  localStorage.setItem('voice-data-storage', voiceDataStorage.value);
  localStorage.setItem('voice-training', voiceTraining.value);
  
  // Update any voice store settings if needed
  // voiceStore.updatePrivacySettings({
  //   dataStorage: voiceDataStorage.value,
  //   trainingEnabled: voiceTraining.value
  // });
};

// Clear voice history
const clearVoiceHistory = async () => {
  if (confirm('Are you sure you want to clear all your voice history? This cannot be undone.')) {
    try {
      // Call API to delete voice history
      await fetch('/api/voice/clear-history', {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          // Include any necessary identification info
        })
      });
      
      alert('Voice history has been cleared successfully.');
    } catch (error) {
      console.error('Error clearing voice history:', error);
      alert('An error occurred while clearing your voice history. Please try again.');
    }
  }
};

// Go back function
const goBack = () => {
  navigateTo('/account');
};
</script>

<style scoped>
.toggle-switch {
  position: relative;
  display: inline-block;
  width: 60px;
  height: 34px;
}

.toggle-switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.toggle-slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  transition: .4s;
  border-radius: 34px;
}

.toggle-slider:before {
  position: absolute;
  content: "";
  height: 26px;
  width: 26px;
  left: 4px;
  bottom: 4px;
  background-color: white;
  transition: .4s;
  border-radius: 50%;
}

input:checked + .toggle-slider {
  background-color: #3498db;
}

input:checked + .toggle-slider:before {
  transform: translateX(26px);
}
</style>
