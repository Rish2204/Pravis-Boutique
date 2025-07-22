import { ref, onMounted, onBeforeUnmount, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import VoiceController from '~/components/voice/VoiceController'

/**
 * Voice Agent Composable
 * Provides reactive state and methods for voice interactions
 */
export const useVoiceAgent = () => {
  const controller = ref(null)
  const transcript = ref('')
  const isListening = ref(false)
  const isSpeaking = ref(false)
  const isInitialized = ref(false)
  const isError = ref(false)
  const error = ref('')
  const useBackend = ref(false)
  const voicePreference = ref('nova')
  
  // Vue Router
  const route = useRoute()
  const router = useRouter()

  /**
   * Initialize the voice controller
   */
  const initialize = () => {
    if (process.server) return
    
    controller.value = new VoiceController()
    
    // Set up callbacks
    controller.value.setCallbacks({
      onTranscriptChange: (text) => {
        transcript.value = text
      },
      onListeningChange: (listening) => {
        isListening.value = listening
      },
      onSpeakingChange: (speaking) => {
        isSpeaking.value = speaking
      },
      onError: (errorMessage) => {
        isError.value = true
        error.value = errorMessage
      }
    })
    
    // Set initial values
    useBackend.value = controller.value.useBackend
    voicePreference.value = controller.value.voicePreference
    isInitialized.value = controller.value.isInitialized
    
    // Set context
    updateContext()
  }

  /**
   * Update context with current route information
   */
  const updateContext = () => {
    if (!controller.value) return
    
    controller.value.setContext({
      currentRoute: route.path,
      currentPage: route.name,
      pageTitle: document.title,
      query: route.query,
      params: route.params
    })
  }

  /**
   * Start listening for voice input
   */
  const startListening = async () => {
    if (!controller.value) return false
    return await controller.value.startListening()
  }

  /**
   * Stop listening for voice input
   */
  const stopListening = async () => {
    if (!controller.value) return ''
    return await controller.value.stopListening()
  }

  /**
   * Process a voice command
   * @param {string} command 
   */
  const processCommand = async (command) => {
    if (!controller.value || !command) return null
    return await controller.value.processCommand(command)
  }

  /**
   * Speak text
   * @param {string} text 
   * @param {Object} options 
   */
  const speak = async (text, options = {}) => {
    if (!controller.value || !text) return false
    return await controller.value.speak(text, options)
  }

  /**
   * Stop speaking
   */
  const stopSpeaking = () => {
    if (!controller.value) return
    controller.value.stopSpeaking()
  }

  /**
   * Toggle backend voice processing
   * @param {boolean} value 
   */
  const toggleBackend = (value) => {
    if (!controller.value) return
    
    const newValue = value === undefined ? !useBackend.value : !!value
    controller.value.setUseBackend(newValue)
    useBackend.value = newValue
  }

  /**
   * Set voice preference
   * @param {string} voice 
   */
  const setVoice = (voice) => {
    if (!controller.value || !voice) return
    
    controller.value.setVoicePreference(voice)
    voicePreference.value = voice
  }

  /**
   * Handle a voice command with routing
   * @param {string} command 
   */
  const handleCommand = async (command) => {
    if (!controller.value || !command) return null
    
    // Stop listening if still active
    if (isListening.value) {
      await stopListening()
    }
    
    // Process the command
    const response = await processCommand(command)
    
    // Handle any routing actions
    if (response && response.action && response.action.type === 'navigate') {
      if (response.action.path) {
        router.push(response.action.path)
      }
    }
    
    return response
  }

  // Watch for route changes to update context
  watch(() => route.path, () => {
    updateContext()
  })

  // Lifecycle hooks
  onMounted(() => {
    initialize()
  })

  onBeforeUnmount(() => {
    if (controller.value) {
      if (isListening.value) {
        controller.value.stopListening()
      }
      if (isSpeaking.value) {
        controller.value.stopSpeaking()
      }
    }
  })

  return {
    // State
    transcript,
    isListening,
    isSpeaking,
    isInitialized,
    isError,
    error,
    useBackend,
    voicePreference,
    
    // Methods
    initialize,
    startListening,
    stopListening,
    processCommand,
    speak,
    stopSpeaking,
    toggleBackend,
    setVoice,
    handleCommand,
    updateContext
  }
}
