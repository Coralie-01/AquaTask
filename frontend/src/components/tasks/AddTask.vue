<template>
  <div class="py-2">
    <div class="flex items-center cursor-pointer shadow-lg bg-base-200 px-2 py-2">
      <i class="fi fi-rr-plus px-3"></i>
      <input
        type="text"
        v-model="task"
        :placeholder="placeholderText"
        class="input w-full bg-base-200 focus:outline-none"
        @focus="handlefocus"
      />
    </div>
    <div v-if="showForm">
      <div class="flex justify-between items-center px-2 shadow-inner bg-base-300 rounded-b-sm">
        <div>
          <i class="fi fi-rr-calendar-check mx-2"> Due date </i>
          <i class="fi fi-rr-label mx-2"> Category </i>
          <i class="fi fi-rr-bell mx-2"> Notifications </i>
        </div>
        <button class="btn m-2 btn-secondary" @click="addTask">Add task</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useUserStore } from '@/store/user'

const showForm = ref(false)
const placeholderText = ref('Add a task')
const task = ref('')

function handlefocus() {
  showForm.value = true
  placeholderText.value = 'Write a task'
}

async function addTask() {
  console.log('add task')
  try {
    console.log(task.value)
    const response = await axios.post('http://localhost:5000/tasks', {
      description: task.value,
      user_id: useUserStore().user_id
    })
    console.log(response)
  } catch (error) {
    console.error(error)
  }
}
</script>
