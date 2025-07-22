<template>
  <div>
    <!-- Voice assistant floating button -->
    <button 
      @click="toggleVoicePanel"
      class="fixed z-50 bottom-4 right-4 rounded-full bg-pravis-600 text-white p-4 shadow-lg hover:bg-pravis-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-pravis-500 transition-transform"
      :class="{ 'scale-90': isListening }"
      :aria-expanded="isOpen ? 'true' : 'false'"
      :aria-label="isOpen ? 'Close voice assistant' : 'Open voice assistant'"
      aria-haspopup="dialog"
      aria-controls="voice-assistant-panel"
    >
      <span class="sr-only">{{ isOpen ? 'Close voice assistant' : 'Open voice assistant' }}</span>
      <svg 
        v-if="!isOpen" 
        xmlns="http://www.w3.org/2000/svg" 
        class="h-6 w-6" 
        fill="none" 
        viewBox="0 0 24 24" 
        stroke="currentColor"
        aria-hidden="true"
      >
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z" />
      </svg>
      <svg 
        v-else 
        xmlns="http://www.w3.org/2000/svg" 
        class="h-6 w-6" 
        fill="none" 
        viewBox="0 0 24 24" 
        stroke="currentColor"
        aria-hidden="true"
      >
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
      </svg>
      
      <!-- Pulse animation when listening -->
      <span 
        v-if="isListening"
        class="absolute inset-0 rounded-full animate-ping bg-pravis-400 opacity-75"
        aria-hidden="true"
      ></span>
    </button>
    
    <!-- Voice assistant panel -->
    <div 
      v-if="isOpen" 
      id="voice-assistant-panel"
      class="fixed z-40 bottom-20 right-4 w-full max-w-sm bg-white dark:bg-gray-800 rounded-lg shadow-xl overflow-hidden transition-all transform origin-bottom-right"
      role="dialog"
      aria-modal="true"
      aria-labelledby="voice-assistant-title"
    >
      <div class="bg-pravis-600 text-white px-4 py-3 flex justify-between items-center">
        <h3 id="voice-assistant-title" class="text-lg font-medium">Voice Assistant</h3>
        <div class="flex items-center space-x-2">
          <!-- Volume control -->
          <button 
            @click="toggleMute"
            class="p-1 rounded-full hover:bg-pravis-500 focus:outline-none focus:ring-2 focus:ring-white"
            :aria-label="isMuted ? 'Unmute' : 'Mute'"
            :aria-pressed="isMuted ? 'true' : 'false'"
          >
            <span class="sr-only">{{ isMuted ? 'Unmute' : 'Mute' }}</span>
            <svg 
              xmlns="http://www.w3.org/2000/svg" 
              class="h-5 w-5" 
              fill="none" 
              viewBox="0 0 24 24" 
              stroke="currentColor"
              aria-hidden="true"
            >
              <path 
                v-if="!isMuted" 
                stroke-linecap="round" 
                stroke-linejoin="round" 
                stroke-width="2" 
                d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z" 
              />
              <path 
                v-else 
                stroke-linecap="round" 
                stroke-linejoin="round" 
                stroke-width="2" 
                d="M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z M17 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2" 
              />
            </svg>
          </button>
          
          <!-- Close button -->
          <button 
            @click="closeVoicePanel"
            class="p-1 rounded-full hover:bg-pravis-500 focus:outline-none focus:ring-2 focus:ring-white"
            aria-label="Close voice assistant panel"
          >
            <span class="sr-only">Close panel</span>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
      </div>
      
      <!-- Conversation history -->
      <div 
        ref="conversationEl"
        class="px-4 py-3 h-64 overflow-y-auto flex flex-col space-y-4"
        aria-live="polite"
        aria-relevant="additions"
        role="log"
        aria-label="Voice assistant conversation history"
      >
        <!-- Welcome message -->
        <div v-if="conversation.length === 0" class="text-center py-8 text-gray-500 dark:text-gray-400">
          <svg xmlns="http://www.w3.org/2000/svg" class="mx-auto h-12 w-12 text-pravis-300" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z" />
          </svg>
          <p class="mt-2">Ask me anything about our boutique products or how I can help you shop today!</p>
        </div>
        
        <!-- Conversation items -->
        <template v-for="(item, index) in conversation" :key="index">
          <!-- User message -->
          <div v-if="item.type === 'user'" class="flex justify-end">
            <div class="bg-pravis-100 dark:bg-pravis-800 text-pravis-800 dark:text-pravis-100 px-4 py-2 rounded-lg max-w-[75%]">
              {{ item.text }}
            </div>
          </div>
          
          <!-- Assistant message -->
          <div v-else class="flex justify-start">
            <div class="bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-100 px-4 py-2 rounded-lg max-w-[75%]">
              {{ item.text }}
            </div>
          </div>
        </template>
        
        <!-- Loading indicator -->
        <div v-if="isProcessing" class="flex justify-start">
          <div class="bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-100 px-4 py-2 rounded-lg">
            <div class="flex space-x-1">
              <div class="w-2 h-2 rounded-full bg-gray-400 dark:bg-gray-500 animate-bounce"></div>
              <div class="w-2 h-2 rounded-full bg-gray-400 dark:bg-gray-500 animate-bounce" style="animation-delay: 0.2s"></div>
              <div class="w-2 h-2 rounded-full bg-gray-400 dark:bg-gray-500 animate-bounce" style="animation-delay: 0.4s"></div>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Voice input area -->
      <div class="px-4 py-3 bg-gray-50 dark:bg-gray-900 border-t border-gray-200 dark:border-gray-700">
        <div class="flex items-center">
          <!-- Voice input button -->
          <button 
            @click="toggleListening"
            class="flex-shrink-0 inline-flex items-center justify-center p-2 rounded-full focus:outline-none focus:ring-2 focus:ring-pravis-500"
            :class="isListening ? 'bg-red-100 text-red-600 dark:bg-red-900 dark:text-red-400' : 'bg-pravis-100 text-pravis-600 dark:bg-pravis-900 dark:text-pravis-400'"
            :aria-label="isListening ? 'Stop listening' : 'Start listening'"
            :aria-pressed="isListening ? 'true' : 'false'"
          >
            <span class="sr-only">{{ isListening ? 'Stop listening' : 'Start listening' }}</span>
            <svg 
              xmlns="http://www.w3.org/2000/svg" 
              class="h-6 w-6" 
              fill="none" 
              viewBox="0 0 24 24" 
              stroke="currentColor"
              aria-hidden="true"
            >
              <path 
                v-if="!isListening"
                stroke-linecap="round" 
                stroke-linejoin="round" 
                stroke-width="2" 
                d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z" 
              />
              <path 
                v-else
                stroke-linecap="round" 
                stroke-linejoin="round" 
                stroke-width="2" 
                d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z M9 10a1 1 0 011-1h4a1 1 0 011 1v4a1 1 0 01-1 1h-4a1 1 0 01-1-1v-4z" 
              />
            </svg>
          </button>
          
          <!-- Text input -->
          <input
            v-model="textInput"
            type="text"
            placeholder="Type a message or press the mic to speak..."
            class="flex-1 ml-3 block w-full px-3 py-2 bg-white dark:bg-gray-800 border border-gray-300 dark:border-gray-700 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-pravis-500 focus:border-pravis-500"
            @keyup.enter="sendTextMessage"
            aria-label="Message input"
            role="textbox"
            aria-multiline="false"
          >
          
          <!-- Send button -->
          <button 
            @click="sendTextMessage"
            class="ml-3 flex-shrink-0 inline-flex items-center justify-center p-2 rounded-full bg-pravis-100 text-pravis-600 dark:bg-pravis-900 dark:text-pravis-400 focus:outline-none focus:ring-2 focus:ring-pravis-500"
            :disabled="!textInput.trim()"
            aria-label="Send message"
          >
            <span class="sr-only">Send message</span>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
              <path d="M10.894 2.553a1 1 0 00-1.788 0l-7 14a1 1 0 001.169 1.409l5-1.429A1 1 0 009 15.571V11a1 1 0 112 0v4.571a1 1 0 00.725.962l5 1.428a1 1 0 001.17-1.408l-7-14z" />
            </svg>
          </button>
        </div>
        
        <!-- Transcript display -->
        <div v-if="isListening && transcript" class="mt-2 text-sm text-gray-500 dark:text-gray-400">
          <p class="italic">{{ transcript }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, computed, onMounted, nextTick } from 'vue'
import { useVoiceStore } from '~/store/voice'
import { useAnalyticsStore } from '~/store/analytics'

// Props
const props = defineProps({
  initialOpen: {
    type: Boolean,
    default: false
  }
})

// Refs
const isOpen = ref(props.initialOpen)
const textInput = ref('')
const conversation = ref([])
const isProcessing = ref(false)
const conversationEl = ref(null)

// Voice store
const voiceStore = useVoiceStore()
const { isListening, transcript, isMuted } = storeToRefs(voiceStore)

// Analytics store
const analyticsStore = useAnalyticsStore()
const hasConsent = computed(() => analyticsStore.hasConsent)

// Computed properties
const voiceSupported = computed(() => voiceStore.isReady)

// Methods
const toggleVoicePanel = () => {
  isOpen.value = !isOpen.value
  if (!isOpen.value && isListening.value) {
    voiceStore.stopListening()
  }
}

const closeVoicePanel = () => {
  isOpen.value = false
  if (isListening.value) {
    voiceStore.stopListening()
  }
}

const toggleListening = async () => {
  if (isListening.value) {
    voiceStore.stopListening()
  } else {
    // Check for analytics consent before enabling voice
    if (!hasConsent.value) {
      // Show consent dialog first
      const consentDialog = document.createElement('div')
      document.body.appendChild(consentDialog)
      
      // Use Vue to render the dialog
      const { createApp, defineAsyncComponent } = await import('vue')
      const app = createApp({
        template: '<ConsentDialog @consentDecision="onDecision" />',
        components: {
          ConsentDialog: defineAsyncComponent(() => import('@/components/common/ConsentDialog.vue'))
        },
        setup() {
          const onDecision = (decision) => {
            // Clean up the dialog
            document.body.removeChild(consentDialog)
            app.unmount()
            
            // If consent given, start listening
            if (decision.consent) {
              voiceStore.startListening()
            }
          }
          
          return { onDecision }
        }
      }).mount(consentDialog)
    } else {
      // Consent already given, start listening
      voiceStore.startListening()
    }
  }
}

const toggleMute = () => {
  voiceStore.setMuted(!isMuted.value)
}

const sendTextMessage = async () => {
  if (!textInput.value.trim()) return
  
  // Play audio feedback
  playAudioFeedback('click')
  
  // Add user message to conversation
  conversation.value.push({
    type: 'user',
    text: textInput.value,
    timestamp: new Date()
  })
  
  // Process message
  isProcessing.value = true
  
  try {
    // Process command as if it were a voice command
    const response = await voiceStore.processCommand(textInput.value)
    
    // Add assistant response to conversation
    if (response && response.text) {
      conversation.value.push({
        type: 'assistant',
        text: response.text,
        timestamp: new Date()
      })
      
      // Announce assistant response to screen reader
      announceToScreenReader(`Assistant says: ${response.text}`, 'polite')
      
      // Play audio feedback for response
      playAudioFeedback('notification')
    }
  } catch (error) {
    // Add error message to conversation
    conversation.value.push({
      type: 'assistant',
      text: 'Sorry, I encountered an error processing your request.',
      error: true,
      timestamp: new Date()
    })
    
    // Announce error to screen reader
    announceToScreenReader('Sorry, I encountered an error processing your request.', 'assertive')
    
    // Play error sound
    playAudioFeedback('error')
  } finally {
    isProcessing.value = false
    textInput.value = '' // Clear input
    
    // Scroll conversation to bottom
    await nextTick()
    scrollToBottom()
  }
}

// Import accessibility utilities
import { announceToScreenReader, createFocusTrap, playAudioFeedback } from '~/utils/accessibility'

// Focus trap for the voice panel
const focusTrap = ref(null)

// Watch for isOpen changes to manage focus trap
watch(isOpen, (newValue) => {
  if (newValue) {
    // Initialize focus trap when panel opens
    nextTick(() => {
      const panel = document.getElementById('voice-assistant-panel')
      if (panel) {
        focusTrap.value = createFocusTrap(panel)
        focusTrap.value.activate()
      }
    })
  } else if (focusTrap.value) {
    // Deactivate focus trap when panel closes
    focusTrap.value.deactivate()
    focusTrap.value = null
  }
})

// Watch for transcript changes to process when user stops speaking
let processingTimeout = null
watch(transcript, (newValue, oldValue) => {
  if (!newValue || !isListening.value) return
  
  // Clear existing timeout
  if (processingTimeout) {
    clearTimeout(processingTimeout)
  }
  
  // Set new timeout to process after user stops speaking
  processingTimeout = setTimeout(async () => {
    if (isListening.value && transcript.value) {
      // Stop listening before processing
      voiceStore.stopListening()
      
      // Add user message to conversation
      conversation.value.push({
        type: 'user',
        text: transcript.value,
        timestamp: new Date()
      })
      
      // Announce to screen reader that user's speech was recognized
      announceToScreenReader(`You said: ${transcript.value}`, 'polite')
      
      // Process voice command
      isProcessing.value = true
      
      try {
        const response = await voiceStore.processCommand(transcript.value)
        
        // Add assistant response to conversation
        if (response && response.text) {
          conversation.value.push({
            type: 'assistant',
            text: response.text,
            timestamp: new Date()
          })
          
          // Announce assistant response to screen reader
          announceToScreenReader(`Assistant says: ${response.text}`, 'polite')
          
          // Play audio feedback for response
          playAudioFeedback('notification')
        }
      } catch (error) {
        // Add error message to conversation
        conversation.value.push({
          type: 'assistant',
          text: 'Sorry, I encountered an error processing your request.',
          error: true,
          timestamp: new Date()
        })
        
        // Announce error to screen reader
        announceToScreenReader('Sorry, I encountered an error processing your request.', 'assertive')
        
        // Play error sound
        playAudioFeedback('error')
      } finally {
        isProcessing.value = false
        
        // Scroll conversation to bottom
        await nextTick()
        scrollToBottom()
      }
    }
  }, 1500) // Wait 1.5 seconds after user stops speaking
})

// Helper function to scroll conversation to bottom
const scrollToBottom = () => {
  if (conversationEl.value) {
    conversationEl.value.scrollTop = conversationEl.value.scrollHeight
  }
}

// Add welcome message on mount
onMounted(() => {
  // Initialize voice system
  voiceStore.initialize()
  
  // Add welcome message if needed
  if (props.initialOpen && conversation.value.length === 0) {
    conversation.value.push({
      type: 'assistant',
      text: 'Hello! I\'m your Pravis Boutique assistant. How can I help you today?',
      timestamp: new Date()
    })
  }
})
</script>
