module.exports = {
    resources: {
        genePDescription: 'The predictions available on this page have been obtained by using the gene-finding software geneid and SGP2. SGP2 combines geneid predictions with tblastx comparison of a query genome from one species (i.e. human) against an informant genome of another species (i.e. from mouse). ',
        
    },

    geneIdtexts: [{ title: "What is geneid?", description: "geneid is a program to predict genes in anonymous genomic sequences designed with a hierarchical structure. In the first step, splice sites, start and stop codons are predicted and scored along the sequence using Position Weight Arrays (PWAs). In the second step, exons are built from the sites. Exons are scored as the sum of the scores of the defining sites, plus the the log-likelihood ratio of a Markov Model for coding DNA. Finally, from the set of predicted exons, the gene structure is assembled, maximizing the sum of the scores of the assembled exons. geneid offers some type of support to integrate predictions from multiple source via external gff files and the redefinition of the general gene structure or model is also feasible. The accuracy of geneid compares favorably to that of other existing tools, but geneid is likely more efficient in terms of speed and memory usage. Currently, geneid v1.2 analyzes the whole human genome in 3 hours (approx. 1 Gbp / hour) on a processor Intel(R) Xeon CPU 2.80 Ghz. "},
                    {title: "Main Features", description: ""},
                    {title: "Examples", description:""},
                    {title: "TrainingGeneid", description: ""},
                    {title: "Gene Predictions on genomes", description:""},
                    {title: "Speed", description:""}
                ],
    predictionOptions: {
        organism: {title: "Organism: ",
                   options: ["Homo sapiens (human)","Drosophila melanogaster (fruit fly)", "Tetraodon nigroviridis (puffer fish)", "Caenorhabditis elegans (worm)"],
                   active: false},
        predictionModes: {title: "Prediction mode: ",
            options: ["Normal mode (signal, exon and gene prediction)","Exon mode (only signals and exons, omitting evidences)"],active: false},
        dnaStrands: {title: "DNA strand: ",options:["Forward and Reverse","Reverse","Forward"],active: false}
    }
}
