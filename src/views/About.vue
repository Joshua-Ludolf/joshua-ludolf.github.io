<script setup>
import { ref } from 'vue'

// Reactive data for skills and experience
const skills = ref({
  programming: 'CSS, HTML, Java, Markdown, Maven, Python, SQL',
  frameworks: 'Django, FastAPI, Flask, JavaFX, PyTorch, TensorFlow',
  operatingSystems: 'Linux, Windows',
  tools: 'Docker, Git, GitHub, GitHub Copilot, IntelliJ IDEA, Jupyter Notebook, VS Code'
})

const experience = ref([
  'Developing backend services using Flask',
  'Creating databases from SQL to Firebase',
  'Processing data for Machine Learning applications',
  'Implementing full-stack web applications'
])

const education = ref({
  previous: {
    degree: 'Bachelor\'s degree in Computer Science',
    institution: 'Texas A&M University of San Antonio',
    graduation: 'May 2025'
  },
  current: {
    degree: 'Master\'s degree in Artificial Intelligence',
    institution: 'University of Texas at Austin', 
    graduation: 'June 2027'
  }
})

const aboutInfo = ref({
  intro: 'Hi, I\'m Joshua Ludolf, an aspiring software developer/artificial intelligence professional. I have a strong foundation in various technologies and am always eager to learn and explore new innovations. In my free time, I enjoy working on personal projects, contributing to open-source, and staying updated with the latest trends in technology.'
})
</script>

<template>
  <div class="page-wrapper">
    <section id="about">
      <div class="container">
        <!-- Introduction -->
        <div class="about-intro">
          <h2>About Me</h2>
          <p class="intro-text">{{ aboutInfo.intro }}</p>
        </div>

        <!-- Cards grid -->
        <div class="about-grid">
          <!-- Skills -->
          <div class="about-card">
            <h3><i class="icon">💻</i> Technical Skills</h3>
            <div class="skills-section">
              <div class="skill-group">
                <h4>Programming Languages</h4>
                <p>{{ skills.programming }}</p>
              </div>
              <div class="skill-group">
                <h4>Frameworks &amp; Libraries</h4>
                <p>{{ skills.frameworks }}</p>
              </div>
              <div class="skill-group">
                <h4>Operating Systems</h4>
                <p>{{ skills.operatingSystems }}</p>
              </div>
              <div class="skill-group">
                <h4>Development Tools</h4>
                <p>{{ skills.tools }}</p>
              </div>
            </div>
          </div>

          <!-- Experience -->
          <div class="about-card">
            <h3><i class="icon">🚀</i> Experience</h3>
            <p>
              I have worked on various projects, including <strong>web applications</strong> and
              <strong>machine learning models</strong>. My experience includes:
            </p>
            <ul class="experience-list">
              <li v-for="item in experience" :key="item">{{ item }}</li>
            </ul>
          </div>

          <!-- Education -->
          <div class="about-card">
            <h3><i class="icon">🎓</i> Education</h3>
            <div class="education-info">
              <h4>Alumni</h4>
              <p>
                {{ education.previous.degree }}<br>
                <strong>{{ education.previous.institution }}</strong><br>
                Graduated: {{ education.previous.graduation }}
              </p>
              <h4>Currently Pursuing</h4>
              <p>
                {{ education.current.degree }}<br>
                <strong>{{ education.current.institution }}</strong><br>
                Expected: {{ education.current.graduation }}
              </p>
            </div>
          </div>

          <!-- Connect CTA -->
          <div class="about-card contact-cta">
            <h3><i class="icon">📧</i> Let's Connect</h3>
            <p>
              I'm always interested in discussing new opportunities, collaborating on
              projects, or simply connecting with fellow tech enthusiasts.
            </p>
            <router-link to="/contact" class="cta-button">Get In Touch</router-link>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
/* Page-specific styles can go here if needed */
</style>
