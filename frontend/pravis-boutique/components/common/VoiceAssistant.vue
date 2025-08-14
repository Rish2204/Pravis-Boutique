<template>
  <div class="voice-assistant">
    <!-- Voice Assistant Button -->
    <button 
      @click="toggleVoiceAssistant"
      class="voice-btn bg-pravis-500 hover:bg-pravis-600 text-white p-3 rounded-full shadow-lg transition-all duration-200"
      :class="{ 
        'animate-pulse': voiceStore.isListening, 
        'opacity-50 cursor-not-allowed': !voiceStore.canUseVoice 
      }"
      :disabled="!voiceStore.canUseVoice"
      title="Voice Assistant"
    >
      <svg v-if="!voiceStore.isListening" class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
        <path fill-rule="evenodd" d="M7 4a3 3 0 016 0v4a3 3 0 11-6 0V4zm4 10.93A7.001 7.001 0 0017 8a1 1 0 10-2 0A5 5 0 015 8a1 1 0 00-2 0 7.001 7.001 0 006 6.93V17H6a1 1 0 100 2h8a1 1 0 100-2h-3v-2.07z" clip-rule="evenodd"></path>
      </svg>
      
      <svg v-else class="w-6 h-6 animate-spin" fill="currentColor" viewBox="0 0 20 20">
        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-12a1 1 0 10-2 0v4a1 1 0 00.293.707l2.828 2.829a1 1 0 101.415-1.415L11 9.586V6z" clip-rule="evenodd"></path>
      </svg>
    </button>

    <!-- Voice Assistant Panel -->
    <Transition name="voice-panel">
      <div v-if="showPanel" class="voice-panel mt-4 p-4 bg-white dark:bg-gray-800 rounded-lg shadow-xl border">
        <div class="mb-3">
          <h3 class="font-semibold text-gray-900 dark:text-white mb-2">Ask Pravi</h3>
          
          <!-- Status -->
          <div class="text-sm text-gray-600 dark:text-gray-400 mb-2">
            <span v-if="voiceStore.isListening" class="text-blue-600">🎤 Listening...</span>
            <span v-else-if="voiceStore.isLoading" class="text-yellow-600">💭 Thinking...</span>
            <span v-else class="text-green-600">💬 Ready to help</span>
          </div>

          <!-- Error Display -->
          <div v-if="voiceStore.error" class="text-red-600 text-sm mb-2 p-2 bg-red-50 dark:bg-red-900/20 rounded">
            {{ voiceStore.error }}
            <button @click="voiceStore.clearError" class="ml-2 text-red-800 hover:text-red-900">×</button>
          </div>

          <!-- Last Query & Response -->
          <div v-if="voiceStore.lastQuery" class="space-y-2 text-sm">
            <div class="p-2 bg-blue-50 dark:bg-blue-900/20 rounded">
              <strong>You:</strong> {{ voiceStore.lastQuery }}
            </div>
            <div v-if="voiceStore.lastResponse" class="p-2 bg-green-50 dark:bg-green-900/20 rounded">
              <strong>Pravi:</strong> {{ voiceStore.lastResponse }}
            </div>
          </div>
        </div>

        <!-- Controls -->
        <div class="flex gap-2">
          <button 
            @click="startListening" 
            :disabled="!voiceStore.canUseVoice"
            class="flex-1 px-3 py-2 bg-blue-600 hover:bg-blue-700 disabled:bg-gray-300 text-white text-sm rounded transition-colors"
          >
            {{ voiceStore.isListening ? 'Listening...' : 'Start Listening' }}
          </button>
          
          <button 
            @click="closePanel" 
            class="px-3 py-2 bg-gray-300 hover:bg-gray-400 text-gray-700 text-sm rounded transition-colors"
          >
            Close
          </button>
        </div>

        <!-- Browser Support Info -->
        <div v-if="!voiceStore.isSupported" class="mt-3 text-xs text-gray-500 dark:text-gray-400">
          Voice features require a modern browser with speech recognition support.
        </div>
      </div>
    </Transition>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

// Store
const voiceStore = useVoiceStore()

// Local state
const showPanel = ref(false)

// Methods
const toggleVoiceAssistant = () => {
  showPanel.value = !showPanel.value
}

const startListening = () => {
  voiceStore.startListening()
}

const closePanel = () => {
  showPanel.value = false
  voiceStore.stopListening()
}

// Initialize
onMounted(() => {
  voiceStore.checkSupport()
})
</script>

<style scoped>
.voice-assistant {
  position: relative;
}

.voice-btn {
  position: fixed;
  bottom: 20px;
  right: 20px;
  z-index: 1000;
}

.voice-panel {
  position: fixed;
  bottom: 80px;
  right: 20px;
  width: 320px;
  max-width: calc(100vw - 40px);
  z-index: 1000;
}

/* Transitions */
.voice-panel-enter-active,
.voice-panel-leave-active {
  transition: all 0.3s ease;
}

.voice-panel-enter-from,
.voice-panel-leave-to {
  opacity: 0;
  transform: translateY(20px);
}
</style>