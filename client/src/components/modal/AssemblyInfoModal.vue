<template>
 <b-modal scrollable :title="metadata ? metadata.display_name:''" title-tag="h2" title-class="modal-title" size="xl" id="assembly-info-modal" @hide="resetInfoModal">
    <b-container>
      <b-row>
       <b-col>
        <b-tabs content-class="mt-3">
          <b-tab title="Assembly Metadata" active>
            <table-component stacked :items="[metadata]">

            </table-component>
          </b-tab>
          <b-tab title="Chromosomes/Sequences" lazy>
          <table-component :items="chromosomes">

          </table-component>
          </b-tab>
          <b-tab v-if="biosample" title="Biosample" lazy>
            <table-component stacked :items="[biosample]">
            </table-component>
          </b-tab>
        </b-tabs>
      </b-col>
      </b-row>
    </b-container>
</b-modal>
</template>

<script>
// import {BCard} from 'bootstrap-vue'
import TableComponent from '../base/TableComponent.vue'

export default {
  name: "assembly-info-modal",
  props: ['metadata','biosample','chromosomes'],
  components:{TableComponent},
  methods:{
    getMetadataFields(assembly, biosample, chromosomes){
      return {chromosomes,biosample,...assembly}
    }
  }
}

</script>

