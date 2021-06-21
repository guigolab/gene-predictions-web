<template>
    <section class="section">
      <div class="container">
        <div class="tree-container" style="">
        <svg id="tree_display" style=""></svg>
        </div>
      </div>
    </section>
</template>

<script>
import { phylotree } from "phylotree";
import "phylotree/build/phylotree.css";
import newick from '../newickFile'

export default {
  name: "PhyloGeneticTree",

  mounted (){
    var example_tree = newick.newick;
    // tree from Yokoyama et al http://www.ncbi.nlm.nih.gov/pubmed/18768804
    let tree = new phylotree(example_tree, {alignTips:'right'});
    // console.log(tree.alignTips);
    const height = 1000;
    const width = 300;
    const alignTips = "right";
    let svg = document.createElement('div');
    svg.setAttribute('id', 'tree_display');
    document.body.appendChild(svg);
    this.rendered_phylotree = tree.render(
        '#tree_display', {
            height:height,
            width:width,
            'left-right-spacing': 'fit-to-size', 
            'top-bottom-spacing': 'fit-to-size',
            'overflow': 'visible',
            alignTips:alignTips
        }
    );
    console.log(this.rendered_phylotree.phylotree.nodes.data.children);
    this.rendered_phylotree.phylotree.nodes.data.children.forEach(node => {
        node.annotation = node.name;
    });
    console.log(this.rendered_phylotree)
    this.rendered_phylotree.links.forEach(d => {

    // TODO: Move away from storing attribute data as root (BREAKS occasionally with d3>3)
    if(d.target.data.annotation) {
      // console.log(d)
      d.target[d.target.data.annotation] = d.target.data.annotation;
    }

  });
    // this.rendered_phylotree.getNodes();
    this.rendered_phylotree.options.alignTips = 'right';
    this.rendered_phylotree.alignTips = 'right';
    // console.log(this.rendered_phylotree.alignTips);
  }
};
</script>

<style scoped>
#spaced {
  letter-spacing: 3px;
}
.section {
  padding: 1.5rem 1.5rem;
  overflow:hidden;
}
#tree_display {
  height:1100px;
}
/* .tree-container {
  width: 25%;
  height: 25%;
} */
.container {
  overflow: inherit;
}
</style>