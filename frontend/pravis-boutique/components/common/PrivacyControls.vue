<template>
  <div class="privacy-controls">
    <h3>Your Data & Privacy</h3>
    
    <div class="consent-status">
      <p>
        <strong>Analytics tracking:</strong>
        <span :class="[hasConsent ? 'status-enabled' : 'status-disabled']">
          {{ hasConsent ? 'Enabled' : 'Disabled' }}
        </span>
      </p>
    </div>
    
    <div class="privacy-actions">
      <div class="consent-toggle">
        <label class="toggle-switch">
          <input 
            type="checkbox" 
            :checked="hasConsent" 
            @change="toggleConsent"
          />
          <span class="toggle-slider"></span>
        </label>
        <span class="toggle-label">
          {{ hasConsent ? 'Disable Analytics' : 'Enable Analytics' }}
        </span>
      </div>
      
      <button 
        class="privacy-button export-button" 
        @click="exportUserData"
      >
        Export My Data
      </button>
      
      <button 
        class="privacy-button delete-button" 
        @click="confirmDataDeletion"
      >
        Delete All My Data
      </button>
    </div>
    
    <!-- Confirmation Dialog -->
    <div v-if="showConfirmDialog" class="confirmation-dialog">
      <div class="dialog-content">
        <h4>Confirm Data Deletion</h4>
        <p>
          Are you sure you want to delete all your data? This action cannot be undone.
        </p>
        <div class="dialog-actions">
          <button 
            class="privacy-button cancel-button" 
            @click="showConfirmDialog = false"
          >
            Cancel
          </button>
          <button 
            class="privacy-button delete-button" 
            @click="deleteUserData"
          >
            Yes, Delete My Data
          </button>
        </div>
      </div>
    </div>
    
    <!-- Privacy Policy Summary -->
    <div class="privacy-summary">
      <h4>What We Collect</h4>
      <ul>
        <li>Page views and navigation patterns</li>
        <li>Product interactions (when you view or purchase items)</li>
        <li>Voice interactions with "Ask Pravi" assistant</li>
        <li>Basic device information (screen size, browser type)</li>
      </ul>
      
      <h4>How We Use Your Data</h4>
      <p>
        We use this information to improve our services, personalize your shopping 
        experience, and enhance our voice assistant capabilities.
      </p>
      
      <div class="privacy-links">
        <NuxtLink to="/privacy">Full Privacy Policy</NuxtLink>
        <NuxtLink to="/terms">Terms of Service</NuxtLink>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useAnalyticsStore } from '@/store/analytics';

const analyticsStore = useAnalyticsStore();
const showConfirmDialog = ref(false);

// Compute if consent is given
const hasConsent = computed(() => analyticsStore.hasConsent);

// Toggle consent status
const toggleConsent = () => {
  // Get the current consent status from localStorage
  const storedConsent = localStorage.getItem('pravis-consent');
  
  if (storedConsent) {
    try {
      const consentData = JSON.parse(storedConsent);
      
      // Toggle consent
      const newConsentData = {
        ...consentData,
        consent: !consentData.consent,
        timestamp: new Date().toISOString()
      };
      
      // Store updated consent
      localStorage.setItem('pravis-consent', JSON.stringify(newConsentData));
      
      // Update analytics store
      analyticsStore.setConsent(newConsentData.consent);
      
      // Track consent change if consent is now given
      if (newConsentData.consent) {
        analyticsStore.trackConsentEvent(newConsentData);
      }
    } catch (error) {
      console.error('Error toggling consent:', error);
    }
  } else {
    // No existing consent, create a new one
    const newConsentData = {
      consent: true,
      timestamp: new Date().toISOString(),
      version: '1.0'
    };
    
    // Store consent
    localStorage.setItem('pravis-consent', JSON.stringify(newConsentData));
    
    // Update analytics store
    analyticsStore.setConsent(true);
    
    // Track consent event
    analyticsStore.trackConsentEvent(newConsentData);
  }
};

// Export user data
const exportUserData = async () => {
  const userData = await analyticsStore.exportUserData();
  
  if (userData) {
    // Create and download a JSON file with the user data
    const dataStr = JSON.stringify(userData, null, 2);
    const dataBlob = new Blob([dataStr], { type: 'application/json' });
    const url = window.URL.createObjectURL(dataBlob);
    
    const a = document.createElement('a');
    a.href = url;
    a.download = 'pravis-data-export.json';
    a.click();
    
    window.URL.revokeObjectURL(url);
  } else {
    alert('Could not export data. Please try again later.');
  }
};

// Show confirmation dialog
const confirmDataDeletion = () => {
  showConfirmDialog.value = true;
};

// Delete user data
const deleteUserData = async () => {
  const result = await analyticsStore.deleteUserData();
  
  if (result.success) {
    alert('Your data has been deleted successfully.');
  } else {
    alert(`Could not delete data: ${result.error || 'Unknown error'}`);
  }
  
  showConfirmDialog.value = false;
};
</script>

<style scoped>
.privacy-controls {
  padding: 24px;
  background: #f8f9fa;
  border-radius: 12px;
  margin: 24px 0;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
}

h3 {
  margin-top: 0;
  color: #2c3e50;
  font-size: 24px;
  margin-bottom: 24px;
  border-bottom: 1px solid #e1e4e8;
  padding-bottom: 12px;
}

.consent-status {
  margin-bottom: 24px;
}

.status-enabled {
  color: #27ae60;
  font-weight: bold;
}

.status-disabled {
  color: #e74c3c;
  font-weight: bold;
}

.privacy-actions {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin-bottom: 32px;
}

.consent-toggle {
  display: flex;
  align-items: center;
  margin-bottom: 16px;
}

.toggle-switch {
  position: relative;
  display: inline-block;
  width: 60px;
  height: 34px;
  margin-right: 16px;
}

.toggle-switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.toggle-slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  transition: .4s;
  border-radius: 34px;
}

.toggle-slider:before {
  position: absolute;
  content: "";
  height: 26px;
  width: 26px;
  left: 4px;
  bottom: 4px;
  background-color: white;
  transition: .4s;
  border-radius: 50%;
}

input:checked + .toggle-slider {
  background-color: #3498db;
}

input:checked + .toggle-slider:before {
  transform: translateX(26px);
}

.toggle-label {
  font-size: 16px;
  font-weight: 500;
}

.privacy-button {
  padding: 12px 24px;
  border-radius: 50px;
  border: none;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.export-button {
  background-color: #3498db;
  color: white;
}

.export-button:hover {
  background-color: #2980b9;
  transform: translateY(-2px);
}

.delete-button {
  background-color: #e74c3c;
  color: white;
}

.delete-button:hover {
  background-color: #c0392b;
  transform: translateY(-2px);
}

.cancel-button {
  background-color: #95a5a6;
  color: white;
}

.cancel-button:hover {
  background-color: #7f8c8d;
}

.confirmation-dialog {
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

.dialog-content {
  background: white;
  border-radius: 12px;
  padding: 32px;
  max-width: 480px;
  width: 90%;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
}

.dialog-content h4 {
  margin-top: 0;
  color: #e74c3c;
  font-size: 20px;
}

.dialog-actions {
  display: flex;
  justify-content: flex-end;
  gap: 16px;
  margin-top: 24px;
}

.privacy-summary {
  margin-top: 32px;
  padding-top: 24px;
  border-top: 1px solid #e1e4e8;
}

.privacy-summary h4 {
  color: #2c3e50;
  margin-bottom: 8px;
  font-size: 18px;
}

.privacy-summary ul {
  padding-left: 20px;
  margin-bottom: 24px;
  color: #555;
}

.privacy-summary p {
  color: #555;
  line-height: 1.6;
  margin-bottom: 24px;
}

.privacy-links {
  display: flex;
  gap: 24px;
  margin-top: 16px;
}

.privacy-links a {
  color: #3498db;
  text-decoration: none;
  font-weight: 500;
}

.privacy-links a:hover {
  text-decoration: underline;
}
</style>
