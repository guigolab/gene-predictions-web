<template>
  <div ref="taxon-container" class="list row shadow p-3">
    <div class="col-md-12">
        <b-row id="filter-bar">
           <!-- <b-col>
            <b-button id="popover-table-target" style="border: none;" variant="outline-info" class="mb-2">
                <b-icon icon="diagram3" variant="outline-info"></b-icon>      
            </b-button>
            <b-popover target="popover-table-target" triggers="hover" placement="top" variant="info">
                See select species in tree mode
            </b-popover>
          </b-col> -->
          <b-col>
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
        :busy.sync="isBusy"
        :fields="fields"
        :per-page="perPage"
        :current-page="currentPage"
        show-empty
        @filtered="onFiltered"
        :filter="filter"
        :filter-included-fields="filterOn"
      >
       <template #cell(actions)="row">
            <b-button size="sm" @click="info(row.item, row.index, $event.target)" class="mr-1">
            Show Files
            </b-button>
        </template>
      </b-table>
      <FileListModal :taxonName="taxonName" :files="files"></FileListModal>
      <b-pagination
        v-model="currentPage"
        :total-rows="totalRows"
        :per-page="perPage"
        aria-controls="taxon-table"
        ></b-pagination>
    </div>
  </div>
</template>

<script>
import TaxonNodeDataService from "../services/TaxonNodeDataService"
import taxonFileService from "../services/TaxonFileService"
import FileListModal from "./modal/FileListModal.vue"
export default {
  name: "taxon-list",
  data() {
    return {
      selectedTaxon:{"tax_id":null,"name":null},
      taxons: [],
      taxonName: "",
      fields: ["tax_id", "name", { key: 'actions', label: '' }],
      selectMode:"single",
      currentPage: 1,
      currentModalPage: 1,
      perPage: 20,
      filter: null,
      filterOn: [],
      files: null,
      isBusy: false,
      totalRows: 1
    };
  },
  components:{
    FileListModal,
  },
    methods: {
        retrieveTaxons() {
        TaxonNodeDataService.getAll()
            .then(response => {
            this.taxons = response.data.filter(taxon => taxon.has_files);
            this.totalRows = this.taxons.length
               })  
            .catch(e => {
            console.log(e);
            });
        },
       info(item, button) {
        taxonFileService.getAll(item.tax_id)
            .then(response => {
            this.files  = response.data;
            this.taxonName = item.name;
            
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
        },
    mounted() {
      this.retrieveTaxons()
    }
};

</script>

<style>
.list {
  text-align: left;
  max-width: 750px;
  margin: auto;
}
/* #filter-bar {
    flex-direction: row-reverse;
} */
</style>
