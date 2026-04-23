<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import profileImage from '@/assets/profile.jpg'

const scrolled = ref(false)
const mobileMenuOpen = ref(false)
const router = useRouter()

const socialLinks = [
  {
    name: 'LinkedIn',
    url: 'https://www.linkedin.com/in/joshua-ludolf',
    icon: 'linkedin'
  },
  {
    name: 'GitHub',
    url: 'https://github.com/joshua-ludolf',
    icon: 'github'
  },
  {
    name: 'Devpost',
    url: 'https://devpost.com/joshua-ludolf',
    icon: 'devpost'
  }
]

const handleScroll = () => {
  scrolled.value = window.scrollY > 20
}

const toggleMobileMenu = () => {
  mobileMenuOpen.value = !mobileMenuOpen.value
}

const closeMobileMenu = () => {
  mobileMenuOpen.value = false
}

onMounted(() => window.addEventListener('scroll', handleScroll))
onUnmounted(() => window.removeEventListener('scroll', handleScroll))

router.afterEach(() => {
  closeMobileMenu()
})
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
        <router-link to="/">Home</router-link>
        <router-link to="/about">About</router-link>
        <router-link to="/projects">Projects</router-link>
        <router-link to="/publication">Publications</router-link>
        <router-link to="/contact">Contact</router-link>
      </nav>

      <!-- Social Icons -->
      <div class="header-socials">
        <a v-for="link in socialLinks" :key="link.name" :href="link.url" :aria-label="link.name" target="_blank" class="social-icon-btn" :data-icon="link.icon">
          <svg v-if="link.icon === 'linkedin'" viewBox="0 0 24 24" fill="currentColor">
            <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.474-2.23-1.659-2.23-.905 0-1.385.605-1.61 1.193-.083.201-.103.481-.103.762v5.844h-3.554s.047-9.474 0-10.449h3.554v1.481c.001.023.001.045.001.068.46-.707 1.282-1.716 3.126-1.716 2.289 0 4.002 1.494 4.002 4.712v5.904zM5.337 8.855c-1.144 0-1.915-.759-1.915-1.71 0-.955.771-1.71 1.958-1.71 1.187 0 1.914.755 1.939 1.71 0 .951-.752 1.71-1.982 1.71zm1.582 11.597H3.635V9.003h3.284v11.449zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.225 0z"/>
          </svg>
          <svg v-else-if="link.icon === 'github'" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v 3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
          </svg>
           <svg v-else-if="link.icon === 'devpost'" viewBox="0 0 100 100" fill="currentColor">
            <!-- Hexagon outline -->
            <polygon points="50,10 85,30 85,70 50,90 15,70 15,30" fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/>
            <!-- D shape inside -->
            <g>
              <rect x="38" y="30" width="6" height="40" fill="currentColor"/>
              <path d="M 44 30 Q 60 30 60 50 Q 60 70 44 70 L 44 30" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
            </g>
          </svg>
         </a>
        </div>

        <!-- Hamburger Menu -->
        <button class="hamburger" @click="toggleMobileMenu" :class="{ active: mobileMenuOpen }" aria-label="Toggle menu">
          <span></span>
          <span></span>
          <span></span>
        </button>
      </div>

      <!-- Mobile Menu -->
      <nav :class="['mobile-nav', { open: mobileMenuOpen }]">
        <router-link to="/" @click="closeMobileMenu">Home</router-link>
        <router-link to="/about" @click="closeMobileMenu">About</router-link>
        <router-link to="/projects" @click="closeMobileMenu">Projects</router-link>
        <router-link to="/publication" @click="closeMobileMenu">Publications</router-link>
        <router-link to="/contact" @click="closeMobileMenu">Contact</router-link>
        <router-link to="/privacy" @click="closeMobileMenu">Privacy Policy</router-link>
        <router-link to="/terms" @click="closeMobileMenu">Terms of Service</router-link>
        <div class="mobile-socials">
          <a v-for="link in socialLinks" :key="link.name" :href="link.url" target="_blank" :aria-label="link.name" class="social-icon-btn" :data-icon="link.icon">
            <svg v-if="link.icon === 'linkedin'" viewBox="0 0 24 24" fill="currentColor">
              <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.474-2.23-1.659-2.23-.905 0-1.385.605-1.61 1.193-.083.201-.103.481-.103.762v5.844h-3.554s.047-9.474 0-10.449h3.554v1.481c.001.023.001.045.001.068.46-.707 1.282-1.716 3.126-1.716 2.289 0 4.002 1.494 4.002 4.712v5.904zM5.337 8.855c-1.144 0-1.915-.759-1.915-1.71 0-.955.771-1.71 1.958-1.71 1.187 0 1.914.755 1.939 1.71 0 .951-.752 1.71-1.982 1.71zm1.582 11.597H3.635V9.003h3.284v11.449zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.225 0z"/>
            </svg>
            <svg v-else-if="link.icon === 'github'" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v 3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
            </svg>
             <svg v-else-if="link.icon === 'devpost'" viewBox="0 0 100 100" fill="currentColor">
               <!-- Hexagon outline -->
               <polygon points="50,10 85,30 85,70 50,90 15,70 15,30" fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/>
               <!-- D shape inside -->
               <g>
                 <rect x="38" y="30" width="6" height="40" fill="currentColor"/>
                 <path d="M 44 30 Q 60 30 60 50 Q 60 70 44 70 L 44 30" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
               </g>
             </svg>
           </a>
         </div>
      </nav>
  </header>
</template>

<style scoped>
.site-header {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: rgba(15, 23, 42, 0.85);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid rgba(79, 70, 229, 0.15);
  transition: background 0.3s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.site-header.scrolled {
  background: rgba(15, 23, 42, 0.95);
  box-shadow: 0 8px 32px rgba(79, 70, 229, 0.15);
}

.header-inner {
  display: flex;
  align-items: center;
  gap: 2rem;
  max-width: 1400px;
  margin: 0 auto;
  padding: 0.85rem 2rem;
  height: 72px;
}

/* Brand */
.header-brand {
  display: flex;
  align-items: center;
  gap: 0.9rem;
  flex-shrink: 0;
  text-decoration: none;
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.header-brand:hover {
  transform: scale(1.02);
}

.nav-avatar {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  object-fit: cover;
  border: 2.5px solid #4f46e5;
  box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);
  transition: box-shadow 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.nav-avatar:hover {
  box-shadow: 0 6px 20px rgba(79, 70, 229, 0.4);
}

.brand-text {
  display: flex;
  flex-direction: column;
  line-height: 1.3;
}

.brand-name {
  color: #fff;
  font-weight: 800;
  font-size: 1.05rem;
  letter-spacing: -0.01em;
}

.brand-role {
  background: linear-gradient(135deg, #06b6d4, #4f46e5);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
}

/* Desktop Nav */
.desktop-nav {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-left: auto;
}

.desktop-nav a {
  color: rgba(255, 255, 255, 0.8);
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  font-size: 0.92rem;
  font-weight: 600;
  transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
}

.desktop-nav a::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  width: 0;
  height: 2px;
  background: linear-gradient(90deg, #4f46e5, #06b6d4);
  transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
  transform: translateX(-50%);
}

.desktop-nav a:hover {
  color: #fff;
  background: rgba(79, 70, 229, 0.15);
}

.desktop-nav a:hover::after {
  width: 20px;
}

.desktop-nav a.router-link-active,
.desktop-nav a.router-link-exact-active {
  color: #fff;
  background: linear-gradient(135deg, rgba(79, 70, 229, 0.2), rgba(6, 182, 212, 0.1));
  box-shadow: 0 4px 12px rgba(79, 70, 229, 0.2);
}

.desktop-nav a.router-link-exact-active::after {
  width: 20px;
}

/* Social icons */
.header-socials {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.social-icon-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  background: none;
  border: none;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;
  color: rgba(255, 255, 255, 0.7);
  position: relative;
  padding: 0;
}

.social-icon-btn::before {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(90deg, #4f46e5, #06b6d4);
  transform: scaleX(0);
  transform-origin: center;
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  pointer-events: none;
}

.social-icon-btn:hover {
  color: #fff;
  transform: translateY(-3px);
}

.social-icon-btn:hover::before {
  transform: scaleX(1);
}

.social-icon-btn svg {
  width: 24px;
  height: 24px;
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), filter 0.3s;
  filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.15));
}

.social-icon-btn:hover svg {
  transform: scale(1.2) rotate(5deg);
  filter: drop-shadow(0 4px 8px rgba(79, 70, 229, 0.4));
}

/* Hamburger */
.hamburger {
  display: none;
  flex-direction: column;
  gap: 6px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 6px;
  margin-left: auto;
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.hamburger:hover {
  transform: scale(1.05);
}

.hamburger span {
  display: block;
  width: 26px;
  height: 2.5px;
  background: rgba(255, 255, 255, 0.85);
  border-radius: 2px;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.hamburger.active span:nth-child(1) {
  transform: rotate(45deg) translateY(10px);
}

.hamburger.active span:nth-child(2) {
  opacity: 0;
}

.hamburger.active span:nth-child(3) {
  transform: rotate(-45deg) translateY(-10px);
}

/* Mobile Nav */
.mobile-nav {
  display: none;
  position: absolute;
  top: 72px;
  left: 0;
  right: 0;
  flex-direction: column;
  padding: 1rem;
  border-top: 1px solid rgba(79, 70, 229, 0.15);
  background: rgba(15, 23, 42, 0.98);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  z-index: 999;
}

.mobile-nav.open {
  display: flex;
  animation: slideDown 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

@keyframes slideDown {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.mobile-nav a {
  color: rgba(255, 255, 255, 0.85);
  text-decoration: none;
  font-size: 1rem;
  font-weight: 600;
  padding: 0.75rem 1rem;
  border-radius: 8px;
  border-bottom: 1px solid rgba(79, 70, 229, 0.1);
  transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}

.mobile-nav a:last-of-type {
  border-bottom: none;
}

.mobile-nav a:hover {
  color: #06b6d4;
  background: rgba(79, 70, 229, 0.1);
  padding-left: 1.25rem;
}

.mobile-nav a.router-link-active,
.mobile-nav a.router-link-exact-active {
  color: #4f46e5;
  background: rgba(79, 70, 229, 0.15);
  font-weight: 700;
}

.mobile-socials {
  display: flex;
  gap: 1rem;
  margin-top: 1.25rem;
  padding-top: 1rem;
  border-top: 1px solid rgba(79, 70, 229, 0.15);
}

@media (max-width: 768px) {
  .desktop-nav {
    display: none;
  }
  
  .hamburger { display: flex; }
  
  .header-inner { 
    padding: 0.75rem 1.5rem;
    gap: 1rem;
  }
  
  .header-brand {
    gap: 0.6rem;
  }
  
  .brand-name {
    font-size: 0.95rem;
  }
  
  .nav-avatar {
    width: 40px;
    height: 40px;
  }
  
  .header-socials {
    gap: 1rem;
  }
}
</style>