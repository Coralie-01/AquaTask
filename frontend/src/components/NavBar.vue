<template>
    <div class="navbar bg-secondary text-neutral-content">
  <div class="flex-1">
    <img src="/src/assets/logo.png" style="width: 6.80806rem;
height: 3.6875rem;
flex-shrink: 0;" />
    <a class="btn btn-ghost normal-case text-xl">AquaTask</a>
  </div>
  <div class="flex-none">
    <div class="dropdown dropdown-end">
      <label tabindex="0" class="btn btn-ghost btn-circle avatar">
        <div class="w-10 rounded-full">
          <i class="fi fi-rr-user icon"></i>
        </div>
      </label>
      <ul tabindex="0" class="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52">
        <li>
          <a class="justify-between">
            Profile
            <span class="badge">New</span>
          </a>
        </li>
        <li><a>Settings</a></li>
        <li><a>Logout</a></li>
      </ul>
    </div>
  </div>
</div>
</template>

<style>
.icon {
  color: white;
  font-size: 2.5rem;
}
</style>