import { createRouter, createWebHistory } from 'vue-router'
import PlanView from '../views/PlanView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'plan',
      component: PlanView
    },
  ]
})

export default router
