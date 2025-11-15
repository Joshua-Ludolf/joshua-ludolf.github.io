<script setup>
import { ref } from 'vue'

// Reactive data for projects
const projects = ref([
  {
    id: 1,
    title: 'FSA-Benchmark Reproduction Research',
    type: 'Research Project',
    description: 'This research project focuses on identifying the best machine learning models to detect slow failures in disk drives. The work involves data analysis, model comparison, and performance benchmarking.',
    technologies: ['Python', 'Machine Learning', 'Data Analysis'],
    githubUrl: 'https://github.com/Joshua-Ludolf/FSA-benchmarking-Reproduction-Research',
    featured: true
  },
  {
    id: 2, 
    title: 'Promising Products',
    type: 'Web Application',
    description: 'A comprehensive web application where I contributed to the machine learning and data processing components. The frontend utilizes modern React.js framework for a responsive user experience.',
    highlights: {
      title: 'My Contributions:',
      items: [
        'Machine Learning implementation',
        'Data processing and analysis', 
        'Backend integration'
      ]
    },
    technologies: ['React.js', 'Python', 'Machine Learning', 'Data Processing'],
    githubUrl: 'https://github.com/Joshua-Ludolf/Promising-Products',
    featured: false
  },
  {
    id: 3,
    title: 'Techxacial', 
    type: 'Banking Application',
    description: 'A financial technology application designed to provide banking services to underbanked and unbanked populations, offering accessible and easy-to-use banking services.',
    highlights: {
      title: 'Key Features:',
      items: [
        'Accessible banking interface',
        'Secure transaction processing',
        'User-friendly design'
      ]
    },
    technologies: ['Flask', 'MySQL', 'React.js', 'Web Development'],
    githubUrl: 'https://github.com/Joshua-Ludolf/TECHXACIAL/',
    featured: false
  },
  {
    id: 4,
    title: 'Fossil Finances',
    type: 'Senior-Focused Banking',
    description: 'A specialized banking service designed specifically for elderly users, featuring an intuitive interface and simplified banking operations.',
    highlights: {
      title: 'Technical Implementation:',
      items: [
        'Flask backend development',
        'Firebase database integration',
        'Senior-friendly UI/UX design'
      ]
    },
    technologies: ['Flask', 'Firebase', 'React.js', 'Accessibility'],
    githubUrl: 'https://github.com/joshua-ludolf/FossilFinances/',
    featured: false
  }
])

const pageInfo = ref({
  title: 'My Projects',
  intro: 'Here are some of the projects I\'ve worked on, showcasing my skills in web development, machine learning, and software engineering. Each project demonstrates different aspects of my technical expertise and problem-solving abilities.'
})
</script>

<template>
  <div class="page-wrapper">
    <div class="container">
      <section id="projects">
      <div class="projects-header">
        <h2>{{ pageInfo.title }}</h2>
        <p class="projects-intro">
          {{ pageInfo.intro }}
        </p>
      </div>
      
      <div class="projects-container">
        <div 
          v-for="project in projects" 
          :key="project.id"
          :class="['project', { 'featured-project': project.featured }]"
        >
          <div class="project-header">
            <h3>{{ project.title }}</h3>
            <span class="project-type">{{ project.type }}</span>
          </div>
          <p class="project-description">
            {{ project.description }}
          </p>
          
          <div v-if="project.highlights" class="project-highlights">
            <p><strong>{{ project.highlights.title }}</strong></p>
            <ul>
              <li v-for="item in project.highlights.items" :key="item">{{ item }}</li>
            </ul>
          </div>
          
          <div class="project-tech">
            <span 
              v-for="tech in project.technologies" 
              :key="tech"
              class="tech-tag"
            >
              {{ tech }}
            </span>
          </div>
          <div class="project-links">
            <a 
              :href="project.githubUrl" 
              target="_blank" 
              class="project-link"
            >
              <i class="icon">🔗</i> View on GitHub
            </a>
          </div>
        </div>
      </div>
      
      <div class="projects-footer">
        <p>Want to see more of my work? Connect with me on GitHub or LinkedIn!</p>
        <div class="cta-buttons">
          <a 
            href="https://github.com/joshua-ludolf" 
            target="_blank" 
            class="btn btn-primary"
          >
            View All Repositories
          </a>
          <router-link to="/contact" class="btn btn-secondary">Get In Touch</router-link>
        </div>
        </div>
      </section>
    </div>
  </div>
</template>

<style scoped>
/* Page-specific styles can go here if needed */
</style>