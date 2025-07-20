const { contextBridge, ipcRenderer } = require('electron')

// Expose protected methods that allow the renderer process to use
// the ipcRenderer without exposing the entire object
contextBridge.exposeInMainWorld('electronAPI', {
  // App control
  minimize: () => ipcRenderer.invoke('minimize'),
  maximize: () => ipcRenderer.invoke('maximize'),
  close: () => ipcRenderer.invoke('close'),

  // System info
  platform: process.platform,

  // Voice agent integration (future)
  startVoiceRecording: () => ipcRenderer.invoke('start-voice-recording'),
  stopVoiceRecording: () => ipcRenderer.invoke('stop-voice-recording'),

  // Analytics events
  trackEvent: (event, data) => ipcRenderer.invoke('track-event', event, data),

  // Notifications
  showNotification: (title, body) => ipcRenderer.invoke('show-notification', title, body),

  // File operations (for future features)
  selectFile: () => ipcRenderer.invoke('select-file'),
  saveFile: data => ipcRenderer.invoke('save-file', data),

  // App metadata
  getVersion: () => ipcRenderer.invoke('get-version'),
  isProduction: () => process.env.NODE_ENV === 'production'
})

// Listen for window events
window.addEventListener('DOMContentLoaded', () => {
  const replaceText = (selector, text) => {
    const element = document.getElementById(selector)
    if (element) { element.innerText = text }
  }

  for (const type of ['chrome', 'node', 'electron']) {
    replaceText(`${type}-version`, process.versions[type])
  }
})
