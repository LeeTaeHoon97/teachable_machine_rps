<template>
  <div class="container">
    <div class="windows">
      <div class="window1">
        <div class="score">score</div>
        <div class="result">result</div>
      </div>
      <div class="window1">title(image 가능?)</div>
      <div class="window1">
        <web-cam
          ref="webcam"
          :device-id="deviceId"
          width="100rem"
          @started="onStarted"
          @stopped="onStopped"
          @error="onError"
          @cameras="onCameras"
          @camera-change="onCameraChange"
        />
      </div>
    </div>

    <code v-if="device">{{ device.label }}</code>

    <select v-model="camera">
      <option>-- Select Device --</option>
      <option
        v-for="device in devices"
        :key="device.deviceId"
        :value="device.deviceId"
      >
        {{ device.label }}
      </option>
    </select>
    <button type="button" class="btn btn-primary" @click="onCapture">
      Capture Photo
    </button>
    <button type="button" class="btn btn-danger" @click="onStop">
      Stop Camera
    </button>
    <button type="button" class="btn btn-success" @click="onStart">
      Start Camera
    </button>
    <h2>Computer's Hand</h2>
    <figure class="figure">
      <img :src="img" class="img-responsive" />
    </figure>
  </div>
</template>

<script>
import { WebCam } from "vue-web-cam";
import { find, head } from "lodash";
import {PythonShell} from 'python-shell';

export default {
  name: "HelloWorld",
  components: {
    WebCam,
  },
  data() {
    return {
      img: null,
      camera: null,
      deviceId: null,
      devices: [],
    };
  },
  computed: {
    device() {
      return find(this.devices, (n) => n.deviceId == this.deviceId);
    },
  },
  watch: {
    camera: function (id) {
      this.deviceId = id;
    },
    devices: function () {
      // Once we have a list select the first one
      let first = head(this.devices);
      if (first) {
        this.camera = first.deviceId;
        this.deviceId = first.deviceId;
      }
    },
  },
  methods: {
    
    onCapture() {
      this.img = this.$refs.webcam.capture();

       var a = document.createElement("a"); //Create <a>
        a.href =  this.img; //Image Base64 Goes here
        a.download = "Image.png"; //File name Here
        a.click(); //Downloaded file
      
      let options = {
        scriptPath: "./src/my_py/",
        args: [this.img]
      };
      PythonShell.run("run.py", options, (err, data) => {
        if (err) throw err;

        console.log(data[0]);
        
      });

      // console.log(this.img);
      // this.img.download();
      
    },
    onStarted(stream) {
      console.log("On Started Event", stream);
    },
    onStopped(stream) {
      console.log("On Stopped Event", stream);
    },
    onStop() {
      this.$refs.webcam.stop();
    },
    onStart() {
      this.$refs.webcam.start();
    },
    onError(error) {
      console.log("On Error Event", error);
    },
    onCameras(cameras) {
      this.devices = cameras;
      console.log("On Cameras Event", cameras);
    },
    onCameraChange(deviceId) {
      this.deviceId = deviceId;
      this.camera = deviceId;
      console.log("On Camera Change Event", deviceId);
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.window1 {
  width: 20rem;
  height: 15rem;
  margin: 1%;
}
.windows {
  width: 100%;
  display: flex;
  /* text-align:center; */
  justify-content: center;
}
.score {
  font-size: 50px;
  margin: 0 0 55px 0;
}
.result {
  font-size: 30px;
}
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
.figure {
  width: 100%;
  height: 100%;
  margin: 0;
}
</style>
