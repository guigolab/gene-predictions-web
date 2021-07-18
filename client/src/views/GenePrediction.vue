<template>
    <b-container>
    <page-heading-component :header="header"></page-heading-component>
    <p>The predictions available on this page have been obtained by using the gene-finding software <b-link to="/geneid">geneid</b-link> and <b-link to="/sgp2">SGP2</b-link>. SGP2 combines geneid predictions with tblastx comparison of a query genome from one species (i.e. human) against an informant genome of another species (i.e. from mouse). </p>
      <b-row>
        <b-col cols="6" md="4" class="tree-viewer">
            <div class="list row shadow p-3">
            <h4>Phylogenetic Tree</h4>
            <TreeView class="item" :item="treeData"></TreeView>
            <!-- <PhyloGramComponent> </PhyloGramComponent> -->
            <!-- <PhyloCanvasComponent> </PhyloCanvasComponent> -->
            <!-- <PhyloGeneticTree> </PhyloGeneticTree> -->
            </div>
        </b-col>
        <b-col cols="12" md ="8">
            <taxon-component></taxon-component>
        </b-col>
      </b-row>
    </b-container>
</template>

<script>
import PageHeadingComponent from '../components/PageHeadingComponent.vue';
import TaxonComponent from '../components/TaxonComponent.vue';
import TreeView from '../components/TreeViewComponent.vue'
// import PhyloCanvasComponent from '../components/PhyloCanvasComponent.vue'
// import PhyloGramComponent from '../components/PhyloGramComponent.vue'
// import PhyloGeneticTree from '../components/PhylogeneticTreeComponent.vue'
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
            console.log(this.treeData)
            })
            .catch(e => {
            console.log(e);
            });
        },
    },
    mounted(){
        this.retrieveTaxons()

    },
    components: {
        PageHeadingComponent,
        TaxonComponent,
        TreeView,
        // PhyloGramComponent,
        // PhyloGeneticTree,
        // PhyloCanvasComponent,
    }
};
</script>
<style>
.tree-viewer {
    max-height: 600px;
    overflow: scroll;
}
</style>
