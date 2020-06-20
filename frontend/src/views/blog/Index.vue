<template>
  <transition name="fade">
    <!-- Main Content -->
    <div v-if="!loading" class="container mt-5">
      <div class="row">
        <div class="col-lg-8 col-md-10 mx-auto" v-for="post in posts">
          <b-card :title="post.title">
            <p>{{post.summary}}</p>
            <b-row>
              <b-col>
                <p class="font-italic">Creado por {{post.author_username}} el {{post.created_on|date}}</p>
              </b-col>
              <b-col>

                <b-button class="float-right" @click.prevent="goToPost(post.slug)">
                  Leer más
                  <i class="fa fa-long-arrow-right"></i>
                </b-button>
              </b-col>
            </b-row>
          </b-card>

        </div>
      </div>
      <!-- Pager -->
      <div class="clearfix">
<!--    TODO: Re-write pagination class on backend so we dont need to replace hardcoded base url -->
        <a v-if="next_url" class="btn btn-primary float-right" href="#"
           @click.prevent="getPosts(next_url.replace('http://127.0.0.1:8000/api/v1/post/',''))">
          Posts antiguos <i class="fa fa-arrow-right"></i>
        </a>
        <a v-if="prev_url" class="btn btn-primary float-left" href="#"
           @click.prevent="getPosts(prev_url.replace('http://127.0.0.1:8000/api/v1/post/',''))">
          <i class="fa fa-arrow-left"></i> Posts nuevos
        </a>
      </div>
    </div>

    <hr>

    <!-- Footer -->
    <footer>
      <div class="container">
        <div class="row">
          <div class="col-lg-8 col-md-10 mx-auto">
            <ul class="list-inline text-center">
              <li class="list-inline-item">
                <a href="#">
                <span class="fa-stack fa-lg">
                  <i class="fas fa-circle fa-stack-2x"></i>
                  <i class="fab fa-twitter fa-stack-1x fa-inverse"></i>
                </span>
                </a>
              </li>
              <li class="list-inline-item">
                <a href="#">
                <span class="fa-stack fa-lg">
                  <i class="fas fa-circle fa-stack-2x"></i>
                  <i class="fab fa-facebook-f fa-stack-1x fa-inverse"></i>
                </span>
                </a>
              </li>
              <li class="list-inline-item">
                <a href="#">
                <span class="fa-stack fa-lg">
                  <i class="fas fa-circle fa-stack-2x"></i>
                  <i class="fab fa-github fa-stack-1x fa-inverse"></i>
                </span>
                </a>
              </li>
            </ul>
            <p class="copyright text-muted">Copyright &copy; Your Website 2019</p>
          </div>
        </div>
      </div>
    </footer>


  </transition>


</template>

<script>
  import {required, email} from 'vuelidate/lib/validators'
  import moment from 'moment'

  moment.locale('es');

  export default {
    name: 'Index',
    data() {
      return {
        loading: false,
        msg: null,
        posts: [],
        next_url: '',
        prev_url: '',
        count: 0,
      }
    },
    beforeMount() {
      this.getPosts('');
    },
    filters: {
      date: function (date) {
        return moment(date).format('ll');
      },
    },
    methods: {
      goToPost(slug) {
        this.$router.push({name: "post", params: {slug: slug}})
      },
      async onSubmit() {
        const thisV = this;
        thisV.$v.form.$touch();
        if (thisV.$v.form.$anyError) {
          return;
        }
        const payload = thisV.form;
        try {
          const response = await this.$store.dispatch('login', payload)
          if (response.status == 200) {
            await thisV.$router.push({name: 'Dashboard'})
          }
        } catch (error) {
          this.$toast.error("Usuario o contraseña incorrecta");
          this.form.password = null;
          this.form.email = null;
          console.log(error)
        }
      },
      async getPosts(params) {
        const thisV = this;
        thisV.loading = true;
        try {
          const response = await thisV.$axios({
            method: "GET",
            url: `api/v1/post/${params}`,
          });
          thisV.posts = response.data.results;
          thisV.next_url = response.data.next;
          thisV.prev_url = response.data.previous;
          thisV.count = response.data.count;
          thisV.loading = false;
        } catch (error) {
          thisV.$toast.error(error.response.data.detail, "");
          thisV.loading = false;
        }
      }
    },
    validations: {
      form: {
        email: {required, email},
        password: {required}
      }
    }
  }
</script>
<style>
  .fade-enter-active, .fade-leave-active {
    transition: opacity .5s;
  }

  .fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */
  {
    opacity: 0;
  }

</style>
