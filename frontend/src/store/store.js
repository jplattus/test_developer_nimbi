import Vue from "vue";
import Vuex from "vuex";
import axios from 'axios';
import router from '../router/index'

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    auth_status: null,
    user: {
      username: null,
      token: null,
    },
  },
  getters: {

  },
  mutations: {
    // Login mutations
    auth_request(state){
      state.auth_status = 'loading'
    },

    auth_error(state){
      state.auth_status = 'error'
    },
    auth_success(state, payload){
      state.auth_status = 'success';
      state.user.username = payload.username;
      state.user.token = payload.token;
      axios.defaults.headers.common['Authorization'] = 'Token ' + payload.token;
    },
    logout(state) {
      state.auth_status = null;
      state.user.username = null;
      state.user.token = null;
      axios.defaults.headers.common['Authorization'] = '';
    },

  },
  actions: {
    // Login actions
    login: ({ commit }, payload) => {
      return new Promise((resolve, reject) => {
        commit('auth_request');
        axios.post('/rest_auth/', payload)
          .then(response => {
            const payload = {
              'username':response.data.username,
              'token':response.data.token,
            };
            commit('auth_success', payload)
            resolve(response)
          })
          .catch(function (error) {
            commit('auth_error')
            reject(error)
          });
      })
    },
    logout({commit}){
      return new Promise((resolve, reject) => {
        commit('logout')
        router.push("/");
        resolve()
      })
    },
  },
});
