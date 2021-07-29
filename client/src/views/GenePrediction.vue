<template>
    <b-container>
    <page-heading-component :header="header"></page-heading-component>
    <p>The predictions available on this page have been obtained by using the gene-finding software <b-link to="/geneid">geneid</b-link> and <b-link to="/sgp2">SGP2</b-link>. SGP2 combines geneid predictions with tblastx comparison of a query genome from one species (i.e. human) against an informant genome of another species (i.e. from mouse). </p>
      <b-row>
        <b-col cols="6" md="4" >
            <h3>Phylogenetic Tree</h3>
            <div class="tree-viewer">
            <TreeView class="item" :item="treeData"></TreeView>
            </div>
        </b-col>
        <b-col cols="12" md ="8">
        <h3>Available precomputed whole-genome prediction data sets</h3>
        <div>
            <taxon-component></taxon-component>
        </div>
        </b-col>
      </b-row>
    </b-container>
</template>

<script>
import PageHeadingComponent from '../components/PageHeadingComponent.vue';
import TaxonComponent from '../components/TaxonComponent.vue';
import TreeView from '../components/TreeViewComponent.vue'
import config from '../static-config'
import TaxonNodeDataService from "../services/TaxonNodeDataService";

export default {
    name: 'gene-prediction',
    data() {
        return {
            header: config.resources.genePDescription,
            treeData: Object
        }
    },
    methods: {
           retrieveTaxons() {
        TaxonNodeDataService.getAll()
            .then(response => {
            this.treeData = response.data[0];
            this.treeData.isOpen = false;
            })
            .catch(e => {
            console.log(e);
            });
        },
    },
    mounted(){
        this.retrieveTaxons()
        // this.test_get()
    },
    components: {
        PageHeadingComponent,
        TaxonComponent,
        TreeView
    }
};
</script>
<style>
.tree-viewer {
    max-height: 600px;
    overflow: scroll;
}
h3 {
margin-bottom: 50px!important;
}
</style>
