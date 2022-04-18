<template>
   <b-modal size="xl" id="data-modal" scrollable :title="organism +' '+model">
      
      <table-component
        stacked
        :items="data"
        :fields="fields"
      >
        <template #cell(fastaLocation)="row">
          <a :href="row.item['fastaLocation']">{{row.item['fastaLocation']}}</a>
        </template>
        <template #cell(faiLocation)="row">
          <a :href="row.item['faiLocation']">{{row.item['faiLocation']}}</a>
        </template> 
        <template #cell(gziLocation)="row">
          <a :href="row.item['gziLocation']">{{row.item['gziLocation']}}</a>
        </template> 
        <template #cell(gffGzLocation)="row">
          <a :href="row.item['gffGzLocation']">{{row.item['gffGzLocation']}}</a>
        </template> 
        <template #cell(tabIndexLocation)="row">
          <a :href="row.item['tabIndexLocation']">{{row.item['tabIndexLocation']}}</a>
        </template> 
        <template #cell(paramLocation)="row">
          <a :href="row.item['paramLocation']">{{row.item['paramLocation']}}</a>
        </template>
        <template v-if="model !== 'param_files'" #cell(actions)="row">
          <b-link class="actions-link" @click="toGenomeBrowser(organism,row.item)">
            Genome browser <b-icon-search/>
          </b-link>
        </template>
      </table-component>
      <!-- <b-table 
        id="files-table"
        striped
        hover
        borderless
        :items="files"
        :fields="fields"
        :per-page="perPage"
        :current-page="currentPage"
        show-empty
        responsive="sm"
        ref="selectableTable"
        :select-mode="selectMode"
        selectable
        @row-selected="downloadFile"
      >
  
        
       <b-pagination
        v-model="currentPage"
        :total-rows="rows"
        :per-page="perPage"
        aria-controls="files-table"
        ></b-pagination> 
      </b-table> -->
    </b-modal>
</template>

<script>
import taxonFileService from "../../services/TaxonFileService";
import TableComponent from "../base/TableComponent.vue";
import portalService from "../../services/DataPortalService"
import {BIconSearch,BLink } from 'bootstrap-vue'

export default {
  name: "file-list-modal",
  props: ['data', 'organism', 'model'],
  computed:{
    fields(){
        return this.data.length ? Object.keys(this.data[0]).concat(['actions']):[]
    }
  },
  components: { TableComponent,BLink ,BIconSearch},
    methods: {
        downloadFile(item) {
            this.$bvModal.hide('data-modal')
            this.$store.dispatch('portal/showLoading')
            taxonFileService.download(item.name)
            .then(response => {
                const url = window.URL.createObjectURL(new Blob([response.data], { type: { type: 'text/plain;charset=utf-8' }}));
                const link = document.createElement('a');
                link.href = url;
                link.setAttribute('download', item.name);
                this.$store.dispatch('portal/hideLoading')
                link.click();
                
            })
        },   
      toGenomeBrowser(name, item){
        portalService.getOrganism(name)
        .then(response => {
            const organism = response.data
            const assemblyName = item.targetGenome ? item.targetGenome : item.name
            console.log(item)
            console.log(assemblyName)
            console.log(organism.genomes)
            // get assembly objet
            const assemblyObj = organism.genomes.filter(el => el.name === assemblyName)[0]
            const annotations = organism.annotations.filter(el => el.targetGenome === assemblyName)
            const assemblyView = {
              name : assemblyName,
              sequence: {
                type: 'ReferenceSequenceTrack',
                trackId: assemblyName,
                adapter: {
                  type: 'BgzipFastaAdapter',
                  fastaLocation: {
                    uri: assemblyObj.fastaLocation,
                    locationType: 'UriLocation',
                  },
                  faiLocation: {
                    uri: assemblyObj.faiLocation,
                    locationType: 'UriLocation',
                  },
                  gziLocation: {
                    uri: assemblyObj.gziLocation,
                    locationType: 'UriLocation',
                  },
                },
              },
              aliases: [assemblyName]
            }
            this.$store.commit('jbrowse/setAssembly', assemblyView)
            const tracks = []
            annotations.forEach(ann => {
              tracks.push({
                type: 'FeatureTrack',
                trackId: ann.name,
                name: ann.name,
                assemblyNames: [assemblyName],
                category: ['Annotation'],
                adapter: {
                  type: 'Gff3TabixAdapter',
                gffGzLocation: {
                  uri: ann.gffGzLocation,
                  locationType: 'UriLocation',
                  },
                index: {
                  location: {
                    uri: ann.tabIndexLocation,
                    locationType: 'UriLocation'
                  }
                }
                }
              })
            })
            this.$store.commit('jbrowse/setTracks', tracks)


            this.$router.push({name:'jbrowse', params:{assemblyName:assemblyName}})
            //load into vuex state
            //and push to jbrowse vies
            //
            //load from assembly
        })
    } 
    }
};

</script>

<style>
.list {
  text-align: left;
  max-width: 750px;
  margin: auto;
}
</style>
