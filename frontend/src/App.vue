<template>
<div>
  <h1>eye that game</h1>
  <van-image
  round
  width="10rem"
  height="10rem"
  src="headimg"
/>
 
  <h2>can you recogni
 which one is fake?</h2>
 </div>

  
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
// import Vue from 'vue';
import { Image as VanImage } from 'vant';


export default {
  name: 'App',
  components: {
    // HelloWorld
    VanImage
  },
  data(){
    return {
      headimg: require("./assets/logo.png")
    }
          
   }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
