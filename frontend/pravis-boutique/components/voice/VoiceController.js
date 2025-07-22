/**
 * VoiceController.js
 * Handles voice recognition and text-to-speech functionality
 * Implements Phase 1 (Web Speech API) and Phase 2 (Whisper via backend) voice integration
 */
export default class VoiceController {
  constructor() {
    // State
    this.isInitialized = false;
    this.isListening = false;
    this.isSpeaking = false;
    this.transcript = '';
    this.recognition = null;
    this.useBackend = false; // Set to true to use Whisper via backend
    this.context = {};
    this.audioRecorder = null;
    this.audioChunks = [];
    this.voicePreference = 'nova'; // Default voice

    // Callbacks
    this.onTranscriptChange = null;
    this.onListeningChange = null;
    this.onSpeakingChange = null;
    this.onError = null;
    
    // Initialize if in browser environment
    if (typeof window !== 'undefined') {
      this.initialize();
    }
  }

  /**
   * Initialize the voice controller
   */
  initialize() {
    // Check for support
    this.webSpeechSupported = 'webkitSpeechRecognition' in window || 'SpeechRecognition' in window;
    this.textToSpeechSupported = 'speechSynthesis' in window;
    
    // Load user preferences
    this.loadPreferences();
    
    // Initialize Web Speech API if supported
    if (this.webSpeechSupported) {
      const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
      this.recognition = new SpeechRecognition();
      this.recognition.continuous = true;
      this.recognition.interimResults = true;
      this.recognition.lang = 'en-US';
      
      // Set up event handlers
      this.recognition.onstart = () => {
        this.isListening = true;
        if (this.onListeningChange) this.onListeningChange(true);
      };
      
      this.recognition.onend = () => {
        this.isListening = false;
        if (this.onListeningChange) this.onListeningChange(false);
      };
      
      this.recognition.onresult = (event) => {
        const transcript = Array.from(event.results)
          .map(result => result[0].transcript)
          .join('');
          
        this.transcript = transcript;
        if (this.onTranscriptChange) this.onTranscriptChange(transcript);
      };
      
      this.recognition.onerror = (event) => {
        console.error('Speech recognition error', event.error);
        if (this.onError) this.onError(event.error);
      };
    }
    
    // Initialize media recorder for backend processing
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      // We'll initialize this when needed
    }
    
    this.isInitialized = true;
  }

  /**
   * Load user preferences from localStorage
   */
  loadPreferences() {
    if (typeof window === 'undefined') return;
    
    const useBackend = localStorage.getItem('voice-use-backend');
    if (useBackend !== null) {
      this.useBackend = useBackend === 'true';
    }
    
    const voicePreference = localStorage.getItem('voice-preference');
    if (voicePreference) {
      this.voicePreference = voicePreference;
    }
  }

  /**
   * Save user preferences to localStorage
   */
  savePreferences() {
    if (typeof window === 'undefined') return;
    
    localStorage.setItem('voice-use-backend', this.useBackend.toString());
    localStorage.setItem('voice-preference', this.voicePreference);
  }

  /**
   * Set whether to use backend for voice processing
   * @param {boolean} useBackend 
   */
  setUseBackend(useBackend) {
    this.useBackend = !!useBackend;
    this.savePreferences();
  }

  /**
   * Set preferred voice for TTS
   * @param {string} voice 
   */
  setVoicePreference(voice) {
    this.voicePreference = voice;
    this.savePreferences();
  }

  /**
   * Set context information for better command processing
   * @param {Object} context 
   */
  setContext(context) {
    this.context = { ...this.context, ...context };
  }

  /**
   * Start listening for voice input
   * @returns {Promise<boolean>} Success status
   */
  async startListening() {
    if (!this.isInitialized) this.initialize();
    
    // If already listening, do nothing
    if (this.isListening) return true;
    
    try {
      if (this.useBackend) {
        // Start recording for backend processing
        return await this.startRecording();
      } else {
        // Use Web Speech API
        this.transcript = '';
        if (this.onTranscriptChange) this.onTranscriptChange('');
        
        this.recognition.start();
        return true;
      }
    } catch (error) {
      console.error('Error starting voice recognition:', error);
      if (this.onError) this.onError(error.message || 'Failed to start listening');
      return false;
    }
  }

  /**
   * Stop listening for voice input
   * @returns {Promise<string>} Final transcript
   */
  async stopListening() {
    // If not listening, do nothing
    if (!this.isListening) return this.transcript;
    
    try {
      if (this.useBackend) {
        // Stop recording and process with backend
        const audioBlob = await this.stopRecording();
        return await this.processAudioWithBackend(audioBlob);
      } else {
        // Use Web Speech API
        this.recognition.stop();
        return this.transcript;
      }
    } catch (error) {
      console.error('Error stopping voice recognition:', error);
      if (this.onError) this.onError(error.message || 'Failed to stop listening');
      return this.transcript;
    }
  }

  /**
   * Start recording audio for backend processing
   * @returns {Promise<boolean>} Success status
   */
  async startRecording() {
    if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
      throw new Error('Media recording not supported in this browser');
    }
    
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      this.audioRecorder = new MediaRecorder(stream);
      this.audioChunks = [];
      
      this.audioRecorder.ondataavailable = (event) => {
        if (event.data.size > 0) {
          this.audioChunks.push(event.data);
        }
      };
      
      this.audioRecorder.onstart = () => {
        this.isListening = true;
        if (this.onListeningChange) this.onListeningChange(true);
      };
      
      this.audioRecorder.onstop = () => {
        this.isListening = false;
        if (this.onListeningChange) this.onListeningChange(false);
        
        // Release microphone
        stream.getTracks().forEach(track => track.stop());
      };
      
      this.audioRecorder.start(100); // Collect data in 100ms chunks
      return true;
    } catch (error) {
      console.error('Error starting audio recording:', error);
      if (this.onError) this.onError(error.message || 'Failed to access microphone');
      return false;
    }
  }

  /**
   * Stop recording audio and return the blob
   * @returns {Promise<Blob>} Audio blob
   */
  async stopRecording() {
    if (!this.audioRecorder || this.audioRecorder.state === 'inactive') {
      return null;
    }
    
    return new Promise((resolve) => {
      this.audioRecorder.onstop = () => {
        this.isListening = false;
        if (this.onListeningChange) this.onListeningChange(false);
        
        const audioBlob = new Blob(this.audioChunks, { type: 'audio/webm' });
        resolve(audioBlob);
      };
      
      this.audioRecorder.stop();
    });
  }

  /**
   * Process audio with backend Whisper integration
   * @param {Blob} audioBlob 
   * @returns {Promise<string>} Transcribed text
   */
  async processAudioWithBackend(audioBlob) {
    if (!audioBlob) return '';
    
    try {
      const formData = new FormData();
      formData.append('audio_file', audioBlob, 'recording.webm');
      
      // Set save_audio to true to store the audio data in the database
      formData.append('save_audio', 'true');
      
      const response = await fetch('/api/v1/voice/transcribe', {
        method: 'POST',
        body: formData,
        credentials: 'include',
      });
      
      if (!response.ok) {
        throw new Error(`Server responded with ${response.status}: ${response.statusText}`);
      }
      
      const data = await response.json();
      const transcript = data.text || '';
      
      this.transcript = transcript;
      if (this.onTranscriptChange) this.onTranscriptChange(transcript);
      
      return transcript;
    } catch (error) {
      console.error('Error processing audio with backend:', error);
      if (this.onError) this.onError(error.message || 'Failed to process audio');
      return '';
    }
  }

  /**
   * Process a voice command
   * @param {string} command Text command to process
   * @returns {Promise<Object>} Command response
   */
  async processCommand(command) {
    if (!command) return null;
    
    try {
      const response = await fetch('/api/v1/voice/process-command', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          text: command,
          context: this.context
        }),
        credentials: 'include',
      });
      
      if (!response.ok) {
        throw new Error(`Server responded with ${response.status}: ${response.statusText}`);
      }
      
      const data = await response.json();
      
      // Speak the response if text is available
      if (data.text) {
        this.speak(data.text);
      }
      
      return data;
    } catch (error) {
      console.error('Error processing command:', error);
      if (this.onError) this.onError(error.message || 'Failed to process command');
      return {
        text: 'Sorry, I encountered an error processing your request.',
        error: true
      };
    }
  }

  /**
   * Speak text using the Web Speech API or backend TTS
   * @param {string} text Text to speak
   * @param {Object} options Speech options
   * @returns {Promise<boolean>} Success status
   */
  async speak(text, options = {}) {
    if (!text) return false;
    
    try {
      this.isSpeaking = true;
      if (this.onSpeakingChange) this.onSpeakingChange(true);
      
      if (this.useBackend) {
        // Use backend TTS
        return await this.speakWithBackend(text, options);
      } else {
        // Use Web Speech API
        return this.speakWithWebSpeech(text, options);
      }
    } catch (error) {
      console.error('Error speaking text:', error);
      this.isSpeaking = false;
      if (this.onSpeakingChange) this.onSpeakingChange(false);
      if (this.onError) this.onError(error.message || 'Failed to speak text');
      return false;
    }
  }

  /**
   * Speak text using Web Speech API
   * @param {string} text Text to speak
   * @param {Object} options Speech options
   * @returns {boolean} Success status
   */
  speakWithWebSpeech(text, options = {}) {
    if (!this.textToSpeechSupported) {
      throw new Error('Text-to-speech not supported in this browser');
    }
    
    // Cancel any ongoing speech
    window.speechSynthesis.cancel();
    
    // Create utterance
    const utterance = new SpeechSynthesisUtterance(text);
    
    // Set options
    utterance.rate = options.rate || 1;
    utterance.pitch = options.pitch || 1;
    utterance.volume = options.volume || 1;
    
    // Find voice if specified
    if (options.voice) {
      const voices = window.speechSynthesis.getVoices();
      const voice = voices.find(v => v.name === options.voice);
      if (voice) utterance.voice = voice;
    }
    
    // Set up events
    utterance.onend = () => {
      this.isSpeaking = false;
      if (this.onSpeakingChange) this.onSpeakingChange(false);
    };
    
    utterance.onerror = (event) => {
      console.error('Speech synthesis error:', event);
      this.isSpeaking = false;
      if (this.onSpeakingChange) this.onSpeakingChange(false);
      if (this.onError) this.onError(event.error || 'Speech synthesis failed');
    };
    
    // Speak
    window.speechSynthesis.speak(utterance);
    return true;
  }

  /**
   * Speak text using backend TTS
   * @param {string} text Text to speak
   * @param {Object} options Speech options
   * @returns {Promise<boolean>} Success status
   */
  async speakWithBackend(text, options = {}) {
    try {
      const response = await fetch('/api/v1/voice/text-to-speech', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          text: text,
          voice: options.voice || this.voicePreference
        }),
      });
      
      if (!response.ok) {
        throw new Error(`Server responded with ${response.status}: ${response.statusText}`);
      }
      
      const audioBlob = await response.blob();
      const audioUrl = URL.createObjectURL(audioBlob);
      
      const audio = new Audio(audioUrl);
      
      audio.onended = () => {
        this.isSpeaking = false;
        if (this.onSpeakingChange) this.onSpeakingChange(false);
        URL.revokeObjectURL(audioUrl); // Clean up
      };
      
      audio.onerror = (error) => {
        console.error('Audio playback error:', error);
        this.isSpeaking = false;
        if (this.onSpeakingChange) this.onSpeakingChange(false);
        if (this.onError) this.onError('Audio playback failed');
        URL.revokeObjectURL(audioUrl); // Clean up
      };
      
      await audio.play();
      return true;
    } catch (error) {
      console.error('Error using backend TTS:', error);
      this.isSpeaking = false;
      if (this.onSpeakingChange) this.onSpeakingChange(false);
      if (this.onError) this.onError(error.message || 'Failed to generate speech');
      return false;
    }
  }

  /**
   * Stop speaking
   */
  stopSpeaking() {
    if (!this.isSpeaking) return;
    
    if (this.textToSpeechSupported) {
      window.speechSynthesis.cancel();
    }
    
    this.isSpeaking = false;
    if (this.onSpeakingChange) this.onSpeakingChange(false);
  }

  /**
   * Get available voices for Web Speech API
   * @returns {Array} Available voices
   */
  getAvailableVoices() {
    if (!this.textToSpeechSupported) return [];
    
    return window.speechSynthesis.getVoices();
  }

  /**
   * Set callbacks for voice events
   * @param {Object} callbacks Callback functions
   */
  setCallbacks(callbacks) {
    if (callbacks.onTranscriptChange) {
      this.onTranscriptChange = callbacks.onTranscriptChange;
    }
    
    if (callbacks.onListeningChange) {
      this.onListeningChange = callbacks.onListeningChange;
    }
    
    if (callbacks.onSpeakingChange) {
      this.onSpeakingChange = callbacks.onSpeakingChange;
    }
    
    if (callbacks.onError) {
      this.onError = callbacks.onError;
    }
  }
}
