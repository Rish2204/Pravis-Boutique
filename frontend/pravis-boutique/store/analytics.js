import { defineStore } from 'pinia';

/**
 * Analytics Store for Pravis Boutique
 * 
 * Handles all analytics tracking with consent management
 * Only tracks data when user has explicitly consented
 * Implements GDPR and CCPA privacy compliance
 */
export const useAnalyticsStore = defineStore('analytics', {
  state: () => ({
    consentGiven: false,
    sessionId: null,
    initialized: false
  }),
  
  getters: {
    hasConsent: (state) => state.consentGiven
  },
  
  actions: {
    /**
     * Initialize analytics service
     * Checks localStorage for existing consent
     */
    initialize() {
      if (this.initialized) return;

      // Check if localStorage is available (client-side only)
      if (process.client) {
        // Generate a unique session ID
        this.sessionId = this.generateSessionId();
        
        // Check for existing consent
        this.checkStoredConsent();
        
        this.initialized = true;
      }
    },
    
    /**
     * Generate a unique session ID
     */
    generateSessionId() {
      return 'session_' + Date.now() + '_' + Math.random().toString(36).substring(2, 9);
    },
    
    /**
     * Check if user has already provided consent
     */
    checkStoredConsent() {
      const storedConsent = localStorage.getItem('pravis-consent');
      
      if (storedConsent) {
        try {
          const consentData = JSON.parse(storedConsent);
          this.consentGiven = consentData.consent;
          
          // If consent was given, track page view
          if (this.consentGiven) {
            this.trackPageView(window.location.pathname);
          }
        } catch (error) {
          console.error('Error parsing stored consent:', error);
          this.consentGiven = false;
        }
      } else {
        this.consentGiven = false;
      }
    },
    
    /**
     * Set user consent preference
     */
    setConsent(consentValue) {
      this.consentGiven = consentValue;
      
      // If consent just granted, start tracking
      if (consentValue) {
        this.trackPageView(window.location.pathname);
      }
    },
    
    /**
     * Track a page view
     */
    trackPageView(pageName, additionalData = {}) {
      if (!this.consentGiven) return;
      
      const eventData = {
        type: 'page_view',
        page: pageName,
        timestamp: new Date().toISOString(),
        sessionId: this.sessionId,
        userAgent: navigator.userAgent,
        ...additionalData
      };
      
      this.sendAnalyticsEvent(eventData);
    },
    
    /**
     * Track user interactions (clicks, taps, swipes)
     */
    trackInteraction(element, action, context = {}) {
      if (!this.consentGiven) return;
      
      const eventData = {
        type: 'user_interaction',
        element: element,
        action: action,
        context: context,
        timestamp: new Date().toISOString(),
        sessionId: this.sessionId,
        viewport: {
          width: window.innerWidth,
          height: window.innerHeight
        }
      };
      
      this.sendAnalyticsEvent(eventData);
    },
    
    /**
     * Track product interactions
     */
    trackProductInteraction(productId, action, details = {}) {
      if (!this.consentGiven) return;
      
      const eventData = {
        type: 'product_interaction',
        productId: productId,
        action: action, // 'view', 'add_to_cart', 'remove_from_cart', 'purchase'
        details: details,
        timestamp: new Date().toISOString(),
        sessionId: this.sessionId
      };
      
      this.sendAnalyticsEvent(eventData);
    },
    
    /**
     * Track voice interactions
     */
    trackVoiceInteraction(command, response, context = {}) {
      if (!this.consentGiven) return;
      
      const eventData = {
        type: 'voice_interaction',
        command: {
          text: command.text,
          confidence: command.confidence || null,
          language: command.language || 'en-US'
        },
        response: {
          text: response.text,
          audio_duration: response.audioDuration || null,
          success: response.success
        },
        context: {
          page: context.currentPage,
          user_intent: context.detectedIntent,
          session_context: context.sessionContext
        },
        timestamp: new Date().toISOString(),
        sessionId: this.sessionId
      };
      
      this.sendAnalyticsEvent(eventData);
    },
    
    /**
     * Track consent events
     */
    trackConsentEvent(consentData) {
      const eventData = {
        type: 'consent_event',
        consent: consentData.consent,
        version: consentData.version,
        timestamp: new Date().toISOString(),
        sessionId: this.sessionId
      };
      
      this.sendAnalyticsEvent(eventData);
    },
    
    /**
     * Send analytics event to backend
     */
    sendAnalyticsEvent(eventData) {
      // Only send if consent is given
      if (!this.consentGiven) return;
      
      // In development, log to console
      if (process.env.NODE_ENV === 'development') {
        console.log('Analytics event:', eventData);
      }
      
      // Send to backend API endpoint
      fetch('/api/analytics/event', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(eventData),
        // Don't wait for response to avoid blocking
        keepalive: true
      }).catch(error => {
        console.error('Error sending analytics:', error);
      });
    },
    
    /**
     * Delete all user data (GDPR compliance)
     */
    async deleteUserData() {
      if (!process.client) return;
      
      try {
        // Clear localStorage consent
        localStorage.removeItem('pravis-consent');
        
        // Set consent to false
        this.consentGiven = false;
        
        // Call backend to delete server-side data
        await fetch('/api/user/delete-data', { 
          method: 'DELETE',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            sessionId: this.sessionId
          })
        });
        
        return { success: true };
      } catch (error) {
        console.error('Error deleting user data:', error);
        return { success: false, error: error.message };
      }
    },
    
    /**
     * Export user data (GDPR compliance)
     */
    async exportUserData() {
      if (!process.client) return null;
      
      try {
        const response = await fetch('/api/user/export-data', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            sessionId: this.sessionId
          })
        });
        
        if (!response.ok) {
          throw new Error('Failed to export data');
        }
        
        return await response.json();
      } catch (error) {
        console.error('Error exporting user data:', error);
        return null;
      }
    }
  }
});
