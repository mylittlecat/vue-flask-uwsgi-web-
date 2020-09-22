<template>
  <div id="app">
    <!--<img src="./assets/logo.png">-->
    <div style="height: 20px;width: 100%">
      <colorfulBanner/>
    </div>

    <HelloWorld/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld'
import colorfulBanner from './components/colorfulBanner'

export default {
  name: 'App',
  components: {
    HelloWorld,
    colorfulBanner
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
