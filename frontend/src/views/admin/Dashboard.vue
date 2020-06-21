<template>
  <div class="animated fadeIn">
    <b-row>
      <b-col>
        <b-card title="Usuarios">
          <p>{{dashboard_data.user_count}} Usuarios</p>
        </b-card>
      </b-col>
      <b-col>
        <b-card title="Sesiones">
          <p>{{dashboard_data.session_count}} Sesiones</p>
        </b-card>
      </b-col>
      <b-col>
        <b-card title="Lecturas">
          <p>{{dashboard_data.path_count}} Post leídos</p>
        </b-card>
      </b-col>
    </b-row>
    <b-card>
      <b-row>
        <b-col sm="5">
          <h4 id="traffic" class="card-title mb-0">Sesiones últimos 7 días</h4>
        </b-col>
        <b-col sm="7" class="d-none d-md-block">
          <b-button
            type="button" variant="primary"
            @click.prevent="getDashboardData"
            class="float-right">
            <b-spinner v-if="loading" small label="Small Spinner"/>
            <i class="icon-reload"/>
          </b-button>
        </b-col>
      </b-row>
      <chart ref="chart"
             class="chart-wrapper"
             v-if="loaded"
             :chart-data="chartData"
             :options="options"
             style="height:300px;margin-top:40px;">
      </chart>
    </b-card>
    <b-card>
      <b-row>
        <b-col>
          <b-table striped hover :items="dashboard_data.path_by_day">

          </b-table>
        </b-col>
      </b-row>
    </b-card>
  </div>
</template>

<script>
  import Chart from './Chart'
  import moment from 'moment'
  import _ from 'lodash'

  export default {
    name: 'dashboard',
    components: {
      Chart
    },
    data() {
      return {
        loaded: false,
        dashboard_data: null,
        chartData: {
          labels: [],
          datasets: [
            {
              label: 'C',
              pointHoverBackgroundColor: '#fff',
              borderWidth: 2,
              data: []
            },

          ]
        },
        options: {
          maintainAspectRatio: false,
          legend: {
            display: false
          },
          scales: {
            xAxes: [{
              gridLines: {
                drawOnChartArea: false
              }
            }],
            yAxes: [{
              ticks: {
                beginAtZero: true,
                maxTicksLimit: 5,
                stepSize: Math.ceil(250 / 5),
                max: 10
              },
              gridLines: {
                display: true
              }
            }]
          },
        }
      }
    },
    mounted() {
      this.getDashboardData();
    },
    methods: {
      async getDashboardData() {
        const thisV = this;
        thisV.loading = true;
        try {
          const response = await thisV.$axios({
            method: "GET",
            url: 'api/anal/dashboard',
          });
          thisV.loading = false;
          thisV.loaded = true;
          thisV.dashboard_data = response.data;
          thisV.chartData.labels = response.data.sessions_by_day.dates;
          thisV.chartData.datasets[0].data = response.data.sessions_by_day.data;
          thisV.options.scales.yAxes[0].ticks.max = Math.max(...response.data.sessions_by_day.data)+10;
          thisV.$refs.chart.$data._chart.update();
        } catch (error) {
          thisV.$toast.error(error.response.data.detail, "");
          thisV.loading = false;
        }
      },


    }
  }
</script>
