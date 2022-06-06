import {createApp} from "vue";
import App from "./App.vue";
import WebCam from 'vue-web-cam'
// import { WebCam } from "vue-web-cam";


Vue.use(WebCam)

new Vue({
  render: h => h(App)
}).$mount("#app");

// const app =createApp(App)
// app.use(WebCam);
// app.mount("#app");