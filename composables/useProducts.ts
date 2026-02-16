import { ref, readonly } from 'vue'
import { useProductData } from './useProductData'

export const useProducts = () => {
  const { getAllProducts, getFeaturedProducts, getProductById, getProductsByCategory, searchProducts: search } = useProductData()

  const products = ref(getAllProducts())
  const loading = ref(false)
  const error = ref<string | null>(null)

  const getProduct = (id: string | number) => {
    return getProductById(id)
  }

  const getRelatedProducts = (productId: string | number, limit = 4) => {
    const product = getProductById(productId)
    if (!product) return []

    return getAllProducts()
      .filter((p) => p.id !== product.id && p.category === product.category)
      .slice(0, limit)
  }

  const submitReview = (_productId: string | number, _reviewData: Record<string, unknown>) => {
    // Will be implemented when database layer is ready
    return null
  }

  return {
    products: readonly(products),
    loading: readonly(loading),
    error: readonly(error),
    getProducts: getAllProducts,
    getProduct,
    getFeaturedProducts,
    getProductsByCategory,
    searchProducts: search,
    getRelatedProducts,
    submitReview,
  }
}
