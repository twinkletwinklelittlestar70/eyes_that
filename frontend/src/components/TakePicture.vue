<template>
  <div class="take-picture">
    <h1>Challenge the AI</h1>
    <p>
      Want to challenge our AI? Please upload a picture and AI will tell you if there is a fake face included! If you are not sure where to find fake face pictures, try search "stylegan fake face" on google and get pictures from picture results!
    </p>
    <div class="uploader">
      <van-uploader
        v-model="fileList"
        :multiple="false"
        preview-size="150px"
        :show-upload="showUpload"
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
      AI answer: {{answer? 'Fake face detected' : 'No fake face'}}
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
      answer: false, // true: fake detected, false: not detected
      facesCoordinates: []
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
        if (!data || !data.is_real) {
          return
        }
        this.showAnswer = true;
        this.answer = data.is_real.filter(i => i === 0).length > 0
        this.facesCoordinates = data.coordinates
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
