<template>
<b-modal id="bv-modal" ref="bv-modal" v-if="showModal">
  <div class="list row shadow p-3">
    <div class="col-md-12">
      <div class="list row mb-2">
        <div class="col-md-6">
          <h4>File List</h4>
        </div>
      </div>
    </div>
    <div class="col-md-12">
      <b-table 
        id="files-table"
        striped
        hover
        :items="files"
        :fields="fields"
        :per-page="perPage"
        :current-page="currentPage"
        show-empty
      >
        <template #cell(index)="data">
          {{ ((currentPage-1) * perPage)+(data.index + 1) }}
        </template>
      </b-table>
      <b-pagination
        v-model="currentPage"
        :total-rows="rows"
        :per-page="perPage"
        aria-controls="files-table"
        ></b-pagination>
    </div>

  </div>
</b-modal>
</template>

<script>
import taxonFileService from "../../services/TaxonFileService";
// import Confirmation from "../components/modal/Confirmation";
// import VisualizeSpeciesModal from "../components/modal/VisualizModal";

export default {
  name: "file-list",
  props: {
      taxon: Object
  },
  data() {
    return {
      files: [],
      fields: ["name","type", "format"],
      currentPage: 1,
      perPage: 3,
      showModal:false
    };
  },
  components:{
    // Confirmation,
    // CreateUserModal
  },
    methods: {
        retrieveFiles(taxon) {
            console.log("pass");
        const taxId = taxon.taxId;
        taxonFileService.getAll(taxId)
            .then(response => {
            this.files = response.data;
            this.showModal = true;
            console.log(response.data);
            })
            .catch(e => {
            console.log(e);
            });
        },
        },
    computed: {
        rows() {
            return this.files.length
            }
        },
    mounted() {
        this.retrieveFiles(this.taxon);
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
