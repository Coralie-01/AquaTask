<template>
  <div class="flex flex-col justify-start p-16">
    <p class="text-2xl">Tasks</p>
    <p class="text-xs">{{ date }}</p>
    <AddTask class="my-8"></AddTask>
    <div class="flex flex-col gap-4">
      <TaskItem v-for="task in tasks" :key="task.id" :task="task.description"></TaskItem>
    </div>
  </div>
</template>

<script setup>
import { defineProps, onMounted, watch, ref } from 'vue'
import AddTask from './tasks/AddTask.vue'
import axios from 'axios'
import { useTasksStore } from '../store/tasks'
import TaskItem from './tasks/TaskItem.vue'

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
    let userId = localStorage.getItem('userId');

    // Check if userId is not null
    if (userId) {
      const response = await axios.get(`http://localhost:5000/get/tasks?user_id=${userId}`);
      console.log(response);
      tasksStore.setTasks(response.data.tasks);
    } else {
      console.error('User ID is not set');
    }
  } catch (error) {
    console.error(error);
  }
})


watch(
  () => tasksStore.tasks,
  (newTasks) => {
    tasks.value = newTasks
  }
)

const tasks = ref(tasksStore.tasks)
</script>
