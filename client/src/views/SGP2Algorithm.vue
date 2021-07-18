<template>
    <b-container>
            <page-heading-component :header="header"></page-heading-component>
            <p>sgp-2 is a program to predict genes by comparing anonymous genomic sequences from different species. It combines tblastx, a sequence similarity search program, with geneid, an "ab initio" gene prediction program (<b-link href="http://www.sanger.ac.uk/Software/formats/GFF/">http://www.sanger.ac.uk/Software/formats/GFF/</b-link>). In "assymetric" mode, genes are predicted in one sequence from one species (the target sequence), using a set of sequences (maybe only one) from the other species (the reference set). Essentially, geneid is used to predict all potential exons along the target sequence. Scores of exons are computed as log-likelihood ratios, function of the splice sites defining the exon, and of the coding bias in composition of the exon sequence as measured by a Markov Model of order five. From the set of predicted exons, geneid assembles the gene structure (eventually multiple genes in both strands) maximizing the sum of the scores of the assembled exons, using a dynamic programming chaining algorithm. When using a reference set of sequences, ideally we would like to incorporate into the scores of the candidate exons, the score of the optimal alignment at the amino acid level between the target exon sequence and the counterpart homologous sequene in the reference set. If a substitution matrix, for instance from the blosum family, is used to score the aligment, the resulting score can also be assumed to be a log-likelihood ratio: informally, the ratio between the likelihood of the aligment when the amino acid sequences code for proteins functionally related, and the likelihood of the alignment, otherwise. In principle, thus, this score could be naturally added to the geneid score for the exon. tblastx provides an appropiate shortcut to find often a good enough approximation to such an optimal aligment, and infer the corresponding score: the optimal alignment can be assumed to correspond to the maximal scoring HSP overlapping the exon. However, when dealing with the fragmentary nature of the mouse shotgun genomic sequence, often different regions of a candidate exon sequence will align optimally to different mouse shotgun sequences. Thus, in the approach used here, we identify the optimal HSPs covering each fraction of the exon, and compute separately the contribution of each HSP into the score of the exon. In the next section, we describe in detail how this computation is performed. </p>
    <b-row>
    <b-col>
    <b-card no-body class="mb-1">
      <b-card-header header-tag="header" class="p-1" role="tab">
        <b-button block v-b-toggle.accordion-1 variant="info">Scoring of candidate exons</b-button>
      </b-card-header>
      <b-collapse id="accordion-1" accordion="my-accordion" visible role="tabpanel">
        <b-card-body>
           <p> Let <img class="small-img" :src="'./static/img/img1.gif'"> be one of the candidate exons predicted by geneid along the a query DNA sequence <img class="small-img" :src="'./static/img/img2.gif'">. In sgp-2 the final score of <img class="small-img" :src="'./static/img/img1.gif'">, <img class="smaller-img" :src="'./static/img/img3.gif'">, is computed as: </p>
           <p><img class="equation-img" :src="'./static/img/img4.gif'"></p>
            <p>where <img class="smaller-img" :src="'./static/img/img5.gif'"> is the score given by geneid to the exon <img class="small-img" :src="'./static/img/img1.gif'">, and <img class="smaller-img" :src="'./static/img/img6.gif'"> is the score derived from the HSPs found by a tblastx search overlapping the exon <img class="small-img" :src="'./static/img/img1.gif'">. Both scores are log-likelihood ratios (and we compute both base two). Assuming independence between their distribution, they could be summed up into a single likelihood ratio. However, the assumption of independence is not realistic,<img class="smaller-img" :src="'./static/img/img5.gif'"> depends on the probability of the sequence of <img class="small-img" :src="'./static/img/img1.gif'">, assuming that <img class="small-img" :src="'./static/img/img1.gif'"> codes for a protein, while <img class="smaller-img" :src="'./static/img/img6.gif'"> depends on the probability of the optimal aligment of <img class="small-img" :src="'./static/img/img1.gif'"> with a sequence fragment of the mouse genome, assuming that both sequences code for related proteins. Obviously, these two probabilities are not independent. Their joint distribution could only be investigated-at least empirically-if the Markov Model of coding DNA used in geneid, and the substituion matrix used by tblastx were inferred from the very same set of coding sequences. Since this is not the case, we use an ad-hoc coefficient, <img class="small-img" :src="'./static/img/img7.gif'">, to weight the contribution of tblastx search, <img class="smaller-img" :src="'./static/img/img6.gif'"> into the final exon score.</p>
            <p> We compute <img class="smaller-img" :src="'./static/img/img6.gif'"> in the following way. Let <img class="smaller-img" :src="'./static/img/img8.gif'"> be the set of HSPs found by tblastx after comparing the query sequence <img class="small-img" :src="'./static/img/img2.gif'"> against a database of DNA sequences (figure [*]??, A). First, we find the maximum scoring projection of the HSPs onto the query sequence. We simply register the maximum score among the scores of all HSPs covering each position, and then partition the query sequence in equally maximally scoring segments <img class="smaller-img" :src="'./static/img/img9.gif'">, with scores <img class="smaller-img" :src="'./static/img/img10.gif'"> (figure [*]???, B). Then, for each predicted exon <img class="small-img" :src="'./static/img/img1.gif'"> (figure [*]????,C), we find <img class="smaller-img" :src="'./static/img/img11.gif'"> the set of maximally scoring segments overlapping <img class="small-img" :src="'./static/img/img1.gif'"></p>
            <p><img class="smaller-img" :src="'./static/img/img12.gif'"></p>
            <p>where <img class="small-img" :src="'./static/img/img13.gif'"> denotes the overlap betwen sequence segments <img class="small-img" :src="'./static/img/img14.gif'"> and <img class="small-img" :src="'./static/img/img15.gif'">, and <img class="smaller-img" :src="'./static/img/img16.gif'"> means no overlap. We compute<img class="smaller-img" :src="'./static/img/img6.gif'"> in the following way: </p>
            <p><img class="equation-img" :src="'./static/img/img17.gif'"></p>
            <p>where <img class="smaller-img" :src="'./static/img/img18.gif'"> denotes the length of sequence segment <img class="small-img" :src="'./static/img/img14.gif'">. That is, each exon gets the score of the maximally scoring HSPs along the exon sequence proportional to the fraction of the HSP covering the exon. In other words, <img class="smaller-img" :src="'./static/img/img6.gif'"> is the integral of the maximum scoring projection function within the exon interval. Once the scores <img class="small-img" :src="'./static/img/img19.gif'"> have been computed for all predicted exons in the sequence <img class="small-img" :src="'./static/img/img2.gif'">, gene prediction proceeds as usual in geneid: the gene structure is assembled maximizing the sum of scores of the assembled exons. </p>
        </b-card-body>
      </b-collapse>
    </b-card>
     <b-card no-body class="mb-1">
      <b-card-header header-tag="header" class="p-1" role="tab">
        <b-button block v-b-toggle.accordion-2 variant="info">Running sgp2</b-button>
      </b-card-header>
      <b-collapse id="accordion-2" accordion="my-accordion" role="tabpanel">
        <b-card-body>
            <p>In the practice, we run sgp-2 in the following way. Given a DNA query sequence (here, human chromosome sequences), and a database of DNA sequences (here, shotgun mouse genomic sequences), we run the query sequence against the databse using tblastx. Results of tblastx search are parsed to obtain the maximum scoring projection of the HSPs onto the query sequence using a simple perl script. The parsing includes discarding all HSPs below a given bit score cutoff, substrating this value from the score of the remaining HSPs, and weighting the resulting score by <img class="small-img" :src="'./static/img/img7.gif'"> (see above). The maximum scoring projection is given to geneid in GFF format `General Feature Format' (Durbin and Haussler, <b-link href="http://www.sanger.ac.uk/Software/formats/GFF/">http://www.sanger.ac.uk/Software/formats/GFF/</b-link>). geneid uses it to rescore the exons predicted along the query sequence as explained, and assembles the corresponding optimal gene structure. </p>
            <div><img class="figure-img" :src="'./static/img/img20.gif'"></div>
            <small><strong>Figure</strong> Rescoring of the exons predicted by geneid according with the results of a tblastx search
(To enlarge the figure, click right mouse button and select "View Image" from panel).</small>
          </b-card-body>
      </b-collapse>
    </b-card>
    </b-col>
        </b-row>
    </b-container>
</template>
<script>
import PageHeadingComponent from '../components/PageHeadingComponent.vue'
export default {
    name: 'sgp2-algorithm',

    data() {
        return {
            chapters: [],
            text: '',
            header: {title: "sgp2 algorithm description"}
        }
    },
    components: {
        PageHeadingComponent,
    },
    mounted() {
    }
}
</script>
<style>
p .small-img {
  height: 2em;
  width: auto;
}
p .smaller-img {
    height:3em;
    width:auto;
}
p .equation-img {
    height: 4em;
    width: auto;
}
div .figure-img {
    width: 100%;
    height: 100%;
}
</style>