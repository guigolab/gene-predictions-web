<template>
  <div ref="taxon-container" class="list row shadow p-3">
    <div class="col-md-12">
        <b-row id="filter-bar">
          <b-col lg="6" class="my-1">
            <b-form-group
            label="Filter"
            label-for="filter-input"
            label-cols-sm="3"
            label-align-sm="right"
            label-size="sm"
            class="mb-0"
            >
            <b-input-group size="sm">
                <b-form-input ref="filter"
                id="filter-input"
                v-model="filter"
                type="search"
                placeholder="Type to Search"
                >
            </b-form-input>
            <b-input-group-append>
              <b-button :disabled="!filter" @click="filter = ''">Clear</b-button>
            </b-input-group-append>
            </b-input-group>
            </b-form-group>
          </b-col>
      </b-row>
      <b-table 
        id="taxon-table"
        striped
        :items="taxons"
        :fields="fields"
        :per-page="perPage"
        :current-page="currentPage"
        show-empty
        @filtered="onFiltered"
        :filter="filter"
        :filter-included-fields="filterOn"
      >
       <template #cell(actions)="row">
            <b-button size="sm" v-show="row.item.has_files" @click="info(row.item, row.index, $event.target)" class="mr-1">
            Show Files
            </b-button>
        </template>
      </b-table>
      <FileListModal :files="files"></FileListModal>
      <b-pagination
        v-model="currentPage"
        :total-rows="rows"
        :per-page="perPage"
        aria-controls="taxon-table"
        ></b-pagination>
    </div>
  </div>
</template>

<script>
import TaxonNodeDataService from "../services/TaxonNodeDataService";
import taxonFileService from "../services/TaxonFileService";
import FileListModal from "./modal/FileListModal.vue"
export default {
  name: "taxon-list",
  data() {
    return {
      selectedTaxon:{"tax_id":null,"name":null},
      taxons: [],
      fields: ["tax_id", "name", { key: 'actions', label: '' }],
      selectMode:"single",
      currentPage: 1,
      currentModalPage: 1,
      perPage: 1000000,
      filter: null,
      filterOn: [],
      files: null
    };
  },
  components:{
    FileListModal,
  },
    methods: {
        retrieveTaxons() {
        TaxonNodeDataService.getAll()
            .then(response => {
            this.taxons = response.data;
               })  
            .catch(e => {
            console.log(e);
            });
        },
       info(item, button) {
        taxonFileService.getAll(item.tax_id)
            .then(response => {
            this.files  = response.data;
            })
            .catch(e => {
            console.log(e);
            });
        this.$root.$emit('bv::show::modal', 'file-list-modal', button)
        },
        onFiltered(filteredItems) {
        // Trigger pagination to update the number of buttons/pages due to filtering
        this.totalRows = filteredItems.length
        this.currentPage = 1
      },
    },
    computed: {
        rows() {
            return this.taxons.length
            }
        },
    mounted() {
        this.retrieveTaxons();
    }
};

</script>

<style>
.list {
  text-align: left;
  max-width: 750px;
  margin: auto;
}
#filter-bar {
    flex-direction: row-reverse;
}
</style>
