/**
 * Global Analytics Plugin for Pravis Boutique
 * Auto-tracks page views, user interactions, and errors
 */

export default defineNuxtPlugin(() => {
  const { $router } = useNuxtApp()
  
  // Only run on client side
  if (process.server) return
  
  const { 
    initializeSession, 
    logPageView, 
    logInteraction, 
    logError, 
    logPerformance,
    trackCookie,
    trackCache
  } = useAnalytics()
  
  // Initialize analytics session
  initializeSession()
  
  // Track initial page load
  logPageView()
  logPerformance('initial_load', performance.now())
  
  // Track route changes
  $router.afterEach((to, from) => {
    nextTick(() => {
      logPageView(to.path)
      logPerformance('route_change', performance.now())
    })
  })
  
  // Track clicks globally
  document.addEventListener('click', (event) => {
    const target = event.target
    const tagName = target.tagName.toLowerCase()
    const className = target.className || ''
    const id = target.id || ''
    const href = target.href || ''
    const textContent = target.textContent?.slice(0, 50) || ''
    
    // Get mouse position
    const mousePosition = {
      x: event.clientX,
      y: event.clientY
    }
    
    // Get element position
    const rect = target.getBoundingClientRect()
    const elementPosition = {
      x: rect.left,
      y: rect.top,
      width: rect.width,
      height: rect.height
    }
    
    logInteraction('click', tagName, {
      className,
      id,
      href,
      textContent,
      mousePosition,
      elementPosition
    })
  })
  
  // Track form submissions
  document.addEventListener('submit', (event) => {
    const form = event.target
    const formData = new FormData(form)
    const fields = Object.fromEntries(formData.entries())
    
    // Remove sensitive data
    const sanitizedFields = Object.keys(fields).reduce((acc, key) => {
      if (!key.toLowerCase().includes('password') && !key.toLowerCase().includes('secret')) {
        acc[key] = typeof fields[key] === 'string' ? fields[key].slice(0, 100) : fields[key]
      }
      return acc
    }, {})
    
    logInteraction('form_submit', 'form', {
      action: form.action,
      method: form.method,
      fields: sanitizedFields,
      fieldCount: Object.keys(fields).length
    })
  })
  
  // Track input changes (debounced)
  let inputTimeout
  document.addEventListener('input', (event) => {
    clearTimeout(inputTimeout)
    inputTimeout = setTimeout(() => {
      const target = event.target
      if (target.tagName.toLowerCase() === 'input' || target.tagName.toLowerCase() === 'textarea') {
        const value = target.value?.slice(0, 50) || '' // Limit length for privacy
        
        logInteraction('input_change', target.tagName.toLowerCase(), {
          type: target.type,
          name: target.name,
          id: target.id,
          valueLength: target.value?.length || 0,
          placeholder: target.placeholder || ''
        })
      }
    }, 1000) // Debounce for 1 second
  })
  
  // Track scroll events (throttled)
  let scrollTimeout
  let lastScrollY = 0
  window.addEventListener('scroll', () => {
    clearTimeout(scrollTimeout)
    scrollTimeout = setTimeout(() => {
      const scrollY = window.scrollY
      const documentHeight = document.documentElement.scrollHeight
      const windowHeight = window.innerHeight
      const scrollPercentage = (scrollY / (documentHeight - windowHeight)) * 100
      
      // Only log significant scroll changes
      if (Math.abs(scrollY - lastScrollY) > 100) {
        logInteraction('scroll', 'window', {
          scrollY,
          scrollPercentage: Math.round(scrollPercentage),
          direction: scrollY > lastScrollY ? 'down' : 'up'
        })
        lastScrollY = scrollY
      }
    }, 500) // Throttle to every 500ms
  })
  
  // Track window resize
  let resizeTimeout
  window.addEventListener('resize', () => {
    clearTimeout(resizeTimeout)
    resizeTimeout = setTimeout(() => {
      logInteraction('window_resize', 'window', {
        width: window.innerWidth,
        height: window.innerHeight,
        devicePixelRatio: window.devicePixelRatio
      })
    }, 1000)
  })
  
  // Track focus/blur events
  window.addEventListener('focus', () => {
    logInteraction('window_focus', 'window', {
      timestamp: new Date().toISOString()
    })
  })
  
  window.addEventListener('blur', () => {
    logInteraction('window_blur', 'window', {
      timestamp: new Date().toISOString()
    })
  })
  
  // Track page visibility changes
  document.addEventListener('visibilitychange', () => {
    logInteraction('visibility_change', 'document', {
      hidden: document.hidden,
      visibilityState: document.visibilityState,
      timestamp: new Date().toISOString()
    })
  })
  
  // Track unhandled errors
  window.addEventListener('error', (event) => {
    logError({
      message: event.message,
      filename: event.filename,
      lineno: event.lineno,
      colno: event.colno,
      stack: event.error?.stack
    }, {
      type: 'javascript_error',
      url: window.location.href
    })
  })
  
  // Track unhandled promise rejections
  window.addEventListener('unhandledrejection', (event) => {
    logError({
      message: 'Unhandled Promise Rejection',
      reason: event.reason
    }, {
      type: 'promise_rejection',
      url: window.location.href
    })
  })
  
  // Track performance metrics
  window.addEventListener('load', () => {
    setTimeout(() => {
      const navigation = performance.getEntriesByType('navigation')[0]
      const paint = performance.getEntriesByType('paint')
      
      if (navigation) {
        logPerformance('navigation_timing', navigation.loadEventEnd - navigation.fetchStart, {
          domContentLoaded: navigation.domContentLoadedEventEnd - navigation.fetchStart,
          domComplete: navigation.domComplete - navigation.fetchStart,
          loadEventEnd: navigation.loadEventEnd - navigation.fetchStart
        })
      }
      
      paint.forEach(entry => {
        logPerformance(entry.name.replace('-', '_'), entry.startTime)
      })
    }, 1000)
  })
  
  // Track localStorage changes
  const originalSetItem = localStorage.setItem
  localStorage.setItem = function(key, value) {
    trackCache(key, value, 'localStorage')
    return originalSetItem.apply(this, arguments)
  }
  
  // Track sessionStorage changes
  const originalSessionSetItem = sessionStorage.setItem
  sessionStorage.setItem = function(key, value) {
    trackCache(key, value, 'sessionStorage')
    return originalSessionSetItem.apply(this, arguments)
  }
  
  // Track cookie changes (override document.cookie)
  let originalCookie = document.cookie
  Object.defineProperty(document, 'cookie', {
    get: function() {
      return originalCookie
    },
    set: function(val) {
      originalCookie = val
      
      // Parse cookie
      const cookieParts = val.split(';')[0].split('=')
      if (cookieParts.length >= 2) {
        const name = cookieParts[0].trim()
        const value = cookieParts[1].trim()
        trackCookie(name, value, { raw: val })
      }
      
      return val
    }
  })
  
  // Add global analytics functions to window for debugging
  if (process.dev) {
    window.PravisAnalytics = {
      exportData: () => useAnalytics().exportAnalyticsData(),
      clearData: () => useAnalytics().clearAnalyticsData(),
      getSummary: () => useAnalytics().getAnalyticsSummary.value,
      getStore: () => useAnalytics().analyticsStore
    }
    
    console.log('🔧 Debug: PravisAnalytics available on window object')
    console.log('📊 Use PravisAnalytics.exportData() to download analytics')
    console.log('🗑️ Use PravisAnalytics.clearData() to clear analytics')
    console.log('📈 Use PravisAnalytics.getSummary() to view summary')
  }
})