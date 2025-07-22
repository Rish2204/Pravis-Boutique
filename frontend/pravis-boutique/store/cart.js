import { defineStore } from 'pinia'

/**
 * Cart store for managing shopping cart state
 */
export const useCartStore = defineStore('cart', {
  state: () => ({
    items: [],
    loading: false,
    error: null,
    checkoutStatus: null
  }),
  
  getters: {
    /**
     * Get total number of items in cart
     */
    count: (state) => state.items.reduce((total, item) => total + item.quantity, 0),
    
    /**
     * Get all items in cart
     */
    cartItems: (state) => state.items,
    
    /**
     * Calculate cart subtotal
     */
    subtotal: (state) => {
      return state.items.reduce((total, item) => {
        return total + (item.price * item.quantity)
      }, 0)
    },
    
    /**
     * Calculate estimated tax amount
     * Using a simple 8% tax rate for demonstration
     */
    taxAmount: (state, getters) => {
      return getters.subtotal * 0.08
    },
    
    /**
     * Calculate grand total
     */
    total: (state, getters) => {
      return getters.subtotal + getters.taxAmount
    },
    
    /**
     * Check if cart is empty
     */
    isEmpty: (state) => state.items.length === 0
  },
  
  actions: {
    /**
     * Add item to cart
     * @param {Object} product - Product to add to cart
     * @param {number} quantity - Quantity to add
     */
    addItem(product, quantity = 1) {
      const existingItem = this.items.find(item => item.id === product.id)
      
      if (existingItem) {
        // Increase quantity if product already in cart
        existingItem.quantity += quantity
      } else {
        // Add new item to cart
        this.items.push({
          id: product.id,
          name: product.name,
          price: product.price,
          image: product.image,
          quantity
        })
      }
      
      // Persist cart to localStorage
      this.saveCart()
      
      return true
    },
    
    /**
     * Update item quantity
     * @param {string|number} productId - Product ID to update
     * @param {number} quantity - New quantity
     */
    updateQuantity(productId, quantity) {
      const item = this.items.find(item => item.id === productId)
      
      if (item) {
        if (quantity <= 0) {
          // Remove item if quantity is zero or negative
          return this.removeItem(productId)
        }
        
        item.quantity = quantity
        this.saveCart()
        return true
      }
      
      return false
    },
    
    /**
     * Remove item from cart
     * @param {string|number} productId - Product ID to remove
     */
    removeItem(productId) {
      const index = this.items.findIndex(item => item.id === productId)
      
      if (index !== -1) {
        this.items.splice(index, 1)
        this.saveCart()
        return true
      }
      
      return false
    },
    
    /**
     * Clear all items from cart
     */
    clearCart() {
      this.items = []
      this.checkoutStatus = null
      
      // Clear cart in localStorage
      if (process.client) {
        localStorage.removeItem('cart-items')
      }
    },
    
    /**
     * Save cart to localStorage
     */
    saveCart() {
      if (process.client) {
        localStorage.setItem('cart-items', JSON.stringify(this.items))
      }
    },
    
    /**
     * Load cart from localStorage
     */
    loadCart() {
      if (process.client) {
        const savedCart = localStorage.getItem('cart-items')
        if (savedCart) {
          try {
            this.items = JSON.parse(savedCart)
          } catch (e) {
            console.error('Failed to parse cart data from localStorage')
          }
        }
      }
    },
    
    /**
     * Process cart checkout
     * @param {Object} checkoutData - Checkout information (shipping, payment, etc)
     */
    async checkout(checkoutData) {
      this.loading = true
      this.checkoutStatus = 'processing'
      this.error = null
      
      try {
        const { useApi } = useNuxtApp()
        const { post } = useApi()
        
        // Prepare order data
        const orderData = {
          items: this.items,
          subtotal: this.subtotal,
          tax: this.taxAmount,
          total: this.total,
          ...checkoutData
        }
        
        // Submit order to API
        const response = await post('/orders', orderData)
        
        if (response.success) {
          this.checkoutStatus = 'success'
          this.clearCart()
          return response.orderId
        } else {
          this.checkoutStatus = 'failed'
          this.error = response.message || 'Checkout failed'
          return false
        }
      } catch (err) {
        this.checkoutStatus = 'failed'
        this.error = err.message || 'Checkout process failed'
        return false
      } finally {
        this.loading = false
      }
    }
  }
})
