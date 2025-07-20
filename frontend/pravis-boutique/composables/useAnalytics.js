export const useAnalytics = () => {
  const consentGiven = ref(false)
  const sessionId = ref(null)
  const initialized = ref(false)

  // Check consent status
  const checkConsent = () => {
    if (process.client) {
      const consent = localStorage.getItem('pravis-consent')
      if (consent) {
        const consentData = JSON.parse(consent)
        consentGiven.value = consentData.consent
        return consentData.consent
      }
    }
    return false
  }

  // Generate unique session ID
  const generateSessionId = () => {
    return 'session_' + Math.random().toString(36).substr(2, 9) + '_' + Date.now()
  }

  // Initialize analytics system
  const init = () => {
    if (!process.client || initialized.value) { return }

    consentGiven.value = checkConsent()
    if (!consentGiven.value) { return }

    sessionId.value = generateSessionId()
    initialized.value = true

    // Track initial page load
    trackPageView('home', { initial_load: true })
  }

  // Track page views
  const trackPageView = async (pageName, additionalData = {}) => {
    if (!consentGiven.value || !initialized.value) { return }

    const eventData = {
      type: 'page_view',
      page: pageName,
      timestamp: new Date().toISOString(),
      sessionId: sessionId.value,
      userAgent: navigator.userAgent,
      viewport: {
        width: window.innerWidth,
        height: window.innerHeight
      },
      ...additionalData
    }

    await sendAnalyticsEvent(eventData)
  }

  // Track user interactions
  const trackInteraction = async (element, action, context = {}) => {
    if (!consentGiven.value || !initialized.value) { return }

    const eventData = {
      type: 'user_interaction',
      element,
      action,
      context,
      timestamp: new Date().toISOString(),
      sessionId: sessionId.value,
      viewport: {
        width: window.innerWidth,
        height: window.innerHeight
      }
    }

    await sendAnalyticsEvent(eventData)
  }

  // Track voice interactions
  const trackVoiceInteraction = async (command, response, context = {}) => {
    if (!consentGiven.value || !initialized.value) { return }

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
      sessionId: sessionId.value
    }

    await sendAnalyticsEvent(eventData)
  }

  // Track product interactions
  const trackProductInteraction = async (productId, action, details = {}) => {
    if (!consentGiven.value || !initialized.value) { return }

    const eventData = {
      type: 'product_interaction',
      productId,
      action, // 'view', 'add_to_cart', 'remove_from_cart', 'purchase'
      details,
      timestamp: new Date().toISOString(),
      sessionId: sessionId.value
    }

    await sendAnalyticsEvent(eventData)
  }

  // Send analytics event to backend
  const sendAnalyticsEvent = async (eventData) => {
    try {
      await $fetch('/api/analytics/event', {
        method: 'POST',
        body: eventData
      })
    } catch (error) {
    }
  }

  // Auto-initialize on client-side
  onMounted(() => {
    if (process.client) {
      init()
    }
  })

  return {
    consentGiven: readonly(consentGiven),
    sessionId: readonly(sessionId),
    initialized: readonly(initialized),
    init,
    checkConsent,
    trackPageView,
    trackInteraction,
    trackVoiceInteraction,
    trackProductInteraction
  }
}
