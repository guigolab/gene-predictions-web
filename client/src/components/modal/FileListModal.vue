<template>
 <b-modal title="File List" id="file-list-modal" >
      <b-table 
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
      <!-- <template #cell(actions)="row">
            <b-button size="sm" :to="{name: 'genome-browser', params: {fileName: row.item.name}}" class="mr-1">
            Visualize Genome
            </b-button> 
        </template> -->
        
        <!-- <b-pagination
        v-model="currentPage"
        :total-rows="rows"
        :per-page="perPage"
        aria-controls="files-table"
        ></b-pagination> -->
      </b-table>
    </b-modal>
</template>

<script>
import taxonFileService from "../../services/TaxonFileService";

export default {
  name: "file-list-modal",
  props: ['files'],
  data() {
    return {
        fields: ["name","type", { key: 'actions', label: '' }, {key: 'download', label: ''}],
        currentPage: 1,
        perPage: 5,
        selectMode:"single",
    };
  },
    methods: {
        downloadFile(item) {
          console.log(item)
            taxonFileService.download(item[0].name)
            .then(response => {
                const url = window.URL.createObjectURL(new Blob([response.data], { type: { type: 'text/plain;charset=utf-8' }}));
                const link = document.createElement('a');
                console.log(link)
                link.href = url;
                link.setAttribute('download', item[0].name);
                link.click();
            })
        },    
    },
    mounted() {
    },
    // computed: {
    // rows() {
    //     return this.files.length
    //     }
    // },
};

</script>

<style>
.list {
  text-align: left;
  max-width: 750px;
  margin: auto;
}
</style>
