// Voice Assistant Pinia Store
import { defineStore } from 'pinia'

export const useVoiceStore = defineStore('voice', {
  state: () => ({
    isListening: false,
    isLoading: false,
    lastQuery: '',
    lastResponse: '',
    error: null,
    isSupported: false
  }),

  getters: {
    canUseVoice: (state) => state.isSupported && !state.isLoading
  },

  actions: {
    checkSupport() {
      this.isSupported = 'webkitSpeechRecognition' in window || 'SpeechRecognition' in window
    },

    async startListening() {
      if (!this.isSupported) {
        this.error = 'Speech recognition not supported in this browser'
        return
      }

      this.isListening = true
      this.error = null
      
      // Mock implementation for now
      setTimeout(() => {
        this.isListening = false
        this.lastQuery = 'Hello, show me some sarees'
        this.processQuery(this.lastQuery)
      }, 2000)
    },

    stopListening() {
      this.isListening = false
    },

    async processQuery(query) {
      if (!query) return

      this.isLoading = true
      this.lastQuery = query

      try {
        // Call backend API
        const config = useRuntimeConfig()
        const apiUrl = `${config.public.apiBaseUrl || 'http://localhost:8000'}/api/v1/voice/query`
        
        const response = await $fetch(apiUrl, {
          method: 'POST',
          body: { query }
        })

        this.lastResponse = response.response
        this.error = null
      } catch (error) {
        console.error('Voice query error:', error)
        this.error = 'Failed to process voice query'
        this.lastResponse = 'Sorry, I encountered an error processing your request.'
      } finally {
        this.isLoading = false
      }
    },

    clearError() {
      this.error = null
    }
  }
})