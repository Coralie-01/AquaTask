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
          <i class="fi fi-rr-calendar-check mx-1"> <DateSelect/></i>
          <i class="fi fi-rr-label mx-1"> <CategorySelect/> </i>
          <i class="fi fi-rr-bell mx-1"> <NotifSelect/> </i>
        </div>
        <button class="btn m-2 btn-info" @click="addTask">Add task</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useTasksStore } from '../../store/tasks'
import DateSelect from '../selects/DateSelect.vue';
import CategorySelect from '../selects/CategorySelect.vue';
import NotifSelect from '../selects/NotifSelect.vue';

const showForm = ref(false)
const placeholderText = ref('Add a task')
const task = ref('')
const tasksStore = useTasksStore()

function handlefocus() {
  showForm.value = true
  placeholderText.value = 'Write a task'
}

async function addTask() {
  try {
    const cat = tasksStore.current_category
    const date = tasksStore.current_date
    const response = await axios.put('http://localhost:5000/tasks', {
      description: task.value,
      user_id: localStorage.getItem('userId'),
      category: cat,
      due_date: date,
      done: false
    })
    tasksStore.addTask(response.data)
    placeholderText.value = 'Add a task'
    showForm.value = false
    task.value = ''
  } catch (error) {
    console.error(error)
  }
}
</script>
