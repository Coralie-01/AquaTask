<template>
  <div class="auth flex bg-base-200 justify-center items-center h-full">
    <div class="card lg:card-side bg-base-100 shadow-xl mb-20">
      <figure><img src="src/assets/logo.png" class="w-96 m-24" alt="Album" /></figure>
      <div class="card-body w-full">
        <h2 class="card-title">Sign in to your account</h2>
        <div class="form-control">
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
          <label class="cursor-pointer label w-40 mt-2">
            <span class="label-text">Remember me</span>
            <input type="checkbox" checked="checked" class="checkbox checkbox-secondary" />
          </label>
        </div>
        <div class="card-actions justify-center">
          <button @click="signin" class="btn btn-primary w-full my-3">Log in</button>
        </div>
        <div class="card-actions justify-start">
          <span>Don’t have an account yet? </span
          ><router-link to="/signup" class="text-secondary font-bold">Register</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useUserStore } from '../store/user'
import router from '../router'

const email = ref('')
const password = ref('')

async function signin() {
  try {
    const response = await axios.post('http://localhost:5000/auth', {
      email: email.value,
      password: password.value
    })
    if (response.status === 200) {
      useUserStore().login(response.data.user_id)
      router.push('/')
    }
  } catch (error) {
    console.error(error)
  }
}
</script>

<style>
.auth {
  height: calc(100vh - 4.68rem);
}
</style>
