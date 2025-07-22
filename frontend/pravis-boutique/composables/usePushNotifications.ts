// Composable for easy access to push notification functionality throughout the app

export const usePushNotifications = () => {
  const { $pushNotifications } = useNuxtApp()
  
  // Reactive state for notification permission
  const permissionState = ref<NotificationPermission | 'default'>('default')
  
  // Check if push notifications are supported
  const isSupported = computed(() => {
    return $pushNotifications?.isSupported || false
  })
  
  // Check current permission state
  const checkPermission = () => {
    if (process.client && 'Notification' in window) {
      permissionState.value = Notification.permission
    }
    return permissionState.value
  }
  
  // Request permission to send notifications
  const requestPermission = async () => {
    if (!$pushNotifications) return { granted: false, reason: 'not-initialized' }
    
    const result = await $pushNotifications.requestPermission()
    
    // Update the permission state
    if (process.client && 'Notification' in window) {
      permissionState.value = Notification.permission
    }
    
    return result
  }
  
  // Subscribe to push notifications with the server's public key
  const subscribe = async (serverPublicKey: string) => {
    if (!$pushNotifications) return null
    return await $pushNotifications.subscribe(serverPublicKey)
  }
  
  // Unsubscribe from push notifications
  const unsubscribe = async () => {
    if (!$pushNotifications) return false
    return await $pushNotifications.unsubscribe()
  }
  
  // Initialize: check permission on client-side
  onMounted(() => {
    checkPermission()
  })
  
  return {
    isSupported,
    permissionState,
    checkPermission,
    requestPermission,
    subscribe,
    unsubscribe
  }
}
