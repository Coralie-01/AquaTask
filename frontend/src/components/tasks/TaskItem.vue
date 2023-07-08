<template>
  <div class="py-2">
    <div
      class="flex cursor-pointer bg-base-200 shadow-lg px-2 py-2 justify-between"
      :class="category"
    >
      <div class="flex flex-row items-center">
        <input v-model="checked" type="checkbox" checked="checked" class="checkbox m-3" />
        <div type="text" class="">{{ task.description }}</div>
      </div>
      <div type="text" class="text-sm flex items-end">
        <i class="fi fi-rr-calendar-check mx-1"></i>{{ date }}
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps, watch, ref, computed, toRef, reactive } from 'vue'
import axios from 'axios'
import { useTasksStore } from '../../store/tasks'

const props = defineProps({
  task: {
    type: Object,
    required: true
  }
})
const checked = ref(props.task.done)
const id = ref(props.task.id)
const category = toRef(() => props.task.category)

const date = computed(() => {
  let today = new Date()
  let tomorrow = new Date(today)
  tomorrow.setDate(tomorrow.getDate() + 1)
  let dueDate = new Date(props.task.due_date)
  // If the due date is today or tomorrow, display "Today" or "Tomorrow"
  if (+dueDate.setHours(0, 0, 0, 0) === +today.setHours(0, 0, 0, 0)) {
    return 'Today'
  } else if (+dueDate.setHours(0, 0, 0, 0) === +tomorrow.setHours(0, 0, 0, 0)) {
    return 'Tomorrow'
  } else {
    let formattedDate = dueDate.toLocaleDateString(undefined, {
      weekday: 'short',
      month: 'long',
      day: 'numeric'
    })
    return formattedDate
  }
})

async function updateTask() {
  try {
    const response = await axios.put('http://localhost:5000/updatetask', {
      id: id.value,
      done: checked.value
    })
    useTasksStore().updateTask(response.data)
  } catch (error) {
    console.error(error)
  }
}

watch(
  () => checked.value,
  (newChecked) => {
    updateTask()
    console.log(newChecked)
  }
)
</script>

<style scoped>
.Red {
  background-color: #fca5a5;
}
.Yellow {
  background-color: #faf089;
}
.Green {
  background-color: #9ae6b4;
}
.Blue {
  background-color: #90cdf4;
}
</style>
