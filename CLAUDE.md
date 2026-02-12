# Pravis Boutique - AI Assistant Guide

## Project Overview

Pravis Boutique is a frontend-only e-commerce web application for an Indian handloom textile boutique, built with Nuxt 3, Vue 3, TypeScript, and Tailwind CSS. Product data is currently static/dummy data; a database layer is planned for a future phase.

## Repository Structure

```
/                           # Nuxt 3 project root
├── app.vue                 # Root app component
├── nuxt.config.ts          # Nuxt configuration (TypeScript strict mode)
├── tsconfig.json           # TypeScript config extending Nuxt
├── package.json            # Dependencies and scripts (v2.0.0)
├── tailwind.config.js      # Tailwind with custom pravis brand theme
├── vitest.config.js        # Unit test configuration
├── cypress.config.js       # E2E test configuration
├── staticwebapp.config.json # Azure Static Web Apps config
├── pages/                  # File-based routing
│   ├── index.vue           # Homepage (hero, featured, about, footer)
│   ├── shop.vue            # Shop page
│   ├── shop/index.vue      # Product listing with filters
│   ├── shop/product/[id].vue  # Dynamic product detail page
│   ├── cart.vue            # Shopping cart
│   ├── contact.vue         # Contact form
│   ├── privacy.vue         # Privacy policy
│   ├── terms.vue           # Terms of service
│   └── account/privacy.vue # User privacy settings
├── components/             # Vue components
│   ├── Navigation.vue      # Top nav bar with logo
│   ├── HeroSection.vue     # Main hero/banner
│   ├── HeroCarousel.vue    # Hero section carousel
│   ├── AnimatedLogo.vue    # P-Peacock SVG brand logo (deliberately static)
│   ├── FeaturedProducts.vue # Featured product grid
│   ├── AboutSection.vue    # About company section
│   ├── FooterSection.vue   # Footer with links
│   └── common/             # Reusable UI components
│       ├── ProductCard.vue
│       ├── Button.vue
│       ├── ContactUsBox.vue
│       ├── DarkModeToggle.vue
│       ├── ConsentDialog.vue
│       └── PrivacyControls.vue
├── composables/            # Vue composables
│   ├── useProductData.ts   # Static product catalog (8 dummy products)
│   └── useProducts.ts      # Product query helpers
├── store/                  # Pinia stores (TypeScript)
│   ├── cart.ts             # Shopping cart (items, totals, localStorage)
│   └── user.ts             # User auth state (profile, login/logout)
├── layouts/
│   └── default.vue         # Default layout wrapper
├── assets/css/
│   └── main.css            # Global styles and Tailwind imports
├── public/                 # Static assets
│   ├── pravis-logo.svg     # Brand logo SVG
│   ├── pravis-peacock-logo.svg
│   ├── pravis-logo.png
│   ├── images/             # Product and hero images
│   └── fonts/              # Self-hosted Inter and Playfair Display
└── cypress/                # E2E test specs
    └── e2e/home.cy.js
```

## Tech Stack

| Layer      | Technology                                     |
|------------|-------------------------------------------------|
| Framework  | Nuxt 3, Vue 3, TypeScript (strict mode)        |
| Styling    | Tailwind CSS 3.3 with custom brand theme       |
| State      | Pinia 2.1                                       |
| Utilities  | VueUse                                          |
| Testing    | Vitest (unit, happy-dom), Cypress (E2E)        |
| Linting    | ESLint with Nuxt + Vue plugins                  |
| Deployment | Azure Static Web Apps                           |

## Development Commands

```bash
npm run dev              # Dev server on localhost:3000
npm run build            # Production build
npm run generate         # Static site generation
npm run start            # Start production server
npm run preview          # Preview production build
npm run typecheck        # TypeScript type checking
npm run lint             # ESLint check
npm run lint:fix         # Auto-fix lint issues
npm run test             # Vitest unit tests
npm run test:watch       # Vitest watch mode
npm run test:coverage    # Coverage report (v8)
npm run test:e2e         # Cypress interactive
npm run test:e2e:headless # Cypress headless
```

## Brand & Design Conventions

### Color Palette

- **Primary (Maroon)**: `pravis-500` (#8B0000) - main brand color
- **Gold accent**: `pravis-300` (#D4AF37) - decorative and accent elements
- **Handloom palette**: `handloom-rust` (#B7472A), `handloom-terracotta` (#E07A5F), `handloom-cream` (#F4F3EE), `handloom-sage` (#81B29A), `handloom-gold` (#F2CC8F), `handloom-deep` (#3D405B)
- **Saffron/Indigo**: Traditional Indian accent color scales

### Typography

- **Display/Headings**: `font-display` (Playfair Display, serif)
- **Body text**: `font-sans` (Inter, sans-serif)
- Loaded from Google Fonts and self-hosted in `public/fonts/`

### Dark Mode

Supported via Tailwind `class` strategy. Use `dark:` prefix for dark mode variants.

## Architecture Patterns

- **File-based routing**: Pages in `pages/` auto-generate routes. Dynamic params use `[id].vue` syntax.
- **Composables**: Shared logic in `composables/`. Prefix with `use`. Product data is static in `useProductData.ts`.
- **State management**: Pinia stores in `store/`. Two stores: `cart` (with localStorage persistence) and `user`.
- **Components**: Reusable/generic components go in `components/common/`. Page-specific components go in `components/`.
- **Layouts**: `layouts/default.vue` wraps all pages.
- **No backend**: The app is frontend-only. Product data comes from static dummy data in `composables/useProductData.ts`. A database layer is planned for later.
- **TypeScript**: Strict mode enabled in `nuxt.config.ts`. Stores and composables use TypeScript.

## Key Conventions

1. **Component naming**: PascalCase for Vue components (e.g., `ProductCard.vue`).
2. **Composable naming**: camelCase with `use` prefix (e.g., `useProductData.ts`).
3. **Store naming**: lowercase TypeScript files (e.g., `store/cart.ts`).
4. **CSS**: Tailwind utility classes. Custom colors in `tailwind.config.js` under `pravis` and `handloom-*` namespaces.
5. **Vue 3 Composition API**: All components use `<script setup>` syntax.
6. **TypeScript strict**: All new code should be TypeScript-first.
7. **No floating animations on logo**: The P-Peacock logo in `AnimatedLogo.vue` is deliberately static.
8. **Currency**: Indian Rupees (INR), formatted with `Intl.NumberFormat('en-IN')`.

## Testing

- **Unit tests**: Vitest with `happy-dom` environment. Config in `vitest.config.js`.
- **E2E tests**: Cypress. Config in `cypress.config.js`. Specs in `cypress/e2e/`.
- **Test library**: `@testing-library/vue` for component testing.

## Deployment

- **Platform**: Azure Static Web Apps (`staticwebapp.config.json` present).
- **Nitro preset**: `node-server` by default (override via `NUXT_PUBLIC_DEPLOYMENT_PRESET` env var).
- **Prerendered routes**: `/`, `/shop`, `/contact`.

## Branch Strategy

- `main` - stable releases
- `main` → `feature/design` - UI/UX design work
- `main` → `feature/database` - storage, retrieval, transformation layers
- `main` → `feature/frontend` - frontend TypeScript modules
