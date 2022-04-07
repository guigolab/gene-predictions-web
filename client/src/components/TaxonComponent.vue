<template>
      <b-col cols="9">
        <b-container fluid>
          <b-row>
            <b-col> 
              <div style="display:flex;margin-bottom:15px;">
            <!-- <h3>Number of species {{filter? "under "+ filter +": "+totalRows:taxons.length}}</h3> -->
            <div>
              <b-button v-if="taxName" 
              @click="taxName=''"
              style="margin-left:5px;"
              pill 
              class="mb-2">
                <b-icon icon="x-circle"></b-icon> {{taxName}} 
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
                placeholder="Search an organism"
                >
            </b-form-input>
            <b-input-group-append>
              <b-button :disabled="!filter" @click="filter = ''">Clear</b-button>
            </b-input-group-append>
            <!-- <label for="param-select">Tracking status</label>
            <b-form-select id="param-select"
                v-model="seqStatus"
                  class="mb-3"
                  :options="seqOptions"
              >
            </b-form-select> -->
            </b-input-group>
            <!-- <b-form-select
            id="sort-by-seq-status"
            v-model="sortBy"
            :options="seqStatus"
            :aria-describedby="ariaDescribedby"
            class="w-75"
            >
            <template #first>
            <option value="">-- none --</option>
            </template>
            </b-form-select> -->
            </b-form-group>
            </div>
            </b-col>
          </b-row>
        </b-container>
        <b-row>
        <b-col>
      <b-table 
        id="taxon-table"
        sticky-header="65vh"
        head-variant="light"
        ref="organismTable"
        :items="organismsProvider"
        :busy.sync="isBusy"
        :filter-ignored-fields="ignoredFields"
        :filter="filter"
        :filter-included-fields="filterOn"
        :sort-direction="sortDirection"
        :fields="fields"
        :current-page="currentPage"
        :per-page="perPage"
        show-empty
        :select-mode="selectMode"
        selectable
        small
        @row-selected="selectedItem"
        primary-key="id"
      >
      <template #cell(sequencing_status)="data">
        <b-badge pill :variant="colorOptions[data.item.sequencing_status]">{{data.item.sequencing_status}}</b-badge>
      </template>
      </b-table>
      </b-col>
      </b-row>
      <b-row>
      <b-col sm="5" md="6" class="my-1">
        <b-form-group
          label="Per page"
          label-for="per-page-select"
          label-cols-sm="6"
          label-cols-md="4"
          label-cols-lg="3"
          label-align-sm="right"
          label-size="sm"
          class="mb-0"
        >
          <b-form-select
            id="per-page-select"
            v-model="perPage"
            :options="pageOptions"
            size="sm"
          ></b-form-select>
        </b-form-group>
      </b-col>
      <b-col sm="7" md="6" class="my-1">
        <b-pagination
          v-model="currentPage"
          :total-rows="totalRows"
          :per-page="perPage"
          align="fill"
          size="sm"
          class="my-0"
          aria-controls="taxon-table"
        ></b-pagination>
      </b-col>
      </b-row>
</template>

<script>
/// HOMEPAGE SHOULD DISPLAY SAMPLES RATHER THAN ABSTRACT ORGANISMS: A TABLE WITH ALL THE SAMPLES
import organismDataService from "../services/OrganismsDataService"
import taxonFileService from "../services/TaxonFileService";

export default {
  name: "taxon-list",
  props: ['taxName'],
  watch: {
    taxName: function() {
      this.$refs.organismTable.refresh()
    }
  },
  data() {
    return {
      organisms: [],
      rawTaxons: [],
      pageOptions: [20,50,100],
      isBusy: false,
      ignoredFields: ['metadata'],
      fields: [
        {key: 'tax_id', label: 'NCBI taxid',sortable: true},
        {key: 'name',label:'Species',sortable: true},
        {key:'common_name', label: 'Common name', sortable: true},
        // {key: 'kingdom',label:'Kingdom', sortable: true,
        // formatter: (value, key, item) => {
        // return item.lineage['kingdom']}, sortByFormatted: true},
        // {key: 'family',label:'Family', sortable: true, formatter: (value, key, item) => {
        // return item.lineage['family']},sortByFormatted: true},
        {key:"sequencing_status", label: 'Sequencing Status', sortable: true},
        {key:'target_list_status', label: 'Target List Status', sortable: true}],
      selectMode:"single",
      currentModalPage: 1,
      currentPage: 1,
      perPage: 20,
      filter: null,
      filterOn: [],
      files: null,
      toTreeLife: false,
      totalRows: 1,
      imageSrc: '',
      colorOptions: {
        insdc_open: 'success',
        insdc_submitted: 'info',
        in_assembly: 'primary',
        data_generation: 'warning',
        sample_acquired: 'secondary',
        no_info: 'light'        
      }
    };
  },
    methods: {
        organismsProvider(ctx,callback){
          const fromParam = (ctx.currentPage - 1) * ctx.perPage
          if(ctx.filter !== ''){
            const params = {filter: ctx.filter,from: fromParam, size: ctx.perPage,sortColumn: ctx.sortBy, sortOrder: ctx.sortDesc,taxName: this.taxName }
            organismDataService.getFilteredOrganisms(params).then(response => {
              this.totalRows = response.data.total
              const items = Object.freeze(response.data.data)
                  callback(items)
              }).catch(() => {
             callback([])
             })
            return null
            }
            else {
            const params = {offset: fromParam , limit: ctx.perPage, sortColumn: ctx.sortBy, sortOrder: ctx.sortDesc,taxName: this.taxName}
            organismDataService.getOrganisms(params).then(response => {
                  this.totalRows = response.data.total
                  const items = Object.freeze(response.data.data)
                  callback(items)
              }).catch(() => {
             callback([])
             })
            return null
          }
            },
        selectedItem(item) {
          console.log(item)
          if(item.length>0){
            taxonFileService.getAll({'taxId': item[0].taxonId})
            .then(response => {
              const files = response.data
              this.$emit('selected-organism', item[0].name, files)
            }
            ).catch(e => {
                  console.log(e);
              });
              }
          }
    },
};

</script>

<style>
/* .list {
  text-align: left;
  max-width: 750px;
  margin: auto;
}
.highlight {
  background-color: springgreen;
} */

</style>
