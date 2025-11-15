<script setup>
import { ref } from 'vue'

const policyInfo = ref({
  title: 'Privacy Policy',
  effectiveDate: 'January 1, 2024',
  lastUpdated: 'June 17, 2025',
  summary: 'This privacy policy explains how Joshua Ludolf collects, uses, and protects your information when you visit this portfolio website.'
})

const informationTypes = ref({
  personal: [
    'Name and email address (when you contact us)',
    'Messages sent through contact forms'
  ],
  technical: [
    'IP address and browser information',
    'Pages visited and time spent on site',
    'Device and screen resolution data'
  ]
})

const dataUsage = ref([
  {
    icon: '📧',
    title: 'Communication',
    description: 'To respond to your inquiries and maintain correspondence'
  },
  {
    icon: '📊',
    title: 'Analytics', 
    description: 'To understand website usage and improve user experience'
  },
  {
    icon: '🔧',
    title: 'Technical Improvements',
    description: 'To enhance website functionality and performance'
  }
])

const securityFeatures = ref([
  'SSL Encryption',
  'Secure Hosting', 
  'Limited Data Collection'
])

const userRights = ref([
  {
    title: 'Access',
    description: 'Request a copy of the personal data we hold about you'
  },
  {
    title: 'Correction',
    description: 'Request correction of inaccurate personal information'
  },
  {
    title: 'Deletion', 
    description: 'Request deletion of your personal information'
  },
  {
    title: 'Opt-out',
    description: 'Choose not to receive promotional communications'
  }
])

const thirdPartyServices = ref([
  {
    name: 'Google Privacy Policy',
    url: 'https://policies.google.com/privacy'
  },
  {
    name: 'AdSense Privacy', 
    url: 'https://support.google.com/adsense/answer/48182'
  }
])
</script>

<template>
  <div class="page-wrapper">
    <section id="privacy" class="container">
      <div class="policy-content">
      <div class="policy-header">
        <h2>{{ policyInfo.title }}</h2>
        <p class="policy-intro">Effective Date: <strong>{{ policyInfo.effectiveDate }}</strong></p>
        <p class="policy-summary">{{ policyInfo.summary }}</p>
      </div>

      <div class="policy-section">
        <h3><i class="section-icon">🔍</i> Information We Collect</h3>
        <p>When you visit this website, we may collect the following types of information:</p>
        <div class="info-grid">
          <div class="info-card">
            <h4>Personal Information</h4>
            <ul>
              <li v-for="item in informationTypes.personal" :key="item">{{ item }}</li>
            </ul>
          </div>
          <div class="info-card">
            <h4>Technical Information</h4>
            <ul>
              <li v-for="item in informationTypes.technical" :key="item">{{ item }}</li>
            </ul>
          </div>
        </div>
      </div>

      <div class="policy-section">
        <h3><i class="section-icon">⚙️</i> How We Use Your Information</h3>
        <p>We use the collected information for the following purposes:</p>
        <div class="usage-list">
          <div 
            v-for="usage in dataUsage" 
            :key="usage.title"
            class="usage-item"
          >
            <span class="usage-icon">{{ usage.icon }}</span>
            <div>
              <strong>{{ usage.title }}</strong>
              <p>{{ usage.description }}</p>
            </div>
          </div>
        </div>
      </div>

      <div class="policy-section">
        <h3><i class="section-icon">🔒</i> Data Security</h3>
        <p>Your privacy and data security are important to us. We implement appropriate technical and organizational measures to protect your personal information against unauthorized access, alteration, disclosure, or destruction.</p>
        <div class="security-features">
          <span 
            v-for="feature in securityFeatures" 
            :key="feature"
            class="security-badge"
          >
            {{ feature }}
          </span>
        </div>
      </div>

      <div class="policy-section">
        <h3><i class="section-icon">🌐</i> Third-Party Services</h3>
        <p>This website uses Google Analytics for website analytics and Google AdSense for advertising. These services have their own privacy policies that govern how they collect and use data:</p>
        <div class="third-party-links">
          <a 
            v-for="service in thirdPartyServices"
            :key="service.name"
            :href="service.url" 
            target="_blank" 
            class="btn btn-secondary"
          >
            {{ service.name }}
          </a>
        </div>
      </div>

      <div class="policy-section">
        <h3><i class="section-icon">👤</i> Your Rights</h3>
        <p>You have the following rights regarding your personal information:</p>
        <div class="rights-grid">
          <div 
            v-for="right in userRights" 
            :key="right.title"
            class="right-item"
          >
            <h4>{{ right.title }}</h4>
            <p>{{ right.description }}</p>
          </div>
        </div>
      </div>

      <div class="policy-section contact-section">
        <h3><i class="section-icon">📬</i> Contact Us</h3>
        <p>If you have any questions about this Privacy Policy or wish to exercise your rights, please contact us:</p>
        <div class="contact-info">
          <p><strong>Email:</strong> <a href="mailto:joshualudolf@gmail.com">joshualudolf@gmail.com</a></p>
          <p><strong>Response Time:</strong> We aim to respond within 48 hours</p>
        </div>
      </div>

      <div class="policy-footer">
        <p><strong>Last Updated:</strong> {{ policyInfo.lastUpdated }}</p>
        <p>We may update this Privacy Policy from time to time. Any changes will be posted on this page with an updated effective date.</p>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
/* Page-specific styles can go here if needed */
</style>