<template>
  <select @change="updateDueDate" class="select select-ghost w-32 max-w-xs">
    <option disabled selected>Due date</option>
    <option>Today</option>
    <option>Tomorrow</option>
    <option>Next week</option>    
  </select>
</template>

<script setup>
import { useTasksStore } from '../../store/tasks'

const updateDueDate = async (event) => {
  const selectedValue = event.target.value;
  useTasksStore().setDueDate(selectedValue)
};

</script>

<style scoped>

.select {
    background-color: transparent;
    outline: none;
    border: none;
}
.select option {
  background-color: transparent;
  color: transparent;
  outline: none;
  border: none;
}

</style>
```