import { ref, useRuntimeConfig } from 'nuxt/app'

/**
 * Composable for handling API requests
 * 
 * @returns {Object} API utilities and state
 */
export const useApi = () => {
  // Get runtime config
  const config = useRuntimeConfig()
  
  // Reactive state
  const loading = ref(false)
  const error = ref(null)
  
  // Base URL from environment
  const baseUrl = config.public.apiBaseUrl + config.public.apiVersion
  
  /**
   * Make a GET request to the API
   *
   * @param {string} endpoint - API endpoint to call
   * @param {Object} options - Fetch options
   * @returns {Promise<any>} Response data
   */
  const get = async (endpoint, options = {}) => {
    loading.value = true
    error.value = null
    
    try {
      const url = `${baseUrl}${endpoint}`
      const response = await fetch(url, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          ...options.headers
        },
        ...options
      })
      
      if (!response.ok) {
        throw new Error(`API Error: ${response.status} ${response.statusText}`)
      }
      
      const data = await response.json()
      return data
    } catch (err) {
      error.value = err.message || 'An error occurred while fetching data'
      throw err
    } finally {
      loading.value = false
    }
  }
  
  /**
   * Make a POST request to the API
   *
   * @param {string} endpoint - API endpoint to call
   * @param {Object} data - Data to send in the request body
   * @param {Object} options - Fetch options
   * @returns {Promise<any>} Response data
   */
  const post = async (endpoint, data, options = {}) => {
    loading.value = true
    error.value = null
    
    try {
      const url = `${baseUrl}${endpoint}`
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          ...options.headers
        },
        body: JSON.stringify(data),
        ...options
      })
      
      if (!response.ok) {
        throw new Error(`API Error: ${response.status} ${response.statusText}`)
      }
      
      return await response.json()
    } catch (err) {
      error.value = err.message || 'An error occurred while posting data'
      throw err
    } finally {
      loading.value = false
    }
  }
  
  /**
   * Make a PUT request to the API
   *
   * @param {string} endpoint - API endpoint to call
   * @param {Object} data - Data to send in the request body
   * @param {Object} options - Fetch options
   * @returns {Promise<any>} Response data
   */
  const put = async (endpoint, data, options = {}) => {
    loading.value = true
    error.value = null
    
    try {
      const url = `${baseUrl}${endpoint}`
      const response = await fetch(url, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          ...options.headers
        },
        body: JSON.stringify(data),
        ...options
      })
      
      if (!response.ok) {
        throw new Error(`API Error: ${response.status} ${response.statusText}`)
      }
      
      return await response.json()
    } catch (err) {
      error.value = err.message || 'An error occurred while updating data'
      throw err
    } finally {
      loading.value = false
    }
  }
  
  /**
   * Make a DELETE request to the API
   *
   * @param {string} endpoint - API endpoint to call
   * @param {Object} options - Fetch options
   * @returns {Promise<any>} Response data
   */
  const del = async (endpoint, options = {}) => {
    loading.value = true
    error.value = null
    
    try {
      const url = `${baseUrl}${endpoint}`
      const response = await fetch(url, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
          ...options.headers
        },
        ...options
      })
      
      if (!response.ok) {
        throw new Error(`API Error: ${response.status} ${response.statusText}`)
      }
      
      return await response.json()
    } catch (err) {
      error.value = err.message || 'An error occurred while deleting data'
      throw err
    } finally {
      loading.value = false
    }
  }
  
  // Return API utilities and state
  return {
    get,
    post,
    put,
    del,
    loading,
    error,
    baseUrl
  }
}
