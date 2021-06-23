<template>
    <b-container>
    <page-heading-component :header="header"></page-heading-component>
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
import{ treeData } from '../newickFile'

export default {
    name: 'gene-prediction',
    data() {
        return {
            header: config.resources.genePDescription,
            treeData: treeData
        }
    },
    mounted(){

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
    max-height: 400px;
    overflow: scroll;
}
</style>
