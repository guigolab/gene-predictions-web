<template>
   <b-modal size="xl" id="data-modal" scrollable :title="organism +' '+model">
      
      <table-component
      :items="data"
      :fields="fields"
      >
        
        
        <template #cell(download)="row">
          <b-button @click="downloadFile(row.item)">Download file</b-button>
        </template>
        <!-- <template #cell(actions)="row">
            <b-button size="sm" :to="{name: 'genome-browser', params: {fileName: row.item.name}}" class="mr-1">
            Visualize Genome
            </b-button> 
        </template>  -->
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
