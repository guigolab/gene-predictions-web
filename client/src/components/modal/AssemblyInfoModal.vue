<template>
 <b-modal scrollable :title="metadata ? metadata.display_name:''" title-tag="h2" title-class="modal-title" size="xl" id="assembly-info-modal" @hide="resetInfoModal">
    <b-container>
      <b-row>
       <b-col>
        <b-tabs content-class="mt-3">
          <b-tab title="Assembly Metadata" active>
            <table-component stacked :items="[metadata]">
              <template #cell(assembly_accession)="row">
                <a class="no-underline" target="_blank" :href="'https://www.ebi.ac.uk/ena/browser/view/'+row.item['assembly_accession']">{{row.item['assembly_accession']}}</a>
              </template> 
              <template #cell(blast_url)="row">
                <a class="no-underline" target="_blank" :href="row.item['blast_url']">{{row.item['blast_url']}}</a>
              </template>
              <template #cell(biosample_accession)="row">
                <a class="no-underline" target="_blank" :href="'https://www.ebi.ac.uk/ena/browser/view/'+row.item['biosample_accession']">{{row.item['biosample_accession']}}</a>
              </template>
            </table-component>
          </b-tab>
          <b-tab title="Chromosomes/Sequences" lazy>
          <table-component :items="chromosomes">
              <template #cell(accession_version)="row">
                <a class="no-underline" target="_blank" :href="'https://www.ebi.ac.uk/ena/browser/view/'+row.item['accession_version']">{{row.item['accession_version']}}</a>
              </template>
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
  props: ['metadata','chromosomes'],
  components:{TableComponent}
}

</script>

