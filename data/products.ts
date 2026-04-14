export interface Product {
  id: number
  name: string
  price: number
  originalPrice: number
  category: string
  fabric: string
  origin: string
  featured: boolean
  color: string
  description: string
  imageReady: boolean
}

export const categories = [
  'All Products',
  'Sarees',
  'Kurtas & Suits',
  'Stoles & Dupattas',
  'Jackets & Tops',
] as const

export type Category = typeof categories[number]

export const products: Product[] = [
  {
    id: 1,
    name: 'Banarasi Silk Saree — Golden Thread',
    price: 15999,
    originalPrice: 19999,
    category: 'Sarees',
    fabric: 'Pure Silk',
    origin: 'Varanasi, UP',
    featured: true,
    color: '#8B0000',
    description: 'Exquisite handwoven Banarasi silk saree with intricate golden zari work and traditional motifs.',
    imageReady: false,
  },
  {
    id: 2,
    name: 'Khadi Cotton Kurta Set — Indigo Blue',
    price: 3999,
    originalPrice: 4999,
    category: 'Kurtas & Suits',
    fabric: 'Khadi Cotton',
    origin: 'Gujarat',
    featured: true,
    color: '#3D405B',
    description: 'Premium khadi cotton kurta set dyed in rich indigo, perfect for everyday elegance.',
    imageReady: false,
  },
  {
    id: 3,
    name: 'Ikat Dupatta — Geometric Patterns',
    price: 2499,
    originalPrice: 2999,
    category: 'Stoles & Dupattas',
    fabric: 'Cotton',
    origin: 'Odisha',
    featured: false,
    color: '#E07A5F',
    description: 'Hand-dyed Ikat dupatta featuring bold geometric patterns in earthy tones.',
    imageReady: false,
  },
  {
    id: 4,
    name: 'Chanderi Silk Suit — Floral Motifs',
    price: 8999,
    originalPrice: 11999,
    category: 'Kurtas & Suits',
    fabric: 'Chanderi Silk',
    origin: 'Madhya Pradesh',
    featured: true,
    color: '#81B29A',
    description: 'Elegant Chanderi silk suit with delicate floral motifs and a lightweight, lustrous drape.',
    imageReady: false,
  },
  {
    id: 5,
    name: 'Handwoven Cotton Stole — Saffron Stripes',
    price: 1299,
    originalPrice: 1599,
    category: 'Stoles & Dupattas',
    fabric: 'Cotton',
    origin: 'West Bengal',
    featured: false,
    color: '#FF9500',
    description: 'Soft handwoven cotton stole with vibrant saffron stripes, a versatile accessory.',
    imageReady: false,
  },
  {
    id: 6,
    name: 'Kantha Embroidered Jacket',
    price: 5999,
    originalPrice: 7999,
    category: 'Jackets & Tops',
    fabric: 'Cotton',
    origin: 'West Bengal',
    featured: true,
    color: '#B7472A',
    description: 'Artisan Kantha embroidered jacket with detailed running stitch work and vintage charm.',
    imageReady: false,
  },
  {
    id: 7,
    name: 'Madurai Cotton Saree — Temple Border',
    price: 4999,
    originalPrice: 5999,
    category: 'Sarees',
    fabric: 'Cotton',
    origin: 'Tamil Nadu',
    featured: false,
    color: '#A0001C',
    description: 'Traditional Madurai cotton saree with iconic temple border design, light and breathable.',
    imageReady: false,
  },
  {
    id: 8,
    name: 'Tussar Silk Shirt — Natural Texture',
    price: 3499,
    originalPrice: 4299,
    category: 'Jackets & Tops',
    fabric: 'Tussar Silk',
    origin: 'Jharkhand',
    featured: false,
    color: '#F2CC8F',
    description: 'Naturally textured Tussar silk shirt with a subtle sheen, ideal for semi-formal occasions.',
    imageReady: false,
  },
]

export function formatPrice(amount: number): string {
  return new Intl.NumberFormat('en-IN', {
    style: 'currency',
    currency: 'INR',
    minimumFractionDigits: 0,
    maximumFractionDigits: 0,
  }).format(amount)
}

export function getWhatsAppLink(productName: string): string {
  const message = encodeURIComponent(`Hi! I'm interested in "${productName}" from Pravis Boutique. Could you share more details?`)
  return `https://wa.me/?text=${message}`
}
