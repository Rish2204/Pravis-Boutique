<template>
  <Transition name="fade">
    <div 
      v-if="showModal" 
      class="fixed inset-0 bg-black bg-opacity-50 z-50 flex items-center justify-center p-4"
      @click.self="$emit('close')"
    >
      <div class="bg-white rounded-2xl max-w-md w-full p-6 shadow-2xl">
        <div class="text-center">
          <div class="w-16 h-16 bg-pravis-600 rounded-full flex items-center justify-center mx-auto mb-4 voice-pulse">
            <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z"></path>
            </svg>
          </div>
          <h3 class="text-xl font-display font-semibold text-pravis-800 mb-2">Hi! I'm Pravi</h3>
          <p class="text-gray-600 mb-6">Your AI shopping assistant. Ask me about our handloom collection, sizing, or styling advice!</p>
          
          <div class="space-y-3 mb-6">
            <button 
              v-for="suggestion in suggestions" 
              :key="suggestion"
              @click="askQuestion(suggestion)"
              class="w-full text-left p-3 bg-pravis-50 rounded-lg hover:bg-pravis-100 transition-colors"
            >
              "{{ suggestion }}"
            </button>
          </div>
          
          <!-- Response area -->
          <div v-if="response" class="mb-4 p-4 bg-gray-50 rounded-lg text-left">
            <p class="text-sm text-gray-700">{{ response }}</p>
          </div>
          
          <div class="flex gap-3">
            <button 
              @click="startVoiceRecording" 
              :disabled="isRecording"
              class="flex-1 bg-pravis-600 text-white px-4 py-2 rounded-lg font-medium hover:bg-pravis-700 transition-colors disabled:opacity-50"
            >
              {{ isRecording ? '🔴 Recording...' : '🎤 Speak' }}
            </button>
            <button 
              @click="$emit('close')" 
              class="flex-1 border border-gray-300 text-gray-700 px-4 py-2 rounded-lg font-medium hover:bg-gray-50 transition-colors"
            >
              Close
            </button>
          </div>
        </div>
      </div>
    </div>
  </Transition>
</template>

<script setup>
import { ref } from 'vue'

defineProps({
  showModal: {
    type: Boolean,
    default: false
  }
})

defineEmits(['close'])

const isRecording = ref(false)
const response = ref('')

const suggestions = [
  'Tell me about silk sarees',
  'What sizes do you have?',
  'Help me choose a wedding saree'
]

const askQuestion = (question) => {
  // Simulate AI response
  response.value = `Great question about "${question}"! For detailed assistance, please contact us via WhatsApp at +91 6300208234. Our team will be happy to help you with personalized recommendations.`
}

const startVoiceRecording = () => {
  // Check if browser supports speech recognition
  if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition
    const recognition = new SpeechRecognition()
    
    recognition.continuous = false
    recognition.interimResults = false
    recognition.lang = 'en-US'
    
    recognition.onstart = () => {
      isRecording.value = true
    }
    
    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript
      askQuestion(transcript)
      isRecording.value = false
    }
    
    recognition.onerror = (event) => {
      console.error('Speech recognition error:', event.error)
      response.value = "Sorry, I couldn't hear you clearly. Please try again or use the text options."
      isRecording.value = false
    }
    
    recognition.onend = () => {
      isRecording.value = false
    }
    
    recognition.start()
  } else {
    response.value = 'Voice recognition is not supported in your browser. Please use the text options or contact us directly.'
  }
}
</script>

<style scoped>
.voice-pulse {
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>