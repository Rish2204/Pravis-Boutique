import { defineStore } from 'pinia'

interface UserProfile {
  id: string
  email: string
  firstName?: string
  lastName?: string
  role?: string
}

export const useUserStore = defineStore('user', {
  state: () => ({
    isAuthenticated: false,
    user: null as UserProfile | null,
  }),

  getters: {
    profile: (state) => state.user,

    fullName: (state) => {
      if (!state.user) return ''
      return `${state.user.firstName ?? ''} ${state.user.lastName ?? ''}`.trim()
    },
  },

  actions: {
    setUser(userData: UserProfile) {
      this.user = userData
      this.isAuthenticated = true
    },

    logout() {
      this.isAuthenticated = false
      this.user = null
      if (import.meta.client) {
        localStorage.removeItem('auth-token')
      }
    },
  },
})
