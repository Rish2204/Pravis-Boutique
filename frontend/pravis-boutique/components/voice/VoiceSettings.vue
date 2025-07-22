<template>
  <div class="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6 max-w-lg mx-auto">
    <h2 class="text-xl font-semibold text-gray-900 dark:text-gray-100 mb-4">Voice Assistant Settings</h2>
    
    <!-- Voice Assistant Toggle -->
    <div class="flex items-center justify-between mb-6">
      <div>
        <h3 class="text-lg font-medium text-gray-900 dark:text-gray-100">Voice Assistant</h3>
        <p class="text-sm text-gray-500 dark:text-gray-400">Enable or disable voice commands</p>
      </div>
      <label class="relative inline-flex items-center cursor-pointer">
        <input 
          type="checkbox" 
          v-model="voiceEnabled" 
          class="sr-only peer"
          @change="updateVoiceEnabled"
        >
        <div class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-pravis-300 dark:peer-focus:ring-pravis-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-pravis-600"></div>
      </label>
    </div>
    
    <!-- Voice Recognition Method -->
    <div class="mb-6">
      <h3 class="text-lg font-medium text-gray-900 dark:text-gray-100 mb-2">Recognition Method</h3>
      <div class="space-y-2">
        <label class="flex items-center">
          <input 
            type="radio" 
            name="recognition-method" 
            value="browser" 
            v-model="recognitionMethod"
            class="w-4 h-4 text-pravis-600 focus:ring-pravis-500"
            @change="updateRecognitionMethod"
          >
          <span class="ml-2 text-gray-700 dark:text-gray-300">Browser (Web Speech API)</span>
        </label>
        <p v-if="recognitionMethod === 'browser'" class="ml-6 text-xs text-gray-500 dark:text-gray-400">
          Uses your browser's built-in speech recognition. Fast but may be less accurate.
        </p>
        
        <label class="flex items-center">
          <input 
            type="radio" 
            name="recognition-method" 
            value="server" 
            v-model="recognitionMethod"
            class="w-4 h-4 text-pravis-600 focus:ring-pravis-500"
            @change="updateRecognitionMethod"
          >
          <span class="ml-2 text-gray-700 dark:text-gray-300">Server (OpenAI Whisper)</span>
        </label>
        <p v-if="recognitionMethod === 'server'" class="ml-6 text-xs text-gray-500 dark:text-gray-400">
          Uses OpenAI's advanced speech recognition. More accurate but requires internet connection.
        </p>
      </div>
    </div>
    
    <!-- Voice Selection -->
    <div class="mb-6">
      <h3 class="text-lg font-medium text-gray-900 dark:text-gray-100 mb-2">Assistant Voice</h3>
      <select 
        v-model="selectedVoice" 
        class="block w-full mt-1 rounded-md bg-gray-100 dark:bg-gray-700 border-transparent focus:border-pravis-500 focus:bg-white dark:focus:bg-gray-800 focus:ring-0 text-gray-900 dark:text-gray-100"
        @change="updateVoice"
      >
        <option 
          v-for="voice in availableVoices" 
          :key="voice.id" 
          :value="voice.id"
        >
          {{ voice.name }} ({{ voice.gender }})
        </option>
      </select>
      <p class="mt-1 text-xs text-gray-500 dark:text-gray-400">
        Select the voice for your assistant
      </p>
    </div>
    
    <!-- Test Voice -->
    <div class="mb-6">
      <h3 class="text-lg font-medium text-gray-900 dark:text-gray-100 mb-2">Test Assistant Voice</h3>
      <div class="flex">
        <input 
          type="text" 
          v-model="testText"
          placeholder="Enter text to test voice..." 
          class="flex-1 rounded-l-md bg-gray-100 dark:bg-gray-700 border-transparent focus:border-pravis-500 focus:bg-white dark:focus:bg-gray-800 focus:ring-0 text-gray-900 dark:text-gray-100"
        />
        <button 
          @click="testVoice"
          class="px-4 py-2 bg-pravis-600 text-white rounded-r-md hover:bg-pravis-700 focus:outline-none focus:ring-2 focus:ring-pravis-500 focus:ring-offset-2"
          :disabled="isSpeaking || !testText"
        >
          <span v-if="!isSpeaking">Test</span>
          <span v-else>Speaking...</span>
        </button>
      </div>
    </div>
    
    <!-- Privacy Information -->
    <div class="bg-gray-50 dark:bg-gray-900 p-4 rounded-md mb-6">
      <h3 class="text-lg font-medium text-gray-900 dark:text-gray-100 mb-2">Privacy Information</h3>
      <p class="text-sm text-gray-600 dark:text-gray-400 mb-2">
        Your voice data is processed according to our privacy policy:
      </p>
      <ul class="list-disc list-inside text-sm text-gray-600 dark:text-gray-400 space-y-1 ml-2">
        <li>Browser processing happens entirely on your device</li>
        <li>Server processing sends audio to our secure servers</li>
        <li>Audio files are deleted after processing</li>
        <li>Voice commands may be stored for service improvement</li>
      </ul>
    </div>
    
    <!-- Clear Voice History -->
    <button 
      @click="clearVoiceHistory"
      class="w-full px-4 py-2 bg-red-600 text-white rounded-md hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2"
    >
      Clear Voice History
    </button>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useVoiceAgent } from '~/composables/useVoiceAgent'
import { useVoiceStore } from '~/store/voice'

// Setup voice agent
const {
  isSpeaking,
  isInitialized,
  useBackend,
  voicePreference,
  speak,
  stopSpeaking,
  toggleBackend,
  setVoice
} = useVoiceAgent()

// UI state
const voiceEnabled = ref(false)
const recognitionMethod = ref('browser')
const selectedVoice = ref('nova')
const testText = ref('Hello, I am your Pravis Boutique assistant!')
const availableVoices = ref([
  { id: 'alloy', name: 'Alloy', gender: 'Neutral' },
  { id: 'echo', name: 'Echo', gender: 'Male' },
  { id: 'fable', name: 'Fable', gender: 'Female' },
  { id: 'onyx', name: 'Onyx', gender: 'Male' },
  { id: 'nova', name: 'Nova', gender: 'Female' },
  { id: 'shimmer', name: 'Shimmer', gender: 'Female' }
])

// Get store for saving preferences
const voiceStore = useVoiceStore()

// Initialize component
onMounted(() => {
  voiceEnabled.value = voiceStore.isEnabled
  recognitionMethod.value = useBackend.value ? 'server' : 'browser'
  selectedVoice.value = voicePreference.value
  
  // Load server-side voice options if server method is selected
  if (recognitionMethod.value === 'server') {
    loadServerVoices()
  }
})

// Update voice enabled state
const updateVoiceEnabled = () => {
  voiceStore.setEnabled(voiceEnabled.value)
}

// Update recognition method
const updateRecognitionMethod = () => {
  const useServerMethod = recognitionMethod.value === 'server'
  toggleBackend(useServerMethod)
  
  // Load server voices if server method is selected
  if (useServerMethod) {
    loadServerVoices()
  }
}

// Update voice preference
const updateVoice = () => {
  setVoice(selectedVoice.value)
}

// Test the selected voice
const testVoice = async () => {
  if (!testText.value || isSpeaking.value) return
  
  await speak(testText.value, {
    voice: selectedVoice.value
  })
}

// Load available voices from server
const loadServerVoices = async () => {
  try {
    const response = await fetch('/api/v1/voice/voices')
    
    if (response.ok) {
      const data = await response.json()
      if (data.voices && Array.isArray(data.voices)) {
        availableVoices.value = data.voices
      }
    }
  } catch (error) {
    console.error('Failed to load server voices:', error)
  }
}

// Clear voice history
const clearVoiceHistory = async () => {
  try {
    const { useApi } = useNuxtApp()
    const { del } = useApi()
    
    await del('/voice/clear-history')
    
    // Show success message
    alert('Voice history has been cleared')
  } catch (error) {
    console.error('Failed to clear voice history:', error)
    alert('Failed to clear voice history')
  }
}
</script>
