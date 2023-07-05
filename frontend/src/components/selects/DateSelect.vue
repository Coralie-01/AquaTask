<template>
  <select class="select select-ghost w-32 max-w-xs">
    <option disabled selected>Due date</option>
    <option>Today</option>
    <option>Tomorrow</option>
    <option>In a week</option>    
  </select>
</template>

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