// import Vue from 'vue'
import router from './router'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap'


import { createApp } from 'vue'
import App from './App.vue'


// createApp(App).mount('#app')


const app = createApp(App)
// app.use(BootstrapVue)
// app.use(IconsPlugin)
app.use(router)
app.mount('#app')
// Vue.config.productionTip=false

// new Vue({
//     router,
//     render:h => h(App),
// }).$mount('#app')

