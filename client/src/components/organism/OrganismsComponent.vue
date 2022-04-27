<template>
    <b-container class="router-container" fluid>
      <tree-bread-crumb-component/>
      <filter-component :filter="filter" :placeholder="'Search in ' + taxName"/>
      <div ref="organismsTable">
      <table-component 
        :items="organismsProvider"
        :busy.sync="isBusy"
        :filter="filter"
        :fields="organismFields"
        :current-page="currentPage"
        :per-page="perPage"
        :primary-key="'id'"
        :custom-fields="customFields"
        :id="tableId"
        :sticky-header="stickyHeader"
        :selectable="hasToken"
        :selectMode="'multi'"
        
        >
        <!-- <template #head(param)>
          <b-badge variant="warning">ParamFiles</b-badge>
        </template> -->
        <template #head(gff)>
          <b-badge variant="primary">Annotations</b-badge>
        </template>
        <template #head(fasta)>
          <b-badge variant="success">Genomes</b-badge>
        </template>
        <template #cell(name)='data'>
          <b-link :to="{name: 'organism-details', params: {name: data.item.name}}">
            {{data.item.name}}
          </b-link>
        </template>
        <!-- <template #cell(param)="data">
            <b-badge style="cursor:pointer" v-if="data['item'].param_files.length" @click.stop="getFiles(data['item'], 'param_files')" pill variant="warning">{{data['item'].param_files.length}}</b-badge>
        </template> -->
        <template #cell(gff)="data">
            <b-badge style="cursor:pointer" v-if="data['item'].annotations.length" @click.stop="getFiles(data['item'], 'annotations')" pill variant="primary">{{data['item'].annotations.length}}</b-badge>
        </template>        
        <template #cell(fasta)="data">
            <b-badge style="cursor:pointer" v-if="data['item'].genomes.length" @click.stop="getFiles(data['item'], 'genomes')" pill variant="success">{{data['item'].genomes.length}}</b-badge>
        </template>
      </table-component>
      </div>
      <pagination-component :per-page="perPage" :page-options="pageOptions" :total-rows="totalRows" :current-page="currentPage" :table-id="tableId"/>
    <file-list-modal :data="data" :model="model" :organism="organism" />
    </b-container>
</template>

<script>
import portalService from "../../services/DataPortalService"
import {BBadge,BLink } from 'bootstrap-vue'
import TableComponent from '../base/TableComponent.vue';
import FilterComponent from '../base/FilterComponent.vue';
import PaginationComponent from '../base/PaginationComponent.vue';
import {mapFields} from '../../utils/helper'
import TreeBreadCrumbComponent from '../taxon/TreeBreadCrumbComponent.vue';
import FileListModal from '../modal/FileListModal.vue';

export default {
  components: 
    {
      BBadge,TableComponent,PaginationComponent,FilterComponent,
      TreeBreadCrumbComponent,FileListModal,
      BLink
    },

  computed: {
    ...mapFields({
      fields: ['filter','perPage', 'taxName','totalRows','currentPage'],
      module: 'portal',
      mutation: 'portal/setField'      
    }),
    organismFields(){
      return this.fields
    },
  },
  data() {
    return {
      tableId:'organisms-table',
      pageOptions: [20,50,100],
      isBusy: false,
      stickyHeader: '70vh',
      fields: [
        {key: 'actions', label:''},
        {key: 'taxid', label: 'TaxId',sortable: true},
        {key: 'name',label:'Name',sortable: true},
        {key: 'common_name', label:'Common name', sortable: true},
        // {key: 'param'},
        {key: 'gff'},
        {key: 'fasta'}
      ],
      organism: null,
      model: '',
      data:[]
    }
  },
  methods: {
    filterSearch(params,callback){
      portalService.getFilteredOrganisms(params).then(response => {
        this.totalRows = response.data.total
        const items = Object.freeze(response.data.data)
        callback(items)
        })
        .catch(() => {
        callback([])
        })
      return null
    },
    defaultSearch(params,callback){
      portalService.getOrganisms(params).then(response => {
          this.totalRows = response.data.total
          const items = Object.freeze(response.data.data)
          callback(items)
        }).catch(() => {
        callback([])
        })
      return null
    },
    organismsProvider(ctx,callback){
      const fromParam = (ctx.currentPage - 1) * ctx.perPage
      if(ctx.filter){
        const params = {filter: ctx.filter,from: fromParam, size: ctx.perPage,sortColumn: ctx.sortBy, sortOrder: ctx.sortDesc,taxName: this.taxName}
        this.filterSearch(params,callback)          
      }
      else {
        const params = {offset: fromParam , limit: ctx.perPage, sortColumn: ctx.sortBy, sortOrder: ctx.sortDesc,taxName: this.taxName}
        this.defaultSearch(params,callback)
      }
    },
    getFiles(organism, model){
      this.$store.dispatch('portal/showLoading')
      portalService.getFiles(model,{taxid:organism.taxid})
      .then(response => {
        this.data = response.data
        this.model = model
        this.organism = organism.name
        this.$bvModal.show('data-modal')
        this.$store.dispatch('portal/hideLoading')
      })
      .catch(e => {
        console.log(e)
         this.$store.dispatch('portal/hideLoading')
      })
    },
  
  }
}
</script>
<style>
.link-badge{
  margin-right:5px
}
</style>