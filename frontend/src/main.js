import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import VCalendar from 'v-calendar';
import 'v-calendar/style.css';


const app = createApp(App)

app.use(router)

// Use plugin with optional defaults
app.use(VCalendar, {})

app.mount('#app')
