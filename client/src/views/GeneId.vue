<template>
        <b-row>
            <page-heading-component :header="header"></page-heading-component>
    <b-col>
      <b-button id="popover-target-1" style="border: none;" variant="outline-info" class="mb-2" to="/geneid-training">
        <b-icon icon="gear-wide" variant="outline-info"></b-icon>
      </b-button>
      <b-popover target="popover-target-1" triggers="hover" placement="top" variant="info">
        Training tutorial      
      </b-popover>
      <b-button  id="popover-target-2" style="border: none;" variant="outline-info" class="mb-2"  to="/software-download">
        <b-icon icon="download" variant="outline-info"></b-icon>
      </b-button>
      <b-popover target="popover-target-2" triggers="hover" placement="top" variant="info">
        Download geneid
      </b-popover>
      <b-button id="popover-target-3" style="border: none;" variant="outline-info" class="mb-2" to="/geneid-accuracy">
        <b-icon icon="eyeglasses" variant="outline-info"></b-icon>
      </b-button>
      <b-popover target="popover-target-3" triggers="hover" placement="top" variant="info">
        Accuracy of geneid
      </b-popover>
      <b-button id="popover-target-4" style="border: none;" variant="outline-info" class="mb-2" href="https://genome.crg.cat/software/geneid/docs_1.2/index.html">
        <b-icon icon="book" variant="outline-info"></b-icon>      
      </b-button>
      <b-popover target="popover-target-4" triggers="hover" placement="top" variant="info">
        geneid v 1.2 Documentation
      </b-popover>
      <b-button id="popover-target-5" style="border: none;" variant="outline-info" class="mb-2">
        <b-icon icon="chat-dots" variant="outline-info"></b-icon>      
      </b-button>
      <b-popover target="popover-target-5" triggers="hover" placement="top" variant="info">
        If you encounter problems using geneid, or have suggestions on how to improve it send an e-mail to <a href="mailto:geneid@crg.es">geneid@crg.es</a>  
      </b-popover>
    <div class="accordion" role="tablist">
        <b-card no-body class="mb-1">
      <b-card-header header-tag="header" class="p-1" role="tab">
        <b-button block v-b-toggle.accordion-0 variant="info">What is geneid</b-button>
      </b-card-header>
      <b-collapse id="accordion-0" accordion="my-accordion" visible role="tabpanel">
        <b-card-body>
          <p>geneid is a program to predict genes in anonymous genomic sequences designed with a hierarchical structure. In the first step, splice sites, start and stop codons are predicted and scored along the sequence using Position Weight Arrays (PWAs). In the second step, exons are built from the sites. Exons are scored as the sum of the scores of the defining sites, plus the the log-likelihood ratio of a Markov Model for coding DNA. Finally, from the set of predicted exons, the gene structure is assembled, maximizing the sum of the scores of the assembled exons. geneid offers some type of support to integrate predictions from multiple source via external gff files and the redefinition of the general gene structure or model is also feasible. The accuracy of geneid compares favorably to that of other existing tools, but geneid is likely more efficient in terms of speed and memory usage. Currently, geneid v1.2 analyzes the whole human genome in 3 hours (approx. 1 Gbp / hour) on a processor Intel(R) Xeon CPU 2.80 Ghz.</p>
        </b-card-body>
      </b-collapse>
    </b-card>
      <b-card no-body class="mb-1">
      <b-card-header header-tag="header" class="p-1" role="tab">
        <b-button block v-b-toggle.accordion-1 variant="info">Main Features</b-button>
      </b-card-header>
      <b-collapse id="accordion-1" accordion="my-accordion" visible role="tabpanel">
        <b-card-body>
          <b-list-group>
            <b-list-group-item>geneid accuracy compared to that of other existing "ab initio" gene prediction tools.</b-list-group-item>
            <b-list-group-item>geneid is very efficient in terms of speed and memory usage. In practice, geneid can analyze chromosome size sequences at a rate of about 1 Gbp per hour on the Intel(R) Xeon CPU 2.80 Ghz. For the largest human chromosome (chr1), it requires 1/2 Gbyte of RAM plus the size of the Fasta sequence.</b-list-group-item>
            <b-list-group-item>geneid offers support to integrate predictions from multiple sources (ESTs, blast HSPs) and to reannotate genomic sequences, via external gff files and together with the redefinition of the "gene model".</b-list-group-item>
            <b-list-group-item>geneid output can be customized to different levels of detail, including exhaustive listing of potential signals and exons. Furthermore, several output formats as gff or XML are available.</b-list-group-item>
            <b-list-group-item>There are available parameter files in geneid v 1.2 for Drosophila Melanogaster, human (which can be also used for vertebrate genomes), Dictyostelium discoideum and Tetraodon nigroviridis (which can be used for Fugu rubripes) among many others for species spanning the four "classical" kingdoms. The additional currently available parameter files can be found under the section LINK HERE </b-list-group-item>
          </b-list-group>
        </b-card-body>
      </b-collapse>
    </b-card>
    <b-card no-body class="mb-1">
      <b-card-header header-tag="header" class="p-1" role="tab">
        <b-button block v-b-toggle.accordion-2 variant="info">Examples</b-button>
      </b-card-header>
      <b-collapse id="accordion-2" accordion="my-accordion" role="tabpanel">
        <b-card-body>
          <b-card-group deck>
          <b-card border-variant="info" header="Samples" header-text-variant="white" header-bg-variant="info"> 
      <!-- <b-card-header header-tag="header" class="p-1" role="tab" title="Samples">
      </b-card-header> -->
        <!-- <b-card-body> -->
          <b-list-group>
            <b-list-group-item><b-link href="https://genome.crg.cat/software/geneid/docs/chapter4/sequence/test.fa">Download input</b-link> </b-list-group-item>
            <b-list-group-item><b-link href="https://genome.crg.cat/software/geneid/docs/chapter4/samples_html/acceptors.html">Prediction of acceptor splice sites</b-link> </b-list-group-item>
            <b-list-group-item><b-link href="https://genome.crg.cat/software/geneid/docs/chapter4/samples_html/exons.html">Prediction of exons</b-link> </b-list-group-item>
            <b-list-group-item><b-link href="https://genome.crg.cat/software/geneid/docs/chapter4/samples_html/genes.html">Gene prediction</b-link> </b-list-group-item>
            <b-list-group-item><b-link href="https://genome.crg.cat/software/geneid/docs/chapter4/samples_html/evidences.html">Improving gene prediction by using re-annotation</b-link> </b-list-group-item>
          <b-list-group-item><b-link href="https://genome.crg.cat/software/geneid/docs/chapter4/samples_html/sr.html">Improving gene prediction by using homology information</b-link> </b-list-group-item>
          </b-list-group>
        <!-- </b-card-body> -->
      </b-card>
      <b-card border-variant="info" header="Formats" header-text-variant="white" header-bg-variant="info">
          <b-list-group>
            <b-list-group-item><b-link href="https://genome.crg.cat/software/geneid/docs/chapter4/formats_html/geneid.html">geneid format (default)</b-link> </b-list-group-item>
            <b-list-group-item><b-link href="https://genome.crg.cat/software/geneid/docs/chapter4/formats_html/gff.html">gff format</b-link> </b-list-group-item>
            <b-list-group-item><b-link href="https://genome.crg.cat/software/geneid/docs/chapter4/formats_html/xml.html">xml format</b-link> </b-list-group-item>
            <b-list-group-item><b-link href="https://genome.crg.cat/software/geneid/docs/chapter4/formats_html/extended.html">extended format (geneid and gff formats)</b-link> </b-list-group-item>
          </b-list-group>
      </b-card>
          </b-card-group>
        </b-card-body>
      </b-collapse>
    </b-card>
    <b-card no-body class="mb-1">
      <b-card-header header-tag="header" class="p-1" role="tab">
        <b-button block v-b-toggle.accordion-3 variant="info">Training geneid</b-button>
      </b-card-header>
      <b-collapse id="accordion-3" accordion="my-accordion" visible role="tabpanel">
        <b-card-body>
          <p>In order to build a parameter file for geneid it is necessary to "train" the program and parameter configurations exist for a number of eukaryotic species. Training basically consists of computing position weight matrices (PWMs) or Markov models for the splice sites and start codong and deriving a model for coding DNA (generally a Markov model of order 4 or 5). The basic requirements for a training set is an annotation file (preferably in geneid gff format and a set of fasta sequences corresponding to the gene models in the annotation file.</p>
          <p>Generally as few as 100 gene models could be enough to build a reasonably accurate geneid parameter file, but generally a user would want to have as many sequences as possible (> 500) to build an optimally accurate matrix and also to be able to set aside some of the gene models for testing purposes (see training document).</p>
          <p>If a user wants to evaluate the accuracy of the newly developed parameter file she will also require an annotation file and fasta files corresponding to the sequences in the evaluation set. However if a user only has a limited number of gene models to train geneid with "(generally less than 500 sequences) she can use a "leave-one-out strategy" for evaluating the accuracty (more information in the training tutorial).</p>
          <p>The user can go through an example of a typical geneid "training" protocol (Training geneid for the parasite Perkinsus marinus) by following <b-link to="/geneid-training"> this tutorial </b-link></p>
        </b-card-body>
      </b-collapse>
    </b-card>
    <b-card no-body class="mb-1">
      <b-card-header header-tag="header" class="p-1" role="tab">
        <b-button block v-b-toggle.accordion-4 variant="info">Gene predictions on genomes</b-button>
      </b-card-header>
      <b-collapse id="accordion-4" accordion="my-accordion" role="tabpanel">
        <b-card-body>
          <p>This <b-link to="/">link</b-link> contains the set of predicted genes using geneid on the recently sequenced genomes (Drosophila melanogaster, Homo sapiens, Mus musculus, Fugu rubripes or Dictyostelium discoideum) for some of their most common releases. </p>
        </b-card-body>
      </b-collapse>
    </b-card>
    <b-card no-body class="mb-1">
      <b-card-header header-tag="header" class="p-1" role="tab">
        <b-button block v-b-toggle.accordion-5 variant="info">Accuracy</b-button>
      </b-card-header>
      <b-collapse id="accordion-5" accordion="my-accordion" role="tabpanel">
        <b-card-body>
          <p>Because of the lack of well annotated large genomic sequences, it is difficult to assess the accuracy of "ab initio" gene finders. We have attempted to analyze the accuracy of geneid in a number of different sets. We believe that in the analysis of large genomic sequences geneid may be superior to other existing tools. A side by side comparison with genscan can be found <b-link to="/geneid-accuracy">here</b-link>.</p>
        </b-card-body>
      </b-collapse>
    </b-card>
    <b-card no-body class="mb-1">
      <b-card-header header-tag="header" class="p-1" role="tab">
        <b-button block v-b-toggle.accordion-6 variant="info">Speed</b-button>
      </b-card-header>
      <b-collapse id="accordion-6" accordion="my-accordion" role="tabpanel">
        <b-card-body>
          <p>The benchmark sequence is the human Chromosome 1 (239 Mb) extracted from
              the goldenPath-UCSC assembly (July 2003 release): </p>
          <p><strong>Computer: </strong>Intel Pentium Intel(R) Xeon CPU 2.80 Ghz. 4Gb RAM </p>
          <p><strong>CPU/real time(s): </strong>1025 / 1045 secs </p>
        </b-card-body>
      </b-collapse>
    </b-card>
    <b-card no-body class="mb-1">
      <b-card-header header-tag="header" class="p-1" role="tab">
        <b-button block v-b-toggle.accordion-7 variant="info">Web Server</b-button>
      </b-card-header>
      <b-collapse id="accordion-7" accordion="my-accordion"  role="tabpanel">
        <b-card-body>
          <gene-id-form-component></gene-id-form-component>
        </b-card-body>
      </b-collapse>
    </b-card>
    </div>
    </b-col>
        </b-row>
</template>
<script>
import configs from '../static-config'
import PageHeadingComponent from '../components/PageHeadingComponent.vue'
import GeneIdFormComponent from '../components/GeneIdFormComponent.vue'
export default {
    name: 'gene-id',

    data() {
        return {
            chapters: [],
            text: '',
            header: {title: configs.resources.geneIdDescription.title}
        }
    },
    components: {
        PageHeadingComponent,
        GeneIdFormComponent
    },
    mounted() {
    }
}
</script>
<style lang="scss">

</style>