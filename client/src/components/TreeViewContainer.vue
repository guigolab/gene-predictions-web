<template>
    <b-col cols="3">
        <b-overlay :show="show">
            <div class="tree-viewer"> 
                <TreeList v-on:selected-organism="onOrganismSelected" v-on:clicked="onChildClicked" class="item" v-if="treeData" :item="treeData"></TreeList>
            </div> 
        </b-overlay>
    </b-col>
</template>
<script>
import treeService from "../services/TreeService"
import TreeList from "./TreeListComponent.vue"

export default {
    data(){
        return {
            treeData: null,
            taxName: '',
            show:false
        }
    },
    methods: {
        getTree() {
            this.show = true
            treeService.getChildren('Eukaryota')
                .then(response => {
                this.treeData = response.data
                this.treeData.isOpen = true
                this.show=false
                this.treeData.children = this.treeData.children.map(child => {
                let taxChild = JSON.parse(child);
                taxChild.isOpen= false
                return taxChild
                    })
                })
                .catch(e => {
                console.log(e);
                });
        },
        onChildClicked(value){
            this.$emit('clicked',value)
        },
        onOrganismSelected(organism){
            this.$emit('selected-organism', organism)
            }
    },
    created(){
        this.getTree()
    },
    components:{
    TreeList,
  }
}
</script>
<style scoped>
.tree-viewer {
    width: 100%;
    height: 75vh;
    display: inline-block;
    overflow: auto;
    padding: 15px;
}
</style>