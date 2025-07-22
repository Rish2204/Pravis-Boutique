/**
 * This utility generates VAPID keys for Web Push Notifications
 * Run with: node ./server/utils/generate-vapid-keys.js
 * 
 * For production, you should:
 * 1. Generate the keys once
 * 2. Store them securely (e.g., in Azure Key Vault)
 * 3. Load them as environment variables
 */

const webpush = require('web-push');

// Generate VAPID keys
const vapidKeys = webpush.generateVAPIDKeys();

// Output the keys
console.log('VAPID Keys generated:');
console.log('\nPublic Key:');
console.log(vapidKeys.publicKey);
console.log('\nPrivate Key:');
console.log(vapidKeys.privateKey);
console.log('\nAdd these to your .env file or Azure configuration:');
console.log('NUXT_PUBLIC_VAPID_PUBLIC_KEY=' + vapidKeys.publicKey);
console.log('VAPID_PRIVATE_KEY=' + vapidKeys.privateKey);

// Also recommend setting a subject (typically a mailto: URL)
console.log('\nAlso set a VAPID subject (typically your email):');
console.log('VAPID_SUBJECT=mailto:contact@pravis-boutique.com');
