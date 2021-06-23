module.exports = {
    resources: {
        genePDescription: { 
        title: "GENE PREDICTIONS ON WHOLE GENOMES",
        description:'The predictions available on this page have been obtained by using the gene-finding software geneid and SGP2. SGP2 combines geneid predictions with tblastx comparison of a query genome from one species (i.e. human) against an informant genome of another species (i.e. from mouse). ',
        },
        geneIdDescription: {
        title: "GENE ID WEB SERVER",
        },
        geneIdtexts: [{title: "What is geneid?", description: "geneid is a program to predict genes in anonymous genomic sequences designed with a hierarchical structure. In the first step, splice sites, start and stop codons are predicted and scored along the sequence using Position Weight Arrays (PWAs). In the second step, exons are built from the sites. Exons are scored as the sum of the scores of the defining sites, plus the the log-likelihood ratio of a Markov Model for coding DNA. Finally, from the set of predicted exons, the gene structure is assembled, maximizing the sum of the scores of the assembled exons. geneid offers some type of support to integrate predictions from multiple source via external gff files and the redefinition of the general gene structure or model is also feasible. The accuracy of geneid compares favorably to that of other existing tools, but geneid is likely more efficient in terms of speed and memory usage. Currently, geneid v1.2 analyzes the whole human genome in 3 hours (approx. 1 Gbp / hour) on a processor Intel(R) Xeon CPU 2.80 Ghz. "},
                        {title: "Main Features", description: ""},
                        {title: "Examples", description:""},
                        {title: "TrainingGeneid", description: `In order to build a parameter file for geneid it is necessary to "train" the program and parameter configurations exist for a number of eukaryotic species. Training basically consists of computing position weight matrices (PWMs) or Markov models for the splice sites and start codong and deriving a model for coding DNA (generally a Markov model of order 4 or 5). The basic requirements for a training set is an annotation file (preferably in geneid gff format and a set of fasta sequences corresponding to the gene models in the annotation file.

                            Generally as few as 100 gene models could be enough to build a reasonably accurate geneid parameter file, but generally a user would want to have as many sequences as possible (> 500) to build an optimally accurate matrix and also to be able to set aside some of the gene models for testing purposes (see training document).
                            
                            If a user wants to evaluate the accuracy of the newly developed parameter file she will also require an annotation file and fasta files corresponding to the sequences in the evaluation set. However if a user only has a limited number of gene models to train geneid with (generally < 500 sequences) she can use a "leave-one-out strategy" for evaluating the accuracty (more information in the training tutorial).
                            
                            The user can go through an example of a typical geneid "training" protocol (Training geneid for the parasite Perkinsus marinus) by following this tutorial`},
                        {title: "Gene Predictions on genomes", description:`This link contains the set of predicted genes using geneid on the recently sequenced genomes (Drosophila melanogaster, Homo sapiens, Mus musculus, Fugu rubripes or Dictyostelium discoideum) for some of their most common releases.`},
                        {title: "Accuracy", description:`Because of the lack of well annotated large genomic sequences, it is difficult to assess the accuracy of "ab initio" gene finders. We have attempted to analyze the accuracy of geneid in a number of different sets. We believe that in the analysis of large genomic sequences geneid may be superior to other existing tools. A side by side comparison with genscan can be found here.`}
        ],
        predictionOptions: {
            organism: {title: "Organism: ",
            options: ["Homo sapiens (human)","Drosophila melanogaster (fruit fly)", "Tetraodon nigroviridis (puffer fish)", "Caenorhabditis elegans (worm)"],
            active: false},
            predictionModes: {title: "Prediction mode: ",
            options: ["Normal mode (signal, exon and gene prediction)","Exon mode (only signals and exons, omitting evidences)"],active: false},
            dnaStrands: {title: "DNA strand: ",options:["Forward and Reverse","Reverse","Forward"],active: false}
        },
        phy: ""
    }
}
