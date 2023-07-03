// store/user.js
import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', {
  state: () => ({
    loggedIn: false,
    user_id: null
  }),
  actions: {
    login(userID) {
      // Implement your login logic here
      this.loggedIn = true
      this.user_id = userID
    },
    logout() {
      // Implement your logout logic here
      this.loggedIn = false
      this.userId = null
    }
  }
})
