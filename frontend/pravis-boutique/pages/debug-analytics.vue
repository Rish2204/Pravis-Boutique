<template>
  <div class="min-h-screen bg-gray-100 dark:bg-gray-900 p-6">
    <div class="max-w-7xl mx-auto">
      <div class="mb-8">
        <h1 class="text-3xl font-bold text-gray-900 dark:text-white mb-2">
          📊 Analytics Debug Dashboard
        </h1>
        <p class="text-gray-600 dark:text-gray-400">
          Real-time analytics and user interaction tracking for Pravis Boutique
        </p>
      </div>

      <!-- Quick Actions -->
      <div class="mb-8 flex flex-wrap gap-4">
        <button 
          @click="exportData"
          class="bg-pravis-600 text-white px-4 py-2 rounded-md hover:bg-pravis-700 transition-colors"
        >
          📥 Export Analytics
        </button>
        <button 
          @click="clearData"
          class="bg-red-600 text-white px-4 py-2 rounded-md hover:bg-red-700 transition-colors"
        >
          🗑️ Clear All Data
        </button>
        <button 
          @click="toggleAutoRefresh"
          :class="[
            'px-4 py-2 rounded-md transition-colors',
            autoRefresh 
              ? 'bg-green-600 text-white hover:bg-green-700' 
              : 'bg-gray-600 text-white hover:bg-gray-700'
          ]"
        >
          {{ autoRefresh ? '⏸️ Stop Auto-refresh' : '▶️ Start Auto-refresh' }}
        </button>
      </div>

      <!-- Analytics Summary -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow">
          <h3 class="text-sm font-medium text-gray-500 dark:text-gray-400 mb-2">Session ID</h3>
          <p class="text-xs font-mono text-gray-900 dark:text-white break-all">{{ summary.sessionId }}</p>
          <p class="text-xs text-gray-500 dark:text-gray-400 mt-1">Duration: {{ formatDuration(summary.sessionDuration) }}</p>
        </div>
        
        <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow">
          <h3 class="text-sm font-medium text-gray-500 dark:text-gray-400 mb-2">Events</h3>
          <p class="text-2xl font-bold text-pravis-600">{{ summary.eventsCount }}</p>
          <p class="text-xs text-gray-500 dark:text-gray-400">Total events logged</p>
        </div>
        
        <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow">
          <h3 class="text-sm font-medium text-gray-500 dark:text-gray-400 mb-2">Page Views</h3>
          <p class="text-2xl font-bold text-indigo-600">{{ summary.pageViewsCount }}</p>
          <p class="text-xs text-gray-500 dark:text-gray-400">Pages visited</p>
        </div>
        
        <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow">
          <h3 class="text-sm font-medium text-gray-500 dark:text-gray-400 mb-2">Interactions</h3>
          <p class="text-2xl font-bold text-saffron-600">{{ summary.interactionsCount }}</p>
          <p class="text-xs text-gray-500 dark:text-gray-400">User interactions</p>
        </div>
      </div>

      <!-- Data Tables -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
        
        <!-- Recent Events -->
        <div class="bg-white dark:bg-gray-800 rounded-lg shadow">
          <div class="p-6 border-b border-gray-200 dark:border-gray-700">
            <h2 class="text-lg font-semibold text-gray-900 dark:text-white">Recent Events</h2>
          </div>
          <div class="max-h-96 overflow-y-auto">
            <div v-if="recentEvents.length === 0" class="p-6 text-center text-gray-500 dark:text-gray-400">
              No events yet. Start navigating the site!
            </div>
            <div v-else class="divide-y divide-gray-200 dark:divide-gray-700">
              <div 
                v-for="event in recentEvents" 
                :key="event.id"
                class="p-4 hover:bg-gray-50 dark:hover:bg-gray-700"
              >
                <div class="flex items-center justify-between mb-2">
                  <span class="text-sm font-medium text-gray-900 dark:text-white">
                    {{ event.eventName }}
                  </span>
                  <span class="text-xs text-gray-500 dark:text-gray-400">
                    {{ formatTime(event.timestamp) }}
                  </span>
                </div>
                <div class="text-xs text-gray-600 dark:text-gray-300 mb-1">
                  {{ event.path }}
                </div>
                <div class="text-xs text-gray-500 dark:text-gray-400">
                  {{ formatEventData(event.data) }}
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Recent Interactions -->
        <div class="bg-white dark:bg-gray-800 rounded-lg shadow">
          <div class="p-6 border-b border-gray-200 dark:border-gray-700">
            <h2 class="text-lg font-semibold text-gray-900 dark:text-white">User Interactions</h2>
          </div>
          <div class="max-h-96 overflow-y-auto">
            <div v-if="recentInteractions.length === 0" class="p-6 text-center text-gray-500 dark:text-gray-400">
              No interactions yet. Click around!
            </div>
            <div v-else class="divide-y divide-gray-200 dark:divide-gray-700">
              <div 
                v-for="interaction in recentInteractions" 
                :key="interaction.id"
                class="p-4 hover:bg-gray-50 dark:hover:bg-gray-700"
              >
                <div class="flex items-center justify-between mb-2">
                  <span class="text-sm font-medium text-gray-900 dark:text-white">
                    {{ interaction.action }} → {{ interaction.element }}
                  </span>
                  <span class="text-xs text-gray-500 dark:text-gray-400">
                    {{ formatTime(interaction.timestamp) }}
                  </span>
                </div>
                <div class="text-xs text-gray-600 dark:text-gray-300 mb-1">
                  {{ interaction.path }}
                </div>
                <div v-if="interaction.details.textContent" class="text-xs text-gray-500 dark:text-gray-400 truncate">
                  "{{ interaction.details.textContent }}"
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Page Views -->
        <div class="bg-white dark:bg-gray-800 rounded-lg shadow">
          <div class="p-6 border-b border-gray-200 dark:border-gray-700">
            <h2 class="text-lg font-semibold text-gray-900 dark:text-white">Page Views</h2>
          </div>
          <div class="max-h-96 overflow-y-auto">
            <div v-if="recentPageViews.length === 0" class="p-6 text-center text-gray-500 dark:text-gray-400">
              No page views yet.
            </div>
            <div v-else class="divide-y divide-gray-200 dark:divide-gray-700">
              <div 
                v-for="pageView in recentPageViews" 
                :key="pageView.id"
                class="p-4 hover:bg-gray-50 dark:hover:bg-gray-700"
              >
                <div class="flex items-center justify-between mb-2">
                  <span class="text-sm font-medium text-gray-900 dark:text-white">
                    {{ pageView.path }}
                  </span>
                  <span class="text-xs text-gray-500 dark:text-gray-400">
                    {{ formatTime(pageView.timestamp) }}
                  </span>
                </div>
                <div class="text-xs text-gray-600 dark:text-gray-300 mb-1">
                  {{ pageView.title }}
                </div>
                <div class="text-xs text-gray-500 dark:text-gray-400">
                  Load time: {{ Math.round(pageView.loadTime) }}ms | {{ pageView.viewport }}
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Local Storage Data -->
        <div class="bg-white dark:bg-gray-800 rounded-lg shadow">
          <div class="p-6 border-b border-gray-200 dark:border-gray-700">
            <h2 class="text-lg font-semibold text-gray-900 dark:text-white">Local Storage</h2>
          </div>
          <div class="max-h-96 overflow-y-auto p-4">
            <div class="space-y-4">
              <div>
                <h4 class="text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Analytics Keys</h4>
                <div class="text-xs text-gray-600 dark:text-gray-400 space-y-1">
                  <div v-for="key in localStorageKeys" :key="key">
                    <span class="font-mono">{{ key }}</span>
                    <span class="ml-2 text-gray-500">
                      ({{ getLocalStorageSize(key) }} items)
                    </span>
                  </div>
                </div>
              </div>
              
              <div v-if="cookieData.length > 0">
                <h4 class="text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Tracked Cookies</h4>
                <div class="text-xs text-gray-600 dark:text-gray-400 space-y-1">
                  <div v-for="cookie in cookieData" :key="cookie.name">
                    <span class="font-mono">{{ cookie.name }}</span>
                    <span class="ml-2 text-gray-500">
                      = {{ cookie.value.slice(0, 20) }}{{ cookie.value.length > 20 ? '...' : '' }}
                    </span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Raw Data Export -->
      <div class="mt-8 bg-white dark:bg-gray-800 rounded-lg shadow">
        <div class="p-6 border-b border-gray-200 dark:border-gray-700">
          <h2 class="text-lg font-semibold text-gray-900 dark:text-white">Raw Analytics Store</h2>
          <p class="text-sm text-gray-600 dark:text-gray-400 mt-1">
            Complete analytics data structure (JSON)
          </p>
        </div>
        <div class="p-6">
          <pre class="bg-gray-100 dark:bg-gray-900 p-4 rounded text-xs overflow-auto max-h-64 text-gray-800 dark:text-gray-200">{{ JSON.stringify(analyticsStore, null, 2) }}</pre>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'

// Page metadata
useHead({
  title: 'Analytics Debug - Pravis Boutique',
  meta: [
    { name: 'robots', content: 'noindex,nofollow' }
  ]
})

const { analyticsStore, exportAnalyticsData, clearAnalyticsData } = useAnalytics()

// Reactive data
const autoRefresh = ref(false)
let refreshInterval = null

// Computed properties  
const summary = computed(() => {
  return {
    sessionId: analyticsStore.sessionId || 'Not started',
    userId: analyticsStore.userId || 'Anonymous',
    eventsCount: analyticsStore.events?.length || 0,
    pageViewsCount: analyticsStore.pageViews?.length || 0,
    interactionsCount: analyticsStore.userInteractions?.length || 0,
    errorsCount: analyticsStore.errors?.length || 0,
    performanceCount: analyticsStore.performance?.length || 0,
    cookiesCount: analyticsStore.cookies?.size || 0,
    cacheCount: analyticsStore.cache?.size || 0,
    sessionDuration: analyticsStore.events?.length > 0 
      ? new Date() - new Date(analyticsStore.events[0].timestamp)
      : 0
  }
})

const recentEvents = computed(() => {
  return [...(analyticsStore.events || [])].reverse().slice(0, 20)
})

const recentInteractions = computed(() => {
  return [...(analyticsStore.userInteractions || [])].reverse().slice(0, 20)
})

const recentPageViews = computed(() => {
  return [...(analyticsStore.pageViews || [])].reverse().slice(0, 10)
})

const localStorageKeys = computed(() => {
  const keys = []
  for (let i = 0; i < localStorage.length; i++) {
    const key = localStorage.key(i)
    if (key?.startsWith('pravis_analytics_')) {
      keys.push(key)
    }
  }
  return keys
})

const cookieData = computed(() => {
  return Array.from(analyticsStore.cookies?.values() || [])
})

// Methods
const exportData = () => {
  exportAnalyticsData()
}

const clearData = () => {
  if (confirm('Are you sure you want to clear all analytics data?')) {
    clearAnalyticsData()
  }
}

const toggleAutoRefresh = () => {
  autoRefresh.value = !autoRefresh.value
  
  if (autoRefresh.value) {
    refreshInterval = setInterval(() => {
      // Force reactivity update
      analyticsStore.events = [...analyticsStore.events]
    }, 2000)
  } else {
    if (refreshInterval) {
      clearInterval(refreshInterval)
      refreshInterval = null
    }
  }
}

const formatTime = (timestamp) => {
  return new Date(timestamp).toLocaleTimeString()
}

const formatDuration = (ms) => {
  const seconds = Math.floor(ms / 1000)
  const minutes = Math.floor(seconds / 60)
  const hours = Math.floor(minutes / 60)
  
  if (hours > 0) return `${hours}h ${minutes % 60}m`
  if (minutes > 0) return `${minutes}m ${seconds % 60}s`
  return `${seconds}s`
}

const formatEventData = (data) => {
  if (!data || typeof data !== 'object') return ''
  const entries = Object.entries(data).slice(0, 3)
  return entries.map(([key, value]) => `${key}: ${String(value).slice(0, 30)}`).join(', ')
}

const getLocalStorageSize = (key) => {
  try {
    const data = JSON.parse(localStorage.getItem(key) || '[]')
    return Array.isArray(data) ? data.length : 1
  } catch {
    return 0
  }
}

onUnmounted(() => {
  if (refreshInterval) {
    clearInterval(refreshInterval)
  }
})
</script>