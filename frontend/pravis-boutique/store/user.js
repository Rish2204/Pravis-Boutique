import { defineStore } from 'pinia'

/**
 * User store for managing authentication and user profile data
 */
export const useUserStore = defineStore('user', {
  state: () => ({
    // User authentication state
    isAuthenticated: false,
    token: null,
    user: null,
    loading: false,
    error: null,
  }),
  
  getters: {
    // Get current user profile
    profile: (state) => state.user,
    
    // Check if user is authenticated
    authenticated: (state) => state.isAuthenticated,
    
    // Check if user is admin
    isAdmin: (state) => state.user?.role === 'admin',
    
    // Get user's full name
    fullName: (state) => {
      if (!state.user) return ''
      return `${state.user.firstName || ''} ${state.user.lastName || ''}`.trim()
    }
  },
  
  actions: {
    /**
     * Login user with credentials
     * @param {Object} credentials - User login credentials
     */
    async login(credentials) {
      const { email, password } = credentials
      this.loading = true
      this.error = null
      
      try {
        const { useApi } = useNuxtApp()
        const { post } = useApi()
        
        const response = await post('/auth/login', { email, password })
        
        if (response.token) {
          this.setToken(response.token)
          this.setUser(response.user)
          this.isAuthenticated = true
          
          // Store token in localStorage for persistence
          if (process.client) {
            localStorage.setItem('auth-token', response.token)
          }
          
          return true
        }
        
        return false
      } catch (err) {
        this.error = err.message || 'Authentication failed'
        return false
      } finally {
        this.loading = false
      }
    },
    
    /**
     * Register a new user account
     * @param {Object} userData - New user registration data
     */
    async register(userData) {
      this.loading = true
      this.error = null
      
      try {
        const { useApi } = useNuxtApp()
        const { post } = useApi()
        
        const response = await post('/auth/register', userData)
        
        if (response.success) {
          // Auto-login if registration successful
          if (response.token) {
            this.setToken(response.token)
            this.setUser(response.user)
            this.isAuthenticated = true
            
            // Store token in localStorage for persistence
            if (process.client) {
              localStorage.setItem('auth-token', response.token)
            }
          }
          
          return true
        }
        
        return false
      } catch (err) {
        this.error = err.message || 'Registration failed'
        return false
      } finally {
        this.loading = false
      }
    },
    
    /**
     * Logout current user
     */
    logout() {
      this.isAuthenticated = false
      this.token = null
      this.user = null
      
      // Remove token from localStorage
      if (process.client) {
        localStorage.removeItem('auth-token')
      }
    },
    
    /**
     * Set authentication token
     * @param {string} token - JWT auth token
     */
    setToken(token) {
      this.token = token
    },
    
    /**
     * Set user profile data
     * @param {Object} userData - User profile data
     */
    setUser(userData) {
      this.user = userData
    },
    
    /**
     * Check if token exists and restore session
     */
    async initAuth() {
      // Skip on server-side
      if (!process.client) return
      
      const token = localStorage.getItem('auth-token')
      if (!token) return
      
      this.setToken(token)
      
      try {
        const { useApi } = useNuxtApp()
        const { get } = useApi()
        
        // Fetch user profile with token
        const user = await get('/auth/me', {
          headers: {
            Authorization: `Bearer ${token}`
          }
        })
        
        if (user) {
          this.setUser(user)
          this.isAuthenticated = true
        }
      } catch (err) {
        // Token invalid, clear auth state
        this.logout()
      }
    },
    
    /**
     * Update user profile
     * @param {Object} profileData - User profile data to update
     */
    async updateProfile(profileData) {
      if (!this.isAuthenticated) return false
      
      this.loading = true
      this.error = null
      
      try {
        const { useApi } = useNuxtApp()
        const { put } = useApi()
        
        const response = await put('/auth/profile', profileData, {
          headers: {
            Authorization: `Bearer ${this.token}`
          }
        })
        
        if (response.user) {
          this.setUser(response.user)
          return true
        }
        
        return false
      } catch (err) {
        this.error = err.message || 'Failed to update profile'
        return false
      } finally {
        this.loading = false
      }
    }
  }
})
