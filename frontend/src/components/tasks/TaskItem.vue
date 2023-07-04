<template>
  <div class="py-2">
    <div class="flex items-center cursor-pointer shadow-lg bg-base-200 px-2 py-2">
      <input v-model="checked" type="checkbox" checked="checked" class="checkbox m-3" />
      <div type="text" class="w-full bg-base-200">{{ task.description }}</div>
    </div>
  </div>
</template>

<script setup>
import { defineProps, watch, ref } from 'vue'
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
