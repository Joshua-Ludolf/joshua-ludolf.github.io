<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import profileImage from '@/assets/profile.jpg'
import linkedinIcon from '@/assets/linkedin-icon.png'
import githubIcon from '@/assets/github-icon.jpg'
import devpostIcon from '@/assets/devpost-icon.jpg'

const scrolled = ref(false)
const mobileMenuOpen = ref(false)

const handleScroll = () => {
  scrolled.value = window.scrollY > 20
}

const toggleMenu = () => {
  mobileMenuOpen.value = !mobileMenuOpen.value
}

const closeMenu = () => {
  mobileMenuOpen.value = false
}

onMounted(() => window.addEventListener('scroll', handleScroll))
onUnmounted(() => window.removeEventListener('scroll', handleScroll))
</script>

<template>
  <header :class="['site-header', { scrolled }]">
    <div class="header-inner">
      <!-- Brand / Logo -->
      <div class="header-brand">
        <img :src="profileImage" alt="Joshua Ludolf" class="nav-avatar" />
        <div class="brand-text">
          <span class="brand-name">Joshua Ludolf</span>
          <span class="brand-role">AI & Software Engineer</span>
        </div>
      </div>

      <!-- Desktop Nav -->
      <nav class="desktop-nav">
        <router-link to="/" @click="closeMenu">Home</router-link>
        <router-link to="/about" @click="closeMenu">About</router-link>
        <router-link to="/projects" @click="closeMenu">Projects</router-link>
        <router-link to="/contact" @click="closeMenu">Contact</router-link>
      </nav>

      <!-- Social Icons -->
      <div class="header-socials">
        <a href="https://www.linkedin.com/in/joshua-ludolf" target="_blank" aria-label="LinkedIn" class="social-icon-btn">
          <img :src="linkedinIcon" alt="LinkedIn" />
        </a>
        <a href="https://github.com/joshua-ludolf" target="_blank" aria-label="GitHub" class="social-icon-btn">
          <img :src="githubIcon" alt="GitHub" />
        </a>
        <a href="https://devpost.com/joshua-ludolf" target="_blank" aria-label="Devpost" class="social-icon-btn">
          <img :src="devpostIcon" alt="Devpost" />
        </a>
      </div>

      <!-- Hamburger -->
      <button class="hamburger" @click="toggleMenu" :aria-expanded="mobileMenuOpen" aria-label="Toggle menu">
        <span></span><span></span><span></span>
      </button>
    </div>

    <!-- Mobile Menu -->
    <nav :class="['mobile-nav', { open: mobileMenuOpen }]">
      <router-link to="/" @click="closeMenu">Home</router-link>
      <router-link to="/about" @click="closeMenu">About</router-link>
      <router-link to="/projects" @click="closeMenu">Projects</router-link>
      <router-link to="/contact" @click="closeMenu">Contact</router-link>
      <router-link to="/privacy" @click="closeMenu">Privacy Policy</router-link>
      <router-link to="/terms" @click="closeMenu">Terms of Service</router-link>
      <div class="mobile-socials">
        <a href="https://www.linkedin.com/in/joshua-ludolf" target="_blank" class="social-icon-btn"><img :src="linkedinIcon" alt="LinkedIn" /></a>
        <a href="https://github.com/joshua-ludolf" target="_blank" class="social-icon-btn"><img :src="githubIcon" alt="GitHub" /></a>
        <a href="https://devpost.com/joshua-ludolf" target="_blank" class="social-icon-btn"><img :src="devpostIcon" alt="Devpost" /></a>
      </div>
    </nav>
  </header>
</template>

<style scoped>
.site-header {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: rgba(26, 37, 47, 0.75);
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  transition: background 0.3s ease, box-shadow 0.3s ease;
}

.site-header.scrolled {
  background: rgba(26, 37, 47, 0.95);
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.35);
}

.header-inner {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  max-width: 1400px;
  margin: 0 auto;
  padding: 0.75rem 2rem;
}

/* Brand */
.header-brand {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  flex-shrink: 0;
  text-decoration: none;
}

.nav-avatar {
  width: 42px;
  height: 42px;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid rgba(52, 152, 219, 0.7);
}

.brand-text {
  display: flex;
  flex-direction: column;
  line-height: 1.2;
}

.brand-name {
  color: #fff;
  font-weight: 700;
  font-size: 1rem;
  letter-spacing: 0.02em;
}

.brand-role {
  color: rgba(52, 152, 219, 0.9);
  font-size: 0.72rem;
  font-weight: 500;
  letter-spacing: 0.04em;
}

/* Desktop Nav */
.desktop-nav {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  margin-left: auto;
}

.desktop-nav a {
  color: rgba(255, 255, 255, 0.8);
  text-decoration: none;
  padding: 0.45rem 0.9rem;
  border-radius: 6px;
  font-size: 0.9rem;
  font-weight: 500;
  transition: color 0.2s, background 0.2s;
}

.desktop-nav a:hover,
.desktop-nav a.router-link-active {
  color: #fff;
  background: rgba(52, 152, 219, 0.2);
}

.desktop-nav a.router-link-exact-active {
  color: #fff;
  background: rgba(52, 152, 219, 0.3);
}

/* Social icons */
.header-socials {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.social-icon-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 34px;
  height: 34px;
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.08);
  transition: background 0.2s, transform 0.2s;
}

.social-icon-btn:hover {
  background: rgba(52, 152, 219, 0.3);
  transform: translateY(-2px);
}

.social-icon-btn img {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  object-fit: cover;
}

/* Hamburger */
.hamburger {
  display: none;
  flex-direction: column;
  gap: 5px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 4px;
  margin-left: auto;
}

.hamburger span {
  display: block;
  width: 24px;
  height: 2px;
  background: rgba(255, 255, 255, 0.85);
  border-radius: 2px;
  transition: transform 0.3s, opacity 0.3s;
}

/* Mobile Nav */
.mobile-nav {
  display: none;
  flex-direction: column;
  padding: 0.5rem 1rem 1rem;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
}

.mobile-nav a {
  color: rgba(255, 255, 255, 0.85);
  text-decoration: none;
  font-size: 1rem;
  font-weight: 500;
  padding: 0.65rem 0.5rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
  transition: color 0.2s;
}

.mobile-nav a:hover,
.mobile-nav a.router-link-active {
  color: #3498db;
}

.mobile-socials {
  display: flex;
  gap: 0.75rem;
  margin-top: 1rem;
  padding-top: 0.75rem;
}

@media (max-width: 768px) {
  .desktop-nav,
  .header-socials {
    display: none;
  }
  .hamburger { display: flex; }
  .mobile-nav.open { display: flex; }
  .header-inner { padding: 0.75rem 1.25rem; }
}
</style>