import './polyfill'
import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import App from './App'
import router from './router/index'
import { store } from "./store/store.js";
import axios from "axios"
import miniToastr from 'mini-toastr'
import Vuelidate from 'vuelidate'
import VueCookies from 'vue-cookies'

Vue.use(Vuelidate);

// Cookies set for user navigation records
// We will be saving an user and a session
// User cookie will be created when new user vitis the page
// Session will be created everytime we visit the page, but remains when we navigate across the SPA
Vue.use(VueCookies);
Vue.$cookies.config('30d');
const usr = Vue.$cookies.get('usr');
const d = new Date().getTime();
if (!usr) {
  Vue.$cookies.set('usr', 'usr'+d);
}
Vue.$cookies.set('sess', d);


Vue.use(BootstrapVue);

Vue.prototype.$axios = axios;
axios.defaults.baseURL = "http://127.0.0.1:8000/";

Vue.prototype.$toast = miniToastr
const toastTypes = {
  success: 'success',
  error: 'error',
  info: 'info',
  warn: 'warn'
};
miniToastr.init({types: toastTypes})
Vue.use(miniToastr);


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: {
    App
  }
})
