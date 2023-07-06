<template>
  <div class="flex flex-col justify-start p-16">
    <div class="flex flex-row justify-between">
      <div class="flex flex-col">
        <p class="text-2xl">Tasks</p>
        <p class="text-xs">{{ date }}</p>
      </div>
      <router-link to="/study"
        ><button class="btn btn-primary">Start a study session</button>
      </router-link>
    </div>
    <AddTask class="my-8"></AddTask>
    <div v-if="showDone" class="flex flex-col gap-4">
      <p class="text-xl">Done</p>
      <TaskItem v-for="task in DoneTasks" :key="task.id" :task="task"></TaskItem>
    </div>
    <div class="flex flex-col gap-4 my-8">
      <p class="text-xl">To do</p>
      <TaskItem v-for="task in Tasks" :key="task.id" :task="task"></TaskItem>
    </div>
  </div>
</template>

<script setup>
import { defineProps, onMounted, computed, ref } from 'vue'
import AddTask from './tasks/AddTask.vue'
import axios from 'axios'
import { useTasksStore } from '../store/tasks'
import TaskItem from './tasks/TaskItem.vue'

const tasksStore = useTasksStore()

let showDone = computed(() => !tasksStore.isDoneEmpty)

defineProps({
  date: {
    type: String,
    required: true
  }
})


onMounted(async () => {
  try {
    // Get user ID from localStorage
    let userId = localStorage.getItem('userId')

    // Check if userId is not null
    if (userId) {
      // Get tasks from API
      const response = await axios.get(`http://localhost:5000/get/tasks/${userId}`)
      if (response.status === 200) {
        tasksStore.setTasks(response.data.tasks)
        tasksStore.setDoneTasks(response.data.donetasks)
      }
    } else {
      console.error('User ID is not set')
    }
  } catch (error) {
    console.error("Couldn't get tasks")
  }
})

let Tasks = computed(() => tasksStore.tasks)
let DoneTasks = computed(() => tasksStore.donetasks)

</script>
