# Pravis Boutique

## Architecture (v2.0)
- **Stack**: Nuxt 3 + Vue 3 + TypeScript + Tailwind CSS + Pinia
- **No backend** - frontend-only webapp (database layer to be added later)
- **Product data**: Static/dummy data in `composables/useProductData.ts`
- **State management**: Pinia stores (`store/cart.ts`, `store/user.ts`)
- **Styling**: Tailwind CSS with custom brand colors (maroon #8B0000, gold #D4AF37)

## Project Structure
```
/                       # Nuxt 3 project root
├── app.vue             # Root app component
├── nuxt.config.ts      # Nuxt configuration (TypeScript strict mode)
├── tsconfig.json       # TypeScript config extending Nuxt
├── package.json        # Dependencies and scripts
├── tailwind.config.js  # Tailwind with custom pravis theme
├── pages/              # File-based routing
│   ├── index.vue       # Homepage (hero, featured, about, footer)
│   ├── shop/index.vue  # Product listing with filters
│   ├── shop/product/[id].vue  # Product detail page
│   ├── cart.vue        # Shopping cart
│   ├── contact.vue     # Contact page
│   ├── privacy.vue     # Privacy policy
│   └── terms.vue       # Terms of service
├── components/         # Vue components
│   ├── Navigation.vue  # Top nav with logo
│   ├── HeroSection.vue / HeroCarousel.vue
│   ├── AnimatedLogo.vue  # P-Peacock SVG logo
│   ├── FeaturedProducts.vue
│   ├── AboutSection.vue
│   ├── FooterSection.vue
│   └── common/         # Reusable UI components
├── composables/        # Vue composables
│   ├── useProductData.ts  # Static product catalog
│   └── useProducts.ts     # Product query helpers
├── store/              # Pinia stores (TypeScript)
│   ├── cart.ts         # Shopping cart (localStorage)
│   └── user.ts         # User auth state
├── layouts/default.vue # Default layout
├── assets/css/main.css # Global styles
└── public/             # Static assets (logos, fonts, images)
```

## Key Commands
```bash
npm run dev          # Start dev server (localhost:3000)
npm run build        # Production build
npm run typecheck    # TypeScript type checking
npm run lint         # ESLint
npm run test         # Vitest unit tests
```

## Branch Strategy
- `main` - stable releases
- `main` → `feature/design` - UI/UX design work
- `main` → `feature/database` - storage, retrieval, transformation layers
- `main` → `feature/frontend` - frontend TypeScript modules
