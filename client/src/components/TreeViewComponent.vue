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
export default {
    name: 'tree-view',
    props: {
     item: Object,
    },
    data(){
        return {
            isOpen: false,
        }
    },
    computed: {
          isFolder() {
            return this.item.children && this.item.children.length;
          }
        },
    methods: {
        toggle() {
            if (this.isFolder) {
                this.isOpen = !this.isOpen;
            }
            if(!this.item.children){
                document.querySelector('#filter-input').value = this.item.name;
                document.querySelector('#filter-input').dispatchEvent(new Event("change"));
                console.log(document.querySelector('#filter-input'));
                // document.querySelector('#taxon-table').click();
            // document.querySelector('#filter-input').value = this.item.name //bad practice for sure
        }
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
ul {
  padding-left: 1em;
  line-height: 1.5em;
  list-style-type: none;
}
</style>