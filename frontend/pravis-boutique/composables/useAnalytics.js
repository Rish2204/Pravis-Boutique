/**
 * Comprehensive Analytics and Logging System for Pravis Boutique
 * Tracks user interactions, cookies, cache, and navigation for testing
 */

import { ref, reactive, computed } from 'vue'

// Global analytics store
const analyticsStore = reactive({
  sessionId: null,
  userId: null,
  events: [],
  pageViews: [],
  userInteractions: [],
  errors: [],
  performance: [],
  cache: new Map(),
  cookies: new Map()
})

export const useAnalytics = () => {
  
  // Initialize session
  const initializeSession = () => {
    if (!analyticsStore.sessionId) {
      analyticsStore.sessionId = generateSessionId()
      analyticsStore.userId = getUserId()
      
      // Track session start
      logEvent('session_start', {
        timestamp: new Date().toISOString(),
        userAgent: navigator.userAgent,
        screenResolution: `${screen.width}x${screen.height}`,
        viewport: `${window.innerWidth}x${window.innerHeight}`,
        language: navigator.language,
        timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
        referrer: document.referrer,
        url: window.location.href
      })
    }
  }

  // Generate unique session ID
  const generateSessionId = () => {
    return `session_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`
  }

  // Get or create user ID
  const getUserId = () => {
    const existing = localStorage.getItem('pravis_user_id')
    if (existing) return existing
    
    const newUserId = `user_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`
    localStorage.setItem('pravis_user_id', newUserId)
    return newUserId
  }

  // Log general events
  const logEvent = (eventName, data = {}) => {
    const event = {
      id: `event_${Date.now()}_${Math.random().toString(36).substr(2, 5)}`,
      sessionId: analyticsStore.sessionId,
      userId: analyticsStore.userId,
      eventName,
      timestamp: new Date().toISOString(),
      url: window.location.href,
      path: window.location.pathname,
      data,
      device: getDeviceInfo(),
      browser: getBrowserInfo()
    }
    
    analyticsStore.events.push(event)
    
    // Save to local storage for persistence
    saveToLocalStorage('events', event)
    
    // Send to backend if available
    sendToBackend('events', event)
    
    console.log('📊 Analytics Event:', eventName, data)
  }

  // Track page views
  const logPageView = (path = window.location.pathname) => {
    const pageView = {
      id: `pageview_${Date.now()}_${Math.random().toString(36).substr(2, 5)}`,
      sessionId: analyticsStore.sessionId,
      userId: analyticsStore.userId,
      path,
      title: document.title,
      timestamp: new Date().toISOString(),
      referrer: document.referrer,
      loadTime: performance.now(),
      viewport: `${window.innerWidth}x${window.innerHeight}`
    }
    
    analyticsStore.pageViews.push(pageView)
    saveToLocalStorage('pageViews', pageView)
    sendToBackend('pageViews', pageView)
    
    console.log('👁️ Page View:', path)
  }

  // Track user interactions
  const logInteraction = (element, action, details = {}) => {
    const interaction = {
      id: `interaction_${Date.now()}_${Math.random().toString(36).substr(2, 5)}`,
      sessionId: analyticsStore.sessionId,
      userId: analyticsStore.userId,
      element,
      action,
      timestamp: new Date().toISOString(),
      path: window.location.pathname,
      details,
      mousePosition: details.mousePosition || null,
      elementPosition: details.elementPosition || null
    }
    
    analyticsStore.userInteractions.push(interaction)
    saveToLocalStorage('interactions', interaction)
    sendToBackend('interactions', interaction)
    
    console.log('🖱️ User Interaction:', element, action, details)
  }

  // Track errors
  const logError = (error, context = {}) => {
    const errorLog = {
      id: `error_${Date.now()}_${Math.random().toString(36).substr(2, 5)}`,
      sessionId: analyticsStore.sessionId,
      userId: analyticsStore.userId,
      message: error.message || error,
      stack: error.stack || null,
      timestamp: new Date().toISOString(),
      path: window.location.pathname,
      context,
      userAgent: navigator.userAgent
    }
    
    analyticsStore.errors.push(errorLog)
    saveToLocalStorage('errors', errorLog)
    sendToBackend('errors', errorLog)
    
    console.error('🚨 Error Logged:', error)
  }

  // Track performance metrics
  const logPerformance = (metric, value, details = {}) => {
    const perfLog = {
      id: `perf_${Date.now()}_${Math.random().toString(36).substr(2, 5)}`,
      sessionId: analyticsStore.sessionId,
      metric,
      value,
      timestamp: new Date().toISOString(),
      path: window.location.pathname,
      details
    }
    
    analyticsStore.performance.push(perfLog)
    saveToLocalStorage('performance', perfLog)
    sendToBackend('performance', perfLog)
    
    console.log('⚡ Performance:', metric, value)
  }

  // Cookie management
  const trackCookie = (name, value, options = {}) => {
    const cookieData = {
      name,
      value,
      options,
      timestamp: new Date().toISOString(),
      path: window.location.pathname
    }
    
    analyticsStore.cookies.set(name, cookieData)
    saveToLocalStorage('cookies', { [name]: cookieData })
    
    console.log('🍪 Cookie Tracked:', name, value)
  }

  // Cache management
  const trackCache = (key, data, type = 'local') => {
    const cacheData = {
      key,
      data,
      type,
      timestamp: new Date().toISOString(),
      path: window.location.pathname,
      size: JSON.stringify(data).length
    }
    
    analyticsStore.cache.set(key, cacheData)
    saveToLocalStorage('cache', { [key]: cacheData })
    
    console.log('💾 Cache Tracked:', key, type)
  }

  // E-commerce specific tracking
  const trackProduct = (action, product, details = {}) => {
    logEvent(`product_${action}`, {
      productId: product.id,
      productName: product.name,
      price: product.price,
      category: product.category,
      ...details
    })
  }

  const trackCart = (action, item, details = {}) => {
    logEvent(`cart_${action}`, {
      itemId: item.id,
      itemName: item.name,
      quantity: item.quantity,
      price: item.price,
      ...details
    })
  }

  const trackCheckout = (step, details = {}) => {
    logEvent(`checkout_${step}`, details)
  }

  // Device and browser info
  const getDeviceInfo = () => {
    return {
      isMobile: /Mobi|Android/i.test(navigator.userAgent),
      isTablet: /Tablet|iPad/i.test(navigator.userAgent),
      isDesktop: !/Mobi|Android|Tablet|iPad/i.test(navigator.userAgent),
      platform: navigator.platform,
      screenSize: `${screen.width}x${screen.height}`,
      viewportSize: `${window.innerWidth}x${window.innerHeight}`
    }
  }

  const getBrowserInfo = () => {
    const ua = navigator.userAgent
    return {
      userAgent: ua,
      language: navigator.language,
      cookieEnabled: navigator.cookieEnabled,
      onLine: navigator.onLine,
      isSafari: /Safari/.test(ua) && !/Chrome/.test(ua),
      isChrome: /Chrome/.test(ua),
      isFirefox: /Firefox/.test(ua),
      isEdge: /Edge/.test(ua)
    }
  }

  // Local storage persistence
  const saveToLocalStorage = (type, data) => {
    try {
      const existing = JSON.parse(localStorage.getItem(`pravis_analytics_${type}`) || '[]')
      existing.push(data)
      
      // Keep only last 1000 entries to prevent storage overflow
      if (existing.length > 1000) {
        existing.splice(0, existing.length - 1000)
      }
      
      localStorage.setItem(`pravis_analytics_${type}`, JSON.stringify(existing))
    } catch (error) {
      console.warn('Failed to save to localStorage:', error)
    }
  }

  // Backend integration
  const sendToBackend = async (endpoint, data) => {
    try {
      if (process.client && window.location.hostname !== 'localhost') {
        // Only send to production backend
        await $fetch(`/api/analytics/${endpoint}`, {
          method: 'POST',
          body: data
        })
      }
    } catch (error) {
      console.warn('Failed to send analytics to backend:', error)
    }
  }

  // Export analytics data
  const exportAnalyticsData = () => {
    const allData = {
      session: {
        sessionId: analyticsStore.sessionId,
        userId: analyticsStore.userId,
        timestamp: new Date().toISOString()
      },
      events: analyticsStore.events,
      pageViews: analyticsStore.pageViews,
      interactions: analyticsStore.userInteractions,
      errors: analyticsStore.errors,
      performance: analyticsStore.performance,
      cookies: Object.fromEntries(analyticsStore.cookies),
      cache: Object.fromEntries(analyticsStore.cache),
      localStorage: {
        events: JSON.parse(localStorage.getItem('pravis_analytics_events') || '[]'),
        pageViews: JSON.parse(localStorage.getItem('pravis_analytics_pageViews') || '[]'),
        interactions: JSON.parse(localStorage.getItem('pravis_analytics_interactions') || '[]'),
        errors: JSON.parse(localStorage.getItem('pravis_analytics_errors') || '[]'),
        performance: JSON.parse(localStorage.getItem('pravis_analytics_performance') || '[]')
      }
    }
    
    // Create downloadable JSON file
    const blob = new Blob([JSON.stringify(allData, null, 2)], { type: 'application/json' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = `pravis-analytics-${analyticsStore.sessionId}.json`
    document.body.appendChild(a)
    a.click()
    document.body.removeChild(a)
    URL.revokeObjectURL(url)
    
    return allData
  }

  // Clear analytics data
  const clearAnalyticsData = () => {
    analyticsStore.events.length = 0
    analyticsStore.pageViews.length = 0
    analyticsStore.userInteractions.length = 0
    analyticsStore.errors.length = 0
    analyticsStore.performance.length = 0
    analyticsStore.cache.clear()
    analyticsStore.cookies.clear()
    
    // Clear localStorage
    const keys = ['events', 'pageViews', 'interactions', 'errors', 'performance', 'cookies', 'cache']
    keys.forEach(key => localStorage.removeItem(`pravis_analytics_${key}`))
    
    console.log('🗑️ Analytics data cleared')
  }

  // Get analytics summary
  const getAnalyticsSummary = computed(() => ({
    sessionId: analyticsStore.sessionId,
    userId: analyticsStore.userId,
    eventsCount: analyticsStore.events.length,
    pageViewsCount: analyticsStore.pageViews.length,
    interactionsCount: analyticsStore.userInteractions.length,
    errorsCount: analyticsStore.errors.length,
    performanceCount: analyticsStore.performance.length,
    cookiesCount: analyticsStore.cookies.size,
    cacheCount: analyticsStore.cache.size,
    sessionDuration: analyticsStore.events.length > 0 
      ? new Date() - new Date(analyticsStore.events[0].timestamp)
      : 0
  }))

  return {
    // Core functions
    initializeSession,
    logEvent,
    logPageView,
    logInteraction,
    logError,
    logPerformance,
    
    // Cookie and cache
    trackCookie,
    trackCache,
    
    // E-commerce specific
    trackProduct,
    trackCart,
    trackCheckout,
    
    // Data management
    exportAnalyticsData,
    clearAnalyticsData,
    
    // Computed properties
    getAnalyticsSummary,
    
    // Raw data access
    analyticsStore: readonly(analyticsStore)
  }
}