<template>
  <div class="take-picture">
    <h1>Take picture</h1>
    <p>
      This is a description text to explain what is the game is the game is the
      game is the game
    </p>
    <div class="uploader">
      <van-uploader
        v-model="fileList"
        :multiple="false"
        preview-size="150px"
        :show-upload="showUpload"
        capture
      />
    </div>
    <van-button
      type="default"
      :loading="uploading"
      loading-text="Uploading..."
      @click="uploadImage"
      >Try it now</van-button
    >
    <div v-show="showAnswer" class="response-container">
      AI answer: {{answer? 'Real' : 'Fake'}}
    </div>
  </div>
</template>

<script>
import { Uploader } from "vant";
import { Button } from "vant";
import { uploadAndRecognizeImage } from '../api/api'

export default {
  name: "TakePicture",
  data() {
    return {
      fileList: [],
      uploading: false,
      showAnswer: false,
      answer: 1 // 0: fake, 1: real
    };
  },
  computed: {
    showUpload() {
      return this.fileList.length < 1; // Only one picture allowed
    },
  },
  components: {
    [Uploader.name]: Uploader,
    [Button.name]: Button,
  },
  methods: {
    uploadImage() {
      this.uploading = true;
      this.showAnswer = false;

      // post upload the image
      uploadAndRecognizeImage(this.fileList[0].file).then((data) => {
        console.log('test upload and recognize return', data)
        this.uploading = false;
        if (!data) {
          return
        }
        this.showAnswer = true;
        this.answer = data.is_real
      })
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.take-picture {
  padding: 20px;
  padding-top: 0;
}
.take-picture .uploader {
  margin: 30px auto;
}

.response-container {
  font-size: larger;
  margin-top: 30px;
}
</style>
