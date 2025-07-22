# Pravis Boutique PWA Features

This document outlines the Progressive Web App (PWA) features implemented in the Pravis Boutique application.

## PWA Features

### Core PWA Features

- **Installable**: The application can be installed on supported devices through the manifest.webmanifest file.
- **Offline Support**: Service workers cache critical assets and API responses for offline usage.
- **Responsive Design**: The application is designed to work on all device sizes and orientations.

### Advanced PWA Features

1. **Workbox Integration**
   - Advanced caching strategies for different asset types (images, fonts, API calls)
   - Precaching of critical application resources
   - Background sync for offline analytics data
   - Custom service worker extensions

2. **Web App Manifest**
   - Comprehensive manifest with app icons in multiple sizes
   - Maskable icons for Android devices
   - Proper app metadata (name, description, theme colors, etc.)
   - App installation promotion

3. **Push Notification Infrastructure**
   - VAPID key generation for push notifications
   - Server API endpoints for subscription management
   - Client-side push notification subscription handling
   - User-friendly notification permission UI component

4. **Offline Analytics**
   - Storage of analytics data when offline
   - Background sync when connection is restored
   - Persistent data collection even in offline scenarios

5. **SEO Optimization**
   - Static site generation for key pages
   - Server-side rendering capabilities for dynamic content
   - Proper metadata for search engines

## Azure Static Web Apps Deployment

The application is configured for seamless deployment to Azure Static Web Apps with:

- Proper routing configuration via staticwebapp.config.json
- Optimized asset caching strategies
- API routes configuration for backend integration
- HTTPS enforcement
- Security headers

## Development Commands

```bash
# Install dependencies
npm install

# Set up PWA features (icons, VAPID keys)
npm run setup:pwa

# Generate VAPID keys for push notifications
npm run generate:vapid

# Development server
npm run dev

# Build for production (SSR)
npm run build

# Generate static site
npm run generate

# Deploy to Azure Static Web Apps
npm run deploy:azure
```

## Environment Variables

Key environment variables for PWA functionality:

```
# PWA Settings
NUXT_PUBLIC_DEPLOYMENT_PRESET=azure-static

# Push Notification Settings (VAPID)
NUXT_PUBLIC_VAPID_PUBLIC_KEY=your_public_key
VAPID_PRIVATE_KEY=your_private_key
VAPID_SUBJECT=mailto:contact@pravis-boutique.com
```

## Testing PWA Features

1. **Lighthouse Testing**: Use Chrome's Lighthouse to verify PWA implementation
2. **Offline Testing**: Test the application with network disconnected
3. **Installation Testing**: Verify app can be installed on various devices
4. **Push Notification Testing**: Test push notification flow (request, subscribe, receive)

## Resources

- [Vite PWA Plugin Documentation](https://vite-pwa-org.netlify.app/frameworks/nuxt.html)
- [Azure Static Web Apps Documentation](https://docs.microsoft.com/en-us/azure/static-web-apps/)
- [Web Push Notifications](https://web.dev/notifications/)
- [Workbox Documentation](https://developers.google.com/web/tools/workbox)
