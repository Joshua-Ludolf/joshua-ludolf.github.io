<script setup>
import { ref, onUnmounted, nextTick } from 'vue'
import { Room, RoomEvent, Track, VideoQuality } from 'livekit-client'
import profileImage from '@/assets/profile.jpg'

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
  about: "Hi, I'm Joshua Ludolf, an aspiring software developer and artificial intelligence professional. I have a strong foundation in various technologies and am always eager to learn and explore new innovations. In my free time, I enjoy working on personal projects, contributing to open-source, and staying updated with the latest trends in technology.",
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
const isSpeaking = ref(false)
const isListening = ref(false)
const currentResponse = ref('')
const avatarPosition = ref({ bottom: '20px', right: '20px' })
const isDragging = ref(false)
const dragOffset = ref({ x: 0, y: 0 })
const showSubtitles = ref(true)
const volume = ref(1)
const rate = ref(1)
const pitch = ref(1)
const tokenEndpoint = import.meta.env.VITE_AVATAR_TOKEN_ENDPOINT || '/api/token'
const videoElement = ref(null)
const audioElement = ref(null)
const liveRoom = ref(null)
const isConnecting = ref(false)
const isLive = ref(false)
const liveError = ref('')

// Quick questions
const quickQuestions = [
  'What are Joshua\'s technical skills?',
  'What is Joshua\'s education background?',
  'What projects has Joshua worked on?',
  'How can I contact Joshua?',
  'What are Joshua\'s interests?',
  'Tell me about Joshua\'s AI experience'
]

onUnmounted(() => {
  stopSpeaking()
  disconnectLiveAvatar()
})

// Toggle avatar window
const toggleAvatar = () => {
  isOpen.value = !isOpen.value
  if (isOpen.value) {
    connectLiveAvatar()
  } else {
    stopSpeaking()
    disconnectLiveAvatar()
  }
}

const connectLiveAvatar = async () => {
  if (liveRoom.value || isConnecting.value) return

  isConnecting.value = true
  liveError.value = ''
  try {
    const identity = `portfolio-${crypto.randomUUID()}`
    const tokenResponse = await fetch(tokenEndpoint, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ room: `joshua-avatar-${identity}`, identity })
    })
    if (!tokenResponse.ok) throw new Error(`Token service returned ${tokenResponse.status}`)

    const { token, url } = await tokenResponse.json()
    const room = new Room({ adaptiveStream: false })
    liveRoom.value = room

    const attachAvatarTrack = (track, publication) => {
      if (track.kind === Track.Kind.Video) {
        if (!videoElement.value) return false
        track.attach(videoElement.value)
        publication.setVideoQuality(VideoQuality.HIGH)
        isLive.value = true
        isConnecting.value = false
        return true
      }

      if (track.kind === Track.Kind.Audio) {
        if (!audioElement.value) return false
        track.attach(audioElement.value)
        audioElement.value.play().catch(() => {})
        return true
      }

      return false
    }

    room.on(RoomEvent.TrackSubscribed, attachAvatarTrack)
    room.on(RoomEvent.Disconnected, () => {
      isLive.value = false
      liveRoom.value = null
    })
    room.on(RoomEvent.ParticipantConnected, () => {
      liveError.value = ''
    })

    await room.connect(url, token)
    await room.localParticipant.setMicrophoneEnabled(true)

    // A remote track can be subscribed before Vue finishes assigning the
    // video ref. Attach any already-subscribed Synthesia track as well.
    await nextTick()
    for (const participant of room.remoteParticipants.values()) {
      for (const publication of participant.trackPublications.values()) {
        if (publication.track) {
          attachAvatarTrack(publication.track, publication)
        }
      }
    }
  } catch (error) {
    console.error('Synthesia avatar connection error:', error)
    liveError.value = 'Live avatar unavailable'
    isConnecting.value = false
    disconnectLiveAvatar()
  }
}

const disconnectLiveAvatar = () => {
  liveRoom.value?.disconnect()
  liveRoom.value = null
  isLive.value = false
  isConnecting.value = false
  if (videoElement.value) {
    videoElement.value.srcObject = null
  }
  if (audioElement.value) {
    audioElement.value.srcObject = null
  }
}

const stopSpeaking = () => {
  isSpeaking.value = false
  currentResponse.value = ''
}

// Handle quick question
const askQuickQuestion = async (question) => {
  await speakQuestion(question)
}

// Speak a question and response
const speakQuestion = async (question) => {
  if (!isOpen.value) {
    isOpen.value = true
    await nextTick()
  }

  if (!liveRoom.value) {
    await connectLiveAvatar()
  }

  if (!liveRoom.value) {
    currentResponse.value = 'The live avatar service is unavailable right now.'
    return
  }

  currentResponse.value = 'Thinking…'
  try {
    await liveRoom.value.localParticipant.publishData(
      new TextEncoder().encode(JSON.stringify({ type: 'user_question', question })),
      { reliable: true, topic: 'avatar.question' }
    )
  } catch (error) {
    console.error('Avatar question error:', error)
    currentResponse.value = 'Unable to send that question to the live avatar.'
  }
}

// Handle custom question from input
const handleCustomQuestion = async () => {
  const input = document.getElementById('custom-question')
  if (!input || !input.value.trim()) return
  
  const question = input.value.trim()
  input.value = ''
  await speakQuestion(question)
}

// Video event handlers
const onVideoEnded = () => {
  // Static image, no video events needed
}

const onVideoPlay = () => {
  // Static image, no video events needed
}

const onVideoPause = () => {
  // Static image, no video events needed
}

// Drag functionality
const startDrag = (e) => {
  if (e.target.tagName === 'BUTTON' || e.target.tagName === 'INPUT' || e.target.closest('.avatar-controls')) return
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
  const maxX = window.innerWidth - 320
  const maxY = window.innerHeight - 480
  avatarPosition.value = {
    right: `${Math.max(0, Math.min(maxX, window.innerWidth - x - 320))}px`,
    bottom: `${Math.max(0, Math.min(maxY, window.innerHeight - y - 480))}px`
  }
}

const stopDrag = () => {
  isDragging.value = false
  document.removeEventListener('mousemove', onDrag)
  document.removeEventListener('mouseup', stopDrag)
}

// Touch support
const startTouchDrag = (e) => {
  if (e.target.tagName === 'BUTTON' || e.target.tagName === 'INPUT' || e.target.closest('.avatar-controls')) return
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
  const maxX = window.innerWidth - 320
  const maxY = window.innerHeight - 480
  avatarPosition.value = {
    right: `${Math.max(0, Math.min(maxX, window.innerWidth - x - 320))}px`,
    bottom: `${Math.max(0, Math.min(maxY, window.innerHeight - y - 480))}px`
  }
}

const stopTouchDrag = () => {
  isDragging.value = false
  document.removeEventListener('touchmove', onTouchDrag)
  document.removeEventListener('touchend', stopTouchDrag)
}

// Volume control
const setVolume = (val) => {
  volume.value = val
}

// Rate control
const setRate = (val) => {
  rate.value = val
}
</script>

<template>
  <!-- Floating Avatar Button -->
  <div 
    v-if="!isOpen"
    class="avatar-float-btn"
    :style="avatarPosition"
    @click="toggleAvatar"
    @mousedown="startDrag"
    @touchstart="startTouchDrag"
    role="button"
    tabindex="0"
    @keydown.enter="toggleAvatar"
    @keydown.space.prevent="toggleAvatar"
    aria-label="Open AI Avatar Assistant"
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
    <div class="avatar-tooltip">Click to talk with Joshua's AI Avatar</div>
  </div>

  <!-- Avatar Window - Synthesia Style -->
  <transition name="avatar-slide">
    <div v-if="isOpen" class="avatar-window" :style="avatarPosition">
      <!-- Video Area -->
      <div class="avatar-video-container" @mousedown="startDrag" @touchstart="startTouchDrag">
        <div class="avatar-video-wrapper">
          <img
            v-show="!isLive"
            :src="profileImage"
            alt="Joshua Ludolf"
            class="avatar-static-image"
          >
          <video
            ref="videoElement"
            v-show="isLive"
            class="avatar-live-video"
            autoplay
            playsinline
          ></video>
          <audio ref="audioElement" autoplay></audio>
          <div v-if="isConnecting" class="avatar-connection-status">Connecting to live avatar…</div>
          <div v-else-if="liveError" class="avatar-connection-status error">{{ liveError }}</div>
        </div>
        
        <!-- Speaking indicator overlay -->
        <div v-if="isSpeaking" class="speaking-indicator">
          <div class="wave"></div>
          <div class="wave"></div>
          <div class="wave"></div>
          <span>Speaking...</span>
        </div>
        
        <!-- Subtitles -->
        <div v-if="showSubtitles && currentResponse" class="subtitles">
          {{ currentResponse }}
        </div>
      </div>

      <!-- Controls Panel -->
      <div class="avatar-controls">
        <!-- Quick Questions -->
        <div class="quick-questions-section">
          <h4>Ask me about Joshua:</h4>
          <div class="quick-chips">
            <button
              v-for="q in quickQuestions"
              :key="q"
              @click="askQuickQuestion(q)"
              class="quick-chip"
              :disabled="isSpeaking"
            >
              {{ q }}
            </button>
          </div>
        </div>

        <!-- Custom Question Input -->
        <div class="custom-question-section">
          <div class="input-group">
            <input
              id="custom-question"
              type="text"
              @keyup.enter="handleCustomQuestion"
              placeholder="Or type your own question..."
              class="custom-input"
              :disabled="isSpeaking"
              autocomplete="off"
            >
            <button
              @click="handleCustomQuestion"
              class="ask-btn"
              :disabled="isSpeaking"
              aria-label="Ask question"
            >
              <svg v-if="!isSpeaking" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <line x1="22" y1="2" x2="11" y2="13"></line>
                <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
              </svg>
              <svg v-else width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="6" y="4" width="4" height="16"></rect>
                <rect x="14" y="4" width="4" height="16"></rect>
              </svg>
            </button>
          </div>
        </div>

        <!-- Voice Settings -->
        <div class="voice-settings">
          <label>
            <input type="checkbox" v-model="showSubtitles"> Subtitles
          </label>
          <div class="slider-group">
            <span>Volume</span>
            <input type="range" v-model="volume" min="0" max="1" step="0.1" @input="setVolume(volume)">
          </div>
          <div class="slider-group">
            <span>Speed</span>
            <input type="range" v-model="rate" min="0.5" max="2" step="0.1" @input="setRate(rate)">
          </div>
        </div>

        <!-- Header Actions -->
        <div class="window-actions">
          <button @click="stopSpeaking" class="icon-btn" :disabled="!isSpeaking" title="Stop speaking" aria-label="Stop speaking">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <rect x="6" y="4" width="4" height="16"></rect>
              <rect x="14" y="4" width="4" height="16"></rect>
            </svg>
          </button>
          <button @click="toggleAvatar" class="icon-btn close-btn" title="Close" aria-label="Close avatar">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <line x1="18" y1="6" x2="6" y2="18"></line>
              <line x1="6" y1="6" x2="18" y2="18"></line>
            </svg>
          </button>
        </div>
      </div>
    </div>
  </transition>
</template>

<style scoped>
/* Floating Button */
.avatar-float-btn {
  position: fixed;
  width: 70px;
  height: 70px;
  border-radius: 50%;
  cursor: pointer;
  z-index: 9998;
  transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.3s;
  user-select: none;
  overflow: hidden;
}

.avatar-float-btn:hover {
  transform: scale(1.1);
  box-shadow: 0 12px 40px rgba(99, 102, 241, 0.5);
}

.avatar-float-btn:focus-visible {
  outline: 3px solid #6366f1;
  outline-offset: 3px;
}

.avatar-ring {
  position: absolute;
  inset: -6px;
  border: 2px solid #6366f1;
  border-radius: 50%;
  opacity: 0.5;
  animation: pulse-ring 2.5s ease-out infinite;
}

.avatar-ring.pulse {
  animation-delay: 0.4s;
}

@keyframes pulse-ring {
  0% { transform: scale(1); opacity: 0.5; }
  100% { transform: scale(1.6); opacity: 0; }
}

.avatar-video-btn {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid white;
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.25);
}

.avatar-badge {
  position: absolute;
  bottom: -2px;
  right: -2px;
  background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
  color: white;
  font-size: 11px;
  font-weight: 700;
  padding: 3px 8px;
  border-radius: 12px;
  border: 2px solid white;
  z-index: 2;
}

.avatar-tooltip {
  position: absolute;
  right: 80px;
  top: 50%;
  transform: translateY(-50%);
  background: #0f172a;
  color: white;
  padding: 10px 14px;
  border-radius: 10px;
  font-size: 13px;
  white-space: nowrap;
  opacity: 0;
  visibility: hidden;
  transition: all 0.2s;
  pointer-events: none;
  box-shadow: 0 8px 24px rgba(0,0,0,0.2);
}

.avatar-float-btn:hover .avatar-tooltip {
  opacity: 1;
  visibility: visible;
  right: 85px;
}

/* Avatar Window */
.avatar-window {
  position: fixed;
  width: 320px;
  height: 480px;
  background: #0f172a;
  border-radius: 20px;
  box-shadow: 0 25px 80px rgba(0, 0, 0, 0.3), 0 10px 32px rgba(0, 0, 0, 0.2);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  z-index: 9999;
  border: 1px solid rgba(99, 102, 241, 0.2);
}

.avatar-slide-enter-active,
.avatar-slide-leave-active {
  transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.avatar-slide-enter-from,
.avatar-slide-leave-to {
  opacity: 0;
  transform: scale(0.85) translateY(30px);
}

/* Video Container */
.avatar-video-container {
  position: relative;
  flex: 1;
  background: #000;
  border-radius: 20px 20px 0 0;
  overflow: hidden;
}

.avatar-video-wrapper {
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
  background: #172033;
}

.avatar-static-image {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: 58% 20%;
  filter: saturate(0.92) contrast(1.04);
}

.avatar-live-video {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
  background: #172033;
}

.avatar-connection-status {
  position: absolute;
  left: 50%;
  bottom: 1rem;
  transform: translateX(-50%);
  padding: 0.5rem 0.75rem;
  color: #fff;
  background: rgba(15, 23, 42, 0.78);
  border: 1px solid rgba(124, 108, 255, 0.45);
  border-radius: 999px;
  font-size: 0.75rem;
  white-space: nowrap;
}

.avatar-connection-status.error {
  border-color: rgba(248, 113, 113, 0.55);
}

.avatar-video {
  width: 100%;
  height: 100%;
  object-fit: cover;
  background: #000;
}

/* Speaking Indicator */
.speaking-indicator {
  position: absolute;
  bottom: 80px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  align-items: center;
  gap: 8px;
  background: rgba(99, 102, 241, 0.9);
  color: white;
  padding: 8px 16px;
  border-radius: 24px;
  font-size: 13px;
  font-weight: 500;
  z-index: 10;
  animation: fadeIn 0.2s;
}

.wave {
  width: 4px;
  height: 16px;
  background: white;
  border-radius: 2px;
  animation: wave 1s ease-in-out infinite;
}

.wave:nth-child(2) { animation-delay: 0.1s; }
.wave:nth-child(3) { animation-delay: 0.2s; }

@keyframes wave {
  0%, 100% { height: 8px; }
  50% { height: 16px; }
}

/* Subtitles */
.subtitles {
  position: absolute;
  bottom: 10px;
  left: 20px;
  right: 20px;
  background: rgba(0, 0, 0, 0.75);
  color: white;
  padding: 12px 16px;
  border-radius: 12px;
  font-size: 14px;
  line-height: 1.5;
  text-align: center;
  max-height: 40%;
  overflow-y: auto;
  z-index: 10;
  animation: slideUp 0.3s;
}

@keyframes slideUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Controls Panel */
.avatar-controls {
  padding: 20px;
  background: #111827;
  border-top: 1px solid rgba(99, 102, 241, 0.15);
  display: flex;
  flex-direction: column;
  gap: 16px;
  max-height: 50%;
  overflow-y: auto;
}

.quick-questions-section h4 {
  margin: 0 0 12px;
  font-size: 13px;
  font-weight: 600;
  color: #94a3b8;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.quick-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.quick-chip {
  background: rgba(99, 102, 241, 0.15);
  border: 1px solid rgba(99, 102, 241, 0.3);
  border-radius: 20px;
  padding: 8px 14px;
  font-size: 12px;
  color: #cbd5e1;
  cursor: pointer;
  transition: all 0.2s;
  white-space: nowrap;
  flex: 1;
  min-width: 120px;
  text-align: center;
}

.quick-chip:hover:not(:disabled) {
  background: rgba(99, 102, 241, 0.3);
  border-color: #6366f1;
  color: white;
  transform: translateY(-1px);
}

.quick-chip:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Custom Question */
.custom-question-section {
  border-top: 1px solid rgba(255,255,255,0.08);
  padding-top: 16px;
}

.input-group {
  display: flex;
  gap: 10px;
}

.custom-input {
  flex: 1;
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 12px;
  padding: 12px 16px;
  font-size: 13px;
  color: #f1f5f9;
  outline: none;
  transition: all 0.2s;
}

.custom-input:focus {
  border-color: #6366f1;
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.2);
  background: rgba(255,255,255,0.08);
}

.custom-input::placeholder {
  color: #64748b;
}

.custom-input:disabled {
  opacity: 0.5;
}

.ask-btn {
  width: 44px;
  height: 44px;
  border-radius: 12px;
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

.ask-btn:hover:not(:disabled) {
  transform: scale(1.05);
  box-shadow: 0 4px 16px rgba(99, 102, 241, 0.5);
}

.ask-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Voice Settings */
.voice-settings {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 16px;
  padding-top: 8px;
  border-top: 1px solid rgba(255,255,255,0.05);
  font-size: 12px;
  color: #94a3b8;
}

.voice-settings label {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
}

.voice-settings input[type="checkbox"] {
  width: 16px;
  height: 16px;
  accent-color: #6366f1;
}

.slider-group {
  display: flex;
  align-items: center;
  gap: 10px;
  flex: 1;
  min-width: 140px;
}

.slider-group input[type="range"] {
  flex: 1;
  accent-color: #6366f1;
}

/* Window Actions */
.window-actions {
  display: flex;
  justify-content: flex-end;
  gap: 8px;
  padding-top: 8px;
}

.icon-btn {
  width: 36px;
  height: 36px;
  border-radius: 10px;
  border: none;
  background: rgba(255,255,255,0.08);
  color: #94a3b8;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
}

.icon-btn:hover:not(:disabled) {
  background: rgba(255,255,255,0.15);
  color: white;
  transform: scale(1.05);
}

.icon-btn:disabled {
  opacity: 0.4;
  cursor: not-allowed;
}

.close-btn:hover {
  background: rgba(239, 68, 68, 0.2) !important;
  color: #ef4444 !important;
}

/* Mobile Responsive */
@media (max-width: 480px) {
  .avatar-window {
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
    padding: 6px 10px;
    min-width: 100px;
  }
  
  .avatar-controls {
    padding: 16px;
  }
}

/* Reduced motion */
@media (prefers-reduced-motion: reduce) {
  .avatar-ring,
  .wave {
    animation: none;
  }
  
  .avatar-slide-enter-active,
  .avatar-slide-leave-active {
    transition: opacity 0.2s;
  }
}
</style>