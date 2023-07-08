<template>
  <div class="py-2">
    <div class="flex items-center cursor-pointer bg-base-200 shadow-lg px-2 py-2" :class="category">
      <input v-model="checked" type="checkbox" checked="checked" class="checkbox m-3" />
      <div type="text" class="w-full">{{ task.description }}</div>
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
