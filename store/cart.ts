import { defineStore } from 'pinia'

interface CartItem {
  id: string | number
  name: string
  price: number
  image?: string
  quantity: number
}

export const useCartStore = defineStore('cart', {
  state: () => ({
    items: [] as CartItem[],
  }),

  getters: {
    count: (state) => state.items.reduce((total, item) => total + item.quantity, 0),

    subtotal: (state) => state.items.reduce((total, item) => total + item.price * item.quantity, 0),

    taxAmount(): number {
      return this.subtotal * 0.08
    },

    total(): number {
      return this.subtotal + this.taxAmount
    },

    isEmpty: (state) => state.items.length === 0,
  },

  actions: {
    addItem(product: Omit<CartItem, 'quantity'>, quantity = 1) {
      const existing = this.items.find((item) => item.id === product.id)

      if (existing) {
        existing.quantity += quantity
      } else {
        this.items.push({ ...product, quantity })
      }

      this.saveCart()
    },

    updateQuantity(productId: string | number, quantity: number) {
      const item = this.items.find((i) => i.id === productId)
      if (!item) return

      if (quantity <= 0) {
        this.removeItem(productId)
        return
      }

      item.quantity = quantity
      this.saveCart()
    },

    removeItem(productId: string | number) {
      const index = this.items.findIndex((i) => i.id === productId)
      if (index !== -1) {
        this.items.splice(index, 1)
        this.saveCart()
      }
    },

    clearCart() {
      this.items = []
      if (import.meta.client) {
        localStorage.removeItem('cart-items')
      }
    },

    saveCart() {
      if (import.meta.client) {
        localStorage.setItem('cart-items', JSON.stringify(this.items))
      }
    },

    loadCart() {
      if (import.meta.client) {
        const saved = localStorage.getItem('cart-items')
        if (saved) {
          try {
            this.items = JSON.parse(saved)
          } catch {
            // Corrupted data, reset
            this.items = []
          }
        }
      }
    },
  },
})
