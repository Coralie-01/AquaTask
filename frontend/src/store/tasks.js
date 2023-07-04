// store/tasks.js
import { defineStore } from 'pinia'

export const useTasksStore = defineStore('tasks', {
  state: () => ({
    tasks: [],
    donetasks: []
  }),
  actions: {
    setTasks(tasks) {
      this.tasks = tasks
    },
    setDoneTasks(donetasks) {
      this.donetasks = donetasks
    },
    addTask(task) {
      this.tasks.push(task)
    },
    clearTasks() {
      this.tasks = []
    },
    updateTask(task) {
      if (task.done) {
        // Remove task from tasks
        this.tasks = this.tasks.filter((t) => t.id !== task.id)
        // Add a copy of task to donetasks
        this.donetasks.push(task)
      } else {
        // Remove task from donetasks
        this.donetasks = this.donetasks.filter((t) => t.id !== task.id)
        // Add a copy of task to tasks
        this.tasks.push(task)
      }
    }
  }
})
