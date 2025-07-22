<template>
  <div v-if="isSupported" class="push-notification-manager">
    <div v-if="permissionState === 'default'" class="notification-prompt">
      <p>{{ promptMessage }}</p>
      <button @click="requestPermission" class="prompt-button">
        Enable notifications
      </button>
    </div>
    <div v-else-if="permissionState === 'denied'" class="notification-denied">
      <p>
        Notifications are blocked. Please update your browser settings to enable
        notifications for this site.
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
// Use the push notification composable
const { isSupported, permissionState, requestPermission } = usePushNotifications()

// Server public key for VAPID (would come from environment variables in production)
// This is a placeholder and should be replaced with an actual key
const serverPublicKey = 'BL3lQNL3MtivHDizzQgRQtSNS3LzG9sFV9jz9kIqcMIXfNbDqnS27BBRptj7gSn_4gNT_RUAkfBgWzfUPdUXVYU'

// Define the notification prompt message
const promptMessage = computed(() => {
  return 'Would you like to receive notifications for new products, promotions, and order updates?'
})

// Handle permission request
const handlePermissionRequest = async () => {
  const result = await requestPermission()
  
  // If permission granted, subscribe to push notifications
  if (result.granted) {
    const { subscribe } = usePushNotifications()
    const subscription = await subscribe(serverPublicKey)
    
    // Here you would typically send the subscription object to your server
    // to store it for future push notification sending
    if (subscription) {
      console.log('Successfully subscribed to push notifications')
      // In a real app, you would do something like:
      // await $fetch('/api/push-subscriptions', {
      //   method: 'POST',
      //   body: { subscription }
      // })
    }
  }
}
</script>

<style scoped>
.push-notification-manager {
  margin: 1rem 0;
  padding: 1rem;
  border-radius: 0.5rem;
  background-color: #f8f9fa;
}

.notification-prompt,
.notification-denied {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.prompt-button {
  padding: 0.5rem 1rem;
  background-color: #4a90e2;
  color: white;
  border: none;
  border-radius: 0.25rem;
  cursor: pointer;
  font-weight: 500;
  align-self: flex-start;
}

.prompt-button:hover {
  background-color: #3a80d2;
}

.notification-denied {
  color: #721c24;
  background-color: #f8d7da;
  padding: 0.75rem;
  border-radius: 0.25rem;
}
</style>
