<template>
<div class="welcome-page">
    <h1>EYES THAT</h1>
    <van-image
    round
    width="10rem"
    height="10rem"
    :src="srcString"
  />
  <img class="welcome-image" src="../assets/logo1.png"/>
  
    <h2>Can you recognize
   which one is fake? Try it now!</h2>

   <button v-on:click="hreftwo" class="primary-button" >Play against the AI</button>
   <button v-on:click="routeToPicture" class="primary-button" >Challenge AI</button>

</div>
</template>

<script>
import router from "../router/index.js";
import {v4 as uuidv4} from 'uuid';
export default {
  name: 'App',
  components: {
    // HelloWorld
  },
  methods:{
    hreftwo(){
      console.log('testwhat')
      let myuuid = uuidv4()
      console.log(myuuid)
      router.push({
          path: '/game',
          query: {
            id: myuuid
          }
        })
    },
    routeToPicture() {
      router.push({
          path: '/picture'
      })
    }
  },
  data(){
    return {
      myuuid:'',
      // headimg: require("../assets/logo.png"),
      srcString: "../assets/logo.png"
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
.welcome-page {
  padding: 30px;
  padding-top: 0;
}

.primary-button {
  margin: 15px auto;
  border: none;
  color: #fff;
  width: 100%;
  padding: .3em 0;
  border-radius: 4px;
  font-size: 1.2rem;
  background: #172f50;
}

.circle-button { 
  width:80px;
  height:80px;
  border-radius:50%
 }

 .welcome-image { 
  width: 100%;
 }

</style>
