<template>
        <li class="tree-container">
            <div class="node-container">
            <div @click="toggle" :class="{bold: isFolder}">
            <b-icon v-if="isFolder" :icon="item.isOpen ? 'chevron-double-down': 'chevron-double-right' " variant="outline-info"></b-icon>
            <span> {{ item.name }}</span>
            </div> 
            <b-button v-if="isFolder" id="tree-leaves-button" pill variant="outline-secondary" size="sm" @click="toTable"> {{item.leaves}} </b-button>
            </div>
            <ul v-show="item.isOpen" v-if="isFolder">
            <tree-view
                class="item"
                v-for="(child, index) in item.children"
                :key="index"
                :item="child"
            ></tree-view>
            </ul>   
        </li>
</template>
<script>

// import TaxonNodeDataService from "../services/TaxonNodeDataService";

export default {
    name: 'tree-view',
    props:['item'],
    data(){
        return {
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
        toggle() {
            if (this.isFolder) {
                this.item.isOpen = !this.item.isOpen
            }
            else {
                document.querySelector('#filter-input').value = this.item.name;
                document.querySelector('#filter-input').dispatchEvent(new Event("change"));                           
            }
            },
        toTable() {
            document.querySelector('#filter-input').value = this.item.name;
            document.querySelector('#filter-input').dispatchEvent(new Event("change"));      
        }
    }
}
</script>
<style>
.item {
  cursor: pointer;
  list-style-type: none;
}
.bold {
  font-weight: bold;
}
.node-container {
    display: flex;
}
#tree-leaves-button {
    margin-left: 3px;
}
ul {
  padding-left: 0.25em;
  line-height: 1.5em;
  list-style-type: none;
}
</style>