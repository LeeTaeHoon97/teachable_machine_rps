<template>

  <!-- <Header msg="Hello"/> -->
  <img alt="Vue logo" src="./assets/logo.png">
  <div id="app">
    <Header/>
    <div id = 'component' class = 'content'>
      <router-view></router-view>
     
    </div>
  </div>
  
</template>

<script>
// import Header from './components/layout/Header.vue'
import Header from './components/layout/Header.vue';

export default {
  name: 'App',
  components: {
    Header,
},
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #020202;
  margin-top: 60px;
}
</style>
