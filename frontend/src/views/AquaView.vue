<template>
    <div class="flex items-center flex-col">
        <div id="aquarium">
  <div class="face" id="front"></div>
  <div class="face" id="bottom"></div>
  <div class="face" id="side"></div>
</div>
</div>

</template>

<script setup>
import { gsap } from "gsap";
import { ref, onMounted } from "vue";

const t1 = gsap.timeline({ repeat: -1, repeatDelay: 0.5 });

onMounted(() => {
  t1.to(".aquarium", {
    "--s": 180,
    duration: 1,
    ease: "power2.inOut",
  });
});

</script>

<style scoped>
#aquarium {
  position: relative;
  perspective: 1000px;
  width: 200px;
  height: 200px;
}

.face {
  position: absolute;
  width: 200px;
  height: 200px;
}

#top {
  background: rgba(0, 153, 204, 0.5);
  transform: rotateX(90deg) translateZ(100px);
}

#side1 {
  background: rgba(0, 153, 204, 0.5);
  transform: rotateY(90deg) translateZ(100px);
}

#side2 {
  background: rgba(0, 153, 204, 0.5);
  transform: rotateY(-90deg) translateZ(100px);
}
</style>