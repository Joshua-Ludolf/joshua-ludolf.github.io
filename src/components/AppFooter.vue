<script setup>
import { ref, computed } from 'vue'

const currentYear = computed(() => new Date().getFullYear())
</script>

<template>
  <footer class="site-footer">
    <div class="footer-inner">
      <p class="footer-copy">&copy; {{ currentYear }} Joshua Ludolf &mdash; Built with Vue.js</p>
      <div class="footer-links">
        <router-link to="/privacy">Privacy</router-link>
        <router-link to="/terms">Terms</router-link>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.site-footer {
  background: linear-gradient(135deg, #1a252f 0%, #2c3e50 100%);
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  padding: 18px 2rem;
  position: fixed;
  bottom: 0;
  width: 100%;
  z-index: 999;
}

.footer-inner {
  max-width: 1400px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
}

.footer-copy {
  margin: 0;
  color: rgba(255, 255, 255, 0.6);
  font-size: 0.85rem;
}

.footer-links {
  display: flex;
  gap: 1.25rem;
}

.footer-links a {
  color: rgba(255, 255, 255, 0.5);
  text-decoration: none;
  font-size: 0.82rem;
  transition: color 0.2s;
}

.footer-links a:hover {
  color: #3498db;
}

@media (max-width: 480px) {
  .footer-inner { justify-content: center; text-align: center; }
}
</style>