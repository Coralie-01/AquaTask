<template>
    <div class="py-2">
      <div class="flex items-center cursor-pointer shadow-lg bg-base-200 px-2 py-2">
          <i class="fi fi-rr-plus px-3"></i>
          <input type="text" :placeholder="placeholderText" class="input w-full bg-base-200 focus:outline-none" @focus="handlefocus" @blur="handleblur">
        </div>
        <div v-if="showForm">
          <div class="flex justify-between items-center px-2 shadow-inner bg-base-300 rounded-b-sm">
            <div>
              <i class="fi fi-rr-calendar-check mx-2"> Due date </i>
              <i class="fi fi-rr-label mx-2"> Category </i>
              <i class="fi fi-rr-bell mx-2"> Notifications </i>
            </div>
            <button class="btn m-2 btn-secondary">Add task</button>
          </div>
        </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  const showForm = ref(false)
  const placeholderText = ref('Add a task')

  function handlefocus() {
    showForm.value = true
    placeholderText.value = 'Write a task'
  }
  function handleblur() {
    showForm.value = false
    placeholderText.value = 'Add a task'
  }
  </script>
  
  