<template>
  <div class="flex items-center">
    <div class="dropdown dropdown-bottom dropdown-end">
      <label tabindex="0" class="px-4 text-xl text-slate-600 align-middle">. . .</label>
      <ul tabindex="0" class="dropdown-content z-[1] menu p-2 shadow bg-base-100 rounded-box w-52">
        <li>
          <a><i class="fi fi-rr-edit-alt mx-1"></i> Edit task name</a>
        </li>
        <li>
          <a><i class="fi fi-rr-calendar-check mx-1"></i> Edit due date</a>
        </li>
        <li>
          <details>
            <summary><i class="fi fi-rr-list-check mx-1"></i> Edit category</summary>
            <ul class="menu-dropdown">
              <li @click="editCategory('Yellow')"><a>Yellow</a></li>
              <li @click="editCategory('Blue')"><a>Blue</a></li>
              <li @click="editCategory('Red')"><a>Red</a></li>
              <li @click="editCategory('Green')"><a>Green</a></li>
              <li @click="editCategory('None')"><a>None</a></li>
            </ul>
          </details>
        </li>
        <div class="divider my-2"></div>
        <li class="text-accent" @click="deleteTask">
          <a><i class="fi fi-rr-trash mx-1"></i> Delete task</a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue'
import axios from 'axios'
import { useTasksStore } from '../../store/tasks'

const props = defineProps({
  task: {
    type: Object,
    required: true
  }
})

const done = props.task.done
const id = props.task.id
const category = props.task.category

async function deleteTask() {
  try {
    await axios.delete(`http://localhost:5000/deletetask/${id}`)
    useTasksStore().deleteTask(id, done)
  } catch (error) {
    console.error(error)
  }
}

async function editCategory(color) {
  try {
    await axios.put(`http://localhost:5000/taskcategory/${id}`, {
      category: color
    })
    useTasksStore().updateCategory(props.task, id, color, done)
  } catch (error) {
    console.error(error)
  }
}
</script>
