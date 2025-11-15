<script setup>
import { ref } from 'vue'

// Reactive data for education information
const education = ref({
  previous: {
    degree: 'Bachelor of Science in Computer Science',
    university: 'Texas A&M University of San Antonio',
    graduationDate: 'May 2025'
  },
  current: {
    degree: 'Master\'s in Artificial Intelligence', 
    university: 'University of Texas at Austin',
    graduationDate: 'June 2027'
  }
})

const portfolioInfo = ref({
  title: 'Welcome to My Portfolio',
  subtitle: 'Passionate Computer Science Student & Aspiring AI Professional',
  description: 'This portfolio showcases my skills, projects, and experiences in computer science. I\'m passionate about software development, data analysis, and problem-solving.'
})
</script>

<template>
  <!-- Hero Section -->
  <section id="hero" class="hero-section">
    <div class="container">
      <div class="hero-content">
        <h2 class="hero-title">{{ portfolioInfo.title }}</h2>
        <p class="hero-subtitle">{{ portfolioInfo.subtitle }}</p>
        
        <!-- Education Cards -->
        <div class="education-cards">
          <div class="education-card">
            <h3>Previous Studies</h3>
            <div class="degree-info">
              <h4>{{ education.previous.degree }}</h4>
              <p class="university">{{ education.previous.university }}</p>
              <p class="graduation-date">Expected Graduation: {{ education.previous.graduationDate }}</p>
            </div>
          </div>
          
          <div class="education-card">
            <h3>Current/Future Studies</h3>
            <div class="degree-info">
              <h4>{{ education.current.degree }}</h4>
              <p class="university">{{ education.current.university }}</p>
              <p class="graduation-date">Expected Graduation: {{ education.current.graduationDate }}</p>
            </div>
          </div>
        </div>
        
        <!-- Call to Action -->
        <div class="cta-section">
          <p class="portfolio-description">
            {{ portfolioInfo.description }}
          </p>
          <div class="cta-buttons">
            <router-link to="/projects" class="btn btn-primary">View My Projects</router-link>
            <router-link to="/contact" class="btn btn-secondary">Get In Touch</router-link>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
/* Page-specific styles can go here if needed */
</style>