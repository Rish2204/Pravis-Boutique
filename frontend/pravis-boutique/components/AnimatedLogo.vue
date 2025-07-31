<template>
  <div class="animated-logo-container">
    <div class="logo-circle">
      <!-- P-Peacock Logo SVG matching your exact brand image -->
      <svg 
        class="peacock-logo" 
        viewBox="0 0 120 100" 
        xmlns="http://www.w3.org/2000/svg"
      >
        <!-- P-Peacock integrated design -->
        <g fill="#D4AF37" stroke="none">
          <!-- Letter P vertical stem -->
          <rect x="15" y="15" width="8" height="70" rx="2"/>
          
          <!-- P upper horizontal section integrated with peacock head -->
          <path d="M23 15 Q45 10 55 25 Q58 35 50 40 L25 40 Z"/>
          
          <!-- Peacock head and beak profile -->
          <path d="M50 25 Q60 20 65 25 Q68 30 60 35 Q55 32 50 30"/>
          
          <!-- Peacock neck flowing from P -->
          <path d="M50 30 Q65 45 70 60 Q68 65 60 60 Q50 50 45 40"/>
          
          <!-- Decorative tail feathers - Traditional Indian motifs -->
          <!-- Main tail feather 1 -->
          <path d="M70 45 Q85 40 95 50 Q100 60 90 65 Q80 68 75 60 Q72 55 70 50"/>
          
          <!-- Main tail feather 2 -->
          <path d="M75 60 Q90 65 100 75 Q105 85 95 88 Q85 85 80 78 Q77 70 75 65"/>
          
          <!-- Ornamental swirls and flourishes -->
          <!-- Swirl 1 - upper decorative element -->
          <path d="M25 20 Q30 15 35 20 Q38 25 35 30 Q30 35 25 30 Q22 25 25 20" fill-opacity="0.8"/>
          
          <!-- Swirl 2 - flowing from peacock -->
          <path d="M60 70 Q70 75 75 85 Q78 90 75 95 Q70 98 65 95 Q60 90 62 85 Q65 80 60 75" fill-opacity="0.8"/>
          
          <!-- Leaf motifs on tail -->
          <ellipse cx="85" cy="55" rx="3" ry="8" transform="rotate(30 85 55)" fill-opacity="0.9"/>
          <ellipse cx="90" cy="75" rx="2.5" ry="6" transform="rotate(45 90 75)" fill-opacity="0.9"/>
          <ellipse cx="80" cy="80" rx="2" ry="5" transform="rotate(60 80 80)" fill-opacity="0.9"/>
          
          <!-- Additional decorative swirls -->
          <path d="M35 25 Q40 22 42 28 Q40 32 35 30" fill-opacity="0.7"/>
          <path d="M32 35 Q38 32 40 38 Q38 42 32 40" fill-opacity="0.7"/>
          
          <!-- Fine detail lines in tail -->
          <path d="M78 50 Q82 52 85 58" stroke="#D4AF37" stroke-width="1" fill="none" opacity="0.8"/>
          <path d="M82 65 Q86 67 88 73" stroke="#D4AF37" stroke-width="1" fill="none" opacity="0.8"/>
          <path d="M85 78 Q88 80 90 85" stroke="#D4AF37" stroke-width="1" fill="none" opacity="0.8"/>
        </g>
      </svg>
    </div>
  </div>
</template>

<script setup>
// Static P-Peacock logo component
</script>

<style scoped>
.animated-logo-container {
  display: flex;
  align-items: center;
  justify-content: center;
}

.logo-circle {
  width: 120px;
  height: 120px;
  background: linear-gradient(135deg, #fff 0%, #f8f8f8 100%);
  border: 4px solid #D4AF37;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  box-shadow: 
    0 8px 32px rgba(212, 175, 55, 0.3),
    inset 0 2px 8px rgba(255, 255, 255, 0.8),
    0 0 0 8px rgba(212, 175, 55, 0.1);
}

.peacock-logo {
  width: 80px;
  height: 66px;
  filter: drop-shadow(0 2px 4px rgba(212, 175, 55, 0.3));
}

/* Responsive design */
@media (max-width: 768px) {
  .logo-circle {
    width: 100px;
    height: 100px;
  }
  
  .peacock-logo {
    width: 66px;
    height: 55px;
  }
}

@media (max-width: 480px) {
  .logo-circle {
    width: 80px;
    height: 80px;
  }
  
  .peacock-logo {
    width: 53px;
    height: 44px;
  }
}
</style>