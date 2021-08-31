<template>
      <b-col>
        <b-container fluid>
          <b-row>
            <b-col> 
              <div style="display:flex;margin-bottom:15px;">
            <h5>Available prediction sets {{filter? "under "+ filter +": "+totalRows:taxons.length}}</h5>
            <div v-if="toTreeLife">
            <b-button id="popover-table-target"
            style="margin-left:5px;"
            pill
              variant="outline-info" 
              class="mb-2"
              :to="{name: 'tree-of-life', params: {node: taxonName}}">
                <!-- <b-icon icon="diagram3" variant="outline-info"></b-icon> -->
                tree of life view      
            </b-button>
            <!-- <b-popover target="popover-table-target" triggers="hover" placement="top" variant="info">
                See selected species in tree mode
            </b-popover> -->
             </div>
            </div>
            </b-col>
          </b-row>
          <b-row>
            <b-col>
            <div style="margin-bottom:15px;">
            <b-form-group
            label-align="right"
            >
            <b-input-group>
                <b-form-input ref="filter"
                id="filter-input"
                v-model="filter"
                type="search"
                placeholder="Type to search a species,class etc.."
                >
            </b-form-input>
            <b-input-group-append>
              <b-button :disabled="!filter" @click="filter = ''">Clear</b-button>
            </b-input-group-append>
            </b-input-group>
            </b-form-group>
            </div>
            </b-col>
          </b-row>
        </b-container>
        
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
        :select-mode="selectMode"
        selectable
        @row-selected="info"
      >
       <!-- <template #cell(actions)="row">
            <b-button size="sm" @click="info(row.item, row.index, $event.target)" class="mr-1">
            Show Files
            </b-button>
        </template> -->
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
      fields: ["tax_id", "name", {key:'tax_class',label: 'Class'},"kingdom",{ key: 'actions', label: '' }],
      selectMode:"single",
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
       info(item) {
         if(item.length>0){
        taxonFileService.getAll(item[0].tax_id)
            .then(response => {
            this.files  = response.data;
            this.taxonName = item[0].name;
            const el = document.getElementById(this.taxonName);
            if(el){
              Array.from(document.querySelectorAll('.highlight')).forEach((el) => el.classList.remove('highlight'));
              el.scrollIntoView({behavior: "smooth"});
              el.classList.add("highlight")
            }   
            console.log(item)
            
            })
            .catch(e => {
            console.log(e);
            });
        this.$root.$emit('bv::show::modal', 'file-list-modal')
        }},
        onFiltered(filteredItems) {
          if (this.filter.length > 3){
            this.taxonName = this.filter.charAt(0).toUpperCase() + this.filter.slice(1)
            const el = document.getElementById(this.taxonName);
            if(el){
              Array.from(document.querySelectorAll('.highlight')).forEach((el) => el.classList.remove('highlight'));
              el.scrollIntoView({behavior: "smooth"});
              el.classList.add("highlight")
            }   
            let index = this.rawTaxons.filter(taxon => taxon.name === this.taxonName)
            if (index.length > 0 && filteredItems.length > 1){
              this.toTreeLife = true;
            }else {
              this.toTreeLife = false;
            }
          }else {
              this.toTreeLife = false;
            }
        // Trigger pagination to update the number of buttons/pages due to filtering
        this.totalRows = filteredItems.length
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
.highlight {
  background-color: springgreen;
}
/* #filter-bar {
    flex-direction: row-reverse;
} */
</style>
