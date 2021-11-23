<template>
 <b-modal scrollable :title="organism" title-tag="h2" title-class="modal-title" size="xl" id="organism-info-modal" ok-only @hide="resetInfoModal">
    <b-container>
      <b-row>
       <b-col>
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
           </b-table>
      </b-col>
      </b-row>
    </b-container>
</b-modal>
</template>

<script>
import taxonFileService from "../../services/TaxonFileService";

export default {
  name: "organism-info-modal",
  props: ['files', 'organism'],
  data() {
    return {
        isBusy: false,
        overlay: false,
        taxonId: null,
        fields: ["name","type", { key: 'actions', label: '' }, {key: 'download', label: ''}],
        currentPage: 1,
        perPage: 5,
        selectMode:"single"
    }
  },
  methods: {
        downloadFile(item) {
            taxonFileService.download(item[0].name)
            .then(response => {
                const url = window.URL.createObjectURL(new Blob([response.data], { type: { type: 'text/plain;charset=utf-8' }}));
                const link = document.createElement('a');
                link.href = url;
                link.setAttribute('download', item[0].name);
                link.click();
            })
        },    
    },
    mounted() {

    },
}

</script>

<style>
.list {
  text-align: left;
  max-width: 80vw;
  margin: auto;
}
</style>
