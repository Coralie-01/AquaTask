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
        <button class="btn btn-accent btn-wide m-4" @click="showTasks">Display Tasks</button>
        <div v-if="tasksVisible">
          <TaskItem v-for="task in Tasks" :key="task.id" :task="task" />
        </div>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import CountDown from '../components/CountDown.vue'
import TaskItem from '../components/tasks/TaskItem.vue'
import { useTasksStore } from '../store/tasks'

const date = ref(new Date())
const tasksStore = useTasksStore()
const Tasks = ref(tasksStore.tasks)
const tasksVisible = ref(false)
const showTasks = () => {
  tasksVisible.value = !tasksVisible.value
}
</script>
```
