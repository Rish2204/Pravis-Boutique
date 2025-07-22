<template>
  <component
    :is="tag"
    :class="[
      'inline-flex items-center justify-center transition-colors duration-150',
      sizeClasses,
      variantClasses,
      roundedClasses,
      { 
        'opacity-50 cursor-not-allowed': disabled,
        'w-full': block
      },
      className
    ]"
    :disabled="disabled || loading"
    :role="tag !== 'button' ? 'button' : undefined"
    :tabindex="tag !== 'button' && !disabled ? '0' : undefined"
    :aria-disabled="disabled || loading ? 'true' : 'false'"
    :aria-busy="loading ? 'true' : 'false'"
    :aria-label="ariaLabel"
    @keydown.space.prevent="handleKeyDown"
    @keydown.enter.prevent="handleKeyDown"
    v-bind="$attrs"
  >
    <!-- Loading spinner -->
    <svg 
      v-if="loading" 
      class="animate-spin -ml-1 mr-2 h-4 w-4" 
      xmlns="http://www.w3.org/2000/svg" 
      fill="none" 
      viewBox="0 0 24 24"
    >
      <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
      <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
    </svg>
    
    <!-- Icon (if present) -->
    <slot name="icon"></slot>
    
    <!-- Default slot for button text -->
    <slot></slot>
  </component>
</template>

<script setup>
import { computed } from 'vue'

// Import audio feedback utilities
import { playAudioFeedback } from '~/utils/accessibility'

// Emits
const emit = defineEmits(['click'])

// Props
const props = defineProps({
  tag: {
    type: String,
    default: 'button'
  },
  variant: {
    type: String,
    default: 'primary',
    validator: (value) => [
      'primary', 
      'secondary', 
      'success', 
      'danger', 
      'warning', 
      'info',
      'light', 
      'dark', 
      'outline-primary', 
      'outline-secondary',
      'link'
    ].includes(value)
  },
  size: {
    type: String,
    default: 'md',
    validator: (value) => ['xs', 'sm', 'md', 'lg', 'xl'].includes(value)
  },
  rounded: {
    type: String,
    default: 'md',
    validator: (value) => ['none', 'sm', 'md', 'lg', 'full'].includes(value)
  },
  loading: {
    type: Boolean,
    default: false
  },
  disabled: {
    type: Boolean,
    default: false
  },
  block: {
    type: Boolean,
    default: false
  },
  className: {
    type: String,
    default: ''
  },
  ariaLabel: {
    type: String,
    default: ''
  },
  playSound: {
    type: Boolean,
    default: false
  }
})

// Compute classes based on variant
const variantClasses = computed(() => {
  switch (props.variant) {
    case 'primary':
      return 'bg-pravis-600 hover:bg-pravis-700 text-white shadow-sm focus:ring-2 focus:ring-offset-2 focus:ring-pravis-500'
    case 'secondary':
      return 'bg-gray-600 hover:bg-gray-700 text-white shadow-sm focus:ring-2 focus:ring-offset-2 focus:ring-gray-500'
    case 'success':
      return 'bg-green-600 hover:bg-green-700 text-white shadow-sm focus:ring-2 focus:ring-offset-2 focus:ring-green-500'
    case 'danger':
      return 'bg-red-600 hover:bg-red-700 text-white shadow-sm focus:ring-2 focus:ring-offset-2 focus:ring-red-500'
    case 'warning':
      return 'bg-yellow-500 hover:bg-yellow-600 text-white shadow-sm focus:ring-2 focus:ring-offset-2 focus:ring-yellow-400'
    case 'info':
      return 'bg-blue-500 hover:bg-blue-600 text-white shadow-sm focus:ring-2 focus:ring-offset-2 focus:ring-blue-400'
    case 'light':
      return 'bg-gray-100 hover:bg-gray-200 text-gray-800 focus:ring-2 focus:ring-offset-2 focus:ring-gray-300'
    case 'dark':
      return 'bg-gray-800 hover:bg-gray-900 text-white shadow-sm focus:ring-2 focus:ring-offset-2 focus:ring-gray-700'
    case 'outline-primary':
      return 'border border-pravis-600 text-pravis-600 hover:bg-pravis-50 focus:ring-2 focus:ring-offset-2 focus:ring-pravis-500'
    case 'outline-secondary':
      return 'border border-gray-600 text-gray-600 hover:bg-gray-50 focus:ring-2 focus:ring-offset-2 focus:ring-gray-500'
    case 'link':
      return 'text-pravis-600 hover:text-pravis-700 underline focus:ring-2 focus:ring-offset-2 focus:ring-pravis-500'
    default:
      return 'bg-pravis-600 hover:bg-pravis-700 text-white shadow-sm focus:ring-2 focus:ring-offset-2 focus:ring-pravis-500'
  }
})

// Compute classes based on size
const sizeClasses = computed(() => {
  switch (props.size) {
    case 'xs':
      return 'px-2 py-1 text-xs'
    case 'sm':
      return 'px-2.5 py-1.5 text-sm'
    case 'md':
      return 'px-4 py-2 text-sm'
    case 'lg':
      return 'px-5 py-2.5 text-base'
    case 'xl':
      return 'px-6 py-3 text-base'
    default:
      return 'px-4 py-2 text-sm'
  }
})

// Compute classes based on rounded value
const roundedClasses = computed(() => {
  switch (props.rounded) {
    case 'none':
      return 'rounded-none'
    case 'sm':
      return 'rounded-sm'
    case 'md':
      return 'rounded-md'
    case 'lg':
      return 'rounded-lg'
    case 'full':
      return 'rounded-full'
    default:
      return 'rounded-md'
  }
})

// Handle keyboard events (space/enter) when not a button
const handleKeyDown = (event) => {
  if ((props.tag !== 'button' && !props.disabled && !props.loading) && 
      (event.key === ' ' || event.key === 'Enter')) {
    // Trigger click event
    emit('click', event)
    
    // Play sound if enabled
    if (props.playSound) {
      playAudioFeedback('click')
    }
    
    // Execute default slot click handler if present
    const defaultSlot = slots.default && slots.default()
    if (defaultSlot) {
      const clickHandler = defaultSlot[0]?.props?.onClick
      if (typeof clickHandler === 'function') {
        clickHandler(event)
      }
    }
  }
}
</script>
