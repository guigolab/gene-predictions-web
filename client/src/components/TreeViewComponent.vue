<template>
        <li class="tree-container">
            <div
            :class="{bold: isFolder}"
            @click="toggle"
            >
            {{ item.name }}
            <span v-if="isFolder">[{{ item.isOpen ? '-' : '+' }}]</span>
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

import TaxonNodeDataService from "../services/TaxonNodeDataService";

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
                TaxonNodeDataService.getChildren(this.item.tax_id)
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
                this.item.isOpen = !this.item.isOpen
            }
                if(this.item.has_files)
                document.querySelector('#filter-input').value = this.item.name;
                document.querySelector('#filter-input').dispatchEvent(new Event("change"));
                console.log(document.querySelector('#filter-input'));
    },
      
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
ul {
  padding-left: 0.25em;
  line-height: 1.5em;
  list-style-type: none;
}
</style>