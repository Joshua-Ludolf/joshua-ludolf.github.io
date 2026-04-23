import { createRouter, createWebHashHistory, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import Publication from '@/views/Publication.vue'
import About from '@/views/About.vue'
import Projects from '@/views/Projects.vue'
import Contact from '@/views/Contact.vue'
import Privacy from '@/views/Privacy.vue'
import Terms from '@/views/Terms.vue'

const router = createRouter({
  history: import.meta.env.DEV
    ? createWebHistory(import.meta.env.BASE_URL)
    : createWebHashHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/about',
      name: 'about',
      component: About
    },
    {
      path: '/projects',
      name: 'projects',
      component: Projects
    },
    {
      path: '/publication',
      name: 'publication',
      component: Publication
    },
    {
      path: '/contact',
      name: 'contact',
      component: Contact
    },
    {
      path: '/privacy',
      name: 'privacy',
      component: Privacy
    },
    {
      path: '/terms',
      name: 'terms',
      component: Terms
    }
  ]
})

export default router