<template>   
<GenomeBrowserComponent></GenomeBrowserComponent>
</template>

<script>
import GenomeBrowserComponent from '../components/GenomeBrowserComponent.vue'

export default {
  name: "genome-page",

  components: {
      GenomeBrowserComponent
  },

    mounted () {
    // var json = [[16857,170055,1],[170080,200055,-1]];
    // var canvas = document.getElementById('canvas');
    // this.scribl = Scrible;
    // Create Chart
    // var chart = new this.scribl.Scribl(canvas,250);
    // let sum = 0
    // json.forEach(function (item) {
    //     sum++;
    //     addGene args: position,length,strand
    //         let gene = chart.addGene(item[0],item[1]-item[0],item[2].toString().substr(0,1) === '1' ? 
    //         "+":"-");
    //         gene.name = "gene_" + sum.toString();
    //         });
    //         console.log(gene);
    // Draw Chart
    // chart.scale.min = 0;
    // chart.scale.max = 200000;
    // chart.tick.major.size = 300000;
    // chart.scrollable = true;
    // chart.scrollValues = [15000, 250000];
    // chart.draw();

    // Create image of chart1
    // var img = chart.canvas.toDataURL("image/png");
    // Add link to download image
    // document.getElementById('export').href = img;
  }

};
</script>

<style>
/* #canvas {
    width: inherit;
    height: inherit;
} */
</style>