/**
 * Accessibility Plugin for Pravis Boutique
 * 
 * This plugin initializes accessibility features when the app loads on the client side.
 * It sets up keyboard focus styles, creates an ARIA live region for announcements,
 * and initializes any required global accessibility handlers.
 */

import { initKeyboardFocusStyles } from '~/utils/accessibility'

export default defineNuxtPlugin({
  name: 'accessibility-plugin',
  enforce: 'pre', // Run before other plugins
  async setup (nuxtApp) {
    // Only run on client side
    if (process.client) {
      // Initialize keyboard focus styles after DOM is loaded
      window.addEventListener('DOMContentLoaded', () => {
        // Initialize keyboard focus styles
        initKeyboardFocusStyles()
        
        // Create global ARIA live region for announcements
        const ariaLive = document.createElement('div')
        ariaLive.id = 'aria-live-announcer'
        ariaLive.className = 'sr-only'
        ariaLive.setAttribute('aria-live', 'polite')
        ariaLive.setAttribute('aria-atomic', 'true')
        document.body.appendChild(ariaLive)

        // Create global ARIA alert region for more urgent announcements
        const ariaAlert = document.createElement('div')
        ariaAlert.id = 'aria-alert-announcer'
        ariaAlert.className = 'sr-only'
        ariaAlert.setAttribute('aria-live', 'assertive')
        ariaAlert.setAttribute('aria-atomic', 'true')
        document.body.appendChild(ariaAlert)
        
        // Add skip to main content link at the beginning of the body
        const skipLink = document.createElement('a')
        skipLink.href = '#main-content'
        skipLink.className = 'skip-to-content'
        skipLink.textContent = 'Skip to main content'
        document.body.insertBefore(skipLink, document.body.firstChild)
        
        // Add CSS for skip link
        const style = document.createElement('style')
        style.textContent = `
          .skip-to-content {
            position: absolute;
            top: -40px;
            left: 0;
            background: #3498db;
            color: white;
            padding: 8px;
            z-index: 100;
            transition: top 0.2s;
          }
          
          .skip-to-content:focus {
            top: 0;
          }
          
          #main-content {
            outline: none;
          }
        `
        document.head.appendChild(style)
        
        // Listen for route changes to announce page navigation
        nuxtApp.$router.afterEach((to) => {
          const pageTitle = document.title || to.meta.title || to.name || 'Page'
          setTimeout(() => {
            const announcer = document.getElementById('aria-live-announcer')
            if (announcer) {
              announcer.textContent = `Navigated to ${pageTitle}`
            }
          }, 100)
        })
      })
      
      // Log that accessibility features are initialized
      console.info('✓ Accessibility features initialized')
    }
  }
})
