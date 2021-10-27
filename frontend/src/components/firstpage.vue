<template>
<div>
    <h1>eye that game</h1>
    <van-image
    round
    width="10rem"
    height="10rem"
    :src="srcString"
  />
  <img src="../assets/logo1.png"/>
  
    <h2>can you recogniza
   which one is fake?</h2>

   <h3>let's try it now</h3>

   <button @click="hreftwo" class="test-one">Start</button>

</div>
</template>

<script>


export default {
  name: 'App',
  components: {
    // HelloWorld
    // VanImage
  },
  method:{
    hreftwo(){
      this.$router.push({path:'/'})
    }
  },
  data(){
    return {
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
  background: #435875;
  
 }

</style>
