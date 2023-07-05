// store/tasks.js
import { defineStore } from 'pinia'

export const useTasksStore = defineStore('tasks', {
  state: () => ({
    tasks: [],
    donetasks: [],
    current_date: '',
    current_category: ''
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
      this.current_category = none
      this.current_date = none
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
    },
    setCategory(category) {
      this.current_category = category
    },
    setDueDate(date) {
      this.current_date = date
    }
  }
})
