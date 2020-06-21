<template>
  <div class="container animated fadeIn">


    <b-row class="mt-5">
      <b-col>
        <b-card :title="title">
          <p class="font-italic">Creado por {{author}} el {{created_on|date}}</p>
          <div v-html="content">

          </div>
        </b-card>
      </b-col>
    </b-row>
    <b-row>
      <b-col>
        <b-button @click.prevent="goToIndex">
          <i class="fa fa-arrow-left"></i>
          Volver
        </b-button>
      </b-col>
    </b-row>

  </div>
</template>

<script>
  import _ from "lodash";
  import moment from 'moment';
  moment.locale('es');

  export default {
    name: "Post",
    data() {
      return {
        title: '',
        content: '',
        author: '',
        created_on: '',
      }
    },
    created() {
      const data = {
        user: this.$cookies.get('usr'),
        session: this.$cookies.get('sess'),
        path: this.$route.path
      }
      this.$axios.post('api/anal/create_navigation', data)
        .then(function (response) {
        })
        .catch(function (error) {
          console.log(error);
        })
    },
    filters: {
      date(value) {
        return moment(value).format('ll')
      }
    },
    beforeMount() {
      const params = this.$route.params;
      if (!_.isEmpty(params)) {
        this.getPost(params.slug);
      }
    },
    destroyed() {
      this.title = '';
      this.content = '';
      this.author = '';
      this.created_on = '';
    },
    methods: {
      goToIndex() {
        this.$router.push("/")
      },
      async getPost(slug) {
        const thisV = this;
        thisV.loading = true;
        try {
          const response = await thisV.$axios({
            method: "GET",
            url: `api/blog/post/${slug}/`,
          });
          thisV.title = response.data.title;
          thisV.content = response.data.content;
          thisV.author = response.data.author_username;
          thisV.created_on = response.data.created_on;
          thisV.loading = false;
        } catch (error) {
          thisV.$toast.error(error.response.data.detail, "");
          thisV.loading = false;
        }
      }
    }
  }
</script>

<style scoped>

</style>
