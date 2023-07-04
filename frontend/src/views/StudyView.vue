<template>
  <div class="drawer lg:drawer-open">
    <input id="my-drawer-2" type="checkbox" class="drawer-toggle" />
    <div class="drawer-content flex flex-col">
      <!-- Page content here -->
      <CountDown class="m-32" />
    </div>
    <div class="drawer-side">
      <label for="my-drawer-2" class="drawer-overlay"></label>
      <ul class="menu items-center w-80 h-full bg-base-200 text-base-content">
        <!-- Sidebar content here -->
        <VDatePicker v-model="date" mode="date" class="my-6 px-2" />
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import CountDown from '../components/CountDown.vue'

const date = ref(new Date())
</script>
```
