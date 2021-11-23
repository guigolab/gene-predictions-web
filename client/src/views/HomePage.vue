<template>
      <b-row>
            <b-row>
                <b-col>
                <b-button id="popover-table-target"
                    style="margin-left:5px;"
                    pill
                    variant="outline-success" 
                    class="mb-2"
                    :to="{name: 'tree-of-life', params: {node: 'Eukaryota'}}">
                    <!-- <b-icon icon="diagram3" variant="outline-info"></b-icon> -->
                    Phylogenetic Tree UI      
                    <b-icon icon='diagram3' font-scale="1"/>
                </b-button>
                </b-col>
            </b-row>
            <TreeViewContainer v-on:selected-organism="onOrganismSelected" v-on:clicked="onChildClicked"></TreeViewContainer>
            <TaxonComponent v-on:selected-organism="onOrganismSelected" :taxName="taxName"></TaxonComponent>
            <organism-info-modal :organism="organism" :files="files"/>
      </b-row>
</template>

<script>

import TaxonComponent from '../components/TaxonComponent.vue';
import TreeViewContainer from '../components/TreeViewContainer.vue'
import OrganismInfoModal from '../components/modal/OrganismInfoModal.vue'


export default {
    name: 'home-page',
    data() {
        return {
            treeData: null,
            taxName: '',
            organism:'',
            files:Array,
        }
    },
        methods: {
            onChildClicked(value){
                this.taxName = value
            },
            onOrganismSelected(name, files){
                this.organism = name
                this.files = files
                this.$root.$emit('bv::show::modal', 'organism-info-modal')
            },
    },
    components: {
        OrganismInfoModal,
        TaxonComponent,
        TreeViewContainer,
        }
    }
</script>
<style>
.tree-viewer {
    width: 100%;
    height: 70vh;
    display: inline-block;
    overflow: auto;
    padding: 15px;
}
</style>
