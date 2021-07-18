<template>
    <b-container>
            <page-heading-component :header="header"></page-heading-component>
        <b-row>
    <b-col>
      <b-button id="popover-target-1" style="border: none;" variant="outline-info" class="mb-2" to="/sgp2-algorithm">
        <b-icon icon="calculator-fill" variant="outline-info"></b-icon>
      </b-button>
      <b-popover target="popover-target-1" triggers="hover" placement="top" variant="info">
        sgp2 algorithm      
      </b-popover>
      <b-button  id="popover-target-2" style="border: none;" variant="outline-info" class="mb-2"  to="/software-download">
        <b-icon icon="download" variant="outline-info"></b-icon>
      </b-button>
      <b-popover target="popover-target-2" triggers="hover" placement="top" variant="info">
        Download sgp2
      </b-popover>
    <div class="accordion" role="tablist">
        <b-card no-body class="mb-1">
      <b-card-header header-tag="header" class="p-1" role="tab">
        <b-button block v-b-toggle.accordion-0 variant="info">What is sgp2</b-button>
      </b-card-header>
      <b-collapse id="accordion-0" accordion="my-accordion" visible role="tabpanel">
        <b-card-body>
          <p>sgp2 is a program to predict genes by comparing anonymous genomic sequences from two different species. It combines tblastx, a sequence similarity search program, with geneid, an "ab initio" gene prediction program. In "assymetric" mode, genes are predicted in one sequence from one species (the target sequence), using a set of sequences (maybe only one) from the other species (the reference set). Essentially, geneid is used to predict all potential exons along the target sequence. Scores of exons are computed as log-likelihood ratios, function of the splice sites defining the exon, the coding bias in composition of the exon sequence as measured by a Markov Model of order five, and of the optimal alignment at the amino acid level between the target exon sequence and the counterpart homologous sequence in the reference set. From the set of predicted exons, the gene structure is assembled (eventually multiple genes in both strands) maximizing the sum of the scores of the assembled exons. A more detailed description of the algorithm can be found <b-link to="sgp2-algorithm">here</b-link>.</p>
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
            <b-list-group-item>sgp2 predictions are more accurate than those obtained by pure "ab initio" gene finding programs.</b-list-group-item>
            <b-list-group-item>Gene prediction can be done in the target and the reference genome simultaneously.</b-list-group-item>
            <b-list-group-item>sgp2 output can be customized to different formats as gff, geneid format or XML are available. Allowing different amount of information associated to each output format.</b-list-group-item>
            <b-list-group-item>Shotgun data can be used at any level of coverage as the informant genome.</b-list-group-item>
            <b-list-group-item>sgp2 is very efficient in terms of speed and memory usage.</b-list-group-item>
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
          <b-list-group>
            <b-list-group-item><b-link href="https://genome.crg.cat/software/sgp2/samples/Hsap_BTK.msk.fa">Download human.fa</b-link> </b-list-group-item>
            <b-list-group-item><b-link href="https://genome.crg.cat/software/sgp2/samples/Mmus_BTK.msk.fa">Download mouse.fa</b-link> </b-list-group-item>
            <b-list-group-item><b-link href="https://genome.crg.cat/software/sgp2/samples/Hsap_BTK.tbx">Download tblastx.file</b-link> </b-list-group-item>

            <b-list-group-item><b-link href="https://genome.crg.cat/software/sgp2/samples/Hsap_BTK.sgp2">sgp2 prediction in human</b-link> </b-list-group-item>
          <b-list-group-item><b-link href="https://genome.crg.cat/software/sgp2/samples/Mmus_BTK.sgp2">sgp2 prediction in mouse</b-link> </b-list-group-item>
          </b-list-group>
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
        <b-button block v-b-toggle.accordion-3 variant="info">tblastx searching</b-button>
      </b-card-header>
      <b-collapse id="accordion-3" accordion="my-accordion" visible role="tabpanel">
        <b-card-body>
            <p>The BLAST algorithms employ heuristics at various stages of the searching process, and the choice of the parameters is very important for the speed, the sensitivity and the specificity of the searches. sgp2 predictions are mainly based on the tblastx results, therefore the selection of the parameters is critical for the final predictions. Although both mostly spread versions of BLAST (<b-link href="http://www.ncbi.nlm.nih.gov/BLAST/">NCBI Blast</b-link> and <b-link href="http://blast.wustl.edu/">WU-blast</b-link>) are accepted as input file for sgp2, we recommend to use <b-link href="http://blast.wustl.edu/">WU-blast</b-link> because it has a more flexible set of parameters.</p>
            <p>For the sgp2 predictions, the following <b-link href="http://blast.wustl.edu/">WU-blast</b-link> set of parameters were suggested to optimize the speed, sensitivity and specificity of the tblastx searches:</p>
            <pre>
        B=100000 V=100000 hspmax=0 gspmax=0 nogap
        altscore='* any -999' altscore='any * -999'
        E=0.01 E2=0.01 S2=80 Z=3000000000
        -filter=xnu+seg
            </pre>
            <p>If you are comparing long sequences you can increase the word size variable to 5 (W=5), which speeds up the search by 60-fold and the sensitivity is nearly the same as the previous parameters. </p>
            <p>More details on the tblastx parameters for long genomic sequences to predict genes with sgp2 can be found in the human mouse prediction section (below) or in the papers of the references section. A deep analysis on tblastx parameters in large genomic sequences can be found in the following article: </p>
       <pre>
        I. Korf. "Serial Blast searching."
        Bioinformatics 19(12):1492-1496 (2003) <b-link href="http://bioinformatics.oupjournals.org/cgi/content/abstract/19/12/1492">[Abstract]</b-link>
                            </pre>
        </b-card-body>
      </b-collapse>
    </b-card>
    <b-card no-body class="mb-1">
      <b-card-header header-tag="header" class="p-1" role="tab">
        <b-button block v-b-toggle.accordion-4 variant="info">Gene predictions on genomes</b-button>
      </b-card-header>
      <b-collapse id="accordion-4" accordion="my-accordion" role="tabpanel">
        <b-card-body>
          <p>This <b-link to="/">link</b-link> contains the set of predicted genes using sgp2 on the recently sequenced genomes ( Homo sapiens, Mus musculus and Rattus norvegicus) for some of their last releases. </p>
        </b-card-body>
      </b-collapse>
    </b-card>
    <b-card no-body class="mb-1">
      <b-card-header header-tag="header" class="p-1" role="tab">
        <b-button block v-b-toggle.accordion-5 variant="info">Comparative gene prediction in human and mouse</b-button>
      </b-card-header>
      <b-collapse id="accordion-5" accordion="my-accordion" role="tabpanel">
        <b-card-body>
            <p>We evaluated the accuracy of sgp2 using a number of different data sets. The lack of a gold standard of gene prediction makes it difficult to get accurate assessments from any single data set. We used different data sets. The results of this initial test can be found <b-link href="https://genome.crg.cat/datasets/sgp2002/index.html">here</b-link>.</p>
            <p>In collaboration with other groups, we developed a two stage procedure that exploit the human and mouse genome sequences to produce a set of genes with a much higher rate of experimental verification using sgp2 and twinscan. The results of this approach can be found <b-link href="https://genome.crg.cat/datasets/mouse2002/index.html">here</b-link>. </p>
        </b-card-body>
      </b-collapse>
    </b-card>
    <b-card no-body class="mb-1">
      <b-card-header header-tag="header" class="p-1" role="tab">
        <b-button block v-b-toggle.accordion-6 variant="info">References</b-button>
      </b-card-header>
      <b-collapse id="accordion-6" accordion="my-accordion" role="tabpanel">
        <b-card-body>
            <ul style="list-style-type:inherit">
                <li>
          <pre>
G. Parra, P. Agarwal, J.F. Abril, T. Wiehe, J.W. Fickett and R. Guigó.
"Comparative gene prediction in human and mouse."
Genome Research 13(1):108-117 (2003) [<b-link href="http://www.genome.org/cgi/content/abstract/13/1/108">Abstract</b-link>]
          </pre>
                </li>
                <li>
          <pre>
R. Guigó, E.T. Dermitzakis, P. Agarwal, C.P. Ponting, G. Parra, A. Reymond, J.F. Abril, E. Keibler, R. Lyle, C. Ucla, S.E. Antonarakis and M.R. Brent.
"Comparison of mouse and human genomes followed by experimental verification yields an estimated 1,019 additional genes."
Proc. Nat. Acad. Sci. 100(3):1140-1145 (2003)   [<b-link href="http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&list_uids=12552088&dopt=Abstract">PubMed</b-link>]   [<b-link href="http://www.pnas.org/cgi/content/abstract/100/3/1140">Abstract</b-link>]   [<b-link href="http://www.pnas.org/cgi/content/full/100/3/1140">Full Text</b-link>] 
          </pre>
                </li>
            </ul>
        </b-card-body>
      </b-collapse>
    </b-card>
    <b-card no-body class="mb-1">
      <b-card-header header-tag="header" class="p-1" role="tab">
        <b-button block v-b-toggle.accordion-7 variant="info">Authors and acknowledgements</b-button>
      </b-card-header>
      <b-collapse id="accordion-7" accordion="my-accordion"  role="tabpanel">
        <b-card-body>
            <p>The current version of sgp2 has been written by <a href="mailto:gparra@imim.es">Genis Parra</a>, <a href="mailto:jabril@imim.es">Josep F. Abril</a> and <a href="mailto:rguigo@crg.es">Roderic Guigó</a>.
With contributions from Enrique Blanco, Thomas Whiehe and Moises Burset. </p>
        </b-card-body>
      </b-collapse>
    </b-card>
    </div>
    </b-col>
        </b-row>
    </b-container>
</template>
<script>
import PageHeadingComponent from '../components/PageHeadingComponent.vue'
export default {
    name: 'sgp2',

    data() {
        return {
            chapters: [],
            text: '',
            header: {title: "sgp2"}
        }
    },
    components: {
        PageHeadingComponent,
    },
    mounted() {
    }
}
</script>
<style lang="scss">

</style>