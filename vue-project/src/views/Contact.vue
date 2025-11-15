<script setup>
import { ref, reactive } from 'vue'

// Reactive form data
const contactForm = reactive({
  name: '',
  email: '',
  subject: 'Contact from Website',
  message: ''
})

// Contact information
const contactInfo = ref({
  email: 'joshualudolf@gmail.com',
  phone: '+1 (830) 331-0424',
  responseTime: '24-48 hours',
  availability: 'Available for calls weekdays 9 AM - 6 PM CST'
})

// Social links
const socialLinks = ref([
  {
    name: 'LinkedIn',
    url: 'https://www.linkedin.com/in/joshua-ludolf',
    class: 'linkedin-btn'
  },
  {
    name: 'GitHub', 
    url: 'https://github.com/joshua-ludolf',
    class: 'github-btn'
  },
  {
    name: 'Devpost',
    url: 'https://devpost.com/joshua-ludolf', 
    class: 'devpost-btn'
  }
])

// Email client functions
const openEmailClient = (client) => {
  if (!contactForm.name || !contactForm.email || !contactForm.message) {
    alert('Please fill in all required fields (Name, Email, and Message).')
    return
  }
  
  const emailBody = `Hi Joshua,

${contactForm.message}

Best regards,
${contactForm.name}
${contactForm.email}`
  
  const encodedSubject = encodeURIComponent(contactForm.subject)
  const encodedBody = encodeURIComponent(emailBody)
  const toEmail = contactInfo.value.email
  
  let emailUrl
  
  switch(client) {
    case 'gmail':
      emailUrl = `https://mail.google.com/mail/?view=cm&fs=1&to=${toEmail}&su=${encodedSubject}&body=${encodedBody}`
      break
    case 'outlook':
      emailUrl = `https://outlook.live.com/mail/0/deeplink/compose?to=${toEmail}&subject=${encodedSubject}&body=${encodedBody}`
      break
    default:
      emailUrl = `mailto:${toEmail}?subject=${encodedSubject}&body=${encodedBody}`
      break
  }
  
  window.open(emailUrl, '_blank')
}

const copyEmail = () => {
  navigator.clipboard.writeText(contactInfo.value.email).then(() => {
    // Could add a toast notification here
    alert('Email copied to clipboard!')
  })
}

const resetForm = () => {
  contactForm.name = ''
  contactForm.email = ''
  contactForm.subject = 'Contact from Website'
  contactForm.message = ''
}
</script>

<template>
  <div class="page-wrapper">
    <div class="container">
      <section id="contact">
      <div class="contact-header">
        <h2>Get In Touch</h2>
        <p class="contact-intro">
          I'm always interested in discussing new opportunities, collaborating on projects, 
          or connecting with fellow developers and tech enthusiasts. Feel free to reach out!
        </p>
      </div>

      <div class="contact-methods">
        <div class="contact-method">
          <h3><i class="icon">📧</i> Email Me</h3>
          
          <!-- Quick Email Links -->
          <div class="email-options">
            <h4>Quick Email Options</h4>
            <div class="email-buttons">
              <a 
                :href="`mailto:${contactInfo.email}?subject=Contact%20from%20Website&body=Hi%20Joshua,%0D%0A%0D%0AI'm%20reaching%20out%20from%20your%20website.%0D%0A%0D%0AName:%20%0D%0AEmail:%20%0D%0AMessage:%20%0D%0A%0D%0ABest%20regards`"
                class="email-btn default-email" 
                target="_blank"
              >
                <span>📧 Open in Default Email App</span>
              </a>
              <a 
                :href="`https://mail.google.com/mail/?view=cm&fs=1&to=${contactInfo.email}&su=Contact%20from%20Website&body=Hi%20Joshua,%0D%0A%0D%0AI'm%20reaching%20out%20from%20your%20website.%0D%0A%0D%0AName:%20%0D%0AEmail:%20%0D%0AMessage:%20%0D%0A%0D%0ABest%20regards`"
                class="email-btn gmail-btn" 
                target="_blank"
              >
                <span>📮 Open in Gmail</span>
              </a>
              <a 
                :href="`https://outlook.live.com/mail/0/deeplink/compose?to=${contactInfo.email}&subject=Contact%20from%20Website&body=Hi%20Joshua,%0D%0A%0D%0AI'm%20reaching%20out%20from%20your%20website.%0D%0A%0D%0AName:%20%0D%0AEmail:%20%0D%0AMessage:%20%0D%0A%0D%0ABest%20regards`"
                class="email-btn outlook-btn" 
                target="_blank"
              >
                <span>📫 Open in Outlook Web</span>
              </a>
            </div>
          </div>

          <!-- Custom Message Form -->
          <div class="custom-email-form">
            <h4>Compose Custom Email</h4>
            <form class="contact-form" @submit.prevent>
              <label for="name">Name:</label>
              <input 
                type="text" 
                id="name" 
                v-model="contactForm.name"
                required 
                autocomplete="name"
              >
              
              <label for="email">Your Email:</label>
              <input 
                type="email" 
                id="email" 
                v-model="contactForm.email"
                required 
                autocomplete="email"
              >
              
              <label for="subject">Subject:</label>
              <input 
                type="text" 
                id="subject" 
                v-model="contactForm.subject"
                required
              >
              
              <label for="message">Message:</label>
              <textarea 
                id="message" 
                v-model="contactForm.message"
                rows="5" 
                required 
                autocomplete="off"
                placeholder="Tell me about your project, question, or just say hello!"
              ></textarea>
              
              <div class="form-buttons">
                <button 
                  type="button" 
                  @click="openEmailClient('default')" 
                  class="btn-primary"
                >
                  📧 Send via Default Email
                </button>
                <button 
                  type="button" 
                  @click="openEmailClient('gmail')" 
                  class="btn-secondary"
                >
                  📮 Send via Gmail
                </button>
                <button 
                  type="button" 
                  @click="openEmailClient('outlook')" 
                  class="btn-secondary"
                >
                  📫 Send via Outlook
                </button>
              </div>
            </form>
          </div>

          <!-- Direct Contact Info -->
          <div class="direct-contact">
            <p><strong>Direct Email:</strong> 
              <a :href="`mailto:${contactInfo.email}`" class="email-link">
                {{ contactInfo.email }}
              </a>
              <button @click="copyEmail" class="copy-btn" title="Copy email to clipboard">
                📋 Copy
              </button>
            </p>
          </div>
        </div>

        <div class="contact-method">
          <h3><i class="icon">📱</i> Call or Text</h3>
          <div class="phone-contact">
            <p class="phone-number">
              <a :href="`tel:${contactInfo.phone}`">{{ contactInfo.phone }}</a>
            </p>
            <p class="phone-note">
              {{ contactInfo.availability }}<br>
              Text messages welcome anytime!
            </p>
          </div>

          <div class="social-contact">
            <h4>Connect on Social Media</h4>
            <div class="social-buttons">
              <a 
                v-for="social in socialLinks"
                :key="social.name"
                :href="social.url" 
                target="_blank" 
                :class="['social-btn', social.class]"
              >
                <span>{{ social.name }}</span>
              </a>
            </div>
          </div>
        </div>
      </div>

      <div class="contact-footer">
        <p><strong>Response Time:</strong> I typically respond to emails within {{ contactInfo.responseTime }}.</p>
        <p><strong>Best For:</strong> Project collaborations, job opportunities, technical questions, or networking.</p>
        </div>
      </section>
    </div>
  </div>
</template>

<style scoped>
/* Page-specific styles can go here if needed */
</style>