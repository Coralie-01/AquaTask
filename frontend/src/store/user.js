// store/user.js
import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', {
  state: () => ({
    loggedIn: false,
  }),
  actions: {
    login() {
      // Implement your login logic here
      this.loggedIn = true
    },
    logout() {
      // Implement your logout logic here
      this.loggedIn = false
    }
  }
})
