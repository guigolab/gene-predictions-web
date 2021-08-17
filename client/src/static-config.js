module.exports = {
    resources: {
        genePDescription: { 
        title: "gene predictions on whole genomes"
        },
        geneIdDescription: {
        title: "geneid",
        description: "geneid is a program to predict genes in anonymous genomic sequences designed with a hierarchical structure. In the first step, splice sites, start and stop codons are predicted and scored along the sequence using Position Weight Arrays (PWAs). In the second step, exons are built from the sites. Exons are scored as the sum of the scores of the defining sites, plus the the log-likelihood ratio of a Markov Model for coding DNA. Finally, from the set of predicted exons, the gene structure is assembled, maximizing the sum of the scores of the assembled exons. geneid offers some type of support to integrate predictions from multiple source via external gff files and the redefinition of the general gene structure or model is also feasible. The accuracy of geneid compares favorably to that of other existing tools, but geneid is likely more efficient in terms of speed and memory usage. Currently, geneid v1.2 analyzes the whole human genome in 3 hours (approx. 1 Gbp / hour) on a processor Intel(R) Xeon CPU 2.80 Ghz. "
        },
        geneIdtexts: [{title: "Main Features", description: ""},
                        {title: "Examples", description:""},
                        {title: "TrainingGeneid", description: `In order to build a parameter file for geneid it is necessary to "train" the program and parameter configurations exist for a number of eukaryotic species. Training basically consists of computing position weight matrices (PWMs) or Markov models for the splice sites and start codong and deriving a model for coding DNA (generally a Markov model of order 4 or 5). The basic requirements for a training set is an annotation file (preferably in geneid gff format and a set of fasta sequences corresponding to the gene models in the annotation file.

                            Generally as few as 100 gene models could be enough to build a reasonably accurate geneid parameter file, but generally a user would want to have as many sequences as possible (> 500) to build an optimally accurate matrix and also to be able to set aside some of the gene models for testing purposes (see training document).
                            
                            If a user wants to evaluate the accuracy of the newly developed parameter file she will also require an annotation file and fasta files corresponding to the sequences in the evaluation set. However if a user only has a limited number of gene models to train geneid with (generally < 500 sequences) she can use a "leave-one-out strategy" for evaluating the accuracty (more information in the training tutorial).
                            
                            The user can go through an example of a typical geneid "training" protocol (Training geneid for the parasite Perkinsus marinus) by following this tutorial`},
                        {title: "Gene Predictions on genomes", description:`This link contains the set of predicted genes using geneid on the recently sequenced genomes (Drosophila melanogaster, Homo sapiens, Mus musculus, Fugu rubripes or Dictyostelium discoideum) for some of their most common releases.`},
                        {title: "Accuracy", description:`Because of the lack of well annotated large genomic sequences, it is difficult to assess the accuracy of "ab initio" gene finders. We have attempted to analyze the accuracy of geneid in a number of different sets. We believe that in the analysis of large genomic sequences geneid may be superior to other existing tools. A side by side comparison with genscan can be found here.`}
        ],
        predictionOptions: {
            predictionModes: [
                {text:'Normal mode (signal, exon and gene prediction)', value:'normal'},
                {text:'Exon mode (only signals and exons, omitting evidences)',value:'-o'},
                {text:'Assembling mode (only assembling evidences)',value:'-O'}
            ],
            dnaStrands: [
                {text:"Forward and Reverse",value:""},
                {text:"Reverse",value:'-C'},
                {text:"Forward",value:'-W'}
            ]
        },
        outputOptions: {
            outputFormat: [{text: 'geneid',value:''},{text: 'GFF',value:'-G'},{text: 'gene including CDS sequence',value:'-D'},{text: 'geneid extended (only genes)',value:'-X'},{text: 'GFF extended (only genes)',value:'-XG'}],
            signals: [{text: 'Acceptor sites',value:'-a'},{text: 'Donor sites',value:'-d'},{text: 'Start codons',value:'-b'},{text: 'Stop codons',value:'-e'}],
            exons: [{text: 'First exons',value:'-f'},{text: 'Internal exons',value:'-i'},{text: 'Terminal exons',value:'-t'},{text: 'Single genes',value:'-s'},{text: 'Open reading frames',value:'-zZ'},{text: 'All exons',value:'-x'}]
        },
        phy: "",
        downloadPageTexts: {
            title: "downloads",
            description: "These distributions contains several directories and files compressed in tar.gz file. Source code and documentation files are included in the distribution, as well as several parameters files and other extra information.",
            geneIDVersions: [
                {
                    version: "v 1.4.4",
                    values: [ 
                            { 
                                description: "full distribution: source code and documentation",
                                info: "documentation does not yet reflect new features; for help, type geneid -h",
                                checkSum: {
                                    type: "md5sum geneid_v1.4.4.Jan_13_2011.tar.gz",
                                    value: "05c00f283a8fa996418aff0bc8db1c6d"
                                },
                                link: "https://genome.crg.es/pub/software/geneid/geneid_v1.4.4.Jan_13_2011.tar.gz",
                            }]
                },
                            
                {
                    version: "v 1.3 preview release 3 (version used for NGASP phase II category 4)",
                    values: [
                    {
                        description: "full distribution: source code and documentation",
                        info: "documentation does not yet reflect new features; for help, type geneid -h",
                        checkSum: {
                            type:"md5sum geneid_v1.3.Mar_30_2007.tar.gz",
                            value: "10cad4e6ae25a57fcc6bb062692626ae"
                        },
                        link:"https://genome.crg.es/pub/software/geneid/geneid_v1.3.Mar_30_2007.tar.gz",
                    },
                   ]
                },
                {
                    version: "v 1.3 preview release 1 (version used for NGASP phase I category 1)",
                    values: [ {
                        description: "full distribution: source code and documentation",
                        info: "documentation does not yet reflect new features; for help, type geneid -h",
                        checkSum: {
                            type: "md5sum geneid_v1.3.Dec_21_2006.tar.gz",
                            value: "1ff0f870e5ec5a553e4603102a9d7c62"
                        },
                        link: "https://genome.crg.es/pub/software/geneid/geneid_v1.3.Dec_21_2006.tar.gz",
                    }]
                },  
                {
                    version: "v 1.2",
                    values: [ 
                        {
                            description: "full distribution: source code and documentation",
                            checkSum: {
                                type: "md5sum geneid_v1.2.March_1_2005.tar.gz",
                                value: "6f350210ead7e49ac76be1fd17ef91f9"
                            },
                            link: "https://genome.crg.es/pub/software/geneid/geneid_v1.2.March_1_2005.tar.gz",
                        },
                        {
                            description: "Solaris 64-bits distribution",
                            info: "Makefiles optimized by Mithun Sridharan, Sun Microsystems GmbH",
                            links: [{name: "full version",value:"https://genome.crg.es/pub/software/geneid/geneid_v1.2.Solarisx64.Jun_07_2006.tar.gz"},{name: "binary file",value:"https://genome.crg.es/pub/software/geneid/geneid_v1.2.Solarisx64.Jun_07_2006"}],
                        },
                        {
                            description: "Linux binary (gcc version 3.3.1)",
                            link: "https://genome.crg.es/pub/software/geneid/geneid.March_1_2005"
                        },
                        {
                            description: "documentation (HTML)",
                            link: "https://genome.crg.cat/software/geneid/docs_1.2/index.html"
                        }
                    ]
                },
                {
                    version: "v 1.1",
                    values: [
                        {
                            description: "full distribution: source code and documentation",
                            link: "https://genome.crg.es/pub/software/geneid/geneid_v1.1.Feb_26_2003.tar.gz"
                        },{
                            description: "Linux binary (gcc version 2.95 19990728)",
                            link: "https://genome.crg.es/pub/software/geneid/geneid.Oct_09_2002"
                        },{
                            description: "documentation (HTML)",
                            link: "https://genome.crg.es/pub/software/geneid/docs.Jul_15_2002.tar.gz"
                        }
                    ]
                },
                {
                    version: " v 1.0",
                    values: [
                        {
                            description: "full distribution: source code and documentation",
                            link: "https://genome.crg.es/pub/software/geneid/geneid_v1.0.Sep_08_2000.tar.gz"
                        },{
                            description: "binary files for some architectures",
                            links: [{name: "Linux", value: "https://genome.crg.es/pub/software/geneid/geneid_v1.0.Linux.Sep_08_2000.tar.gz"},{name: "SGI", value: "https://genome.crg.es/pub/software/geneid/geneid_v1.0.SGI.Sep_08_2000.tar.gz"},
                                    {name: "Solaris", value: "https://genome.crg.es/pub/software/geneid/geneid_v1.0.Solaris.Aug_22_2000.tar.gz"}]

                        },{
                            description: "(Parallel version): -- Requires UNIX/LINUX pthreads library --",
                            link: "https://genome.crg.es/pub/software/geneid/geneidP_v1.0.Jan_08_2001.tar.gz"
                        }
                    ]
                }   
            ],
            SGP2Versions: [
                {
                    version: "v 1.1", 
                    values: [
                        {description: "full distribution: source code and documentation", link: "ftp://genome.crg.es/pub/software/sgp2/sgp2_v1.1.May_8_2012.tar.gz"}
                    ] 
                }
            ]
            ,
            links: {ftpServer: "https://genome.crg.es/pub/software/geneid/",
            changeLog: "https://genome.crg.cat/software/geneid/ChangeLog",
            geneIDinstructions: "https://genome.crg.cat/software/geneid/docs/chapter3/index.html",
            sgp2Instructions: "https://genome.crg.cat/software/sgp2/README"
        },
        }
    }
}
