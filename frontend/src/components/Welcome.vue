<template>
<div>
    <h1>EYES THAT</h1>
    <van-image
    round
    width="10rem"
    height="10rem"
    :src="srcString"
  />
  <img class="tupian" src="../assets/logo1.png"/>
  
    <h2>Can you recognize
   which one is fake?</h2>

   <h3>let's try it now</h3>

   <button v-on:click="hreftwo" class="test-one" style="
   width:80px;
   height:80px;
   border-radius:50%">Start</button>

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

.test-one { 
  margin: 0 auto;
  
  border: none;
  color: #fff;
  width: 100%;
  padding: 1rem 0;
  border-radius: 4px;
  font-size: 1.6rem;
  background: #172f50;
 }

 .tupian { 
  height:300px;
  width:500px;
 }

</style>
