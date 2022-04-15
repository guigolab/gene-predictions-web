<template>
   <b-modal size="xl" id="data-modal" scrollable :title="organism +' '+model">
      
      <table-component
      stacked
      :items="data"
      >
        <template #cell(download)="row">
          {{row.item}}
        <b-button @click="downloadFile(row.item)">Download file</b-button>
        </template>
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


export default {
  name: "file-list-modal",
  props: ['data', 'organism', 'model'],
  data() {
    return {
        fields: [
          "name", 
          {key: 'download', label: ''}
        ],
    };
  },
  components: { TableComponent },
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
