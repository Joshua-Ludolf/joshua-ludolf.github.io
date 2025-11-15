// Unified styles: merged main.css + vue-layout.css + original styles.css
import './assets/styles.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(router)

app.mount('#app')
