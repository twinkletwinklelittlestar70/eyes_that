<template>
  <div class="hello">
    <h2>your accuracy is {{ right}}/10</h2>
    <h2>AI's accuracy is {{aiaccuracy}}/10</h2>
    <h1>feel difficult to do?</h1>
    <van-button @click="See('https://medium.com/@kcimc/how-to-recognize-fake-ai-generated-images-4d1f6f9a2842')">SOME TIPS FOR YOU? </van-button>
    <van-button v-on:click="backtoindex">try again? </van-button>
  </div>
</template>

<script>
import { Button } from 'vant';
import router from "../router/index.js";
// import { getAllImages } from '../api/api.js'Z

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  components: {
    [Button.name]: Button,
  },
  methods: {
    backtoindex()
    {
      router.push({
          path: '/index',
          query: {
        
          }
        })
    },
    See(e) {
      window.location.href=e
    }
  },
 
    created() {
  // Simple GET request using axios
  this.right = this.$route.query.right
  this.aiaccuracy=(this.$route.query.aiscore*10)
 
    },
  
data(){
  return {
      aiscore:this.$route.query.aiscore,
      right:this.$route.query.right
    }
}
}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
