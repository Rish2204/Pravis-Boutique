/**
 * Composable for handling product-related API requests
 */
export const useProducts = () => {
  // Get core API utilities
  const { get, post } = useApi()
  
  // State
  const products = ref([])
  const featuredProducts = ref([])
  const loading = ref(false)
  const error = ref(null)
  
  /**
   * Fetch all products
   * @param {Object} options - Query options (category, limit, sort, etc.)
   * @returns {Promise<Array>} - Array of products
   */
  const getProducts = async (options = {}) => {
    loading.value = true
    error.value = null
    
    try {
      // Build query parameters
      const queryParams = new URLSearchParams()
      
      if (options.category) {
        queryParams.append('category', options.category)
      }
      
      if (options.limit) {
        queryParams.append('limit', options.limit.toString())
      }
      
      if (options.sort) {
        queryParams.append('sort', options.sort)
      }
      
      if (options.page) {
        queryParams.append('page', options.page.toString())
      }
      
      const queryString = queryParams.toString() ? `?${queryParams.toString()}` : ''
      const data = await get(`/products${queryString}`)
      
      products.value = data.products || data || []
      return products.value
    } catch (err) {
      error.value = err.message || 'Failed to fetch products'
      return []
    } finally {
      loading.value = false
    }
  }
  
  /**
   * Fetch a single product by ID
   * @param {string|number} id - Product ID
   * @returns {Promise<Object|null>} - Product data
   */
  const getProduct = async (id) => {
    if (!id) {
      error.value = 'Product ID is required'
      return null
    }
    
    loading.value = true
    error.value = null
    
    try {
      const data = await get(`/products/${id}`)
      return data
    } catch (err) {
      error.value = err.message || `Failed to fetch product with ID: ${id}`
      return null
    } finally {
      loading.value = false
    }
  }
  
  /**
   * Fetch featured products
   * @param {number} limit - Maximum number of products to fetch
   * @returns {Promise<Array>} - Array of featured products
   */
  const getFeaturedProducts = async (limit = 6) => {
    loading.value = true
    error.value = null
    
    try {
      const data = await get(`/products/featured?limit=${limit}`)
      featuredProducts.value = data.products || data || []
      return featuredProducts.value
    } catch (err) {
      error.value = err.message || 'Failed to fetch featured products'
      return []
    } finally {
      loading.value = false
    }
  }
  
  /**
   * Search products
   * @param {string} query - Search query
   * @param {Object} options - Additional search options
   * @returns {Promise<Array>} - Array of matching products
   */
  const searchProducts = async (query, options = {}) => {
    loading.value = true
    error.value = null
    
    try {
      // Build query parameters
      const queryParams = new URLSearchParams()
      queryParams.append('q', query)
      
      if (options.category) {
        queryParams.append('category', options.category)
      }
      
      if (options.limit) {
        queryParams.append('limit', options.limit.toString())
      }
      
      if (options.sort) {
        queryParams.append('sort', options.sort)
      }
      
      if (options.page) {
        queryParams.append('page', options.page.toString())
      }
      
      const queryString = queryParams.toString() ? `?${queryParams.toString()}` : ''
      const data = await get(`/products/search${queryString}`)
      
      return data.products || data || []
    } catch (err) {
      error.value = err.message || 'Failed to search products'
      return []
    } finally {
      loading.value = false
    }
  }
  
  /**
   * Get product categories
   * @returns {Promise<Array>} - Array of categories
   */
  const getCategories = async () => {
    loading.value = true
    error.value = null
    
    try {
      const data = await get('/products/categories')
      return data.categories || data || []
    } catch (err) {
      error.value = err.message || 'Failed to fetch product categories'
      return []
    } finally {
      loading.value = false
    }
  }
  
  /**
   * Get related products
   * @param {string|number} productId - Product ID to find related items for
   * @param {number} limit - Maximum number of related products to fetch
   * @returns {Promise<Array>} - Array of related products
   */
  const getRelatedProducts = async (productId, limit = 4) => {
    loading.value = true
    error.value = null
    
    try {
      const data = await get(`/products/${productId}/related?limit=${limit}`)
      return data.products || data || []
    } catch (err) {
      error.value = err.message || 'Failed to fetch related products'
      return []
    } finally {
      loading.value = false
    }
  }
  
  /**
   * Submit a product review
   * @param {string|number} productId - Product ID to review
   * @param {Object} reviewData - Review data (rating, comment, etc.)
   * @returns {Promise<Object|null>} - Submitted review data
   */
  const submitReview = async (productId, reviewData) => {
    loading.value = true
    error.value = null
    
    try {
      const data = await post(`/products/${productId}/reviews`, reviewData)
      return data
    } catch (err) {
      error.value = err.message || 'Failed to submit product review'
      return null
    } finally {
      loading.value = false
    }
  }
  
  return {
    // State
    products: readonly(products),
    featuredProducts: readonly(featuredProducts),
    loading: readonly(loading),
    error: readonly(error),
    
    // Methods
    getProducts,
    getProduct,
    getFeaturedProducts,
    searchProducts,
    getCategories,
    getRelatedProducts,
    submitReview
  }
}
