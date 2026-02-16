/**
 * Dummy product data for Pravis Handlooms
 * Instagram-inspired authentic handloom products
 */

const dummyProducts = [
  {
    id: 1,
    name: "Banarasi Silk Saree - Golden Thread",
    description: "Exquisite handwoven Banarasi silk saree with intricate golden zari work. Perfect for weddings and special occasions.",
    price: 15999,
    originalPrice: 19999,
    category: "sarees",
    subcategory: "silk",
    colors: ["golden", "cream", "maroon"],
    sizes: ["standard"],
    rating: 4.8,
    reviews: 124,
    inStock: true,
    images: [
      "/images/banarasi-saree-1.jpg",
      "/images/banarasi-saree-2.jpg",
      "/images/banarasi-saree-3.jpg"
    ],
    tags: ["handwoven", "silk", "wedding", "traditional", "banarasi"],
    fabric: "Pure Silk",
    weave: "Handloom",
    origin: "Varanasi, Uttar Pradesh",
    careInstructions: "Dry clean only",
    featured: true
  },
  {
    id: 2,
    name: "Khadi Cotton Kurta Set - Indigo Blue",
    description: "Comfortable handspun khadi cotton kurta with matching palazzo. Natural indigo dye creates beautiful variations.",
    price: 3999,
    originalPrice: 4999,
    category: "kurtas",
    subcategory: "cotton",
    colors: ["indigo", "white", "navy"],
    sizes: ["S", "M", "L", "XL"],
    rating: 4.6,
    reviews: 89,
    inStock: true,
    images: [
      "/images/khadi-kurta-1.jpg",
      "/images/khadi-kurta-2.jpg"
    ],
    tags: ["khadi", "cotton", "casual", "comfortable", "indigo"],
    fabric: "Khadi Cotton",
    weave: "Handspun",
    origin: "Gujarat",
    careInstructions: "Machine wash cold",
    featured: true
  },
  {
    id: 3,
    name: "Ikat Dupatta - Geometric Patterns",
    description: "Traditional Ikat weave dupatta with mesmerizing geometric patterns in earthy tones.",
    price: 2499,
    originalPrice: 2999,
    category: "dupattas",
    subcategory: "cotton",
    colors: ["terracotta", "cream", "brown"],
    sizes: ["standard"],
    rating: 4.7,
    reviews: 67,
    inStock: true,
    images: [
      "/images/ikat-dupatta-1.jpg",
      "/images/ikat-dupatta-2.jpg"
    ],
    tags: ["ikat", "geometric", "traditional", "dupatta"],
    fabric: "Cotton",
    weave: "Ikat",
    origin: "Odisha",
    careInstructions: "Hand wash recommended",
    featured: false
  },
  {
    id: 4,
    name: "Chanderi Silk Suit - Floral Motifs",
    description: "Elegant Chanderi silk suit with delicate floral hand-block prints and gold accents.",
    price: 8999,
    originalPrice: 11999,
    category: "suits",
    subcategory: "silk",
    colors: ["pink", "gold", "cream"],
    sizes: ["S", "M", "L", "XL"],
    rating: 4.9,
    reviews: 156,
    inStock: true,
    images: [
      "/images/chanderi-suit-1.jpg",
      "/images/chanderi-suit-2.jpg",
      "/images/chanderi-suit-3.jpg"
    ],
    tags: ["chanderi", "silk", "floral", "block-print", "elegant"],
    fabric: "Chanderi Silk",
    weave: "Handloom",
    origin: "Madhya Pradesh",
    careInstructions: "Dry clean only",
    featured: true
  },
  {
    id: 5,
    name: "Handwoven Cotton Stole - Saffron Stripes",
    description: "Soft handwoven cotton stole with traditional saffron and cream stripes. Perfect accessory for any outfit.",
    price: 1299,
    originalPrice: 1599,
    category: "stoles",
    subcategory: "cotton",
    colors: ["saffron", "cream", "gold"],
    sizes: ["standard"],
    rating: 4.5,
    reviews: 43,
    inStock: true,
    images: [
      "/images/cotton-stole-1.jpg",
      "/images/cotton-stole-2.jpg"
    ],
    tags: ["cotton", "stole", "stripes", "accessory"],
    fabric: "Cotton",
    weave: "Handloom",
    origin: "West Bengal",
    careInstructions: "Machine wash gentle",
    featured: false
  },
  {
    id: 6,
    name: "Kantha Embroidered Jacket",
    description: "Unique reversible jacket with traditional Kantha embroidery in vibrant colors.",
    price: 5999,
    originalPrice: 7999,
    category: "jackets",
    subcategory: "cotton",
    colors: ["multi", "red", "blue"],
    sizes: ["S", "M", "L"],
    rating: 4.8,
    reviews: 92,
    inStock: false,
    images: [
      "/images/kantha-jacket-1.jpg",
      "/images/kantha-jacket-2.jpg"
    ],
    tags: ["kantha", "embroidered", "reversible", "unique"],
    fabric: "Cotton",
    weave: "Hand Embroidered",
    origin: "West Bengal",
    careInstructions: "Dry clean preferred",
    featured: true
  },
  {
    id: 7,
    name: "Madurai Cotton Saree - Temple Border",
    description: "Classic Madurai cotton saree with traditional temple border design in rich colors.",
    price: 4999,
    originalPrice: 5999,
    category: "sarees",
    subcategory: "cotton",
    colors: ["maroon", "gold", "green"],
    sizes: ["standard"],
    rating: 4.6,
    reviews: 78,
    inStock: true,
    images: [
      "/images/madurai-saree-1.jpg",
      "/images/madurai-saree-2.jpg"
    ],
    tags: ["cotton", "temple-border", "traditional", "madurai"],
    fabric: "Cotton",
    weave: "Handloom",
    origin: "Tamil Nadu",
    careInstructions: "Machine wash cold",
    featured: false
  },
  {
    id: 8,
    name: "Tussar Silk Shirt - Natural Texture",
    description: "Contemporary shirt made from natural Tussar silk with unique texture and sheen.",
    price: 3499,
    originalPrice: 4299,
    category: "shirts",
    subcategory: "silk",
    colors: ["natural", "beige", "brown"],
    sizes: ["S", "M", "L", "XL", "XXL"],
    rating: 4.4,
    reviews: 61,
    inStock: true,
    images: [
      "/images/tussar-shirt-1.jpg",
      "/images/tussar-shirt-2.jpg"
    ],
    tags: ["tussar", "silk", "contemporary", "texture"],
    fabric: "Tussar Silk",
    weave: "Handloom",
    origin: "Jharkhand",
    careInstructions: "Dry clean only",
    featured: false
  }
]

const categories = [
  { id: 'all', name: 'All Products', count: dummyProducts.length },
  { id: 'sarees', name: 'Sarees', count: dummyProducts.filter(p => p.category === 'sarees').length },
  { id: 'kurtas', name: 'Kurtas & Suits', count: dummyProducts.filter(p => ['kurtas', 'suits'].includes(p.category)).length },
  { id: 'stoles', name: 'Stoles & Dupattas', count: dummyProducts.filter(p => ['stoles', 'dupattas'].includes(p.category)).length },
  { id: 'jackets', name: 'Jackets & Tops', count: dummyProducts.filter(p => ['jackets', 'shirts'].includes(p.category)).length }
]

const filters = {
  fabric: ['Cotton', 'Silk', 'Khadi Cotton', 'Chanderi Silk', 'Tussar Silk'],
  colors: ['Golden', 'Indigo', 'Terracotta', 'Cream', 'Saffron', 'Maroon', 'Natural'],
  priceRange: [
    { min: 0, max: 2000, label: 'Under ₹2,000' },
    { min: 2000, max: 5000, label: '₹2,000 - ₹5,000' },
    { min: 5000, max: 10000, label: '₹5,000 - ₹10,000' },
    { min: 10000, max: 20000, label: '₹10,000 - ₹20,000' },
    { min: 20000, max: 999999, label: 'Above ₹20,000' }
  ],
  origin: ['Varanasi', 'Gujarat', 'Odisha', 'Madhya Pradesh', 'West Bengal', 'Tamil Nadu', 'Jharkhand']
}

export const useProductData = () => {
  
  const getAllProducts = () => {
    return dummyProducts
  }

  const getFeaturedProducts = () => {
    return dummyProducts.filter(product => product.featured)
  }

  const getProductById = (id) => {
    return dummyProducts.find(product => product.id === parseInt(id))
  }

  const getProductsByCategory = (category) => {
    if (category === 'all') return dummyProducts
    return dummyProducts.filter(product => product.category === category)
  }

  const searchProducts = (query) => {
    const searchTerm = query.toLowerCase()
    return dummyProducts.filter(product => 
      product.name.toLowerCase().includes(searchTerm) ||
      product.description.toLowerCase().includes(searchTerm) ||
      product.tags.some(tag => tag.toLowerCase().includes(searchTerm))
    )
  }

  const filterProducts = (products, filters) => {
    let filtered = [...products]
    
    if (filters.fabric && filters.fabric.length > 0) {
      filtered = filtered.filter(p => filters.fabric.includes(p.fabric))
    }
    
    if (filters.colors && filters.colors.length > 0) {
      filtered = filtered.filter(p => 
        p.colors.some(color => filters.colors.includes(color))
      )
    }
    
    if (filters.priceRange) {
      filtered = filtered.filter(p => 
        p.price >= filters.priceRange.min && p.price <= filters.priceRange.max
      )
    }
    
    if (filters.inStock) {
      filtered = filtered.filter(p => p.inStock)
    }
    
    return filtered
  }

  const getCategories = () => categories
  const getFilters = () => filters

  const formatPrice = (price) => {
    return new Intl.NumberFormat('en-IN', {
      style: 'currency',
      currency: 'INR',
      minimumFractionDigits: 0
    }).format(price)
  }

  return {
    getAllProducts,
    getFeaturedProducts,
    getProductById,
    getProductsByCategory,
    searchProducts,
    filterProducts,
    getCategories,
    getFilters,
    formatPrice
  }
}