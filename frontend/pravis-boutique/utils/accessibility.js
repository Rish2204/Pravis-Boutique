/**
 * Accessibility utility functions for Pravis Boutique
 */

/**
 * Announces a message to screen readers using an ARIA live region
 * @param {string} message - The message to announce
 * @param {string} priority - The announcement priority ('polite' or 'assertive')
 */
export const announceToScreenReader = (message, priority = 'polite') => {
  // Use existing aria-live region if available, or create a new one
  let announcer = document.getElementById('aria-live-announcer')
  
  if (!announcer) {
    announcer = document.createElement('div')
    announcer.id = 'aria-live-announcer'
    announcer.setAttribute('aria-live', priority)
    announcer.setAttribute('aria-atomic', 'true')
    announcer.className = 'sr-only' // Screen reader only
    document.body.appendChild(announcer)
  }

  // Set the priority (politeness level)
  announcer.setAttribute('aria-live', priority)
  
  // Update the content after a small delay to ensure announcement
  setTimeout(() => {
    announcer.textContent = message
  }, 50)
}

/**
 * Handles keyboard navigation for interactive elements like dropdown menus
 * @param {Event} event - The keydown event
 * @param {Array} items - Array of selectable elements
 * @param {number} currentIndex - Current focused item index
 * @returns {number} - New index after key navigation
 */
export const handleKeyboardNavigation = (event, items, currentIndex) => {
  let newIndex = currentIndex
  
  switch (event.key) {
    case 'ArrowDown':
      event.preventDefault()
      newIndex = (currentIndex + 1) % items.length
      break
      
    case 'ArrowUp':
      event.preventDefault()
      newIndex = (currentIndex - 1 + items.length) % items.length
      break
      
    case 'Home':
      event.preventDefault()
      newIndex = 0
      break
      
    case 'End':
      event.preventDefault()
      newIndex = items.length - 1
      break
      
    case 'Enter':
    case ' ':
      // Handled by the calling component
      break
      
    case 'Escape':
      // Should close the component
      break
      
    default:
      // Allow searching by first letter
      const char = event.key.toLowerCase()
      if (char.length === 1 && /[a-z0-9]/.test(char)) {
        // Find next item starting with this character
        const startIndex = (currentIndex + 1) % items.length
        for (let i = 0; i < items.length; i++) {
          const idx = (startIndex + i) % items.length
          const text = items[idx].textContent.toLowerCase()
          if (text.startsWith(char)) {
            newIndex = idx
            break
          }
        }
      }
      break
  }
  
  return newIndex
}

/**
 * Creates focus trap for modal dialogs
 * @param {HTMLElement} container - The container to trap focus within
 * @returns {Object} - Focus trap methods
 */
export const createFocusTrap = (container) => {
  let focusableElements = []
  let firstFocusable = null
  let lastFocusable = null
  let previouslyFocused = null
  
  const initialize = () => {
    previouslyFocused = document.activeElement
    
    // Get all focusable elements
    focusableElements = Array.from(
      container.querySelectorAll(
        'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
      )
    ).filter(el => !el.disabled && !el.getAttribute('aria-hidden'))
    
    firstFocusable = focusableElements[0]
    lastFocusable = focusableElements[focusableElements.length - 1]
    
    // Focus first element
    if (firstFocusable) {
      setTimeout(() => firstFocusable.focus(), 50)
    }
  }
  
  const handleKeydown = (event) => {
    if (event.key === 'Tab') {
      // If shift + tab on first element, move to last element
      if (event.shiftKey && document.activeElement === firstFocusable) {
        event.preventDefault()
        lastFocusable.focus()
      }
      // If tab on last element, move to first element
      else if (!event.shiftKey && document.activeElement === lastFocusable) {
        event.preventDefault()
        firstFocusable.focus()
      }
    }
  }
  
  const activate = () => {
    initialize()
    container.addEventListener('keydown', handleKeydown)
  }
  
  const deactivate = () => {
    container.removeEventListener('keydown', handleKeydown)
    // Restore focus to element that had it before trap was activated
    if (previouslyFocused && previouslyFocused.focus) {
      setTimeout(() => previouslyFocused.focus(), 0)
    }
  }
  
  return {
    activate,
    deactivate
  }
}

/**
 * Plays audio feedback for actions
 * @param {string} type - The type of feedback ('success', 'error', 'warning', etc.)
 */
export const playAudioFeedback = (type) => {
  // Check user preferences first
  const audioPreferences = localStorage.getItem('pravis-audio-preferences')
  if (audioPreferences && JSON.parse(audioPreferences).disabled) {
    return
  }
  
  // Map of audio files to feedback types
  const audioMap = {
    success: '/audio/success.mp3',
    error: '/audio/error.mp3',
    warning: '/audio/warning.mp3',
    click: '/audio/click.mp3',
    addToCart: '/audio/add-to-cart.mp3',
    notification: '/audio/notification.mp3'
  }
  
  const audioSrc = audioMap[type] || audioMap.click
  
  // Create and play the audio
  const audio = new Audio(audioSrc)
  audio.volume = 0.5 // 50% volume by default
  
  try {
    audio.play().catch(error => {
      // Ignore autoplay restrictions errors
      console.warn('Audio feedback blocked:', error)
    })
  } catch (error) {
    // Fallback for older browsers
    console.warn('Audio feedback failed:', error)
  }
}

/**
 * Creates custom focus outline styles for keyboard navigation
 */
export const initKeyboardFocusStyles = () => {
  let usingMouse = false
  
  // Add class to body when using mouse
  document.body.addEventListener('mousedown', () => {
    usingMouse = true
    document.body.classList.add('using-mouse')
  })
  
  // Remove class when using keyboard
  document.body.addEventListener('keydown', (event) => {
    if (event.key === 'Tab') {
      usingMouse = false
      document.body.classList.remove('using-mouse')
    }
  })
  
  // Add stylesheet for keyboard focus styles
  const style = document.createElement('style')
  style.textContent = `
    body:not(.using-mouse) *:focus {
      outline: 2px solid #3498db !important;
      outline-offset: 2px !important;
    }
    
    .sr-only {
      position: absolute;
      width: 1px;
      height: 1px;
      padding: 0;
      margin: -1px;
      overflow: hidden;
      clip: rect(0, 0, 0, 0);
      white-space: nowrap;
      border-width: 0;
    }
  `
  document.head.appendChild(style)
}
