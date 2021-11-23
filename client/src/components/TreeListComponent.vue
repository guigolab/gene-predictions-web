<template>
<div>
<li class="tree-container" :id="item.name">
    <div v-if="item.name !== 'Eukaryota'">
        <div class="node-wrapper">
            <div @click="toggle(item)" class="d-flex justify-content-between align-items-center node-container">
                <b-icon v-if="isFolder" :icon="item.isOpen?'slash-circle':'plus-circle'" font-scale="1" :rotate="item.isOpen?'45':'0'"></b-icon>
                <div  :class="{bold: isFolder}" style="margin-left: 2px">
                {{item.name}}
                </div>
                <div style="display:contents" v-if="isFolder">
                    <b-link style="margin-right: 5px" :to="{name: 'tree-of-life', params: {node: item.name}}">
                        <b-icon icon='diagram3' font-scale="1"></b-icon>
                    </b-link>
                    <b-badge @click="toTable(item.name)" variant="success" pill>{{item.leaves}} </b-badge>
                </div>
            </div>
        </div>
    </div>
    <ul v-show="item.isOpen" v-if="isFolder">
    <tree-list
        class="item"
        v-on:clicked="onChildClicked"
        v-on:selected-organism="onOrganismSelected"
        v-for="(child, index) in item.children"
        :key="index"
        :item="child"
    ></tree-list>
    </ul>   
</li>
</div>
</template>
<script>
import treeService from "../services/TreeService"
import organismDataService from '../services/OrganismsDataService'

export default {
    name: 'tree-list',
    props:['item'],
    data(){
        return {
            organism:Object,
            selected: false
        }
    },
    computed: {
          isFolder() {
            return this.item.children && this.item.children.length;
          },
          isOpen() {
            return this.item.isOpen
          }
        },
    methods: {
        toggle(item) {
            if (this.isFolder) {
                if (!item.children.some(child => child.name)){
                    treeService.getChildren(item.name)
                    .then(response => {
                    if(response.data['children'].length > 0) {
                        this.item.children = response.data['children'].map(child => {
                            let taxChild = JSON.parse(child);
                            taxChild.isOpen = false;
                            return taxChild
                        })
                    } 
                    })
                    .catch(e => {
                    console.log(e);
                    });
                }
                this.item.isOpen = !this.item.isOpen
            }
            else {
            organismDataService.getOrganism(item.name).then(response => {
              this.organism = response.data
              this.$emit('selected-organism', this.organism)
            }
            ).catch(e => {
                  console.log(e);
              });
             }
            },
        toTable(name) {
            this.$emit('clicked', name)     
        },
        onChildClicked(value){
            this.$emit('clicked', value)
        },
        onOrganismSelected(organism){
            this.$emit('selected-organism', organism)
        }
    },
}
</script>
<style scoped>

.item {
  cursor: pointer;
  list-style-type: none;
}
.bold {
  font-weight: bold;
  width: 100%;
}
.node-container {
    background-color: rgb(233, 236, 239);
    padding: 10px;
    margin: 5px;
}
#tree-leaves-button {
    margin-left: 3px;
}

</style>