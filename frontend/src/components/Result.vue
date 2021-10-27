<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <van-button @click="buttonHandler">VAN BUTTON </van-button>
  </div>
</template>

<script>
import { Button } from 'vant';
import { getAllImages } from '../api/api.js'

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  components: {
    [Button.name]: Button,
  },
  methods: {
    buttonHandler(e) {
      console.log('clicking the button', e)
      getAllImages().then(data => {
        console.log('handler:', data)
      })
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
