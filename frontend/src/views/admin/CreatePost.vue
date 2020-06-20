<template>
  <div class="animated fadeIn">
    <b-card title="Crear Post">
      <template v-slot:title>
        <h4 class="mb-0">Hello World</h4>
      </template>
      <b-row>
        <b-col>
          <b-form v-if="show">
            <b-form-group
              id="title"
              label="Título:"
              label-for="input-1"
            >
              <b-form-input
                id="input-1"
                type="text"
                v-model="$v.form.title.$model"
              ></b-form-input>
            </b-form-group>

            <b-form-group id="input-group-2" label="Contenido:" label-for="input-2">
              <vue-editor v-model="$v.form.content.$model"/>
            </b-form-group>

            <b-button :disabled="loading"
                      @click.prevent="onSubmit"
                      type="submit"
                      class="float-right ml-2"
                      variant="primary">
              <b-spinner v-if="loading" small></b-spinner>
              Guardar
            </b-button>

            <b-button :disabled="loading"
                      @click.prevent="confirmDeletePost(form.slug)"
                      type="submit"
                      class="float-right ml-2"
                      variant="danger">
              <b-spinner v-if="loading" small></b-spinner>
              Borrar Post
            </b-button>


          </b-form>
        </b-col>
      </b-row>
    </b-card>
  </div>
</template>

<script>

  import {VueEditor} from "vue2-editor";
  import {required, maxLength} from 'vuelidate/lib/validators'
  import Swal from 'sweetalert2'
  import _ from 'lodash'

  export default {
    name: "CreatePost",
    components: {
      VueEditor
    },
    beforeMount() {
      const params = this.$route.params;
      if (!_.isEmpty(params)) {
        this.getPost(params.slug);
      }
    },
    destroyed() {

    },
    data() {
      return {
        loading: false,
        form: {
          title: '',
          content: '',
          slug: '',
        },
        show: true
      }
    },
    methods: {
      onSubmit(evt) {
        evt.preventDefault();

        // FORM validation
        this.$v.form.$touch();
        if (this.$v.form.$anyError) {
          Swal.fire(
            'Oops!',
            "Faltan campos que completar",
            'warning'
          );
          return;
        }

        // Contitional usage of the same button CREATE / UPDATE
        if (this.form.slug === '') {
          this.savePost();
        } else {
          this.updatePost(this.form.slug);
        }
      },
      onReset(evt) {
        evt.preventDefault()
        // Reset our form values
        this.form.title = '';
        this.form.content = '';
        this.form.slug = '';

        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      },

      // CRUD functions
      async savePost() {
        const thisV = this;
        thisV.loading = true;
        try {
          const response = await thisV.$axios({
            method: "POST",
            url: 'api/v1/post/',
            data: {
              content: thisV.form.content,
              title: thisV.form.title,
            },
          });
          Swal.fire(
            'Creado!',
            'Tu post fue creado con éxito.',
            'success'
          );
          thisV.$router.push({name: 'lista-post'});
          thisV.loading = false;
        } catch (error) {
          thisV.$toast.error(error.response.data.detail, "");
          thisV.loading = false;
        }
      },
      async updatePost(slug) {
        const thisV = this;
        thisV.loading = true;
        try {
          const response = await thisV.$axios({
            method: "PUT",
            url: `api/v1/post/${slug}/`,
            data: {
              content: thisV.form.content,
              title: thisV.form.title,
            },
          });
          Swal.fire(
            'Editado!',
            'Tu post fue editado con éxito.',
            'success'
          );
          thisV.$router.push({name: 'lista-post'});
          thisV.loading = false;
        } catch (error) {
          thisV.$toast.error(error.response.data.detail, "");
          thisV.loading = false;
        }
      },
      confirmDeletePost(slug) {
        Swal.fire({
          title: '¿Seguro que quieres borrar este post?',
          text: "Esta accion no se podrá revertir.",
          icon: 'warning',
          showCancelButton: true,
          confirmButtonColor: '#20a8d8',
          cancelButtonColor: '#f86c6b',
          confirmButtonText: 'Estoy seguro',
          cancelButtonText: 'Me arrepentí'
        }).then((result) => {
          if (result.value) {
            this.deletePost(slug);
            Swal.fire(
              'Borrado!',
              'Tu post fue borrado para siempre.',
              'success'
            )
          }
        })
      },
      async deletePost(slug) {
        const thisV = this;
        thisV.loading = true;
        try {
          const response = await thisV.$axios({
            method: "DELETE",
            url: `api/v1/post/${slug}/`,
          });
          thisV.$toast.success('Post borrado con éxito', "");
          thisV.$router.push({name: 'lista-post'});
          thisV.loading = false;
        } catch (error) {
          thisV.$toast.error(error.response.data.detail, "");
          thisV.loading = false;
        }
      },
      async getPost(slug) {
        const thisV = this;
        thisV.loading = true;
        try {
          const response = await thisV.$axios({
            method: "GET",
            url: `api/v1/post/${slug}/`,
          });
          thisV.$toast.success('Post cargado con éxito', "");
          thisV.form.title = response.data.title;
          thisV.form.content = response.data.content;
          thisV.form.slug = response.data.slug;
          thisV.loading = false;
        } catch (error) {
          thisV.$toast.error(error.response.data.detail, "");
          thisV.loading = false;
        }
      }
    },
    validations: {
      form: {
        title: {required},
        content: {required}
      }
    }
  }
</script>

<style scoped>

</style>
