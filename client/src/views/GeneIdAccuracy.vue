<template>
    <b-container>
            <page-heading-component :header="header"></page-heading-component>
        <b-row>
    <b-col>
    <b-card no-body class="mb-1">
      <b-card-header header-tag="header" class="p-1" role="tab">
        <b-button block v-b-toggle.accordion-1 variant="info">A side by side comparison of geneid and genscan</b-button>
      </b-card-header>
      <b-collapse id="accordion-1" accordion="my-accordion" visible role="tabpanel">
        <b-card-body>
            <p>Because of the lack of well annnotated large genomic sequences, it is difficult to assess the accuracy of "ab initio" gene finders. We have attempted to analyze the accuracy of geneid in a number of different sets. In this page, we presente the results compared with <b-link href="http://genes.mit.edu/GENSCAN.html">genscan</b-link>. Accuracy measures are the usual ones (see the page <b-link href="https://genome.crg.cat/courses/SeqAnalysis/GeneIdentification/Evaluation.html"> Accuracy of Gene Identification Programs</b-link> in this server, for a description). </p>
            <div>
                <h6>ACCURACY IN DIFFERENT DATA SETS:</h6>
                <b-list-group>
                    <b-list-group-item>
                        <b-card>
                                <strong><b-link href="https://genome.crg.cat/databases/gpeval2000/">h178</b-link></strong>
                                <p>This is a set of well annotated human sequences. The sort of dataset were genefinders are tipically evaluated. This set contains only single gene sequences, it is biased towards short genes, and it is likely to have been included in the training set of genefinders. Therefore, it is unclear how well results n this set can be extrapolated to large genomic sequences. genscan outperforms geneid on this set, although geneid tends to predict less false positives.
<pre>

               nucleotide               exon
           Sn    Sp    CC     Sn    Sp  SnSp       ME    WE
geneid   0.89  0.90  0.89   0.66  0.74  0.70     0.18  0.08
genscan  0.97  0.86  0.91   0.83  0.75  0.79     0.06  0.14
</pre></p>
                        </b-card>
                    </b-list-group-item>
                    <b-list-group-item>
                        <b-card>
                            <strong><b-link href="https://genome.crg.cat/databases/gpeval2000/">h178Art</b-link></strong>
                            <p>To simulate large genomic sequences, single gene sequences in h178 have been embedded in simulated intergenic DNA. Thus, the 178 single gene sequences have been collapsed into 42 multigene sequences of about 200 Kb each. Although preliminary results seem to indicate that the actual accuracy of genefinders can be better estimated in this data set than in the original set of single gene sequences, it is actually unclear how realistic this procedure is, and therefore how well results in this set can be extrapolated to large genomic sequences. while genscan outperformed geneid on the set of single gene sequences, geneid outperforms genscan now. genscan, however, is still superior in sensitivity. 
<pre>

                nucleotide               exon
           Sn    Sp    CC     Sn    Sp  SnSp       ME    WE
geneid   0.89  0.79  0.84   0.67  0.61  0.64     0.18  0.25
genscan  0.94  0.64  0.78   0.68  0.45  0.57     0.11  0.42
</pre></p>
                        </b-card>
                    </b-list-group-item><b-list-group-item>
                        <b-card>
                            <p><strong>h800</strong></p>
                            <p>This is a set of 800 human single gene sequences in embl, release 56, not present in embl, release 50. Therefore, these sequences are less likely to have been included in the training sets of current genefinders (including the current version of geneid). It is unclear, however, how well annotated these sequences are. In particular, they may include unannotated genes, and genscan may have already been used to annotated some of them. genscan and geneid perform comparably. genscan is more sensitive, while geneid produces less false positives. 
<pre>

               nucleotide               exon
           Sn    Sp    CC     Sn    Sp  SnSp      ME    WE
geneid   0.89  0.82  0.85   0.59  0.63  0.61    0.19  0.18
genscan  0.95  0.77  0.85   0.71  0.58  0.64    0.09  0.28
</pre></p>
                        </b-card>
                    </b-list-group-item><b-list-group-item>
                        <b-card>
                            <p><strong>h800Art</strong></p>
                            <p> The 800 human sequences above embedded in simulated intergenic DNA and collapsed in 195 multigene sequences. geneid outperforms genscan.
<pre>
    
               nucleotide               exon
           Sn    Sp    CC     Sn    Sp  SnSp      ME    WE
geneid   0.90  0.76  0.83   0.60  0.52  0.56    0.19  0.32
genscan  0.93  0.61  0.77   0.62  0.36  0.49    0.12  0.50
</pre></p>
                        </b-card>
                    </b-list-group-item><b-list-group-item>
                        <b-card>
                            <p><strong>SGR-C1</strong></p>
                            <p> This is a set of 25 real genomic sequences of about 100 Kb each from chromosome 1, annotated at the Sanger Center. It is unclear how exhaustive the annotation is, and it is likely that genscan has been used to obtain it. genscan slightly outperforms geneid on this set. 
<pre>
    
               nucleotide               exon
           Sn    Sp    CC     Sn    Sp  SnSp      ME    WE
geneid   0.81  0.34  0.57   0.56  0.34  0.45    0.28  0.57
genscan  0.91  0.33  0.61   0.68  0.29  0.48    0.15  0.64
</pre></p>
                        </b-card>
                    </b-list-group-item><b-list-group-item>
                        <b-card>
                            <p><strong>Chromosome 22</strong></p>
                            <p> We ran geneid on the sequence of chromosome 22, and compared the predictions with two different annotations. genscan released predictions were also compared to these two sets of annotations. The completeness of the annotation of chromosome 22 sequences is unclear, and genscan may had already been used to annotated it. geneid and genscan perform comparably on this set. </p>
                            <p><strong>annotation 1</strong></p>
                            <p>
<pre>
    
               nucleotide               exon
           Sn    Sp    CC     Sn    Sp  SnSp      ME    WE
geneid	 0.23  0.30  0.25   0.56  0.22  0.39    0.19  0.66
genscan  0.23  0.31  0.26   0.58  0.19  0.38    0.14  0.69
</pre></p>
                            <p><strong>annotation 2</strong></p>
                            <p> 
<pre>
    
               nucleotide               exon
           Sn    Sp    CC     Sn    Sp  SnSp      ME    WE
geneid   0.27  0.43  0.34   0.53  0.32  0.43    0.21  0.50
genscan  0.28  0.45  0.35   0.54  0.28  0.41    0.17  0.55
</pre></p>
                        </b-card>
                    </b-list-group-item>
                </b-list-group>
            </div>
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
    name: 'geneid-accuracy',

    data() {
        return {
            chapters: [],
            text: '',
            header: {title: "geneid accuracy"}
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