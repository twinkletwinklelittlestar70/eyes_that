import { createRouter, createWebHistory } from 'vue-router'
import HelloWorld from '../components/HelloWorld.vue'
import NotFound from '../components/NotFound.vue'
import FirstPage from '../components/FirstPage.vue'
import SecondPage from '../components/SecondPage.vue'

const routes = [{
    path: '/index',
    name:'FirstPage',
    component: FirstPage
 }, {
    path: '/game',
    name:'SecondPage',
    component: SecondPage
 }, {                       // 下面两个是示范应该怎么写页面
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
