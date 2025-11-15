<script setup>
import { ref } from 'vue'

const termsInfo = ref({
  title: 'Terms of Service',
  effectiveDate: 'January 1, 2024',
  lastUpdated: 'January 1, 2024',
  summary: 'By accessing and using this portfolio website, you agree to comply with these terms and conditions.'
})

const websiteUsage = ref({
  permitted: [
    'View and browse portfolio content',
    'Contact me for professional inquiries',
    'Share links to this website'
  ],
  prohibited: [
    'Copying or redistributing content without permission',
    'Attempting to hack or disrupt the website',
    'Using automated systems to scrape content'
  ]
})

const intellectualProperty = ref([
  '📝 Text & Articles',
  '🎨 Design & Graphics', 
  '💻 Code Examples',
  '📷 Images & Media'
])

const externalLinksInfo = ref([
  'External links are provided for your convenience and information',
  'I do not endorse or take responsibility for external website content',
  'External sites have their own terms and privacy policies',
  'I am not liable for any issues arising from your use of external sites'
])

const liabilityLimitations = ref([
  {
    title: 'Website Availability',
    description: 'While I strive to maintain website availability, I cannot guarantee uninterrupted access or error-free operation.'
  },
  {
    title: 'Content Accuracy',
    description: 'Information is provided "as is" and may be subject to change without notice. I make no warranties regarding accuracy or completeness.'
  },
  {
    title: 'Limitation of Liability',
    description: 'I shall not be liable for any direct, indirect, incidental, or consequential damages arising from your use of this website.'
  }
])

const contactGuidelines = ref({
  appropriate: [
    'Job opportunities and collaborations',
    'Technical questions about projects',
    'Professional networking',
    'Speaking or presentation requests'
  ],
  inappropriate: [
    'Spam or promotional messages',
    'Solicitation of services',
    'Off-topic or personal requests',
    'Harassment or offensive content'
  ]
})
</script>

<template>
  <div class="page-wrapper">
    <section id="terms" class="container">
      <div class="policy-content">
      <div class="policy-header">
        <h2>{{ termsInfo.title }}</h2>
        <p class="policy-intro">Effective Date: <strong>{{ termsInfo.effectiveDate }}</strong></p>
        <p class="policy-summary">{{ termsInfo.summary }}</p>
      </div>

      <div class="policy-section">
        <h3><i class="section-icon">🌐</i> Website Usage</h3>
        <div class="terms-grid">
          <div class="terms-card">
            <h4>Permitted Use</h4>
            <ul>
              <li v-for="item in websiteUsage.permitted" :key="item">{{ item }}</li>
            </ul>
          </div>
          <div class="terms-card">
            <h4>Prohibited Activities</h4>
            <ul>
              <li v-for="item in websiteUsage.prohibited" :key="item">{{ item }}</li>
            </ul>
          </div>
        </div>
      </div>

      <div class="policy-section">
        <h3><i class="section-icon">⚖️</i> Intellectual Property</h3>
        <div class="ip-notice">
          <p>All content on this website, including but not limited to:</p>
          <div class="ip-items">
            <span 
              v-for="item in intellectualProperty" 
              :key="item"
              class="ip-badge"
            >
              {{ item }}
            </span>
          </div>
          <p>...is the intellectual property of Joshua Ludolf and is protected by copyright laws. Unauthorized reproduction or distribution is prohibited.</p>
        </div>
      </div>

      <div class="policy-section">
        <h3><i class="section-icon">🔗</i> External Links</h3>
        <div class="links-info">
          <p>This website contains links to external websites and resources. Please note:</p>
          <div class="disclaimer-box">
            <ul>
              <li v-for="info in externalLinksInfo" :key="info">{{ info }}</li>
            </ul>
          </div>
        </div>
      </div>

      <div class="policy-section">
        <h3><i class="section-icon">⚠️</i> Disclaimer & Limitations</h3>
        <div class="liability-section">
          <div 
            v-for="limitation in liabilityLimitations" 
            :key="limitation.title"
            class="liability-item"
          >
            <h4>{{ limitation.title }}</h4>
            <p>{{ limitation.description }}</p>
          </div>
        </div>
      </div>

      <div class="policy-section">
        <h3><i class="section-icon">📧</i> Professional Inquiries</h3>
        <div class="inquiry-guidelines">
          <p>When contacting me through this website:</p>
          <div class="contact-terms">
            <div class="contact-do">
              <h4>✅ Appropriate Inquiries</h4>
              <ul>
                <li v-for="item in contactGuidelines.appropriate" :key="item">{{ item }}</li>
              </ul>
            </div>
            <div class="contact-dont">
              <h4>❌ Inappropriate Content</h4>
              <ul>
                <li v-for="item in contactGuidelines.inappropriate" :key="item">{{ item }}</li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      <div class="policy-section">
        <h3><i class="section-icon">🏛️</i> Governing Law</h3>
        <div class="legal-info">
          <p>These terms and conditions are governed by the laws of the <strong>United States</strong>. Any disputes arising from your use of this website shall be subject to the exclusive jurisdiction of the courts in the applicable state.</p>
          <div class="jurisdiction-note">
            <p><strong>Note:</strong> By using this website, you consent to the jurisdiction and venue of these courts.</p>
          </div>
        </div>
      </div>

      <div class="policy-footer">
        <p><strong>Last Updated:</strong> {{ termsInfo.lastUpdated }}</p>
        <p>These terms may be updated periodically. Continued use of the website constitutes acceptance of any changes.</p>
        <div class="terms-contact">
          <p><strong>Questions?</strong> Contact me at <a href="mailto:joshualudolf@gmail.com">joshualudolf@gmail.com</a></p>
        </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
/* Page-specific styles can go here if needed */
</style>