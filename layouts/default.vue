<template>
  <div>
    <!-- Consistent Header across all pages -->
    <header class="pravis-header">
      <div class="header-pattern"></div>
      <div class="header-content">
        <div class="logo-section">
          <AnimatedLogo />
        </div>
        <div class="brand-text">
          <h1 class="brand-name">pravis</h1>
          <p class="brand-tagline">Drape in Elegance</p>
        </div>
        <div class="sparkle-accent"></div>
      </div>
    </header>

    <!-- Page Content -->
    <main>
      <slot />
    </main>

    <!-- Footer -->
    <footer class="bg-pravis-900 text-white py-8 mt-16">
      <div class="container mx-auto px-4 text-center">
        <p>&copy; 2025 Pravis Boutique. All rights reserved.</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
import AnimatedLogo from '~/components/AnimatedLogo.vue'
</script>

<style scoped>
/* Header matching brand image */
.pravis-header {
  position: relative;
  background: linear-gradient(135deg, #5d1a1a 0%, #7d2525 50%, #5d1a1a 100%);
  padding: 2rem 0;
  overflow: hidden;
}

/* Decorative pattern overlay */
.header-pattern {
  position: absolute;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.05'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
}

.header-content {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 2rem;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

.logo-section {
  flex-shrink: 0;
}

.brand-text {
  text-align: left;
}

.brand-name {
  font-family: 'Playfair Display', serif;
  font-style: italic;
  font-weight: 400;
  font-size: 5rem;
  color: #d4af37;
  margin: 0;
  line-height: 1;
  letter-spacing: 0.02em;
}

.brand-tagline {
  font-family: 'Playfair Display', serif;
  font-style: italic;
  font-size: 1.5rem;
  color: #d4af37;
  margin: 0.5rem 0 0 0;
  opacity: 0.9;
}

/* Sparkle accent */
.sparkle-accent {
  position: absolute;
  right: 10%;
  top: 20%;
  width: 40px;
  height: 40px;
  background: radial-gradient(circle, #d4af37 0%, transparent 70%);
  opacity: 0.6;
}

.sparkle-accent::before,
.sparkle-accent::after {
  content: '';
  position: absolute;
  width: 100%;
  height: 100%;
  background: inherit;
}

.sparkle-accent::before {
  transform: rotate(45deg);
}

.sparkle-accent::after {
  transform: rotate(90deg) scale(0.7);
}

/* Responsive */
@media (max-width: 768px) {
  .header-content {
    flex-direction: column;
    gap: 1rem;
  }
  
  .brand-text {
    text-align: center;
  }
  
  .brand-name {
    font-size: 3.5rem;
  }
  
  .brand-tagline {
    font-size: 1.2rem;
  }
  
  .sparkle-accent {
    display: none;
  }
}

@media (max-width: 480px) {
  .brand-name {
    font-size: 2.5rem;
  }
  
  .brand-tagline {
    font-size: 1rem;
  }
}
</style>
