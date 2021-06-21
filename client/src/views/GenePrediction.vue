<template>
    <b-container>
    <page-heading-component></page-heading-component>
      <b-row>
        <b-col cols="6" md="4" class="tree-viewer">
            <PhyloCanvasComponent></PhyloCanvasComponent>
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
import PhyloCanvasComponent from '../components/PhyloCanvasComponent.vue'
// import PhyloGram from '../components/PhyloGramComponent.vue'
// import PhyloGeneticTree from '../components/PhylogeneticTreeComponent.vue'
export default {
    name: 'gene-prediction',
    components: {
        // PhyloCanvasComponent,
        PageHeadingComponent,
        TaxonComponent,
        PhyloCanvasComponent
    }
};
</script>
<style>
.tree-viewer {
    max-height: 400px;
    overflow: scroll;
}
</style>
