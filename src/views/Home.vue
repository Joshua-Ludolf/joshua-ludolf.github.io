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
    degree: 'Master\'s degree in Artificial Intelligence', 
    university: 'University of Texas at Austin',
        graduationDate: 'May 2026'
  }
})

const portfolioInfo = ref({
  title: 'Welcome to My Portfolio',
  subtitle: 'Passionate Computer Science Student & Aspiring AI Professional',
  description: 'This portfolio showcases my skills, projects, and experiences in computer science. I\'m passionate about software development, data analysis, and problem-solving.'
})

const skillCategories = ref([
  {
    title: 'Specialized Expertise',
    description: 'Deep knowledge in artificial intelligence, machine learning model development, and data processing for advanced applications.',
    icon: '🧠'
  },
  {
    title: 'Full-Stack Development',
    description: 'End-to-end web application development from backend services to responsive frontend interfaces using modern technologies.',
    icon: '🏗️'
  },
  {
    title: 'Data & Analytics',
    description: 'Database design, SQL optimization, data processing pipelines, and analytics for informed decision-making.',
    icon: '📊'
  }
])
</script>

<template>
  <!-- Hero Section -->
  <section id="hero" class="hero-section">
    <div class="hero-content">
      <p class="hero-eyebrow">👋 Hi, I'm Joshua Ludolf</p>
      <h1 class="hero-title">
        Building the future with<br>
        <span>AI &amp; Software</span>
      </h1>
      <p class="hero-subtitle">{{ portfolioInfo.subtitle }}</p>

      <!-- Education Cards -->
      <div class="education-cards">
        <div class="education-card">
          <h3>Alumni</h3>
          <div class="degree-info">
            <h4>{{ education.previous.degree }}</h4>
            <p class="university">{{ education.previous.university }}</p>
            <p class="graduation-date">Graduated {{ education.previous.graduationDate }}</p>
          </div>
        </div>
        <div class="education-card">
          <h3>Currently Pursuing</h3>
          <div class="degree-info">
            <h4>{{ education.current.degree }}</h4>
            <p class="university">{{ education.current.university }}</p>
            <p class="graduation-date">Expected {{ education.current.graduationDate }}</p>
          </div>
        </div>
      </div>

      <!-- CTA -->
      <p class="portfolio-description">{{ portfolioInfo.description }}</p>
      <div class="cta-buttons">
        <router-link to="/projects" class="btn btn-primary">View My Projects</router-link>
        <router-link to="/contact" class="btn btn-secondary">Get In Touch</router-link>
      </div>
    </div>
  </section>

  <!-- Technical Expertise Section -->
  <section class="skills-preview-section">
    <div class="container">
      <h2 class="section-title">Technical Expertise</h2>
      <div class="expertise-grid">
        <div v-for="expertise in skillCategories" :key="expertise.title" class="expertise-card">
          <div class="expertise-icon">{{ expertise.icon }}</div>
          <h3>{{ expertise.title }}</h3>
          <p>{{ expertise.description }}</p>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.hero-eyebrow {
  font-size: 1rem;
  font-weight: 600;
  color: rgba(255,255,255,0.65);
  letter-spacing: 0.04em;
  margin-bottom: 0.75rem;
}
</style>