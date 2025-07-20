<template>
  <div>
    <div class="container mx-auto px-4 py-16">
      <div class="max-w-4xl mx-auto bg-white rounded-lg shadow-lg p-8">
        <div class="text-center mb-8">
          <h1 class="font-display text-4xl font-bold text-gray-800 mb-4">
            Privacy Policy
          </h1>
          <p class="text-gray-600">
            Last updated: {{ lastUpdated }}
          </p>
        </div>

        <div class="prose prose-lg max-w-none">
          <h2>1. Information We Collect</h2>
          <p>
            At Pravis Boutique, we collect information to provide you with the best AI-powered shopping experience through our voice agent "Ask Pravi".
          </p>

          <h3>Voice Data</h3>
          <ul>
            <li>Voice recordings and transcriptions from interactions with Ask Pravi</li>
            <li>Speech patterns and language preferences</li>
            <li>Audio quality and device information</li>
          </ul>

          <h3>Usage Analytics</h3>
          <ul>
            <li>Pages visited and features used</li>
            <li>Time spent on different sections</li>
            <li>Device type, browser, and operating system</li>
            <li>IP address and general location (city/country level)</li>
          </ul>

          <h3>Shopping Preferences</h3>
          <ul>
            <li>Fashion preferences and style choices</li>
            <li>Size, color, and brand preferences</li>
            <li>Search history and browsing behavior</li>
            <li>Wishlist and saved items</li>
          </ul>

          <h2>2. How We Use Your Information</h2>
          <p>We use the collected information to:</p>
          <ul>
            <li><strong>Improve Ask Pravi:</strong> Train and enhance our AI voice agent</li>
            <li><strong>Personalization:</strong> Provide tailored fashion recommendations</li>
            <li><strong>Analytics:</strong> Understand user behavior and improve our platform</li>
            <li><strong>Communication:</strong> Send updates about new features or collections</li>
          </ul>

          <h2>3. Data Sharing and Third Parties</h2>
          <p>We do not sell your personal data. We may share information with:</p>
          <ul>
            <li><strong>AI Training Partners:</strong> Anonymized voice data for model improvement</li>
            <li><strong>Analytics Providers:</strong> Aggregated usage statistics</li>
            <li><strong>Cloud Services:</strong> Secure hosting and processing (AWS, Google Cloud)</li>
            <li><strong>Legal Requirements:</strong> When required by law or legal process</li>
          </ul>

          <h2>4. Voice Data Specific Policies</h2>
          <p>Special considerations for voice interactions:</p>
          <ul>
            <li>Voice recordings are processed in real-time and may be stored temporarily</li>
            <li>Transcriptions are created automatically and used for AI training</li>
            <li>You can request deletion of your voice data at any time</li>
            <li>Voice data is encrypted in transit and at rest</li>
          </ul>

          <h2>5. Data Retention</h2>
          <p>We retain your data for different periods:</p>
          <ul>
            <li><strong>Voice recordings:</strong> Up to 2 years or until deletion requested</li>
            <li><strong>Transcriptions:</strong> Up to 5 years for AI training purposes</li>
            <li><strong>Analytics data:</strong> Up to 3 years in aggregated form</li>
            <li><strong>Account data:</strong> Until account deletion or 7 years of inactivity</li>
          </ul>

          <h2>6. Your Rights and Controls</h2>
          <p>You have the right to:</p>
          <ul>
            <li><strong>Access:</strong> Request a copy of your personal data</li>
            <li><strong>Correct:</strong> Update or correct inaccurate information</li>
            <li><strong>Delete:</strong> Request deletion of your data ("right to be forgotten")</li>
            <li><strong>Opt-out:</strong> Disable voice recording or analytics collection</li>
            <li><strong>Export:</strong> Download your data in portable format</li>
          </ul>

          <h2>7. Security Measures</h2>
          <p>We protect your data using:</p>
          <ul>
            <li>End-to-end encryption for voice data transmission</li>
            <li>Secure cloud infrastructure with regular security audits</li>
            <li>Access controls and employee training on data privacy</li>
            <li>Regular security updates and vulnerability assessments</li>
          </ul>

          <h2>8. International Data Transfers</h2>
          <p>
            Your data may be processed in countries outside your location. We ensure adequate protection through:
          </p>
          <ul>
            <li>Standard contractual clauses</li>
            <li>Adequacy decisions by data protection authorities</li>
            <li>Appropriate safeguards and security measures</li>
          </ul>

          <h2>9. Changes to This Policy</h2>
          <p>
            We may update this privacy policy to reflect changes in our practices or legal requirements. We will notify you of significant changes through the app or email.
          </p>

          <h2>10. Contact Us</h2>
          <p>
            For privacy questions or to exercise your rights, contact us at:
          </p>
          <ul>
            <li><strong>Email:</strong> privacy@pravisboutique.com</li>
            <li><strong>Data Protection Officer:</strong> dpo@pravisboutique.com</li>
            <li><strong>Address:</strong> Pravis Boutique, Hyderabad, India</li>
          </ul>
        </div>

        <div class="mt-8 pt-8 border-t text-center">
          <button
            class="btn-primary px-6 py-3"
            @click="goBack"
          >
            ← Back to Boutique
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PrivacyPage',
  data () {
    return {
      lastUpdated: new Date().toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      })
    }
  },
  head () {
    return {
      title: 'Privacy Policy - Pravis Boutique',
      meta: [
        {
          hid: 'description',
          name: 'description',
          content: 'Privacy Policy for Pravis Boutique explaining how we collect, use, and protect your data including voice interactions with Ask Pravi.'
        }
      ]
    }
  },
  methods: {
    goBack () {
      this.$router.go(-1)
    }
  }
}
</script>

<style scoped>
.prose {
  color: #374151;
}

.prose h2 {
  color: #1f2937;
  font-weight: 700;
  margin-top: 2rem;
  margin-bottom: 1rem;
}

.prose h3 {
  color: #374151;
  font-weight: 600;
  margin-top: 1.5rem;
  margin-bottom: 0.75rem;
}

.prose p {
  margin-bottom: 1rem;
  line-height: 1.7;
}

.prose ul {
  margin: 1rem 0;
  padding-left: 1.5rem;
}

.prose li {
  margin-bottom: 0.5rem;
}

.prose strong {
  font-weight: 600;
  color: #1f2937;
}
</style>
