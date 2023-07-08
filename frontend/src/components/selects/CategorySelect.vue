<template>
  <select @change="updateCategory" class="select select-ghost w-32 max-w-xs">
    <option disabled selected>Category</option>
    <option>Yellow</option>
    <option>Blue</option>
    <option>Red</option>
    <option>Green</option>
  </select>
</template>

<script setup>
import { useTasksStore } from '../../store/tasks'

const updateCategory = async (event) => {
  const selectedValue = event.target.value
  useTasksStore().setCategory(selectedValue)
}
</script>

<style scoped>
.select {
  background-color: transparent;
  outline: none;
  border: none;
}
.select option {
  background-color: transparent;
  color: #000;
}
</style>
```
