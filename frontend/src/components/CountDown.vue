<template>
  <div class="flex flex-col items-center gap-32">
    <slider
      v-if="!sessionStarted"
      v-model="totalMinutes"
      orientation="circular"
      :min="0"
      :max="120"
      :step="5"
      color="hsl(var(--s))"
      trackColor="hsl(var(--p))"
      width="20rem"
      alwaysShowHandle="true"
      handleScale="4"
      class="bg-base-300 rounded-full"
    />
    <slider
      v-else
      v-model="remainingTime"
      orientation="circular"
      :min="0"
      :max="7200"
      color="hsl(var(--s))"
      trackColor="hsl(var(--p))"
      width="20rem"
      alwaysShowHandle="true"
      handleScale="4"
      class="bg-base-300 rounded-full"
    />
    <div v-if="!sessionStarted">
      <span class="text-7xl">{{ totalMinutes }}:00</span>
    </div>
    <div v-if="sessionStarted">
      <span class="countdown font-mono text-6xl">
        <span :style="'--value:' + Math.floor(remainingTime / 60)"></span>:
        <span :style="'--value:' + (remainingTime % 60)"></span>
      </span>
    </div>
    <button v-if="!sessionStarted" class="btn btn-secondary" @click="startSession">
      Start Session
    </button>
    <button v-else class="btn btn-accent" @click="abandonSession">Abandon</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import slider from 'vue3-slider'

let totalMinutes = ref(0)
let remainingTime = ref(0)
let intervalId = null
let sessionStarted = ref(false)

const startSession = () => {
  console.log('startSession')
  remainingTime.value = totalMinutes.value * 60 // convert minutes to seconds
  sessionStarted.value = true
  intervalId = setInterval(() => {
    if (remainingTime.value > 0) {
      remainingTime.value--
    } else {
      clearInterval(intervalId)
      intervalId = null
    }
  }, 1000)
}

const abandonSession = () => {
  if (intervalId) {
    clearInterval(intervalId)
    intervalId = null
  }
  remainingTime.value = totalMinutes.value * 60
  sessionStarted.value = false
}
</script>
