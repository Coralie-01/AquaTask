<template>
    <div class="flex flex-col justify-start p-16">
        <p class="text-2xl">Tasks</p>
        <p class="text-xs">{{ date }}</p>
    </div>
</template>

<script setup>
import { defineProps } from 'vue';

defineProps({
  date: {
    type: Date,
    required: true,
  },
});

</script>