<template>
  <div class="player flex flex-col">
  <button class="btn btn-sm text-xs" v-if="!loggedIn" @click="logIn" target="_self">Login with Spotify</button>
  <div
    class="player-control bg-gradient-to-r from-slate-900 to-sky-900 w-full flex flex-col gap-2 text-base-100 rounded-full"
  >
    <div class="current-track flex flex-row items-center mt-4 ml-6">
      <i class="fi fi-brands-spotify mx-2 text-4xl text-primary"></i>
      <div class="flex flex-col">
        <span class="font-bold">{{ songName }}</span>
        <span class="text-slate-400">{{ songAuthor }}</span>
      </div>
    </div>
    <div class="flex flex-row items-center gap-4 mx-4">
      <span>{{ songPos }}</span>
      <progress class="progress progress-primary" :value="songPos_ms" :max="songTime_ms" id="progress"></progress>
      <span>{{ songTime }}</span>
    </div>
    <div class="player-buttons flex mb-2 justify-center">
      <button class="button-previous" id="previous">
        <i class="fi fi-ss-rewind text-xl"></i>
      </button>
      <button class="button-play mx-3" id="togglePlay">
        <i v-if="currentlyPlaying" class="fi fi-ss-pause-circle text-4xl"></i>
        <i v-else class="fi fi-ss-play-circle text-4xl"></i>
      </button>
      <button class="button-next" id="next">
        <i class="fi fi-ss-forward text-xl"></i>
      </button>
    </div>
  </div>
</div>
</template>

<script setup>
import { ref, computed, watch, onMounted, onUnmounted } from 'vue'

const spotifyLoginUrl = 'http://localhost:5000/spotifylogin'

const loggedIn = ref(false)
const currentlyPlaying = ref(false)
const songName = ref('No track playing')
const songAuthor = ref('')
const songPos_ms = ref(0)
const songTime_ms = ref(200000)
const songPos = computed(() => {
  return formatTime(songPos_ms.value)
})
const songTime = computed(() => {
  return formatTime(songTime_ms.value)
})
const Token = ref('')

let stateUpdateTimer = null
    // Call stopStateUpdateTimer() when you want to stop the periodic state update
  // For example, when the playback pauses or stops:
  
function startStateUpdateTimer(player) {
    stateUpdateTimer = setInterval(() => {
      updatePlaybackState(player)
    }, 1000) // Update every 1 second (1000 milliseconds)
  }

  function stopStateUpdateTimer() {
    clearInterval(stateUpdateTimer)
  }

async function updatePlaybackState(player) {
  const state = await player.getCurrentState()
  if (state && state.position !== null && state.duration !== null) {
    currentlyPlaying.value = !state.paused
    songPos_ms.value = state.position
    songTime_ms.value = state.duration
    songName.value = state.track_window.current_track.name
    // Special cases for song with multiple artists
    if (state.track_window.current_track.artists.length > 1) {
      songAuthor.value =
        state.track_window.current_track.artists[0].name +
        ' & ' +
        state.track_window.current_track.artists[1].name
    } else {
      songAuthor.value = state.track_window.current_track.artists[0].name
    }
  }
}

async function connectToAquaTaskPlayer(token) {
  // Call the getMyDevices endpoint to retrieve the available devices
  console.log(token)
  const response = await fetch('https://api.spotify.com/v1/me/player/devices', {
    headers: {
      Authorization: 'Bearer ' + token[0]
    }
  })

  if (response.ok) {
    const data = await response.json()
    const devices = data.devices
    console.log(devices)

    // Find the AquaTask player device by name or other identifier
    const aquaTaskPlayer = devices.find((device) => device.name === 'AquaTask Player')

    if (aquaTaskPlayer) {
      // Connect Spotify to the AquaTask player device
      const deviceId = aquaTaskPlayer.id
      console.log(deviceId)

      // Activate the device
      // Start play
      await fetch(`https://api.spotify.com/v1/me/player/play`, {
        method: 'PUT',
        headers: {
          Authorization: 'Bearer ' + token[0],
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          device_id: deviceId,
        })
      })


      await fetch(`https://api.spotify.com/v1/me/player`, {
        method: 'PUT',
        headers: {
          Authorization: 'Bearer ' + token[0],
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          device_ids: [deviceId],
          play: true,
        })
      })
      // Put repeat mode off 
      await fetch(`https://api.spotify.com/v1/me/player/repeat?state=off`, {
        method: 'PUT',
        headers: {
          Authorization: 'Bearer ' + token[0],
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          device_id: deviceId,
        })
      })
      // Put shuffle mode off
      await fetch(`https://api.spotify.com/v1/me/player/shuffle?state=false`, {
        method: 'PUT',
        headers: {
          Authorization: 'Bearer ' + token[0],
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          device_id: deviceId,
        })
      })
      


      console.log('Spotify connected to AquaTask Player')
    } else {
      console.log('AquaTask Player not found')
    }
  } else {
    console.error('Failed to retrieve devices:', response.status, response.statusText)
  }
}

function formatTime(position) {
  const minutes = Math.floor(position / 60000)
  const seconds = Math.floor((position % 60000) / 1000)
  const formattedSeconds = seconds < 10 ? '0' + seconds : seconds
  return `${minutes}:${formattedSeconds}`
}

function logIn() {
  loggedIn.value = true
  window.location.href = spotifyLoginUrl
}



window.onSpotifyWebPlaybackSDKReady = () => {
  let token = ''
  let player = null

  // Function to fetch the access token from the server
  async function fetchAccessToken() {
    console.log('Fetching access token from server...')
    const response = await fetch('http://localhost:5000/getAccessToken') // Replace with your actual endpoint
    const data = await response.json()
    token = data.access_token
    initializePlayer()
  }

  // Initialize the Spotify player once the access token is retrieved
  function initializePlayer() {
    player = new Spotify.Player({
      name: 'AquaTask Player',
      getOAuthToken: (cb) => {
        cb(token)
      },
      volume: 0.5
    })

    // Error handling
    player.addListener('initialization_error', ({ message }) => {
      console.error(message)
    })
    player.addListener('authentication_error', ({ message }) => {
      console.error(message)
    })
    player.addListener('account_error', ({ message }) => {
      console.error(message)
    })
    player.addListener('playback_error', ({ message }) => {
      console.error(message)
    })

    // Ready
    player.addListener('ready', ({ device_id }) => {
      updatePlaybackState(player)
      console.log('Ready with Device ID', device_id)
      connectToAquaTaskPlayer(token)

      // Start the state update timer when the player is ready
      startStateUpdateTimer(player)
    })

    // Not Ready
    player.addListener('not_ready', ({ device_id }) => {
      console.log('Device ID has gone offline', device_id)
    })

    // Playback Status updates
    player.addListener('player_state_changed', () => {
      updatePlaybackState(player)
    })

    // Toggle play/pause
    document.getElementById('togglePlay').onclick = function () {
      player.togglePlay()
    }

    // Next/previous track
    document.getElementById('next').onclick = function () {
      player.nextTrack().then()
    }
    document.getElementById('previous').onclick = function () {
      player.previousTrack().then()
    }

    // Set position
    document.getElementById('progress').onclick = function (event) {
      const pos_percentage = event.offsetX / this.offsetWidth
      const newTime = pos_percentage * songTime_ms.value

      player.seek(newTime).then(() => {
        
      })
    }

 
    // Connect to the player!
    player.connect()
  }

  // Call the fetchAccessToken function to retrieve the access token
  fetchAccessToken()
}
</script>
