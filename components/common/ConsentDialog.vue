<template>
  <div v-if="showDialog" class="consent-overlay" role="dialog" aria-modal="true" aria-labelledby="consent-dialog-title">
    <div class="consent-dialog" tabindex="-1" ref="dialogRef">
      <div class="boutique-logo">
        <h2 id="consent-dialog-title">Welcome to Pravis Boutique!</h2>
      </div>

      <div class="disclaimer-content">
        <p>
          We use cookies and analytics to improve your shopping experience.
          Would you like to allow us to collect anonymous usage data?
        </p>
      </div>

      <div class="consent-options" role="radiogroup" aria-labelledby="consent-dialog-title">
        <label class="consent-option">
          <input
            type="radio"
            name="consent"
            value="accept"
            v-model="selectedOption"
          />
          <span class="checkmark" aria-hidden="true"></span>
          <span>Sure, Why not!</span>
        </label>

        <label class="consent-option">
          <input
            type="radio"
            name="consent"
            value="decline"
            v-model="selectedOption"
          />
          <span class="checkmark" aria-hidden="true"></span>
          <span>Maybe, Not right now!</span>
        </label>
      </div>

      <button
        class="continue-button"
        @click="handleConsentSubmit"
        :disabled="!selectedOption"
        aria-label="Continue with selected preference"
      >
        Continue
      </button>

      <div class="privacy-note">
        <small>
          You can change your preference anytime in Settings.
          <NuxtLink to="/privacy" target="_blank">Privacy Policy</NuxtLink>
        </small>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'

const emit = defineEmits<{
  consentDecision: [decision: boolean]
}>()

const showDialog = ref(false)
const selectedOption = ref<string | null>(null)
const dialogRef = ref<HTMLElement | null>(null)

onMounted(() => {
  const existingConsent = localStorage.getItem('pravis-consent')
  if (!existingConsent) {
    showDialog.value = true
  }
})

const handleConsentSubmit = () => {
  if (!selectedOption.value) return

  const consent = selectedOption.value === 'accept'

  localStorage.setItem('pravis-consent', JSON.stringify({
    consent,
    timestamp: new Date().toISOString(),
    version: '1.0'
  }))

  emit('consentDecision', consent)
  showDialog.value = false
}
</script>

<style scoped>
.consent-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 10000;
  backdrop-filter: blur(5px);
}

.consent-dialog {
  background: linear-gradient(135deg, #fff 0%, #f8f9ff 100%);
  border-radius: 20px;
  padding: 32px;
  max-width: 480px;
  width: 90vw;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  text-align: center;
  animation: slideIn 0.3s ease-out;
}

@keyframes slideIn {
  from { opacity: 0; transform: translateY(-30px); }
  to { opacity: 1; transform: translateY(0); }
}

.boutique-logo h2 {
  color: #2c3e50;
  font-family: 'Playfair Display', serif;
  margin-bottom: 20px;
  font-size: 28px;
}

.disclaimer-content {
  margin: 24px 0;
  color: #555;
  line-height: 1.6;
  font-size: 16px;
}

.consent-options {
  margin: 32px 0;
  text-align: left;
}

.consent-option {
  display: flex;
  align-items: center;
  margin: 16px 0;
  cursor: pointer;
  font-size: 18px;
  font-weight: 500;
  color: #2c3e50;
  transition: all 0.2s ease;
  padding: 12px;
  border-radius: 10px;
}

.consent-option:hover {
  background: #f0f4ff;
  transform: translateX(5px);
}

.consent-option input[type="radio"] {
  display: none;
}

.checkmark {
  width: 24px;
  height: 24px;
  border: 2px solid #8B0000;
  border-radius: 50%;
  margin-right: 16px;
  position: relative;
  transition: all 0.2s ease;
}

.consent-option input[type="radio"]:checked + .checkmark {
  background: #8B0000;
  border-color: #8B0000;
}

.consent-option input[type="radio"]:checked + .checkmark::after {
  content: '\2713';
  position: absolute;
  color: white;
  font-size: 16px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.continue-button {
  background: linear-gradient(135deg, #8B0000 0%, #A0001C 100%);
  color: white;
  border: none;
  padding: 16px 32px;
  border-radius: 50px;
  font-size: 18px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  margin-top: 24px;
}

.continue-button:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(139, 0, 0, 0.4);
}

.continue-button:disabled {
  background: #bdc3c7;
  cursor: not-allowed;
}

.privacy-note {
  margin-top: 20px;
  color: #7f8c8d;
}

.privacy-note a {
  color: #8B0000;
  text-decoration: none;
}
</style>
