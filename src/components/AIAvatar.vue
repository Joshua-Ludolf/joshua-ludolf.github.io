<script setup>
import { ref, onMounted, nextTick } from 'vue'

// Knowledge base about Joshua Ludolf
const knowledgeBase = {
  name: 'Joshua Ludolf',
  title: 'Computer Science Student & Aspiring AI Professional',
  education: {
    previous: {
      degree: 'Bachelor of Science in Computer Science',
      university: 'Texas A&M University of San Antonio',
      graduationDate: 'May 2025'
    },
    latest: {
      degree: "Master's degree in Artificial Intelligence",
      university: 'University of Texas at Austin',
      graduationDate: 'May 2026'
    }
  },
  skills: {
    programming: 'CSS, HTML, Java, Markdown, Maven, Python, SQL',
    frameworks: 'Django, FastAPI, Flask, JavaFX, PyTorch, TensorFlow',
    operatingSystems: 'Linux, Windows',
    tools: 'Docker, Git, GitHub, GitHub Copilot, IntelliJ IDEA, Jupyter Notebook, VS Code'
  },
  experience: [
    'Developing backend services using Flask',
    'Creating databases from SQL to Firebase',
    'Processing data for Machine Learning applications',
    'Implementing full-stack web applications'
  ],
  about: "Hi, I'm Joshua Ludolf, an aspiring software developer/artificial intelligence professional. I have a strong foundation in various technologies and am always eager to learn and explore new innovations. In my free time, I enjoy working on personal projects, contributing to open-source, and staying updated with the latest trends in technology.",
  contact: {
    email: 'joshualudolf@gmail.com',
    phone: '+1 (830) 331-0424',
    availability: 'Available for calls weekdays 9 AM - 6 PM CST',
    responseTime: '24-48 hours'
  },
  socialLinks: [
    { name: 'LinkedIn', url: 'https://www.linkedin.com/in/joshua-ludolf' },
    { name: 'GitHub', url: 'https://github.com/joshua-ludolf' },
    { name: 'Devpost', url: 'https://devpost.com/joshua-ludolf' }
  ],
  interests: [
    'Artificial Intelligence & Machine Learning',
    'Full-Stack Web Development',
    'Data Science & Analytics',
    'Open Source Contribution',
    'Software Architecture',
    'Cloud Computing'
  ]
}

// Avatar state
const isOpen = ref(false)
const messages = ref([])
const inputValue = ref('')
const isTyping = ref(false)
const avatarPosition = ref({ bottom: '20px', right: '20px' })
const isDragging = ref(false)
const dragOffset = ref({ x: 0, y: 0 })

// Quick questions for users
const quickQuestions = [
  'What are Joshua\'s technical skills?',
  'What is Joshua\'s education background?',
  'What projects has Joshua worked on?',
  'How can I contact Joshua?',
  'What are Joshua\'s interests?',
  'What is Joshua\'s experience with AI/ML?'
]

// Initialize with welcome message
onMounted(() => {
  messages.value.push({
    id: Date.now(),
    type: 'bot',
    content: `Hi! I'm Joshua's AI avatar. I can answer questions about his background, skills, projects, education, and more. What would you like to know?`,
    timestamp: new Date()
  })
})

// Toggle chat window
const toggleChat = () => {
  isOpen.value = !isOpen.value
  if (isOpen.value) {
    nextTick(() => {
      scrollToBottom()
    })
  }
}

// Send message
const sendMessage = async () => {
  if (!inputValue.value.trim()) return
  
  const userMessage = inputValue.value.trim()
  inputValue.value = ''
  
  messages.value.push({
    id: Date.now(),
    type: 'user',
    content: userMessage,
    timestamp: new Date()
  })
  
  isTyping.value = true
  await nextTick()
  scrollToBottom()
  
  // Simulate thinking time
  await new Promise(resolve => setTimeout(resolve, 800 + Math.random() * 1200))
  
  const botResponse = generateResponse(userMessage)
  messages.value.push({
    id: Date.now() + 1,
    type: 'bot',
    content: botResponse,
    timestamp: new Date()
  })
  
  isTyping.value = false
  await nextTick()
  scrollToBottom()
}

// Generate response based on knowledge base
const generateResponse = (question) => {
  const q = question.toLowerCase()
  
  // Education questions
  if (q.includes('education') || q.includes('degree') || q.includes('university') || q.includes('study') || q.includes('school')) {
    return `Joshua has two degrees:
    
**Bachelor of Science in Computer Science**  
Texas A&M University of San Antonio  
Graduated: May 2025

**Master's degree in Artificial Intelligence**  
University of Texas at Austin  
Graduated: May 2026`
  }
  
  // Skills questions
  if (q.includes('skill') || q.includes('technolog') || q.includes('program') || q.includes('language') || q.includes('framework') || q.includes('tool')) {
    return `Joshua's technical skills include:

**Programming Languages:** ${knowledgeBase.skills.programming}

**Frameworks & Libraries:** ${knowledgeBase.skills.frameworks}

**Operating Systems:** ${knowledgeBase.skills.operatingSystems}

**Development Tools:** ${knowledgeBase.skills.tools}`
  }
  
  // Experience questions
  if (q.includes('experience') || q.includes('work') || q.includes('project') || q.includes('built') || q.includes('develop')) {
    return `Joshua's experience includes:

${knowledgeBase.experience.map(e => `• ${e}`).join('\n')}

He's passionate about building full-stack web applications and machine learning models.`
  }
  
  // Contact questions
  if (q.includes('contact') || q.includes('email') || q.includes('phone') || q.includes('reach') || q.includes('touch') || q.includes('hire')) {
    return `You can contact Joshua through:

**Email:** ${knowledgeBase.contact.email}  
**Phone:** ${knowledgeBase.contact.phone}  
**Availability:** ${knowledgeBase.contact.availability}  
**Response Time:** ${knowledgeBase.contact.responseTime}

**Social Media:**
${knowledgeBase.socialLinks.map(s => `• ${s.name}: ${s.url}`).join('\n')}`
  }
  
  // Interests questions
  if (q.includes('interest') || q.includes('hobby') || q.includes('passion') || q.includes('like') || q.includes('enjoy')) {
    return `Joshua's interests include:

${knowledgeBase.interests.map(i => `• ${i}`).join('\n')}

He enjoys working on personal projects, contributing to open-source, and staying updated with the latest tech trends.`
  }
  
  // AI/ML specific questions
  if (q.includes('ai') || q.includes('artificial intelligence') || q.includes('machine learning') || q.includes('ml') || q.includes('deep learning') || q.includes('pytorch') || q.includes('tensorflow')) {
    return `Joshua is pursuing a Master's in Artificial Intelligence at UT Austin (graduating May 2026). His AI/ML experience includes:

• Working with **PyTorch** and **TensorFlow** for model development
• Processing data for Machine Learning applications
• Building and training neural networks
• Experience with data pipelines for ML workflows

He's particularly interested in applying AI to real-world problems and building intelligent systems.`
  }
  
  // About/General questions
  if (q.includes('who') || q.includes('about') || q.includes('bio') || q.includes('background') || q.includes('joshua') || q.includes('josh')) {
    return knowledgeBase.about
  }
  
  // LinkedIn/GitHub specific
  if (q.includes('linkedin')) {
    return `Joshua's LinkedIn: https://www.linkedin.com/in/joshua-ludolf`
  }
  
  if (q.includes('github')) {
    return `Joshua's GitHub: https://github.com/joshua-ludolf`
  }
  
  if (q.includes('devpost')) {
    return `Joshua's Devpost: https://devpost.com/joshua-ludolf`
  }
  
  // Default response
  return `I can help you with information about Joshua's:
  
• **Education** (degrees, universities)
• **Technical Skills** (languages, frameworks, tools)
• **Experience** (projects, work history)
• **Contact Info** (email, phone, social links)
• **Interests** (AI/ML, web dev, open source)

Try asking: "What are Joshua's skills?" or "How can I contact Joshua?"`
}

// Handle quick question click
const askQuickQuestion = (question) => {
  inputValue.value = question
  sendMessage()
}

// Scroll to bottom of messages
const scrollToBottom = () => {
  const container = document.querySelector('.avatar-messages')
  if (container) {
    container.scrollTop = container.scrollHeight
  }
}

// Handle enter key
const handleKeyDown = (e) => {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault()
    sendMessage()
  }
}

// Drag functionality for avatar button
const startDrag = (e) => {
  isDragging.value = true
  const rect = e.currentTarget.getBoundingClientRect()
  dragOffset.value = {
    x: e.clientX - rect.left,
    y: e.clientY - rect.top
  }
  document.addEventListener('mousemove', onDrag)
  document.addEventListener('mouseup', stopDrag)
  e.preventDefault()
}

const onDrag = (e) => {
  if (!isDragging.value) return
  
  const x = e.clientX - dragOffset.value.x
  const y = e.clientY - dragOffset.value.y
  
  // Keep within viewport
  const maxX = window.innerWidth - 60
  const maxY = window.innerHeight - 60
  
  avatarPosition.value = {
    right: `${Math.max(0, Math.min(maxX, window.innerWidth - x - 60))}px`,
    bottom: `${Math.max(0, Math.min(maxY, window.innerHeight - y - 60))}px`
  }
}

const stopDrag = () => {
  isDragging.value = false
  document.removeEventListener('mousemove', onDrag)
  document.removeEventListener('mouseup', stopDrag)
}

// Touch support for mobile
const startTouchDrag = (e) => {
  const touch = e.touches[0]
  isDragging.value = true
  const rect = e.currentTarget.getBoundingClientRect()
  dragOffset.value = {
    x: touch.clientX - rect.left,
    y: touch.clientY - rect.top
  }
  document.addEventListener('touchmove', onTouchDrag, { passive: false })
  document.addEventListener('touchend', stopTouchDrag)
}

const onTouchDrag = (e) => {
  if (!isDragging.value) return
  e.preventDefault()
  
  const touch = e.touches[0]
  const x = touch.clientX - dragOffset.value.x
  const y = touch.clientY - dragOffset.value.y
  
  const maxX = window.innerWidth - 60
  const maxY = window.innerHeight - 60
  
  avatarPosition.value = {
    right: `${Math.max(0, Math.min(maxX, window.innerWidth - x - 60))}px`,
    bottom: `${Math.max(0, Math.min(maxY, window.innerHeight - y - 60))}px`
  }
}

const stopTouchDrag = () => {
  isDragging.value = false
  document.removeEventListener('touchmove', onTouchDrag)
  document.removeEventListener('touchend', stopTouchDrag)
}

// Clear chat
const clearChat = () => {
  messages.value = [{
    id: Date.now(),
    type: 'bot',
    content: `Hi! I'm Joshua's AI avatar. I can answer questions about his background, skills, projects, education, and more. What would you like to know?`,
    timestamp: new Date()
  }]
}
</script>

<template>
  <!-- Floating Avatar Button -->
  <div 
    v-if="!isOpen"
    class="avatar-float-btn"
    :style="avatarPosition"
    @click="toggleChat"
    @mousedown="startDrag"
    @touchstart="startTouchDrag"
    role="button"
    tabindex="0"
    @keydown.enter="toggleChat"
    @keydown.space.prevent="toggleChat"
    aria-label="Open AI Assistant"
  >
    <div class="avatar-ring"></div>
    <div class="avatar-ring pulse"></div>
    <div class="avatar-ring pulse" style="animation-delay: 0.4s;"></div>
    <img 
      src="@/assets/profile.jpg" 
      alt="Joshua Ludolf AI Avatar" 
      class="avatar-image"
    >
    <div class="avatar-badge" aria-hidden="true">AI</div>
    <div class="avatar-tooltip">Ask me about Joshua</div>
  </div>

  <!-- Chat Window -->
  <transition name="chat-slide">
    <div v-if="isOpen" class="avatar-chat-window" :style="avatarPosition">
      <!-- Header -->
      <div class="chat-header">
        <div class="avatar-info">
          <img src="@/assets/profile.jpg" alt="Joshua Ludolf" class="chat-avatar-img">
          <div>
            <h3>Joshua's AI Avatar</h3>
            <span class="status-indicator">
              <span class="status-dot"></span>
              Online
            </span>
          </div>
        </div>
        <div class="chat-actions">
          <button @click="clearChat" class="icon-btn" title="Clear chat" aria-label="Clear conversation">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M3 6h18M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/>
            </svg>
          </button>
          <button @click="toggleChat" class="icon-btn" title="Close" aria-label="Close chat">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <line x1="18" y1="6" x2="6" y2="18"></line>
              <line x1="6" y1="6" x2="18" y2="18"></line>
            </svg>
          </button>
        </div>
      </div>

      <!-- Messages -->
      <div class="avatar-messages" ref="messagesContainer">
        <div 
          v-for="msg in messages" 
          :key="msg.id" 
          :class="['message', msg.type]"
        >
          <div class="message-bubble">
            <div class="message-content" v-html="formatMessage(msg.content)"></div>
            <span class="message-time">{{ formatTime(msg.timestamp) }}</span>
          </div>
        </div>
        
        <!-- Typing indicator -->
        <div v-if="isTyping" class="message bot typing-indicator">
          <div class="message-bubble">
            <div class="typing-dots">
              <span></span>
              <span></span>
              <span></span>
            </div>
          </div>
        </div>
      </div>

      <!-- Quick Questions -->
      <div class="quick-questions" v-if="messages.length <= 2">
        <span class="quick-label">Try asking:</span>
        <div class="quick-chips">
          <button 
            v-for="q in quickQuestions" 
            :key="q" 
            @click="askQuickQuestion(q)"
            class="quick-chip"
          >
            {{ q }}
          </button>
        </div>
      </div>

      <!-- Input Area -->
      <div class="chat-input-area">
        <form @submit.prevent="sendMessage" class="input-form">
          <input
            type="text"
            v-model="inputValue"
            @keydown="handleKeyDown"
            placeholder="Ask me anything about Joshua..."
            class="chat-input"
            aria-label="Ask a question"
            autocomplete="off"
          >
          <button 
            type="submit" 
            class="send-btn"
            :disabled="!inputValue.trim() || isTyping"
            aria-label="Send message"
          >
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <line x1="22" y1="2" x2="11" y2="13"></line>
              <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
            </svg>
          </button>
        </form>
        <p class="input-hint">Press Enter to send • Shift+Enter for new line</p>
      </div>
    </div>
  </transition>
</template>

<script>
// Helper to format message content with basic markdown
function formatMessage(content) {
  return content
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    .replace(/\*(.*?)\*/g, '<em>$1</em>')
    .replace(/\n/g, '<br>')
    .replace(/•/g, '•')
}
</script>

<style scoped>
/* Floating Button */
.avatar-float-btn {
  position: fixed;
  width: 60px;
  height: 60px;
  border-radius: 50%;
  cursor: pointer;
  z-index: 9998;
  transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.3s;
  user-select: none;
}

.avatar-float-btn:hover {
  transform: scale(1.1);
  box-shadow: 0 8px 32px rgba(99, 102, 241, 0.4);
}

.avatar-float-btn:focus-visible {
  outline: 3px solid #6366f1;
  outline-offset: 3px;
}

.avatar-ring {
  position: absolute;
  inset: -4px;
  border: 2px solid #6366f1;
  border-radius: 50%;
  opacity: 0.6;
  animation: pulse-ring 2s ease-out infinite;
}

.avatar-ring.pulse {
  animation-delay: 0.3s;
}

@keyframes pulse-ring {
  0% { transform: scale(1); opacity: 0.6; }
  100% { transform: scale(1.5); opacity: 0; }
}

.avatar-image {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid white;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
  position: relative;
  z-index: 1;
}

.avatar-badge {
  position: absolute;
  bottom: -4px;
  right: -4px;
  background: #6366f1;
  color: white;
  font-size: 10px;
  font-weight: 700;
  padding: 2px 6px;
  border-radius: 10px;
  border: 2px solid white;
  z-index: 2;
}

.avatar-tooltip {
  position: absolute;
  right: 70px;
  top: 50%;
  transform: translateY(-50%);
  background: #1e293b;
  color: white;
  padding: 8px 12px;
  border-radius: 8px;
  font-size: 13px;
  white-space: nowrap;
  opacity: 0;
  visibility: hidden;
  transition: all 0.2s;
  pointer-events: none;
}

.avatar-float-btn:hover .avatar-tooltip {
  opacity: 1;
  visibility: visible;
  right: 75px;
}

/* Chat Window */
.avatar-chat-window {
  position: fixed;
  width: 380px;
  max-width: calc(100vw - 40px);
  height: 520px;
  max-height: calc(100vh - 40px);
  background: white;
  border-radius: 20px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15), 0 8px 24px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  z-index: 9999;
  border: 1px solid rgba(99, 102, 241, 0.1);
}

.chat-slide-enter-active,
.chat-slide-leave-active {
  transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.chat-slide-enter-from,
.chat-slide-leave-to {
  opacity: 0;
  transform: scale(0.8) translateY(20px);
}

/* Header */
.chat-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 20px;
  background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
  color: white;
  border-radius: 20px 20px 0 0;
}

.avatar-info {
  display: flex;
  align-items: center;
  gap: 12px;
}

.chat-avatar-img {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid rgba(255,255,255,0.3);
}

.avatar-info h3 {
  margin: 0;
  font-size: 16px;
  font-weight: 600;
}

.status-indicator {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  opacity: 0.9;
}

.status-dot {
  width: 8px;
  height: 8px;
  background: #22c55e;
  border-radius: 50%;
  animation: blink 2s infinite;
}

@keyframes blink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

.chat-actions {
  display: flex;
  gap: 8px;
}

.icon-btn {
  width: 36px;
  height: 36px;
  border-radius: 10px;
  border: none;
  background: rgba(255,255,255,0.15);
  color: white;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
}

.icon-btn:hover {
  background: rgba(255,255,255,0.25);
  transform: scale(1.05);
}

/* Messages */
.avatar-messages {
  flex: 1;
  overflow-y: auto;
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  background: #f8fafc;
}

.message {
  display: flex;
  max-width: 85%;
  animation: fadeInUp 0.3s ease-out;
}

@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.message.bot {
  align-self: flex-start;
}

.message.user {
  align-self: flex-end;
  flex-direction: row-reverse;
}

.message-bubble {
  padding: 12px 16px;
  border-radius: 18px;
  position: relative;
  line-height: 1.5;
  font-size: 14px;
}

.message.bot .message-bubble {
  background: white;
  border-bottom-left-radius: 4px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e2e8f0;
}

.message.user .message-bubble {
  background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
  color: white;
  border-bottom-right-radius: 4px;
}

.message-content {
  word-wrap: break-word;
}

.message-time {
  display: block;
  font-size: 10px;
  margin-top: 4px;
  opacity: 0.6;
  text-align: right;
}

.message.bot .message-time {
  color: #64748b;
}

.message.user .message-time {
  color: rgba(255,255,255,0.7);
}

/* Typing Indicator */
.typing-indicator .message-bubble {
  padding: 16px;
}

.typing-dots {
  display: flex;
  gap: 4px;
}

.typing-dots span {
  width: 8px;
  height: 8px;
  background: #6366f1;
  border-radius: 50%;
  animation: typing 1.4s infinite ease-in-out;
}

.typing-dots span:nth-child(2) { animation-delay: 0.2s; }
.typing-dots span:nth-child(3) { animation-delay: 0.4s; }

@keyframes typing {
  0%, 60%, 100% { transform: translateY(0); }
  30% { transform: translateY(-6px); }
}

/* Quick Questions */
.quick-questions {
  padding: 0 20px 16px;
  border-bottom: 1px solid #e2e8f0;
  background: #f8fafc;
}

.quick-label {
  display: block;
  font-size: 12px;
  color: #64748b;
  margin-bottom: 10px;
  font-weight: 500;
}

.quick-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.quick-chip {
  background: white;
  border: 1px solid #e2e8f0;
  border-radius: 20px;
  padding: 8px 14px;
  font-size: 12px;
  color: #475569;
  cursor: pointer;
  transition: all 0.2s;
  white-space: nowrap;
}

.quick-chip:hover {
  border-color: #6366f1;
  color: #6366f1;
  background: #f0f4ff;
}

/* Input Area */
.chat-input-area {
  padding: 16px 20px;
  background: white;
  border-top: 1px solid #e2e8f0;
  border-radius: 0 0 20px 20px;
}

.input-form {
  display: flex;
  gap: 10px;
  align-items: center;
}

.chat-input {
  flex: 1;
  border: 2px solid #e2e8f0;
  border-radius: 24px;
  padding: 12px 18px;
  font-size: 14px;
  outline: none;
  transition: all 0.2s;
  background: #f8fafc;
}

.chat-input:focus {
  border-color: #6366f1;
  background: white;
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.15);
}

.chat-input::placeholder {
  color: #94a3b8;
}

.send-btn {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  border: none;
  background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
  color: white;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
  flex-shrink: 0;
}

.send-btn:hover:not(:disabled) {
  transform: scale(1.05);
  box-shadow: 0 4px 16px rgba(99, 102, 241, 0.4);
}

.send-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.input-hint {
  margin: 10px 0 0;
  font-size: 11px;
  color: #94a3b8;
  text-align: center;
}

/* Mobile Responsive */
@media (max-width: 480px) {
  .avatar-chat-window {
    width: calc(100vw - 20px);
    height: calc(100vh - 20px);
    max-width: none;
    max-height: none;
    border-radius: 16px;
    bottom: 10px !important;
    right: 10px !important;
  }
  
  .avatar-float-btn {
    bottom: 20px !important;
    right: 20px !important;
  }
  
  .quick-chip {
    font-size: 11px;
    padding: 6px 12px;
  }
}

/* Dark mode support */
@media (prefers-color-scheme: dark) {
  .avatar-messages {
    background: #0f172a;
  }
  
  .message.bot .message-bubble {
    background: #1e293b;
    border-color: #334155;
  }
  
  .chat-input {
    background: #1e293b;
    border-color: #334155;
    color: #f1f5f9;
  }
  
  .chat-input:focus {
    background: #1e293b;
  }
  
  .quick-chip {
    background: #1e293b;
    border-color: #334155;
    color: #cbd5e1;
  }
  
  .quick-chip:hover {
    background: #312e81;
    border-color: #6366f1;
  }
  
  .chat-input-area {
    background: #0f172a;
    border-color: #334155;
  }
}
</style>