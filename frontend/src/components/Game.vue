<template>
  <div>
    <h1>Can you tell whether this is real or fake?</h1>
  
    <van-image 
     square
    width="20rem"
    height="20rem"
    :src="this.srcString"
    class="app"
  />
  <h3> </h3>
  <button v-if="!tag" v-on:click="guessreal" class="test-one" style="
   width:130px;
   height:60px">real</button>
    <h4> </h4>
  <button v-if="!tag" v-on:click="guessfake" class="test-one" style="
   width:130px;
   height:60px">fake</button>
   <h5> </h5>
  <button v-if="tag" v-on:click='submit' class="test-one" style="
   width:130px;
   height:60px">submit</button>
   </div>
</template>

<script>
import { Image as VanImage } from 'vant';
import router from "../router/index.js";
import axios from 'axios';
export default {
  name: 'App',
  components: {
    VanImage
  },
 
  methods:{
  guessreal(){
    this.index=this.index+1
    if (this.index==10)
      this.tag=true
    this.srcString=this.list[this.index].url
    this.ans.push(1)
  },
   guessfake(){
    this.index=this.index+1
    if (this.index==10)
      this.tag=true
    this.srcString=this.list[this.index].url
    this.ans.push(0)
  },
  submit(){
    let _that=this
    var i
    for (i=0;i<10;i++)
    {
      if(_that.ans[i]==_that.list[i].type)
        _that.right=_that.right+1
    }
   axios.post('/api/submit_answers', JSON.stringify(
     {
    task_id: _that.taskid
  }),
  {headers:{
    'Content-Type':'application/json'
  }

  })
  .then(function (response) {
    console.log("sljfdl")
    console.log(response.data.ai_score.accuracy);
    _that.aiscore=response.data.ai_score.accuracy
    console.log(_that.aiscore)
     router.push({
          path: '/result',
          query: {
            aiscore:_that.aiscore,
            right:_that.right
          }
        })
   
  })
  .catch(function (error) {
    console.log(error);
  });

 
  
  }
  },
  created() {
  // Simple GET request using axios
  // this.uuid = this.$route.query.id
  // console.log(this.myuuid)
  let that =this
  axios.get("/api/get_images?number=10",)
    .then(response => {console.log(response),
      that.list = response.data.list, that.taskid=response.data.task_id,that.srcString=that.list[0].url});
},
 
  data() {
    return {
      url:'',
      index:0,
      list:[],
      aiscore:0,
      ans:[],
      right:0,
      // myuuid:this.$route.query.id,
      headimg: require("../assets/logo.png"),
      srcString:'',
      tag:false
      
    }
  }
}


</script>

<style>
.test-one { 
  margin: 0 auto;
  
  border: none;
  color: #fff;
  width: 100%;
  padding: 1rem 0;
  border-radius: 4px;
  font-size: 1.4rem;
  align-items: center;
  justify-content: center;
  background: #0a2750;
  display: flex;
  flex-direction: column;
 }
 .hoverBg{
  background: #ccc;
  color: #fff;
}
.clickBg{
  background: red;
  color: #fff;
}


</style>
