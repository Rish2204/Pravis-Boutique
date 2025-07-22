// This plugin handles push notification functionality
// Only runs on the client side due to the .client suffix

export default defineNuxtPlugin({
  name: 'push-notifications',
  enforce: 'pre', // run before other plugins
  async setup() {
    const { public: publicRuntimeConfig } = useRuntimeConfig()
    
    // Check if we're in a browser environment and service workers are supported
    const isSupported = 
      process.client && 
      'serviceWorker' in navigator && 
      'PushManager' in window
    
    // Function to request notification permission
    const requestPermission = async () => {
      if (!isSupported) return { granted: false, reason: 'not-supported' }
      
      try {
        const permission = await Notification.requestPermission()
        return { granted: permission === 'granted', reason: permission }
      } catch (error) {
        console.error('Error requesting notification permission:', error)
        return { granted: false, reason: 'error' }
      }
    }
    
    // Function to subscribe to push notifications
    const subscribeToPushNotifications = async (serverPublicKey: string) => {
      if (!isSupported) return null
      
      try {
        const registration = await navigator.serviceWorker.ready
        
        // Get existing subscription or create a new one
        let subscription = await registration.pushManager.getSubscription()
        
        if (!subscription) {
          subscription = await registration.pushManager.subscribe({
            userVisibleOnly: true,
            applicationServerKey: urlBase64ToUint8Array(serverPublicKey)
          })
        }
        
        return subscription
      } catch (error) {
        console.error('Error subscribing to push notifications:', error)
        return null
      }
    }
    
    // Function to unsubscribe from push notifications
    const unsubscribeFromPushNotifications = async () => {
      if (!isSupported) return false
      
      try {
        const registration = await navigator.serviceWorker.ready
        const subscription = await registration.pushManager.getSubscription()
        
        if (subscription) {
          await subscription.unsubscribe()
          return true
        }
        
        return false
      } catch (error) {
        console.error('Error unsubscribing from push notifications:', error)
        return false
      }
    }
    
    // Helper function to convert base64 to Uint8Array
    // (needed for applicationServerKey)
    function urlBase64ToUint8Array(base64String: string) {
      const padding = '='.repeat((4 - (base64String.length % 4)) % 4)
      const base64 = (base64String + padding)
        .replace(/-/g, '+')
        .replace(/_/g, '/')
      
      const rawData = window.atob(base64)
      const outputArray = new Uint8Array(rawData.length)
      
      for (let i = 0; i < rawData.length; ++i) {
        outputArray[i] = rawData.charCodeAt(i)
      }
      
      return outputArray
    }
    
    return {
      provide: {
        pushNotifications: {
          isSupported,
          requestPermission,
          subscribe: subscribeToPushNotifications,
          unsubscribe: unsubscribeFromPushNotifications
        }
      }
    }
  }
})
