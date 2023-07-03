<template>
  <div class="drawer lg:drawer-open">
    <input id="my-drawer-2" type="checkbox" class="drawer-toggle" />
    <div class="drawer-content flex flex-col">
      <!-- Page content here -->
      <!--label for="my-drawer-2" class="btn btn-primary drawer-button lg:hidden">Open drawer</label-->
      <PlanNer :date="formattedDate" :dayweek="dayweek"></PlanNer>
    </div> 
    <div class="drawer-side">
      <label for="my-drawer-2" class="drawer-overlay"></label> 
      <ul class="menu p-4 w-80 h-full bg-base-200 text-base-content">
        <!-- Sidebar content here -->
        <VDatePicker v-model="selectedDate" mode="date"/>
        <li><a>{{ formattedDate }} </a></li>
      </ul>
    
    </div>
  </div>
</template>

<script setup>
import { ref,computed } from 'vue'
import PlanNer from '../components/PlanNer.vue'

const selectedDate = ref(new Date());
const formattedDate = computed(() => {
  const options = {weekday: 'long' , month: 'long', day: 'numeric', year: 'numeric'}
  return selectedDate.value.toLocaleDateString(undefined, options);
});
</script>

