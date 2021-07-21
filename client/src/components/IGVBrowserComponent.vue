<template>
<b-container fluid="xl">
    <b-row>
    <b-col>
        <div id="igv-div"></div>
    </b-col>
    </b-row>
</b-container>
</template>

<script>

import igv from 'igv'


export default {
  name: "igv-browser",
  props: ['tracks'],
  methods: {
  },
  mounted(){
    var igvDiv = document.getElementById("igv-div");
      var options =
        {
            genome: "hg38",
            locus: "chr8:127,736,588-127,739,371",
            tracks: this.tracks
            //  [
            //     {
            //         "name": "HG00103",
            //         "url": "https://s3.amazonaws.com/1000genomes/data/HG00103/alignment/HG00103.alt_bwamem_GRCh38DH.20150718.GBR.low_coverage.cram",
            //         "indexURL": "https://s3.amazonaws.com/1000genomes/data/HG00103/alignment/HG00103.alt_bwamem_GRCh38DH.20150718.GBR.low_coverage.cram.crai",
            //         "format": "cram"
            //     }
            // ]
        };

        igv.createBrowser(igvDiv, options)
                .then(function () {

                    console.log("Created IGV browser");
                })
          }
};
</script>

<style>
 
</style>