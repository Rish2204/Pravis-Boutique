# Pravis Boutique Frontend Deployment Guide

This document outlines the steps to deploy the Pravis Boutique Nuxt.js frontend application both locally and on Azure.

## Prerequisites

- Node.js 16+ installed
- npm or yarn package manager
- Azure account for cloud deployment
- Azure CLI installed for Azure deployments

## Local Development Environment Setup

1. **Clone the repository**:
   ```bash
   git clone [repository-url]
   cd pravis-boutique/frontend/pravis-boutique
   ```

2. **Install dependencies**:
   ```bash
   # Using npm
   npm install

   # Using yarn
   yarn install
   ```

3. **Set up environment variables**:
   ```bash
   # Copy the example .env file
   cp .env.example .env

   # Edit the .env file with your local configuration
   # Particularly, configure the API URL to connect to your backend
   ```

4. **Start the development server**:
   ```bash
   # Using npm
   npm run dev

   # Using yarn
   yarn dev
   ```

5. **Access the application**:
   - The application will be available at http://localhost:3000

## Building for Production

1. **Generate static files**:
   ```bash
   # Using npm
   npm run generate

   # Using yarn
   yarn generate
   ```

   This will create a `.output` directory with your static site.

2. **Preview the production build locally**:
   ```bash
   # Using npm
   npm run preview

   # Using yarn
   yarn preview
   ```

## Azure Deployment

### Deployment with Azure Static Web Apps

1. **Login to Azure CLI**:
   ```bash
   az login
   ```

2. **Create resource group (if needed)**:
   ```bash
   az group create --name pravis-boutique-rg --location eastus
   ```

3. **Create Azure Static Web App**:
   ```bash
   az staticwebapp create \
     --name pravis-boutique-web \
     --resource-group pravis-boutique-rg \
     --location "eastus2" \
     --source https://github.com/yourusername/pravis-boutique \
     --branch main \
     --app-location "/frontend/pravis-boutique" \
     --output-location ".output/public" \
     --login-with-github
   ```

   Alternatively, you can create the Static Web App through the Azure Portal and connect it to your GitHub repository.

4. **Configure environment variables**:
   You can set environment variables for your Static Web App through the Azure Portal or using the Azure CLI:

   ```bash
   az staticwebapp appsettings set \
     --name pravis-boutique-web \
     --resource-group pravis-boutique-rg \
     --setting-names \
       NUXT_PUBLIC_API_BASE_URL="https://pravis-boutique-api.azurewebsites.net" \
       NUXT_PUBLIC_API_VERSION="/api/v1" \
       NUXT_PUBLIC_APP_NAME="Pravis Boutique" \
       NUXT_PUBLIC_ENABLE_VOICE_AGENT="true" \
       NUXT_PUBLIC_ENABLE_ANALYTICS="true"
   ```

5. **Configure routes for SPA**:
   Create a `staticwebapp.config.json` file in the root of your project:

   ```json
   {
     "routes": [
       {
         "route": "/api/*",
         "methods": ["GET", "POST", "PUT", "DELETE"],
         "allowedRoles": ["anonymous"],
         "backendUri": "https://pravis-boutique-api.azurewebsites.net/api/*"
       },
       {
         "route": "/*",
         "serve": "/index.html",
         "statusCode": 200
       }
     ],
     "navigationFallback": {
       "rewrite": "/index.html",
       "exclude": ["/images/*.{png,jpg,gif}", "/css/*", "/js/*"]
     },
     "responseOverrides": {
       "404": {
         "rewrite": "/404.html",
         "statusCode": 404
       }
     },
     "globalHeaders": {
       "content-security-policy": "default-src https: 'unsafe-eval' 'unsafe-inline'; object-src 'none'",
       "cache-control": "must-revalidate, max-age=60"
     }
   }
   ```

### Deployment with Azure App Service (alternative approach)

1. **Build your application**:
   ```bash
   # Using npm
   npm run generate

   # Using yarn
   yarn generate
   ```

2. **Create Azure Web App**:
   ```bash
   az webapp create \
     --resource-group pravis-boutique-rg \
     --plan pravis-boutique-plan \
     --name pravis-boutique-web \
     --runtime "NODE|16-lts"
   ```

3. **Configure environment variables**:
   ```bash
   az webapp config appsettings set \
     --resource-group pravis-boutique-rg \
     --name pravis-boutique-web \
     --settings \
       NUXT_PUBLIC_API_BASE_URL="https://pravis-boutique-api.azurewebsites.net" \
       NUXT_PUBLIC_API_VERSION="/api/v1" \
       NUXT_PUBLIC_APP_NAME="Pravis Boutique" \
       NUXT_PUBLIC_ENABLE_VOICE_AGENT="true" \
       NUXT_PUBLIC_ENABLE_ANALYTICS="true"
   ```

4. **Deploy code to Azure**:
   ```bash
   # ZIP the project files
   zip -r frontend.zip .output/public

   # Deploy the ZIP file
   az webapp deployment source config-zip \
     --resource-group pravis-boutique-rg \
     --name pravis-boutique-web \
     --src frontend.zip
   ```

5. **Configure the web app for SPA**:
   Create a `web.config` file in your project root:

   ```xml
   <?xml version="1.0" encoding="utf-8"?>
   <configuration>
     <system.webServer>
       <rewrite>
         <rules>
           <rule name="SPA" stopProcessing="true">
             <match url=".*" />
             <conditions logicalGrouping="MatchAll">
               <add input="{REQUEST_FILENAME}" matchType="IsFile" negate="true" />
               <add input="{REQUEST_FILENAME}" matchType="IsDirectory" negate="true" />
             </conditions>
             <action type="Rewrite" url="/" />
           </rule>
         </rules>
       </rewrite>
       <staticContent>
         <mimeMap fileExtension=".webmanifest" mimeType="application/manifest+json" />
       </staticContent>
     </system.webServer>
   </configuration>
   ```

## Continuous Integration/Continuous Deployment (CI/CD)

For automated deployments, set up a GitHub Actions workflow:

1. Create a `.github/workflows/frontend-deploy.yml` file in your repository
2. Configure the workflow to deploy on merge to main branch
3. Use Azure credentials to authenticate and deploy automatically

Example GitHub Actions workflow:

```yaml
name: Deploy Frontend

on:
  push:
    branches: [ main ]
    paths:
      - 'frontend/pravis-boutique/**'

jobs:
  build_and_deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Set up Node.js
        uses: actions/setup-node@v2
        with:
          node-version: '16'
          
      - name: Install dependencies
        run: |
          cd frontend/pravis-boutique
          npm ci
          
      - name: Build
        run: |
          cd frontend/pravis-boutique
          npm run generate
        env:
          NUXT_PUBLIC_API_BASE_URL: https://pravis-boutique-api.azurewebsites.net
          NUXT_PUBLIC_API_VERSION: /api/v1
          
      - name: Deploy
        uses: Azure/static-web-apps-deploy@v1
        with:
          azure_static_web_apps_api_token: ${{ secrets.AZURE_STATIC_WEB_APPS_TOKEN }}
          repo_token: ${{ secrets.GITHUB_TOKEN }}
          action: "upload"
          app_location: "frontend/pravis-boutique"
          output_location: ".output/public"
          skip_app_build: true
```

## PWA Configuration

The Pravis Boutique frontend is configured as a Progressive Web App (PWA). To ensure it works correctly:

1. **Icons**: Place icon files in the `public/icons` directory
2. **Manifest**: The PWA manifest is generated based on your Nuxt config
3. **Service Worker**: Workbox service worker is configured for offline support

## Static Asset Optimization

1. **Image optimization**:
   - Use modern image formats (WebP)
   - Implement responsive images with `srcset`
   - Lazy-load images below the fold

2. **CSS/JS optimization**:
   - The production build automatically minimizes CSS and JS
   - Use code splitting to reduce initial load time

## Troubleshooting

- Check browser console for client-side errors
- Verify Azure Static Web App logs
- Test API connectivity from the frontend
- Ensure environment variables are correctly set

For assistance, contact the DevOps team or reference the Azure documentation.
