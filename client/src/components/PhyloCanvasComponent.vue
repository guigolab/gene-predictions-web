<template>
<div id="phylocanvas" @click="toggleNode" ></div>
</template>
<script>
import PhyloCanvas from 'phylocanvas';
import 'phylocanvas/polyfill';
import newick from '../newickFile'
export default {
    name: "phylocanvas",
    data() {
        return {
            newick:newick,
            selected: [],
            width: 400,
            height: 8000,
            tree: Object
        }
    },
    methods: {
        toggleNode(){
            // let selectedNodes = this.tree.getSelectedNodeIds();
            // this.tree.fitInPanel(this.tree.findLeaves(this.tree.leaves));
            this.tree.branches.root.collapsed = false;
            this.tree.zoom = 1.5;
            
            this.tree.setSize(250,1000);
            // this.tree.alignLabels = true;
            // console.log(this.tree.lineWidth)
            Object.entries(this.tree.branches).forEach(([key,value]) => {

                if (value.selected.includes(key)){
                    console.log(this)
                    // value.branchLength = 1;
                    value.collapsed = false;
                    value.drawBranchLabels();
                    // value.drawLabel();
                    // console.log(value.totalBranchLength)
                }
            });
            // this.tree.resizeToContainer();
                // if (item.id === this.tree.branches.root.id){
                //     // item.collapsed = true;
                //     console.log(item)
                // }
            
            // this.tree.branches.entries.forEach(item => {
            //     console.log(item);
            // });

            // this.tree.getSelectedNodeIds().array.forEach(element => {
            //     console.log(this.tree.branches)
            // });

        },
        // onHover() {
        //     Object.entries(this.tree.branches).forEach(([key,value]) => {

        //         // if (true){
        //             console.log(key)
        //             // value.branchLength = 1;
        //             // value.collapsed = false;
        //             // value.drawBranchLabels();
        //             // value.drawLabel();
        //             this.tree.tooltip.createContent(key)
        //             console.log(value.getChildProperties('label'))
        //         // }
        //      });

        // }

    },
    mounted() {
        this.tree = PhyloCanvas.createTree('phylocanvas', {"height": this.height, "width": this.width, "zoom": 3});
        this.tree.setTreeType('rectangular'); // Supported for rectangular, circular, and hierarchical tree types
        this.tree.defaultCollapsed = {"min": 0, "max": 100};
        this.tree.shiftKeyDrag = true;
        this.tree.disableZoom = true;
        this.tree.zoom = 1.5;
        this.tree.setSize(500,400);
        this.tree.load(this.newick, {format:"newick"});
        this.tree.hoverLabel = true;
        this.tree.branchScalar = 40;

        // tree.branches.root.collapsed=true;
        // tree.zoom = 3;
    }
}
</script>
<style>
</style>