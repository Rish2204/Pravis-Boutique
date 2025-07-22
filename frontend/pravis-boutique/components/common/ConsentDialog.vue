<template>
  <div v-if="showDialog" class="consent-overlay" role="dialog" aria-modal="true" aria-labelledby="consent-dialog-title">
    <div class="consent-dialog" tabindex="-1" ref="dialogRef">
      <div class="boutique-logo">
        <h2 id="consent-dialog-title">Welcome to Pravis Boutique!</h2>
      </div>
      
      <div class="disclaimer-content">
        <p>
          <strong>A Friendly Disclaimer:</strong> This App comes with an AI Agent 
          called <em>"Ask Pravi"</em>. This agent collects data and feedback for 
          training purposes. Should you choose to accept.
        </p>
      </div>

      <div class="consent-options" role="radiogroup" aria-labelledby="consent-dialog-title">
        <label class="consent-option">
          <input
            type="radio"
            name="consent"
            value="accept"
            v-model="selectedOption"
            aria-describedby="accept-description"
            @keydown.space.prevent="selectedOption = 'accept'"
          />
          <span class="checkmark" aria-hidden="true"></span>
          <span>Sure, Why not!</span>
          <span id="accept-description" class="sr-only">Accept data collection and AI voice assistant training</span>
        </label>

        <label class="consent-option">
          <input
            type="radio"
            name="consent"
            value="decline"
            v-model="selectedOption"
            aria-describedby="decline-description"
            @keydown.space.prevent="selectedOption = 'decline'"
          />
          <span class="checkmark" aria-hidden="true"></span>
          <span>Maybe, Not right now!</span>
          <span id="decline-description" class="sr-only">Decline data collection and AI voice assistant training</span>
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

<script setup>
import { ref, onMounted, nextTick } from 'vue';
import { useAnalyticsStore } from '@/store/analytics';
import { createFocusTrap, playAudioFeedback } from '~/utils/accessibility';

const emit = defineEmits(['consentDecision']);

const showDialog = ref(false);
const selectedOption = ref(null);
const dialogRef = ref(null);
const focusTrap = ref(null);
const analyticsStore = useAnalyticsStore();

onMounted(() => {
  // Check if user has already made a consent decision
  const existingConsent = localStorage.getItem('pravis-consent');
  if (!existingConsent) {
    showDialog.value = true;
    
    // Setup focus trap once dialog is visible
    nextTick(() => {
      if (dialogRef.value) {
        focusTrap.value = createFocusTrap(dialogRef.value);
        focusTrap.value.activate();
      }
    });
  }
  
  // Add keyboard event listener for Escape key
  const handleKeydown = (event) => {
    if (event.key === 'Escape' && showDialog.value) {
      // Default to declining on escape
      selectedOption.value = 'decline';
      handleConsentSubmit();
    }
  };
  
  window.addEventListener('keydown', handleKeydown);
  
  // Clean up event listener
  return () => {
    window.removeEventListener('keydown', handleKeydown);
    if (focusTrap.value) {
      focusTrap.value.deactivate();
    }
  };
});

const handleConsentSubmit = () => {
  if (selectedOption.value) {
    // Play audio feedback
    playAudioFeedback(selectedOption.value === 'accept' ? 'success' : 'click');
    
    const consentData = {
      consent: selectedOption.value === 'accept',
      timestamp: new Date().toISOString(),
      version: '1.0'
    };
    
    // Store consent in localStorage
    localStorage.setItem('pravis-consent', JSON.stringify(consentData));
    
    // Update analytics store
    analyticsStore.setConsent(consentData.consent);
    
    // Track consent decision if consent was given
    if (consentData.consent) {
      analyticsStore.trackConsentEvent(consentData);
    }
    
    // Deactivate focus trap before closing
    if (focusTrap.value) {
      focusTrap.value.deactivate();
    }
    
    // Emit event to parent component
    emit('consentDecision', consentData);
    
    showDialog.value = false;
  }
};
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
  position: relative;
  animation: slideIn 0.3s ease-out;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(-30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
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

.disclaimer-content em {
  color: #e74c3c;
  font-weight: 600;
  font-style: normal;
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
  border: 2px solid #3498db;
  border-radius: 50%;
  margin-right: 16px;
  position: relative;
  transition: all 0.2s ease;
}

.consent-option input[type="radio"]:checked + .checkmark {
  background: #3498db;
  border-color: #3498db;
}

.consent-option input[type="radio"]:checked + .checkmark::after {
  content: '✓';
  position: absolute;
  color: white;
  font-size: 16px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.continue-button {
  background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
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
  box-shadow: 0 8px 20px rgba(52, 152, 219, 0.4);
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
  color: #3498db;
  text-decoration: none;
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}
</style>
