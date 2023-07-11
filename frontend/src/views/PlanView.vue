<template>
  <div class="drawer lg:drawer-open">
    <input id="my-drawer-2" type="checkbox" class="drawer-toggle" />
    <div class="drawer-content flex flex-col">
      <!-- Page content here -->
      <!--label for="my-drawer-2" class="btn btn-primary drawer-button lg:hidden">Open drawer</label-->
      <PlanNer :date="formattedDate"></PlanNer>
    </div>
    <div class="drawer-side screen bg-base-200 shadow-lg">
      <label for="my-drawer-2" class="drawer-overlay"></label>
      <ul class="menu items-center w-80 screen text-base-content justify-between">
        <!-- Sidebar content here -->
        <VDatePicker v-model="selectedDate" mode="date" class="my-6 px-2" />
        <SpotifyPlayer />
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import PlanNer from '../components/PlanNer.vue'
import SpotifyPlayer from '../components/SpotifyPlayer.vue'

const selectedDate = ref(new Date())
const formattedDate = computed(() => {
  const options = { weekday: 'long', month: 'long', day: 'numeric', year: 'numeric' }
  return selectedDate.value.toLocaleDateString(undefined, options)
})
</script>

<style scoped>
.screen {
  height: calc(100vh - 4.68rem);
}
</style>
```
