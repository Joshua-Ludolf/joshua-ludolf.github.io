<script setup>
import profileImage from '@/assets/profile.jpg'
import linkedinIcon from '@/assets/linkedin-icon.png'
import githubIcon from '@/assets/github-icon.jpg'
import devpostIcon from '@/assets/devpost-icon.jpg'
</script>

<template>
  <header class="font">
    <h1>Joshua Ludolf's Portfolio</h1>
    <img :src="profileImage" alt="Profile Picture" class="profile-pic">
    <div class="social-links">
      <nav>
        <a class="linkedin" href="https://www.linkedin.com/in/joshua-ludolf" target="_blank">
          <img :src="linkedinIcon" width="50" height="50" alt="LinkedIn">
        </a>
        <a class="github" href="https://github.com/joshua-ludolf" target="_blank"> 
          <img :src="githubIcon" width="50" height="50" alt="GitHub">
        </a>
        <a class="devpost" href="https://devpost.com/joshua-ludolf" target="_blank">
          <img :src="devpostIcon" width="50" height="50" alt="Devpost">
        </a>                        
      </nav>
    </div>
    <br>
    
    <nav class="Real-Nav">
      <ul>
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/about">About</router-link></li>
        <li><router-link to="/projects">Projects</router-link></li>
        <li><router-link to="/contact">Contact</router-link></li>
        <li><router-link to="/privacy">Privacy Policy</router-link></li>
        <li><router-link to="/terms">Terms of Service</router-link></li>
      </ul>
    </nav>
  </header>
</template>

<style scoped>
/* Header-specific styles can go here if needed */
</style>