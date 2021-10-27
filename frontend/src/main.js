import Vue, { createApp } from 'vue'
import CircleMenu from 'vue-circle-menu'
import router from './router'
import App from './App.vue'

const app = createApp(App)
app.use(router)
app.mount('#app')

Vue.component('CircleMenu', CircleMenu)

