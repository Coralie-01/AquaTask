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
      <TaskItem v-for="task in doneTasks" :key="task.id" :task="task"></TaskItem>
    </div>
    <div class="flex flex-col gap-4 my-8">
      <p class="text-xl">To do</p>
      <TaskItem v-for="task in tasks" :key="task.id" :task="task"></TaskItem>
    </div>
  </div>
</template>

<script setup>
import { defineProps, onMounted, watch, ref } from 'vue'
import AddTask from './tasks/AddTask.vue'
import axios from 'axios'
import { useTasksStore } from '../store/tasks'
import TaskItem from './tasks/TaskItem.vue'
import { computed } from 'vue'

const showDone = computed(() => doneTasks.value.length > 0)

defineProps({
  date: {
    type: String,
    required: true
  }
})

const tasksStore = useTasksStore()

onMounted(async () => {
  try {
    // Get user ID from localStorage
    let userId = localStorage.getItem('userId')

    // Check if userId is not null
    if (userId) {
      const response = await axios.get(`http://localhost:5000/get/todo?user_id=${userId}`)
      tasksStore.setTasks(response.data.tasks)
      const doneResponse = await axios.get(`http://localhost:5000/get/donetasks?user_id=${userId}`)
      tasksStore.setDoneTasks(doneResponse.data.tasks)
    } else {
      console.error('User ID is not set')
    }
  } catch (error) {
    console.error(error)
  }
})

watch(
  () => tasksStore.tasks,
  (newTasks) => {
    tasks.value = newTasks
  }
)

watch(
  () => tasksStore.donetasks,
  (newDoneTasks) => {
    doneTasks.value = newDoneTasks
  }
)

const tasks = ref(tasksStore.tasks)
const doneTasks = ref(tasksStore.donetasks)

</script>
