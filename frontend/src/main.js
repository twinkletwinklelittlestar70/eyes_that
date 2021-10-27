<<<<<<< HEAD
import  { createApp } from 'vue'
// import CircleMenu from 'vue-circle-menu'
=======
import { createApp } from 'vue'
>>>>>>> 3bbdc88d00a1b83fefd930611888625001d9591a
import router from './router'
import App from './App.vue'

const app = createApp(App)
app.use(router)
app.mount('#app')
