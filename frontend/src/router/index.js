import { createRouter, createWebHistory } from 'vue-router'
import Result from '../components/Result.vue'
import NotFound from '../components/NotFound.vue'
import Welcome from '../components/Welcome.vue'
import Game from '../components/Game.vue'
import TakePicture from '../components/TakePicture.vue'

const routes = [{
    path: '/index', // 欢迎页面。包含游戏规则等。
    name:'Welcome',
    component: Welcome
 }, {
    path: '/game',  // 游戏页面。包含游戏进行时的数据
    name:'Game',
    component: Game
 }, {
    path: '/result',  // 结果页面。展示准确率和who winds
    name:'Result',
    component: Result
 }, {
   path: '/picture',  // 结果页面。展示准确率和who winds
   name:'TakePicture',
   component: TakePicture
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
