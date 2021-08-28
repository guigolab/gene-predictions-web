<template>
  <div id="app">
    <nav-bar-component></nav-bar-component>
    <b-container fluid>
      <router-view />
    </b-container>
  </div>
</template>

<script>
// import { Slide } from 'vue-burger-menu'
import NavBarComponent from './components/NavBarComponent.vue'

export default {
  name: "app",
  components: {
        // Slide,
    NavBarComponent,

    }

};
</script>
<style>
  h1 {
    text-align: center;
    font-family: Raleway;
  }
</style>