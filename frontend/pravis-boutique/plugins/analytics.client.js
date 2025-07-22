import { useAnalyticsStore } from '~/store/analytics';

export default defineNuxtPlugin(({ $router }) => {
  const analyticsStore = useAnalyticsStore();
  
  // Initialize analytics service
  analyticsStore.initialize();
  
  // Track page views on route changes
  $router.afterEach((to) => {
    if (process.client) {
      analyticsStore.trackPageView(to.fullPath);
    }
  });
  
  // Return utility functions for tracking events throughout the app
  return {
    provide: {
      analytics: {
        // Track user interactions
        trackInteraction: (element, action, context = {}) => {
          analyticsStore.trackInteraction(element, action, context);
        },
        
        // Track product interactions
        trackProductInteraction: (productId, action, details = {}) => {
          analyticsStore.trackProductInteraction(productId, action, details);
        },
        
        // Track voice interactions
        trackVoiceInteraction: (command, response, context = {}) => {
          analyticsStore.trackVoiceInteraction(command, response, context);
        },
        
        // Check if user has given consent
        hasConsent: () => analyticsStore.hasConsent,
        
        // Open consent dialog programmatically (useful for voice features)
        requestConsent: () => {
          // Return a promise that resolves when consent decision is made
          return new Promise((resolve) => {
            // Create and mount the consent dialog
            const consentDialog = document.createElement('div');
            document.body.appendChild(consentDialog);
            
            // Use Vue to render the dialog
            createApp({
              template: '<ConsentDialog @consentDecision="onDecision" />',
              components: {
                ConsentDialog: defineAsyncComponent(() => import('@/components/common/ConsentDialog.vue'))
              },
              setup() {
                const onDecision = (decision) => {
                  // Clean up the dialog
                  document.body.removeChild(consentDialog);
                  
                  // Resolve the promise with the decision
                  resolve(decision);
                };
                
                return { onDecision };
              }
            }).mount(consentDialog);
          });
        }
      }
    }
  };
});
