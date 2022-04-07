<template>
<b-container fluid="xl">
    <b-row>
    <b-col>
        <div ref="igvdiv" id="igv-div"></div>
    </b-col>
    </b-row>
</b-container>
</template>

<script>


import igv from 'igv'
import taxonFileService from '../services/TaxonFileService'

export default {
  name: "igv-browser",
  data(){
      return {
          fastaURL: null,
          indexUrl: null,
          tracks: []
      }
  },
  mounted(){
    // var igvDiv = document.getElementById("igvdiv");
    taxonFileService.download('GCA_000180735.1.fasta.gz')
    .then(response => {
        console.log(response.data)
        this.fastaURL = response.data
    })
    .then(() => {
        return taxonFileService.download('/home/gff3files/tetraodon_nigroviridis.no_extra_evidence.gff3')
    })
    .then(response => {
        console.log(response.data)
        this.tracks.push(response.data)
    })
    const igvDiv = this.$refs.igvdiv
    
    //   var options =
    //     {
    //         genome: "hg38",
    //         locus: "chr8:127,736,588-127,739,371",
    //         tracks: 
    //          [
    //             {
    //                 "url": "http://ftp.ensembl.org/pub/current_fasta/aquila_chrysaetos_chrysaetos/dna_index/Aquila_chrysaetos_chrysaetos.bAquChr1.2.dna.toplevel.fa.gz",
    //                 "indexURL": "http://ftp.ensembl.org/pub/current_fasta/aquila_chrysaetos_chrysaetos/dna_index/Aquila_chrysaetos_chrysaetos.bAquChr1.2.dna.toplevel.fa.gz.fai",
    //             }
    //         ]
    //     };
    //data:application/gzip;base64,

        igv.createBrowser(igvDiv, {reference: {
            "id": "bAquChr1.2",
            "name": "bAquChr1.2",
            "fastaURL": this.fastaURL,
            "indexURL": this.indexURL,
            // "cytobandURL": "https://s3.amazonaws.com/igv.broadinstitute.org/annotations/hg38/cytoBandIdeo.txt",
            "tracks": this.tracks
            //  [
            // {
            //     "name": "Primary assembly",
            //     "url": "http://ftp.ensembl.org/pub/current_gff3/aquila_chrysaetos_chrysaetos/Aquila_chrysaetos_chrysaetos.bAquChr1.2.105.primary_assembly.Z.gff3.gz",
            //     // "order": 1000000,
            //     "indexed": false
            // }
            // ]
        }})
                .then(function () {

                    console.log("Created IGV browser");
                })
          }
};
</script>

<style>
 
</style>