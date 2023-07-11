<template>
  <div class="flex flex-col items-center gap-32">
    <div class="relative rounded-full w-96 h-96">
      <div class="aquarium absolute bottom-0 w-full rounded-full h-full"></div>
      <div class="water absolute bottom-0 w-full rounded-full h-full"></div>
      <!--div class="absolute top-0 bg-base-300 w-full h-1/5 rounded-t-full"></div-->
      <round-slider
        v-if="!sessionStarted"
        v-model="totalMinutes"
        start-angle="132"
        end-angle="+275"
        min="0"
        max="120"
        line-cap="round"
        radius="200"
        step="5"
        width="10"
        pathColor="hsl(var(--p))"
        rangeColor="hsl(var(--s))"
        handleSize="+20"
        handleColor="hsl(var(--s))"
        showTooltip="false"
        class="absolute inset-0 left-1/2 transform -translate-x-1/2 top-1/2 transform -translate-y-1/2"
      ></round-slider>
      <round-slider
        v-if="sessionStarted"
        v-model="remainingTime"
        start-angle="132"
        end-angle="+275"
        min="0"
        max="7200"
        line-cap="round"
        radius="200"
        step="5"
        width="10"
        pathColor="hsl(var(--p))"
        rangeColor="hsl(var(--s))"
        handleSize="+20"
        handleColor="hsl(var(--s))"
        showTooltip="false"
        readOnly="true"
        class="absolute inset-0 left-1/2 transform -translate-x-1/2 top-1/2 transform -translate-y-1/2"
      ></round-slider>
      <div
        class="top-aquarium absolute top-3 bg-base-200 h-9 w-11/12 outline outline-base-300 rounded-full shadow-lg drop-shadow-2xl"
        style="left: 50%; transform: translateX(-50%)"
      ></div>
      <div class="absolute bottom-40 left-12 small-fish"></div>
      <div class="absolute bottom-52 left-24 small-fish-2"></div>
      <div class="fish" :class="{ 'fish-animation': sessionStarted }">
        <img
          src="/src/assets/fish.png"
          class="absolute bottom-20 w-3/7"
          style="left: 50%; transform: translateX(-50%)"
        />
      </div>
    </div>
    <div v-if="!sessionStarted">
      <span class="text-7xl">{{ totalMinutes }} : 00</span>
    </div>
    <div v-if="sessionStarted">
      <span class="countdown font-mono text-7xl">
        <span :style="'--value:' + Math.floor(remainingTime / 3600)"></span>:
        <span :style="'--value:' + Math.floor((remainingTime % 3600) / 60)"></span>:
        <span :style="'--value:' + (remainingTime % 60)"></span>
      </span>
    </div>
    <button v-if="!sessionStarted" class="btn btn-info" @click="startSession">Start Session</button>
    <button v-else class="btn btn-accent" @click="abandonSession">Abandon</button>
    <span v-if="sessionStarted" class="text-2xl text-center">Congrats, you have stayed focus for {{ spentMinutes }} mins and {{ spentSeconds }} seconds.</span>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import roundSlider from 'vue-three-round-slider'

let sliderValue = ref(15) // to set up the countdown init time
let remainingTime = ref(0) // to keep track of the remaining time during session
let intervalId = null
let sessionStarted = ref(false) // to switch mode when a session is started

//let totalMinutes = computed(() => (120 / 90) * (sliderValue.value - 15))
let totalMinutes = ref(0)


let spentMinutes = computed(() => Math.floor(totalMinutes.value - (remainingTime.value % 36000 / 60)))
let spentSeconds = computed(() => Math.floor((60 - (remainingTime.value ) % 60)))

// count down the remaining time
const startSession = () => {
  if(totalMinutes.value === 0) {
    return
  }
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
// back to initial state when abandon session
const abandonSession = () => {
  if (intervalId) {
    clearInterval(intervalId)
    intervalId = null
  }
  remainingTime.value = totalMinutes.value * 60
  sessionStarted.value = false
}
</script>

<style scoped>
.water {
  background: linear-gradient(to top, hsl(var(--in)) 70%, transparent 70%);
}

.aquarium {
  background: linear-gradient(to top, hsl(var(--b3)) 90%, transparent 90%);
}

.small-fish {
  width: 2rem;
  height: 1rem;
  background: hsl(var(--b3));
  border-radius: 50%;
  animation: swim 4s ease infinite;
}

.small-fish-2 {
  width: 2rem;
  height: 1rem;
  background: hsl(var(--b3));
  border-radius: 50%;
  animation: swim 3s ease-out infinite;
}

.fish {
  animation: swim 5s ease-in-out infinite;
}

.fish-animation {
  animation: swim-flip 5s ease-in-out infinite;
}

@keyframes swim {
  0% {
    transform: translateX(0);
  }
  50% {
    transform: translateX(2rem);
  }
  100% {
    transform: translateX(0);
  }
}

@keyframes swim-flip {
  0% {
    transform: translateX(0);
  }
  30% {
    transform: translateX(-4rem);
  }
  40% {
    transform: rotateY(180deg) translateX(4rem);
  }
  60% {
    transform: translateX(4rem) rotateY(180deg);
  }
  80% {
    transform: translateX(4rem);
  }
  100% {
    transform: translateX(0);
  }
}
</style>
