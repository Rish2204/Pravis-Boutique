import { describe, it, expect, vi, beforeEach } from 'vitest'
import { usePushNotifications } from './usePushNotifications'

// Mock service worker
const mockServiceWorker = {
  ready: vi.fn().mockResolvedValue({
    pushManager: {
      getSubscription: vi.fn(),
      subscribe: vi.fn()
    }
  })
}

// Mock window object
global.navigator.serviceWorker = mockServiceWorker

// Mock local storage
const localStorageMock = (() => {
  let store = {}
  return {
    getItem: vi.fn((key) => store[key] || null),
    setItem: vi.fn((key, value) => {
      store[key] = value.toString()
    }),
    clear: vi.fn(() => {
      store = {}
    }),
    removeItem: vi.fn((key) => {
      delete store[key]
    })
  }
})()

Object.defineProperty(window, 'localStorage', {
  value: localStorageMock
})

describe('usePushNotifications', () => {
  beforeEach(() => {
    vi.clearAllMocks()
    localStorageMock.clear()
  })

  it('should check if push notifications are supported', () => {
    const { isPushSupported } = usePushNotifications()
    
    // Since we mocked service worker, it should be supported
    expect(isPushSupported.value).toBe(true)
  })

  it('should handle notification permission status', async () => {
    // Mock permission status
    vi.spyOn(Notification, 'permission', 'get').mockReturnValue('default')
    
    const { permissionStatus, requestPermission } = usePushNotifications()
    
    expect(permissionStatus.value).toBe('default')
    
    // Mock permission request
    const requestPermissionSpy = vi.spyOn(Notification, 'requestPermission')
    requestPermissionSpy.mockResolvedValueOnce('granted')
    
    await requestPermission()
    
    expect(requestPermissionSpy).toHaveBeenCalled()
  })

  it('should try to subscribe to push notifications', async () => {
    // Mock subscription status
    const mockSubscription = {
      endpoint: 'https://example.com/push-endpoint',
      getKey: vi.fn((key) => new Uint8Array([1, 2, 3]))
    }
    
    mockServiceWorker.ready.mockResolvedValue({
      pushManager: {
        getSubscription: vi.fn().mockResolvedValue(null),
        subscribe: vi.fn().mockResolvedValue(mockSubscription)
      }
    })
    
    const { subscribe, currentSubscription } = usePushNotifications()
    
    // Initial state should be null
    expect(currentSubscription.value).toBe(null)
    
    // Subscribe
    await subscribe({
      userVisibleOnly: true,
      applicationServerKey: 'test-key'
    })
    
    // After subscribing, the subscription should be set
    expect(currentSubscription.value).not.toBe(null)
  })
})
