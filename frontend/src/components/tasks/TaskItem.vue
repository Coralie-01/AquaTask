<template>
  <div class="py-2">
    <div class="flex items-center cursor-pointer shadow-lg bg-base-200 px-2 py-2">
      <input type="checkbox" checked="checked" class="checkbox m-3" />
      <div type="text" class="w-full bg-base-200">{{ task }}</div>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue'

defineProps({
  task: {
    type: String,
    required: true
  },
  dueDate: {
    type: String
  },
  category: {
    type: String
  }
})
</script>
