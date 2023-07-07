<template>
  <div class="auth flex flex-row flex-wrap justify-center items-center">
    <div class="flex flex-col my-60 px-12 gap-4 text-base-100">
      <div class="flex-1">
        <span class="text-7xl">AquaTask</span>
      </div>
      <div class="flex-1">
        <span class="text-3xl">Stay focus, dive into productivity </span>
      </div>
      <div class="flex-1">
        <figure><img src="src/assets/logo.png" class="w-96" alt="Album" /></figure>
      </div>
    </div>
    <div class="shrink">
    <div class="card card-side bg-base-100 shadow-xl mb-32">
      <div class="card-body w-full">
        <h2 class="card-title">Sign up</h2>
        <div class="form-control w-96">
          <label class="label mt-2">
            <span class="label-text">Your email</span>
          </label>
          <input
            type="text"
            v-model="email"
            placeholder="name@company.com"
            class="input input-bordered"
          />
          <label class="label mt-2">
            <span class="label-text">Password</span>
          </label>
          <input
            type="password"
            v-model="password"
            placeholder="• • • • • • • • • • •"
            class="input input-bordered"
          />
          <label class="label mt-2">
            <span class="label-text">Confirm password</span>
          </label>
          <input
            type="password"
            v-model="confirmPassword"
            placeholder="• • • • • • • • • • •"
            class="input input-bordered"
          />
          <label class="cursor-pointer justify-start label mt-2">
            <input type="checkbox" checked="checked" class="checkbox checkbox-secondary mr-2" />
            <span class="label-text">I accept the <a href="#">Terms and Conditions</a></span>
          </label>
        </div>
        <div class="card-actions justify-center">
          <button @click="signup" class="btn btn-primary w-full my-3">Create an account</button>
        </div>
        <div class="card-actions justify-start">
          <span>Already have an account ? </span
          ><router-link to="/auth" class="text-secondary font-bold">Sign in here</router-link>
        </div>
      </div>
    </div>
  </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'

const email = ref('')
const password = ref('')
const confirmPassword = ref('')

async function signup() {
  if (password.value !== confirmPassword.value) {
    alert('Passwords do not match')
    return
  }
  try {
    const response = await axios.post('http://localhost:5000/register', {
      email: email.value,
      password: password.value
    })
    console.log(response)
  } catch (error) {
    console.log(error)
  }
}
</script>

<style>
.auth {
  height: calc(100vh - 4.68rem);
  background: linear-gradient(to bottom, hsl(var(--s)) 0%, #764ba2 100%);
}
</style>
