import { createRouter, createWebHistory } from 'vue-router'
import PlanView from '../views/PlanView.vue'
import AuthView from '../views/AuthView.vue'
import SignupView from '../views/SignupView.vue'
import StudyView from '../views/StudyView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'plan',
      component: PlanView
    },
    {
      path: '/auth',
      name: 'auth',
      component: AuthView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignupView
    },
    {
      path: '/study',
      name: 'study',
      component: StudyView
    }
  ]
})

export default router
