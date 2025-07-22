#!/bin/bash

# Script to install and set up push notification dependencies

# Make the script exit on any error
set -e

echo "Setting up push notification dependencies..."

# Install web-push library for VAPID key generation and sending notifications
npm install --save web-push

# Create necessary directories if they don't exist
mkdir -p public/icons

echo "Creating PWA icons..."

# Check if the pravis-logo.png exists to use as source
if [ -f "public/pravis-logo.png" ]; then
  SOURCE_LOGO="public/pravis-logo.png"
else
  echo "WARNING: public/pravis-logo.png not found. Using placeholder icons."
  # Create placeholder icons - in a real project, replace with actual brand icons
  
  # Create 64x64 icon
  echo "Creating placeholder 64x64 icon..."
  echo '<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64"><rect width="64" height="64" fill="#4a90e2"/><text x="50%" y="50%" text-anchor="middle" dy=".3em" font-family="Arial" font-size="24" fill="white">PB</text></svg>' > public/icons/icon-64x64.svg
  
  # Create 192x192 icon
  echo "Creating placeholder 192x192 icon..."
  echo '<svg xmlns="http://www.w3.org/2000/svg" width="192" height="192" viewBox="0 0 192 192"><rect width="192" height="192" fill="#4a90e2"/><text x="50%" y="50%" text-anchor="middle" dy=".3em" font-family="Arial" font-size="72" fill="white">PB</text></svg>' > public/icons/icon-192x192.svg
  
  # Create 512x512 icon
  echo "Creating placeholder 512x512 icon..."
  echo '<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512"><rect width="512" height="512" fill="#4a90e2"/><text x="50%" y="50%" text-anchor="middle" dy=".3em" font-family="Arial" font-size="196" fill="white">PB</text></svg>' > public/icons/icon-512x512.svg
  
  # Create 512x512 maskable icon
  echo "Creating placeholder 512x512 maskable icon..."
  echo '<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512"><rect width="512" height="512" fill="#4a90e2"/><circle cx="256" cy="256" r="200" fill="#3a80d2"/><text x="50%" y="50%" text-anchor="middle" dy=".3em" font-family="Arial" font-size="196" fill="white">PB</text></svg>' > public/icons/maskable-icon-512x512.svg
  
  # Create 72x72 badge icon
  echo "Creating placeholder 72x72 badge icon..."
  echo '<svg xmlns="http://www.w3.org/2000/svg" width="72" height="72" viewBox="0 0 72 72"><circle cx="36" cy="36" r="36" fill="#4a90e2"/><text x="50%" y="50%" text-anchor="middle" dy=".3em" font-family="Arial" font-size="24" fill="white">PB</text></svg>' > public/icons/badge-72x72.svg
  
  echo "Converting SVG to PNG..."
  # Use ImageMagick if available to convert SVG to PNG
  if command -v convert >/dev/null 2>&1; then
    convert public/icons/icon-64x64.svg public/icons/icon-64x64.png
    convert public/icons/icon-192x192.svg public/icons/icon-192x192.png
    convert public/icons/icon-512x512.svg public/icons/icon-512x512.png
    convert public/icons/maskable-icon-512x512.svg public/icons/maskable-icon-512x512.png
    convert public/icons/badge-72x72.svg public/icons/badge-72x72.png
    
    # Clean up SVG files
    rm public/icons/*.svg
  else
    echo "ImageMagick not found. Please manually convert the SVG files to PNG format."
    echo "Alternatively, you can use online tools or other image conversion utilities."
  fi
fi

# Generate VAPID keys for push notifications
echo "Generating VAPID keys..."
node ./server/utils/generate-vapid-keys.js

echo "Setup complete! Please add the generated VAPID keys to your .env file."
echo "You can now build your PWA with 'npm run generate' for static sites or 'npm run build' for SSR."
