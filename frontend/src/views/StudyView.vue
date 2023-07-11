<template>
  <div class="drawer lg:drawer-open">
    <input id="my-drawer-2" type="checkbox" class="drawer-toggle" />
    <div class="drawer-content flex flex-col items-center">
      <!-- Page content here -->
      <span class="text-4xl mt-24">Fill your aquarium today !</span>
      <CountDown class="m-16" />
    </div>
    <div class="drawer-side screen">
      <label for="my-drawer-2" class="drawer-overlay"></label>
      <ul class="menu items-center w-80 screen bg-base-200 text-base-content">
        <!-- Sidebar content here -->
        <VDatePicker v-model="date" mode="date" class="my-6 px-2" />
        <button class="btn btn-accent btn-wide m-4" @click="showTasks">Display Tasks</button>
        <div v-if="tasksVisible">
          <TaskItem v-for="task in Tasks" :key="task.id" :task="task" />
        </div>
        <SpotifyPlayer />
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import CountDown from '../components/CountDown.vue'
import TaskItem from '../components/tasks/TaskItem.vue'
import { useTasksStore } from '../store/tasks'
import SpotifyPlayer from '../components/SpotifyPlayer.vue'

const date = ref(new Date())
const tasksStore = useTasksStore()
const Tasks = ref(tasksStore.tasks)
const tasksVisible = ref(false)
const showTasks = () => {
  tasksVisible.value = !tasksVisible.value
}
</script>
```

<style scoped>
.screen {
  height: calc(100vh - 4.68rem);
}
</style>
```
