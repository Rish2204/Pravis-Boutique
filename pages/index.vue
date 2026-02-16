<template>
  <div class="min-h-screen font-sans bg-pravis-50">
    <!-- Navigation -->
    <Navigation />

    <!-- Hero Section -->
    <HeroSection />

    <!-- Featured Products -->
    <FeaturedProducts />

    <!-- About Section -->
    <AboutSection />

    <!-- Footer -->
    <FooterSection />
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'

// Smooth scrolling for anchor links
onMounted(() => {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault()
      const target = document.querySelector(this.getAttribute('href'))
      if (target) {
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        })
      }
    })
  })
  
  // Scroll animations
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  }
  
  const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('fade-in')
      }
    })
  }, observerOptions)
  
  // Observe elements for animation
  document.querySelectorAll('.hover-lift').forEach(el => {
    observer.observe(el)
  })
})
</script>

<style>
/* Global styles for animations */
.fade-in {
  animation: fadeIn 0.6s ease-out;
}

@keyframes fadeIn {
  from { 
    opacity: 0; 
    transform: translateY(20px); 
  }
  to { 
    opacity: 1; 
    transform: translateY(0); 
  }
}
</style>
