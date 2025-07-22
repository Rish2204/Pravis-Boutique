import { defineStore } from 'pinia'
import { useAnalyticsStore } from './analytics'

/**
 * Voice agent store for managing voice interaction state
 */
export const useVoiceStore = defineStore('voice', {
  state: () => ({
    isEnabled: false,
    isListening: false,
    transcript: '',
    lastCommand: null,
    lastResponse: null,
    error: null,
    isSpeaking: false,
    recognitionSupported: false,
    speechSupported: false,
    volume: 0.8,
    muted: false
  }),
  
  getters: {
    /**
     * Check if voice agent is ready to use
     */
    isReady: (state) => state.isEnabled && state.recognitionSupported && state.speechSupported,
    
    /**
     * Get current voice agent status
     */
    status: (state) => {
      if (!state.recognitionSupported) return 'unsupported'
      if (!state.isEnabled) return 'disabled'
      if (state.isListening) return 'listening'
      if (state.isSpeaking) return 'speaking'
      return 'ready'
    }
  },
  
  actions: {
    /**
     * Initialize voice recognition and synthesis
     */
    initialize() {
      if (!process.client) return
      
      // Check for Web Speech API support
      this.recognitionSupported = 'webkitSpeechRecognition' in window || 'SpeechRecognition' in window
      this.speechSupported = 'speechSynthesis' in window
      
      // Get stored settings
      const storedEnabled = localStorage.getItem('voice-enabled')
      const storedVolume = localStorage.getItem('voice-volume')
      const storedMuted = localStorage.getItem('voice-muted')
      
      if (storedEnabled !== null) {
        this.isEnabled = storedEnabled === 'true'
      }
      
      if (storedVolume !== null) {
        this.volume = parseFloat(storedVolume)
      }
      
      if (storedMuted !== null) {
        this.muted = storedMuted === 'true'
      }
    },
    
    /**
     * Enable or disable voice agent
     * @param {boolean} enabled - Enable state
     */
    setEnabled(enabled) {
      this.isEnabled = !!enabled
      
      if (process.client) {
        localStorage.setItem('voice-enabled', this.isEnabled)
      }
      
      // Stop listening if disabling
      if (!this.isEnabled && this.isListening) {
        this.stopListening()
      }
    },
    
    /**
     * Set voice volume
     * @param {number} volume - Volume level (0-1)
     */
    setVolume(volume) {
      this.volume = Math.max(0, Math.min(1, volume))
      
      if (process.client) {
        localStorage.setItem('voice-volume', this.volume.toString())
      }
    },
    
    /**
     * Toggle muted state
     * @param {boolean} muted - Muted state
     */
    setMuted(muted) {
      this.muted = !!muted
      
      if (process.client) {
        localStorage.setItem('voice-muted', this.muted.toString())
      }
    },
    
    /**
     * Start voice recognition
     */
    startListening() {
      if (!process.client || !this.recognitionSupported || !this.isEnabled) return
      
      // This would be implemented with actual Web Speech API code
      // For demonstration purposes, we'll just set the state
      this.isListening = true
      this.transcript = ''
      
      // Actual implementation would use browser's SpeechRecognition API
      // const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition
      // this.recognition = new SpeechRecognition()
      // this.recognition.continuous = true
      // this.recognition.interimResults = true
      // this.recognition.onresult = this.handleRecognitionResult
      // this.recognition.start()
    },
    
    /**
     * Stop voice recognition
     */
    stopListening() {
      if (!process.client || !this.isListening) return
      
      // This would stop the actual Web Speech API recognition
      // For demonstration purposes, we'll just set the state
      this.isListening = false
      
      // Actual implementation would use:
      // if (this.recognition) {
      //   this.recognition.stop()
      // }
    },
    
    /**
     * Process voice command
     * @param {string} command - Voice command to process
     */
    async processCommand(command) {
      if (!command || !this.isEnabled) return
      
      this.lastCommand = {
        text: command,
        timestamp: new Date().toISOString()
      }
      
      try {
        const { useApi } = useNuxtApp()
        const { post } = useApi()
        
        // Send command to backend for processing
        const response = await post('/voice/command', {
          command: command,
          context: {
            currentRoute: window.location.pathname,
            pageTitle: document.title
          }
        })
        
        this.lastResponse = {
          text: response.text,
          action: response.action,
          timestamp: new Date().toISOString()
        }
        
        // Speak response if not muted
        if (response.text && !this.muted) {
          this.speak(response.text)
        }
        
        // Process any actions returned by the API
        if (response.action) {
          this.handleVoiceAction(response.action)
        }
        
        // Track analytics if consent is given
        const analyticsStore = useAnalyticsStore()
        if (analyticsStore.consentGiven) {
          analyticsStore.trackVoiceInteraction(
            this.lastCommand,
            this.lastResponse,
            { currentPage: window.location.pathname }
          )
        }
        
        return this.lastResponse
      } catch (err) {
        this.error = err.message || 'Failed to process voice command'
        this.lastResponse = {
          text: 'Sorry, I encountered an error processing your request.',
          error: true,
          timestamp: new Date().toISOString()
        }
        
        if (!this.muted) {
          this.speak(this.lastResponse.text)
        }
        
        return this.lastResponse
      }
    },
    
    /**
     * Speak text using speech synthesis
     * @param {string} text - Text to speak
     */
    speak(text) {
      if (!process.client || !this.speechSupported || !text || this.muted) return
      
      this.isSpeaking = true
      
      // This would be implemented with actual Web Speech API code
      // For demonstration purposes, we'll just set the state
      setTimeout(() => {
        this.isSpeaking = false
      }, 2000)
      
      // Actual implementation would use:
      // const utterance = new SpeechSynthesisUtterance(text)
      // utterance.volume = this.volume
      // utterance.onend = () => {
      //   this.isSpeaking = false
      // }
      // window.speechSynthesis.speak(utterance)
    },
    
    /**
     * Handle voice command actions
     * @param {Object} action - Action object from voice API
     */
    handleVoiceAction(action) {
      if (!action || !action.type) return
      
      const router = useRouter()
      
      switch (action.type) {
        case 'navigate':
          // Navigate to a different page
          if (action.path) {
            router.push(action.path)
          }
          break
          
        case 'addToCart':
          // Add product to cart
          if (action.productId) {
            const cartStore = useCartStore()
            cartStore.addItem({
              id: action.productId,
              name: action.productName || 'Product',
              price: action.price || 0,
              image: action.image || '',
              quantity: action.quantity || 1
            })
          }
          break
          
        case 'checkout':
          // Navigate to checkout
          router.push('/checkout')
          break
          
        case 'search':
          // Perform search
          if (action.query) {
            router.push(`/search?q=${encodeURIComponent(action.query)}`)
          }
          break
          
        default:
          console.log('Unknown voice action type:', action.type)
      }
    }
  }
})
