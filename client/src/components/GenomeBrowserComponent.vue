<template>
<b-container>
    <b-row>
    <b-col class="col-container">
        <canvas id="canvas" width="940px" height="400px" style="margin-left:auto; margin-right:auto"></canvas>  
    </b-col>
    </b-row>
</b-container>
</template>

<script>

import Scrible from 'scribl';
// import taxonFileService from "../services/TaxonFileService";

export default {
  name: "genome-browser",
  props: ['tracks'],
  methods: {
  },
  mounted(){
        var canvas = document.getElementById('canvas');
        this.scribl = Scrible;
        var chart = new this.scribl.Scribl(canvas,600);
        var chartGenes = [];
        this.tracks.forEach(function (item) {
            console.log(item.id)
            let gene = chart.addGene(item.start,item.end - item.start, item.strand.toString().substr(0,1) === '1' ? "+":"-")
            // let gene = chart.addGene(item.start,item[1]-item[0],item[2].toString().substr(0,1) === '1' ? 
            // "+":"-");
            gene.name = item.id;
            gene.onMouseOver = gene.name
            chartGenes.push(gene)

        });
        //Draw Chart
        // chart.laneSizes = 30;
        chart.scrollable = true;
        chart.scrollValues = [100, 25000];
        chart.draw();
            // Create image of chart1
            // var img = chart.canvas.toDataURL("image/png");
            // Add link to download image
            // document.getElementById('export').href = img;
          }
};
</script>

<style>
   #scribl-zoom-slider {
    width: 4px;
}

#scroll-wrapper{
    width: inherit!important;
}
/* .col-container > div */
/* #canvas {
    width: inherit;
    height: inherit;
} */
</style>