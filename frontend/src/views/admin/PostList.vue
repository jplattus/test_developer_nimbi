<template>
  <div class="animated fadeIn">
    <b-card>
      <b-card-body>
        <h1>Post</h1>

        <v-server-table url="/api/blog/post" :columns="columns" :options="options" :theme="theme" ref='table' id="dataTable">
          <div class="text-center" slot="actions" slot-scope="props">
              <router-link :to="{ name: 'post', params: { slug: props.row.slug }}">
                <i class="fa fa-lg fa-eye text-primary"></i>
              </router-link>&nbsp;
              <router-link :to="{ name: 'editar-post', params: { slug: props.row.slug }}">
                <i class="fa fa-lg fa-edit text-primary"></i>
              </router-link>&nbsp;
            </div>
        </v-server-table>
      </b-card-body>
    </b-card>

  </div>

</template>


<script>
  import Vue from 'vue'
  import {ServerTable, Event} from 'vue-tables-2'

  window.axios = require('axios');


  var d = new Date();

  Vue.use(ServerTable);

  export default {
    name: 'PostList',
    components: {
      ServerTable,
    },
    mounted() {
      Event.$on('vue-tables.loading', () => {
        this.loading = true;
      });

      Event.$on('vue-tables.loaded', () => {
        this.loading = false;
      });
    },
    data() {
      return {
        loading: false,
        columns: [
          'title',
          'author_username',
          'actions',
        ],
        data: [],
        useVuex: false,
        theme: 'bootstrap4',
        template: 'default',
        options: {
          responseAdapter: function (resp) {
            const results = resp.data.results;
            const items = [];
            for (let key in results) {
              const item = results[key];
              items.push(item)
            }

            return {
              data: items,
              count: resp.data.count
            };
          },
          texts: {
            filter: "Filtrar:",
            filterBy: 'Filtrar por {column}',
            count: ' ',
            filterPlaceholder: "Buscar...",
            columns: 'Columnas',
            limit: "Registros:",
          },
          perPage: 5,
          headings: {
            title: 'Título',
            author_username: 'Autor',
            actions: 'Acciones',
          },
          debounce: 800,
          pagination: {
            dropdown: false,
            chunk: 10
          }
        },

      }
    },
  };
</script>

<style lang="scss">
  #dataTable {
    width: 100%;
    margin: 0 auto;

    .VuePagination {
      text-align: center;
      justify-content: center;
    }

    .table td {
      padding: 0.30em;
    }

    .vue-title {
      text-align: center;
      margin-bottom: 10px;
    }

    .VueTables__search-field {
      display: flex;
    }

    .VueTables__search-field input {
      margin-left: 0.12rem;
    }

    .VueTables__limit-field {
      display: flex;
    }

    .VueTables__limit-field select {
      margin-left: 0.25rem !important;
    }

    .VueTables__table th {
      text-align: center;
      padding: 0.25rem;
    }

    .VueTables__child-row-toggler {
      width: 16px;
      height: 16px;
      line-height: 16px;
      display: block;
      margin: auto;
      text-align: center;
    }

    .VueTables__child-row-toggler--closed::before {
      content: "+";
    }

    .VueTables__columns-dropdown {
      padding-right: 20px;
    }

    .VueTables__date-filter {
      border: 1px solid #ccc;
      padding: 6px;
      border-radius: 4px;
      cursor: pointer;
    }

    .VueTables__number-field {
      border: 4px solid #ccc;
      padding: 6px;
      border-radius: 4px;
      cursor: pointer;
    }

    .VueTables__child-row-toggler--open::before {
      content: "-";
    }
  }

</style>
