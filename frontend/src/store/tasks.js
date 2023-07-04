// store/tasks.js
import { defineStore } from 'pinia'

export const useTasksStore = defineStore('tasks', {
  state: () => ({
    tasks: []
  }),
  actions: {
    setTasks(tasks) {
      this.tasks = tasks
    },
    addTask(task) {
      this.tasks.push(task)
    },
    clearTasks() {
      this.tasks = []
    }
  }
})
