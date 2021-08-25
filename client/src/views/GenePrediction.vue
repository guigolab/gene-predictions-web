<template>
    <b-container>
    <page-heading-component :header="header"></page-heading-component>
    <p>The predictions available on this page have been obtained by using the gene-finding software <b-link to="/geneid">geneid</b-link> and <b-link to="/sgp2">SGP2</b-link>. SGP2 combines geneid predictions with tblastx comparison of a query genome from one species (i.e. human) against an informant genome of another species (i.e. from mouse). </p>
      <b-row>
        <b-col cols="6" md="4" >
            <div style="display:flex;margin-bottom:15px;">
            <h3>Phylogenetic Tree</h3>
            <b-button id="popover-tree-target" style="border: none;" variant="outline-info" class="mb-2">
                <b-icon icon="info-circle-fill" variant="outline-info"></b-icon>      
            </b-button>
            <b-popover target="popover-tree-target" triggers="hover" placement="top" variant="info">
                click over a node to open it, click the button to view children in table
            </b-popover>
            </div>
            <div class="tree-viewer">
            <TreeView class="item" v-if="treeData" :item="treeData"></TreeView>
            <div v-else>
            <b-icon icon="arrow-clockwise" animation="spin" font-scale="4"></b-icon>
            </div>
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
import treeService from "../services/TreeService"

export default {
    name: 'gene-prediction',
    data() {
        return {
            header: config.resources.genePDescription,
            treeData: null,
        }
    },
    methods: {
           getTree() {
        treeService.getTree('root')
            .then(response => {
            this.treeData = response.data[0];
            })
            .catch(e => {
            console.log(e);
            });
        },
    },
    mounted(){
        this.getTree()
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
    max-height: 50%;
    overflow: scroll;
}
/* h3 {
margin-bottom: 50px!important;
} */
</style>
