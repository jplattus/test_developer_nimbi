<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <div class="app">
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand href="#">Nimbi Blog</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav right>
        <b-navbar-nav>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">

          <b-nav-item href="#" v-if="auth_status!=='success'" >
            <router-link class="text-white" to="/admin/login">Ingresar</router-link>
          </b-nav-item>

          <b-nav-item-dropdown v-if="auth_status==='success'" right>
            <!-- Using 'button-content' slot -->
            <template v-slot:button-content>
              <em>{{username}}</em>
            </template>
            <b-dropdown-item to="/admin/dashboard" href="#">Admin</b-dropdown-item>
            <b-dropdown-item @click.prevent="logout" href="#">Sign Out</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <div class="container-fluid">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>

  import {mapState} from "vuex";

  export default {
    name: "Navbar",
    computed: {
      ...mapState({
        auth_status: state => state.auth_status,
        username: state => state.user.username,
      })
    },
    methods: {
      logout() {
        this.$store.dispatch('logout')
      }
    }
  }
</script>

<style scoped>

</style>
