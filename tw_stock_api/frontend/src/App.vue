<template>
  <div>
    <router-view/>
  </div>
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
</template>

<script>
import { mapActions } from 'vuex';


export default {
  name: 'App',
  async mounted() {
    if (this.$route.query.token) {
      this.setAuthToken({ token: this.$route.query.token });
    }
  },
  methods: {
    ...mapActions('auth', [
      'setAuthToken',
    ]),
  },
}
</script>

<style>
/* #app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} */
/* @import '@/assets/styles/index.css'; */
</style>
