<script setup>
import { ref, computed } from 'vue'

const currentYear = computed(() => new Date().getFullYear())
</script>

<template>
  <footer>
    <p>
      <strong>
        &copy; {{ currentYear }} Joshua Ludolf
      </strong>
    </p>
  </footer>
</template>

<style scoped>
/* Footer-specific styles can go here if needed */
</style>