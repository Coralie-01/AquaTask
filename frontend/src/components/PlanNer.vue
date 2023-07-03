<template>
    <div class="flex flex-col justify-start p-16">
        <p class="text-2xl">Tasks</p>
        <p class="text-xs">{{ date }}</p>
        <AddTask class="my-8"></AddTask>
    </div>
</template>

<script setup>
import { defineProps } from 'vue';
import AddTask from './tasks/AddTask.vue';

defineProps({
  date: {
    type: Date,
    required: true,
  },
});

</script>