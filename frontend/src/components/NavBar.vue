<template>
  <div class="navbar bg-secondary text-neutral-content">
    <div class="flex-1">
      <img
        src="/src/assets/logo.png"
        style="width: 6.80806rem; height: 3.6875rem; flex-shrink: 0"
      />
      <router-link to="/" class="btn btn-ghost normal-case text-xl">AquaTask</router-link>
    </div>
    <div class="flex-none">
      <div class="dropdown dropdown-end">
        <label tabindex="0" class="btn btn-ghost btn-circle avatar">
          <router-link to="/auth" v-if="!userStore.loggedIn">
            <div class="w-10 rounded-full">
              <i class="fi fi-sr-enter icon"></i>
            </div>
          </router-link>
          <div v-else>
            <div class="w-10 rounded-full">
              <i class="fi fi-rr-user icon"></i>
            </div>
          </div>
        </label>
        <ul
          tabindex="0"
          v-if="userStore.loggedIn"
          class="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52 text-black"
        >
          <li>
            <a class="justify-between">
              Profile
              <span class="badge">New</span>
            </a>
          </li>
          <li><a>Settings</a></li>
          <li>
            <button @click="logout"><a>Logout</a></button>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from '../store/user'
import { useTasksStore } from '../store/tasks'
import { onMounted } from 'vue'

const userStore = useUserStore()
const tasksStore = useTasksStore()

function logout() {
  localStorage.removeItem('userId')
  tasksStore.clearTasks()
  userStore.logout()
}
// keep user logged in if page is refreshed
onMounted(() => {
  if (localStorage.getItem('userId')) {
    userStore.login()
  }
})
</script>

<style>
.icon {
  color: white;
  font-size: 2.5rem;
}
</style>
