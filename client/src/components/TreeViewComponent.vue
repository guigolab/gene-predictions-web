<template>
        <li class="tree-container" :id="item.name">
            <div v-if="item.name !== 'root'" class="node-container">
            <!-- <div @click="toggle" :class="{bold: isFolder}"> -->
            <div @click="toggle" :class="{bold: isFolder}">
            {{item.name}}
            <!-- <b-icon v-if="isFolder" :icon="item.isOpen ? 'chevron-double-down': 'chevron-double-right' " variant="outline-info"></b-icon> -->
            </div> 
            <b-button v-if="isFolder" id="tree-leaves-button" pill variant="outline-secondary" size="sm" @click="toTable"> {{item.leaves}} </b-button>
             <!-- <b-popover target="tree-leaves-button" triggers="hover" placement="top" variant="info">
                {{item.name}}
            </b-popover> -->
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
/* ul { */
  /* padding-left: 0.25em;
  line-height: 1.5em;
  list-style-type: none; */
/* } */
ul {
  margin: 0px 0px 0px 0px;
  list-style: none;
   padding-left: 0.5em;
  line-height: 2em;
  font-family: Arial;
}
ul li {
  font-size: 16px;
  position: relative;
}
ul li:before {
  position: absolute;
  left: -15px;
  top: -17px;
  content: "";
  display: block;
  border-left: 3px solid #17a2b8;
  height: 1em;
  border-bottom: 3px solid #17a2b8;
  width: 15px;
  height: 33px;
}
ul li:after {
  position: absolute;
  left: -15px;
  bottom: -7px;
  content: "";
  display: block;
  border-left: 3px solid #17a2b8;
  height: 100%;
}
ul li.root {
  margin: 0px 0px 0px 0px;
}
ul li.root:before {
  display: none;
}
ul li.root:after {
  display: none;
}
ul li:last-child:after {
  display: none;
}
</style>