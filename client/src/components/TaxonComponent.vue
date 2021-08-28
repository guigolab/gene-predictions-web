<template>
      <b-col>
         <div style="display:flex;margin-bottom:15px;">
            <h3>Available prediction sets</h3>
            <div v-if="toTreeLife">
            <b-button id="popover-table-target" 
              style="border: none;" 
              variant="outline-info" 
              class="mb-2"
              :to="{name: 'tree-of-life', params: {node: taxonName}}">
                <b-icon icon="diagram3" variant="outline-info"></b-icon>      
            </b-button>
            <b-popover target="popover-table-target" triggers="hover" placement="top" variant="info">
                See selected species in tree mode
            </b-popover>
             </div>
            </div>
            <div>
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
            </div>
      <b-table 
        id="taxon-table"
        sticky-header="600px"
        head-variant="light"
        :items="taxons"
        :busy.sync="isBusy"
        :fields="fields"
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
      <!-- <b-pagination
        v-model="currentPage"
        :total-rows="totalRows"
        :per-page="perPage"
        aria-controls="taxon-table"
        ></b-pagination> -->
      </b-col>
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
      rawTaxons: [],
      taxonName: "",
      fields: ["tax_id", "name", { key: 'actions', label: '' }],
      selectMode:"single",
      currentPage: 1,
      currentModalPage: 1,
      perPage: 1000000,
      filter: null,
      filterOn: [],
      files: null,
      isBusy: false,
      toTreeLife: false,
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
            this.rawTaxons = response.data
            //filter taxon to display
            this.taxons = this.rawTaxons.filter(taxon => taxon.has_files)
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
          if (this.filter.length > 3){
            this.taxonName = this.filter.charAt(0).toUpperCase() + this.filter.slice(1)
            console.log(this.taxonName)
            let index = this.rawTaxons.filter(taxon => taxon.name === this.taxonName)
            console.log(index)
            if (index.length > 0){
              this.toTreeLife = true;
            }
          }
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
