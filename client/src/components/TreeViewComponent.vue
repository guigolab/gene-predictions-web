<template>
        <li>
            <div
            :class="{bold: isFolder}"
            @click="toggle"
            >
            {{ item.name }}
            <span v-if="isFolder">[{{ isOpen ? '-' : '+' }}]</span>
            </div> 
            <ul v-show="isOpen" v-if="isFolder">
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
    props: {
     item: Object,
    },
    data(){
        return {
            // isOpen: false,
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
        // retrieveChildren() {
        // TaxonNodeDataService.getChildren(this.item.tax_id)
        //     .then(response => {
        //         console.log(response.data)
        //     return response.data;
        //     })
        //     .catch(e => {
        //     console.log(e);
        //     });
        // },
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
                    // else {

                    // this.item.children = [JSON.parse(response.data['children'])];
                    // }
                    })
                    .catch(e => {
                    console.log(e);
                    });
                
                // this.item.children.forEach(function (value) {
                //     console.log(this.item);
                //     });
                this.item.children.map(child => {
                    child.isOpen = false
                    })
                // if(this.item.isOpen){
                // }
                this.item.isOpen = !this.item.isOpen
            }
            if(!this.item.children){
                document.querySelector('#filter-input').value = this.item.name;
                document.querySelector('#filter-input').dispatchEvent(new Event("change"));
                console.log(document.querySelector('#filter-input'));
                // document.querySelector('#taxon-table').click();
            // document.querySelector('#filter-input').value = this.item.name //bad practice for sure
        }
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