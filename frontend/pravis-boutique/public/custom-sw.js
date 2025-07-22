/**
 * Custom Service Worker to handle push notifications
 * This extends the auto-generated service worker from Vite PWA
 */

// Listen for push events
self.addEventListener('push', (event) => {
  // Fallback message
  let notificationData = {
    title: 'New Update',
    body: 'There is new content available.',
    icon: '/icons/icon-192x192.png',
    badge: '/icons/badge-72x72.png',
    data: {
      url: '/'
    }
  };

  // Parse the data from the push event if available
  if (event.data) {
    try {
      notificationData = { ...notificationData, ...JSON.parse(event.data.text()) };
    } catch (error) {
      console.error('Error parsing notification data:', error);
    }
  }

  // Show the notification
  const showNotification = self.registration.showNotification(
    notificationData.title,
    {
      body: notificationData.body,
      icon: notificationData.icon,
      badge: notificationData.badge,
      data: notificationData.data,
      actions: notificationData.actions || [],
      vibrate: [100, 50, 100],
      requireInteraction: notificationData.requireInteraction || false
    }
  );
  
  // Wait until the notification is shown
  event.waitUntil(showNotification);
});

// Handle notification clicks
self.addEventListener('notificationclick', (event) => {
  // Close the notification
  event.notification.close();
  
  // Get the URL to navigate to
  const url = event.notification.data?.url || '/';
  
  // Handle any action clicks
  if (event.action) {
    console.log(`User clicked action: ${event.action}`);
    // You could handle specific actions here
  }
  
  // Open or focus the window with the URL
  const navigateToUrl = clients.matchAll({
    type: 'window',
    includeUncontrolled: true
  }).then((windowClients) => {
    // Check if there's already a window/tab open with the target URL
    for (const client of windowClients) {
      if (client.url === url && 'focus' in client) {
        return client.focus();
      }
    }
    
    // If no window/tab is open, open one
    if (clients.openWindow) {
      return clients.openWindow(url);
    }
  });
  
  event.waitUntil(navigateToUrl);
});

// Handle offline analytics
self.addEventListener('fetch', (event) => {
  const url = new URL(event.request.url);
  
  // Check if the request is for analytics
  if (url.pathname.includes('/analytics') && event.request.method === 'POST') {
    // Clone the request to use it twice
    const analyticsRequest = event.request.clone();
    
    // Try to send the analytics data
    const sendAnalytics = fetch(event.request).catch(() => {
      // If sending fails, store in IndexedDB for later
      return saveAnalyticsOffline(analyticsRequest);
    });
    
    event.waitUntil(sendAnalytics);
  }
});

// Helper function to save analytics data for offline use
async function saveAnalyticsOffline(request) {
  try {
    // Get the request data
    const data = await request.json();
    
    // Open the IndexedDB database
    const db = await openDatabase();
    
    // Add the analytics data to the store
    const tx = db.transaction('offline-analytics', 'readwrite');
    await tx.objectStore('offline-analytics').add({
      timestamp: Date.now(),
      data
    });
    
    await tx.complete;
    console.log('Saved analytics data for offline use');
  } catch (error) {
    console.error('Error saving offline analytics:', error);
  }
}

// Helper function to open the IndexedDB database
function openDatabase() {
  return new Promise((resolve, reject) => {
    const request = indexedDB.open('pravis-boutique-offline', 1);
    
    request.onupgradeneeded = (event) => {
      const db = event.target.result;
      db.createObjectStore('offline-analytics', { keyPath: 'timestamp' });
    };
    
    request.onsuccess = (event) => {
      resolve(event.target.result);
    };
    
    request.onerror = (event) => {
      reject(event.target.error);
    };
  });
}

// Periodic sync for offline analytics
self.addEventListener('periodicsync', (event) => {
  if (event.tag === 'sync-offline-analytics') {
    event.waitUntil(syncOfflineAnalytics());
  }
});

// Function to sync offline analytics
async function syncOfflineAnalytics() {
  try {
    const db = await openDatabase();
    const tx = db.transaction('offline-analytics', 'readonly');
    const store = tx.objectStore('offline-analytics');
    const items = await store.getAll();
    
    if (items.length === 0) {
      return;
    }
    
    console.log(`Attempting to sync ${items.length} offline analytics records`);
    
    // Batch the items and send them
    const analyticsEndpoint = '/api/analytics/batch';
    
    const response = await fetch(analyticsEndpoint, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ items: items.map(item => item.data) })
    });
    
    if (response.ok) {
      // If successful, clear the items from IndexedDB
      const deleteTx = db.transaction('offline-analytics', 'readwrite');
      const deleteStore = deleteTx.objectStore('offline-analytics');
      
      for (const item of items) {
        await deleteStore.delete(item.timestamp);
      }
      
      await deleteTx.complete;
      console.log(`Successfully synced ${items.length} analytics records`);
    }
  } catch (error) {
    console.error('Error syncing offline analytics:', error);
  }
}
