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

const skillCategories = ref([
  {
    title: 'Languages',
    icon: '💻',
    tags: ['Python', 'Java', 'HTML', 'CSS', 'SQL', 'Markdown']
  },
  {
    title: 'Frameworks',
    icon: '⚙️',
    tags: ['PyTorch', 'TensorFlow', 'Flask', 'Django', 'FastAPI', 'Vue.js']
  },
  {
    title: 'Tools & Platforms',
    icon: '🛠️',
    tags: ['Docker', 'Git', 'GitHub', 'VS Code', 'Jupyter', 'Linux']
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

  <!-- Skills preview -->
  <section class="skills-preview-section">
    <div class="container">
      <h2 class="section-title">What I Work With</h2>
      <div class="skills-grid">
        <div v-for="cat in skillCategories" :key="cat.title" class="skill-category">
          <h3>{{ cat.icon }} {{ cat.title }}</h3>
          <div class="skill-tags">
            <span v-for="tag in cat.tags" :key="tag" class="skill-tag">{{ tag }}</span>
          </div>
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