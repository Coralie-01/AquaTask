import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import pinia from './store'
import VCalendar from 'v-calendar'
//import RoundSlider from 'vue-three-round-slider'
import 'v-calendar/style.css'
import './index.css'

const app = createApp(App)

app.use(router)
app.use(pinia)

// Use plugin with optional defaults
app.use(VCalendar, {})
//app.use(RoundSlider)

app.mount('#app')
