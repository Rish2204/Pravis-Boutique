<template>
  <button 
    @click="toggleDarkMode"
    class="p-2 rounded-full focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-pravis-500 transition-colors"
    :class="darkModeClasses"
    :title="modeTitle"
  >
    <span class="sr-only">{{ modeTitle }}</span>
    <!-- Sun icon -->
    <svg 
      v-if="currentMode === 'dark'" 
      xmlns="http://www.w3.org/2000/svg" 
      class="h-5 w-5" 
      viewBox="0 0 20 20" 
      fill="currentColor"
    >
      <path fill-rule="evenodd" d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z" clip-rule="evenodd" />
    </svg>
    <!-- Moon icon -->
    <svg 
      v-else 
      xmlns="http://www.w3.org/2000/svg" 
      class="h-5 w-5" 
      viewBox="0 0 20 20" 
      fill="currentColor"
    >
      <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z" />
    </svg>
  </button>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

// Props
const props = defineProps({
  variant: {
    type: String,
    default: 'default',
    validator: value => ['default', 'contrast', 'minimal'].includes(value)
  }
})

// State
const currentMode = ref('light')

// Computed properties
const modeTitle = computed(() => {
  return currentMode.value === 'dark' 
    ? 'Switch to light mode' 
    : 'Switch to dark mode'
})

const darkModeClasses = computed(() => {
  if (props.variant === 'contrast') {
    return currentMode.value === 'dark'
      ? 'bg-white text-gray-900'
      : 'bg-gray-800 text-white'
  } else if (props.variant === 'minimal') {
    return currentMode.value === 'dark'
      ? 'text-yellow-400 hover:text-yellow-500'
      : 'text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200'
  } else {
    return currentMode.value === 'dark'
      ? 'bg-gray-100 text-pravis-800 hover:bg-gray-200'
      : 'bg-gray-800 text-pravis-200 hover:bg-gray-700'
  }
})

// Methods
const toggleDarkMode = () => {
  const { $colorMode } = useNuxtApp()
  const nextMode = currentMode.value === 'dark' ? 'light' : 'dark'
  $colorMode.set(nextMode)
  currentMode.value = nextMode
}

// Initialize on mount
onMounted(() => {
  if (process.client) {
    const { $colorMode } = useNuxtApp()
    currentMode.value = $colorMode.value
  }
})
</script>
