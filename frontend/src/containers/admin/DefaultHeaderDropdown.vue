<template>
  <AppHeaderDropdown right no-caret>
    <template slot="header">
      <img
        src="img/avatars/6.jpg"
        class="img-avatar"
        alt="admin@bootstrapmaster.com" />
    </template>
    <template slot="dropdown">
      <div>
        <h6 class="text-capitalize text-center">Hola {{username}}</h6>
        <ol>
          <li @click.prevent="logout">Cerrar sesión</li>
        </ol>
      </div>
    </template>
  </AppHeaderDropdown>
</template>

<script>
import { HeaderDropdown as AppHeaderDropdown } from '@coreui/vue'
import {mapState} from "vuex";
export default {
  name: 'DefaultHeaderDropdown',
  components: {
    AppHeaderDropdown
  },
  computed: {
    ...mapState({
      username : state => state.user.username,
    })
  },
  methods: {
    logout(){
      this.$store.dispatch('logout');
    }
  }
}
</script>

