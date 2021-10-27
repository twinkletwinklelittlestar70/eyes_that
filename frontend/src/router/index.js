import { createRouter, createWebHistory } from 'vue-router'
import HelloWorld from '../components/HelloWorld.vue'
import NotFound from '../components/NotFound.vue'
import FirstPage from '../components/FirstPage.vue'
import SecondPage from '../components/SecondPage.vue'

const routes = [{
    path: '/index', // 欢迎页面。包含游戏规则等。
    name:'FirstPage',
    component: FirstPage
 }, {
    path: '/game',  // 游戏页面。包含
    name:'SecondPage',
    component: SecondPage
 }, {
    path: '/result',
    name:'HelloWorld',
    component: HelloWorld
 }, {
  path: '/:pathMatch(.*)*', 
  name: 'NotFound', 
  component: NotFound
}]
const router = createRouter({
  history: createWebHistory(),
  routes
})
export default router
