# Pravis Boutique — Design Specification

> Single source of truth for the Pravis Boutique web application design.
> Used to sync and compare across branches: `main`, `master`, `feature/design`, `feature/database`, `feature/frontend`.

---

## 1. Brand Identity

### Name & Tagline
- **Brand**: Pravis Boutique
- **Tagline**: "Drape in Elegance"
- **Domain**: Premium Indian handloom textiles and sarees

### Logo
- **Concept**: Stylized letter "P" combined with a peacock motif
- **Format**: PNG (base64-embedded), displayed at 120px desktop / 100px tablet / 80px mobile
- **Presentation**: Centered within a circular gold frame, drop shadow `rgba(0,0,0,0.1)`
- **Usage**: Header layout (alongside brand name) and footer (gold variant)

### Color Palette

| Token | Hex | Usage |
|-------|-----|-------|
| Maroon Primary | `#8B0000` | Buttons, nav links, icons, borders, focus rings |
| Maroon Secondary | `#A0001C` | Hover states, gradients, stat numbers |
| Deep Maroon | `#5F0000` | Header backgrounds, deep hover |
| Dark Maroon | `#7F0000` | Accent dark |
| Very Dark Maroon | `#3F0000` | Footer background |
| Gold Accent | `#D4AF37` | Logo, headings, SVG motifs, sparkle accents |
| Dark Gold | `#B8860B` | Gold hover states |
| Light Tint | `#FDF2F8` | Page backgrounds, card fills |
| Light Pink | `#F8E8EC` | Very light background variant |
| Cream | `#F4F3EE` | Handloom card backgrounds, SVG fills |
| Handloom Rust | `#B7472A` | Accent color |
| Handloom Terracotta | `#E07A5F` | Product accent color |
| Handloom Sage | `#81B29A` | Product accent, CTA buttons |
| Handloom Gold | `#F2CC8F` | Product accent |
| Handloom Deep | `#3D405B` | Section headings, deep text |
| Saffron 500 | `#FF9500` | Saffron orange accent |
| Indigo 500 | `#6366F1` | Traditional indigo accent |

**Pravis Scale (Tailwind):**
```
50: #FDF2F8  100: #F8E8EC  200: #E8BAC2  300: #D4AF37
400: #B8860B  500: #8B0000  600: #A0001C  700: #7F0000
800: #5F0000  900: #3F0000  950: #1F0000
```

### Typography

| Role | Font | Weight | Style |
|------|------|--------|-------|
| Brand name | Playfair Display | 400 | Italic |
| Section headings | Playfair Display | 700 | Normal |
| Body text | Inter | 300–700 | Normal |
| UI elements | Inter | 400–600 | Normal |

- **Heading sizes**: Hero 5rem/7rem, Section 4xl, Page 3xl, Card 2xl
- **Body sizes**: Base 16px, Small 14px, XS 12px
- **Line height**: Body 1.6–1.7, Headings 1.0–1.2

### CSS Custom Properties
```css
:root {
  --pravis-primary: #8B0000;
  --pravis-gold: #D4AF37;
}
```

---

## 2. Layout System

### Global Structure
```
┌─────────────────────────────────────┐
│  Header (layout: default.vue)       │
│  ┌─────────────────────────────────┐│
│  │ AnimatedLogo + "pravis" gold    ││
│  │ "Drape in Elegance" tagline     ││
│  └─────────────────────────────────┘│
├─────────────────────────────────────┤
│  Navigation (sticky top, z-40)      │
│  Logo | Shop About Contact Cart     │
├─────────────────────────────────────┤
│  <Page Content>                     │
├─────────────────────────────────────┤
│  Footer (4-column, dark maroon)     │
│  Brand | Links | Contact | Newsletter│
└─────────────────────────────────────┘
```

### Header
- **Background**: `linear-gradient(135deg, #5d1a1a 0%, #7d2525 50%, #5d1a1a 100%)`
- **Pattern overlay**: SVG cross/plus tile at 5% white opacity
- **Layout**: Flex row centered, max-width 1200px, gap 2rem
- **Brand name**: Playfair Display italic, 5rem, gold `#D4AF37`
- **Tagline**: Playfair Display italic, 1.5rem, gold 90% opacity
- **Sparkle accent**: Radial gold glow, top-right, 4-pointed star via pseudo-elements

### Navigation Bar
- **Style**: White bg, sticky top, z-40, shadow-lg (adds shadow-xl on scroll past 100px)
- **Height**: h-16 (64px)
- **Desktop**: Flex row, justify-between, logo left + links right
- **Mobile**: Hamburger menu → dropdown with stacked links
- **Logo**: 40x40 inline SVG — "P" with peacock gradient (maroon → gold), cream crossbar, gold decorative dots
- **Links**: Shop, About, Contact, Cart — text-pravis-800, hover:text-pravis-600

### Footer
- **Background**: `bg-pravis-900` (darkest maroon)
- **Grid**: 4 columns (md), single column mobile, gap-8, max-width 7xl
- **Column 1**: Gold logo variant + brand name + social icons (Twitter, Pinterest, Instagram)
- **Column 2**: Quick Links (Shop, Our Story, Size Guide, Care, Returns)
- **Column 3**: Contact (phone, email, address with SVG icons)
- **Column 4**: Newsletter signup (email input + subscribe button)
- **Bottom bar**: Copyright left, Privacy/Terms/Shipping links right

### Responsive Breakpoints
- **Mobile**: < 480px — brand name 2.5rem, sparkle hidden, single column
- **Tablet**: < 768px — brand name 3.5rem, header stacks vertically
- **Medium**: 768px+ (md) — 2-column grids, desktop nav visible
- **Large**: 1024px+ (lg) — 3-4 column grids, full layout
- **XL**: 1280px+ (xl) — 4-column product grids

---

## 3. Pages

### 3.1 Homepage (`/`)
**Sections in order:**
1. **Navigation** — sticky top bar
2. **HeroSection** — full-width, 2-column (text + SVG saree illustration)
3. **FeaturedProducts** — 4-column product grid
4. **AboutSection** — 2-column (story + values card)
5. **FooterSection** — 4-column dark footer

**Hero Section:**
- Background: `linear-gradient(135deg, #fdf2f8 → #D4AF37 → #A0001C)`
- Overlay: Dual radial gradients (maroon + gold at 25% and 75%)
- Left column: "Authentic Handloom Heritage" (5xl/7xl), subtitle, two CTA buttons
  - "Shop Now": maroon fill, white text, rounded-full, hover:scale-105
  - "WhatsApp Inquiry": outline maroon border, hover fills solid
- Right column: 400x500 SVG saree drape with:
  - Tiled pattern fill (#8B0000 base, gold circles+squares)
  - Gold horizontal border bars
  - Three translucent gold circular motifs
  - Gold pleat detail path
  - Two pulsing accent circles (pravis-300, pravis-600, 20% opacity)

**Featured Products:**
- White bg, py-20
- Header: "Featured Collection" — Playfair Display, dark maroon
- Grid: 4 columns (lg), gap-8, using ProductCard component
- 4 products: Banarasi Silk (#8B0000), Chanderi Cotton (#E07A5F), Anarkali Suit (#81B29A), Kanjivaram Silk (#3D405B)
- CTA: "View All Products" — sage/gold fill, rounded-full

**About Section:**
- Background: `#fdf2f8` cream tint with subtle radial overlay
- Left: "Our Heritage Story" + brand narrative + stats row (500+ Artisan Partners, 15+ States, 10K+ Customers)
- Right: White values card — 3 items with gold checkmark circles (Authentic Artisanship, Sustainable Practices, Fair Trade)

**Scroll behavior**: IntersectionObserver adds fade-in animation (0.6s ease-out, translateY 20px → 0)

### 3.2 Shop (`/shop`)
- Hero banner: maroon-to-saffron gradient, "Handloom Collection" white text
- Product grid: 1/2/3/4 columns responsive, gap-6
- Each card: white, rounded-lg, shadow-md, hover:shadow-lg
  - Image area: h-48, gradient pravis-100 to saffron-100, heart icon, fabric label
  - Product info: name (2-line clamp), description (2-line clamp)
  - Star rating: yellow-400 filled vs gray-300 empty, review count
  - Price: ₹ format, pravis-600, line-through for original
  - Origin badge: gray pill
  - CTA: "Inquire on WhatsApp" — full-width maroon button → wa.me deeplink
- Empty state: gray circle + box icon + "No products found"

**Hardcoded products (7):** Banarasi Silk Saree (₹15,999), Handwoven Cotton Kurta (₹4,500), Kashmiri Pashmina (₹18,500), Chanderi Dupatta (₹3,200), Linen Saree (₹6,800), Rajasthani Lehenga (₹22,000), Floral Cotton Suit (₹3,800)

### 3.3 Product Detail (`/shop/product/[id]`)
- Dynamic route using product ID
- Image gallery, product info, add-to-cart, quantity selector
- Wishlist toggle, share buttons (Facebook, Twitter, Pinterest, Email)
- Related products section
- Review form (name, email, rating, title, content)

### 3.4 Cart (`/cart`)
- Placeholder/under-development page
- Gray circle with shopping cart SVG icon (w-24 h-24)
- Gold-tinted "Under Development" banner
- CTAs: "Browse Products" (maroon), "WhatsApp Us" (green), "Continue Shopping" (text link)

### 3.5 Contact (`/contact`)
- Hero: maroon banner, "Get in Touch" white text (4xl/5xl)
- 2-column layout (lg):
  - Left: Address, Phone, Email blocks with pravis-100 icon squares + social links
  - Right: Contact form card (white, shadow-lg) — name grid, email, subject, textarea, submit
- Full dark mode support

### 3.6 Privacy Policy (`/privacy`)
- Centered white card (max-w-4xl, shadow-lg)
- Prose typography with 10 numbered sections
- Embedded PrivacyControls component at bottom
- "Back to Previous Page" maroon button

### 3.7 Terms of Service (`/terms`)
- Same layout as privacy page
- 9 numbered sections
- No embedded privacy controls

### 3.8 Account Privacy (`/account/privacy`)
- Privacy settings management page
- Embeds PrivacyControls component
- "Back to Account" and "View Privacy Policy" navigation buttons
- Full dark mode support

---

## 4. Components

### 4.1 ProductCard
- White card, rounded-lg, shadow-sm, lifts on hover (-translate-y-1 + shadow-md)
- Image: aspect 3:4, object-cover, fade-in on load, spinner while loading
- Badges: "Sale" (red pill) or "New" (green pill), top-left
- Hover overlay: semi-transparent black with 3 action buttons (Quick View, Add to Cart, Wishlist)
- Info: name, category, price (with sale strike-through), star rating
- Full dark mode support

### 4.2 Button (reusable)
- **Variants**: primary (pravis-600), secondary (gray), success (green), danger (red), warning (yellow), info (blue), light, dark, outline-primary, outline-secondary, link
- **Sizes**: xs, sm, md, lg, xl
- **Shapes**: rounded-none / sm / md / lg / full
- **States**: disabled (opacity-50), loading (animated spinner), block (full-width)
- **Polymorphic**: renders as `<button>`, `<a>`, `<NuxtLink>`, or any tag

### 4.3 ConsentDialog
- Full-screen modal overlay (blur backdrop, z-10000)
- White gradient card, 480px max, slide-in animation (0.3s)
- "Welcome to Pravis Boutique!" — Playfair Display 28px
- Two radio options with custom maroon checkmarks
- "Continue" pill button — maroon gradient, disabled until selection
- Stores decision in localStorage `pravis-consent`

### 4.4 PrivacyControls
- Gray card (#f8f9fa), rounded-12px
- Analytics toggle: 60x34 pill switch (gray → maroon on)
- "Delete All My Data" red button with confirmation modal
- Summary: "What We Collect" list, "How We Use Your Data", privacy/terms links
- Reads/writes localStorage directly

### 4.5 ContactUsBox
- White card, rounded-2xl, shadow-xl
- Phone + Email blocks with pravis-600 SVG icons
- "Send Us a Message" maroon CTA button
- Full dark mode support

### 4.6 DarkModeToggle
- Circular icon button — moon/sun SVG swap
- 3 variants: default, contrast, minimal
- Uses Nuxt Color Mode module

---

## 5. Interaction Patterns

### Hover Effects
- Cards: lift -8px with maroon shadow (`.hover-lift`)
- Buttons: scale(1.05) or translateY(-2px) with colored shadow
- Links: color transition to pravis-600
- Navigation: shadow intensifies on scroll

### Transitions
- Page transitions: `name: 'page', mode: 'out-in'`
- Scroll fade-in: opacity 0→1, translateY 20px→0, 0.6s ease-out (IntersectionObserver)
- Dialog slide-in: translateY(-30px)→0, 0.3s ease-out
- Toggle switch: 0.4s knob slide

### Accessibility
- `*:focus-visible`: 2px solid #8B0000 outline, 2px offset
- `prefers-reduced-motion`: all animations suppressed
- ARIA roles: dialog (aria-modal), article (product cards), radiogroup (consent)
- Print styles: overlays and modals hidden

### WhatsApp Integration
- Multiple CTAs link to `wa.me` deeplinks with pre-filled messages
- Used in: Shop page product cards, Cart page, Hero section

---

## 6. Product Catalog (Static Data)

### Products (8 items)

| # | Name | Price (₹) | Was (₹) | Category | Fabric | Origin | Featured |
|---|------|-----------|---------|----------|--------|--------|----------|
| 1 | Banarasi Silk Saree - Golden Thread | 15,999 | 19,999 | Sarees | Pure Silk | Varanasi, UP | Yes |
| 2 | Khadi Cotton Kurta Set - Indigo Blue | 3,999 | 4,999 | Kurtas | Khadi Cotton | Gujarat | Yes |
| 3 | Ikat Dupatta - Geometric Patterns | 2,499 | 2,999 | Dupattas | Cotton | Odisha | No |
| 4 | Chanderi Silk Suit - Floral Motifs | 8,999 | 11,999 | Suits | Chanderi Silk | Madhya Pradesh | Yes |
| 5 | Handwoven Cotton Stole - Saffron Stripes | 1,299 | 1,599 | Stoles | Cotton | West Bengal | No |
| 6 | Kantha Embroidered Jacket | 5,999 | 7,999 | Jackets | Cotton | West Bengal | Yes |
| 7 | Madurai Cotton Saree - Temple Border | 4,999 | 5,999 | Sarees | Cotton | Tamil Nadu | No |
| 8 | Tussar Silk Shirt - Natural Texture | 3,499 | 4,299 | Shirts | Tussar Silk | Jharkhand | No |

### Categories
- All Products
- Sarees
- Kurtas & Suits
- Stoles & Dupattas
- Jackets & Tops

### Filter Facets
- **Fabric**: Cotton, Silk, Khadi Cotton, Chanderi Silk, Tussar Silk
- **Colors**: Golden, Indigo, Terracotta, Cream, Saffron, Maroon, Natural
- **Price Ranges**: Under ₹2,000 / ₹2,000–5,000 / ₹5,000–10,000 / ₹10,000–20,000 / Above ₹20,000
- **Origin**: Varanasi, Gujarat, Odisha, Madhya Pradesh, West Bengal, Tamil Nadu, Jharkhand

### Price Display
- Format: INR (₹) with Indian number system (`en-IN` locale)
- Sale prices: current in bold maroon, original in gray strike-through

---

## 7. State Management

### Cart Store
- **Items**: array of `{ id, name, price, image?, quantity }`
- **Computed**: count, subtotal, taxAmount (8%), total, isEmpty
- **Persistence**: localStorage key `cart-items`
- **Actions**: addItem, updateQuantity, removeItem, clearCart

### User Store
- **State**: `{ isAuthenticated, user: { id, email, firstName, lastName, role } }`
- **Computed**: profile, fullName
- **Persistence**: localStorage key `auth-token`
- **Actions**: setUser, logout

### Consent
- **Storage**: localStorage key `pravis-consent`
- **Shape**: `{ consent: boolean, timestamp: string, version: "1.0" }`

---

## 8. Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | Nuxt 3 / Vue 3 |
| Language | TypeScript (strict mode) |
| Styling | Tailwind CSS |
| State | Pinia |
| Testing | Vitest + Cypress |
| Fonts | Google Fonts (Playfair Display, Inter) |

---

## 9. Branch Strategy

| Branch | Purpose |
|--------|---------|
| `main` | Stable releases |
| `master` | Mirror of main (kept in sync) |
| `feature/design` | UI/UX design work |
| `feature/database` | Storage, retrieval, transformation layers |
| `feature/frontend` | TypeScript frontend modules |

This file (`pravisBoutique.md`) exists on all branches as the single source of truth for comparing design state across branches.

---

*Last updated: February 2026*
