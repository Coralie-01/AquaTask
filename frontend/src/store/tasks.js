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
      this.tasks = [...tasks]
    },
    setDoneTasks(donetasks) {
      this.donetasks = [...donetasks]
    },
    addTask(task) {
      this.tasks.push(task)
      this.current_category = ''
      this.current_date = ''
    },
    clearTasks() {
      this.tasks = []
    },
    clearDoneTasks() {
      this.donetasks = []
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
    },
    deleteTask(id, done) {
      if (done) {
        // Remove task from donetasks
        this.donetasks = this.donetasks.filter((t) => t.id !== id)
      } else {
        // Remove task from tasks
        this.tasks = this.tasks.filter((t) => t.id !== id)
      }
    },
    updateCategory(task, id, newcat, done) {
      let newTask = { ...task, category: newcat }
      if (done) {
        // Find the index of the task in the donetasks array
        let index = this.donetasks.findIndex((task) => task.id === id)
        // Update the task in the donetasks array
        this.donetasks.splice(index, 1, newTask)
      } else {
        // Find the index of the task in the tasks array
        let index = this.tasks.findIndex((task) => task.id === id)
        // Update the task in the tasks array
        this.tasks.splice(index, 1, newTask)
      }
    }
  },
  getters: {
    isDoneEmpty() {
      return this.donetasks.length === 0
    }
  }
})
