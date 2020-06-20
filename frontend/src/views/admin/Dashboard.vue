<template>
  <div class="animated fadeIn">
    <b-card>
      <b-row>
        <b-col sm="5">
          <h4 id="traffic" class="card-title mb-0">Rendimiento Equipos</h4>
          <div class="small text-muted">Última actualización: </div>
        </b-col>
        <b-col sm="7" class="d-none d-md-block">
          <b-button
                    type="button" variant="primary"
                    class="float-right">
            <b-spinner small label="Small Spinner"/>
            <i class="icon-reload"/>
          </b-button>
        </b-col>
      </b-row>
    </b-card>
  </div>
</template>

<script>
export default {
  name: 'dashboard'
}
</script>
