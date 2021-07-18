<template>
    <b-container>
            <page-heading-component :header="header"></page-heading-component>
        <b-row>
    <b-col class="training-container">
   <div>
       <b-card>
        <p> <strong>IMPORTANT:</strong> The user interested in training geneid should have access to a unix/linux working environment and have at least basic knowledge of linux command line instructions, BASH shell scripting and the UNIX-based computer languages <b-link href="http://en.wikipedia.org/wiki/AWK">gawk</b-link> and <b-link href="http://en.wikipedia.org/wiki/Perl">perl</b-link> . Furthermore, some programs are C-based and require compilation. Instructions on how to compile should be contained within the program packages. Finally it is likely that the user will have to make gawk and perl scripts executable after downloading them. This can be done by running the following linux command: <strong>chmod 755 filename.awk[pl]</strong>. The user should also check that the different "shebangs" for gawk, perl and bash indicate the proper path of the different executables and are at the top of every script. For example "#!/usr/bin/perl" is known as the perl shebang. It is put at the top of a perl script, and it tells the web server (like Apache) where to find the perl executable.</p>
       <p><strong>Initial set of files required for training/evaluation of geneid:</strong></p>
        <b-list-group>
            <b-list-group-item>Fasta sequences containing the training set gene models: <b-link href="https://genome.crg.cat/software/geneid/docs/training/sequence/pmarinus4training.fa">pmarinus4training.fa</b-link></b-list-group-item>
            <b-list-group-item>Fasta sequences containing the evaluation set gene models: <b-link href="https://genome.crg.cat/software/geneid/docs/training/sequence/pmarinus4evaluation.fa">pmarinus4evaluation.fa</b-link></b-list-group-item>
            <b-list-group-item>Sequence including gene models of training set in tabular format: <b-link href="https://genome.crg.cat/software/geneid/docs/training/sequence/pmarinus4training.tbl">pmarinus4training.tbl</b-link></b-list-group-item>
            <b-list-group-item>Sequence including gene models of evaluation set in tabular format: <b-link href="https://genome.crg.cat/software/geneid/docs/training/sequence/pmarinus4evaluation.tbl">pmarinus4evaluation.tbl</b-link></b-list-group-item>
            <b-list-group-item>Annotation file corresponding to training set gene models: <b-link href="https://genome.crg.cat/software/geneid/docs/training/sequence/pmarinus4training.gff">pmarinus4training.gff</b-link></b-list-group-item>
            <b-list-group-item>Annotation file corresponding to training set gene models: <b-link href="https://genome.crg.cat/software/geneid/docs/training/sequence/pmarinus4evaluation.gff">pmarinus4evaluation.gff</b-link></b-list-group-item>
        </b-list-group>
        <small><strong>NOTE:</strong> For Perkinsus marinus we used 765 sequences as part of the training set and 250 gene models to test the newly developed parameter file.</small>
       </b-card>
   </div>
   <b-card>
       <b-card-body>
           <p>In the first step of training process the CDS and intronic regions (in fasta format) of the each of the annotated gene models are extracted from the fasta files given their annotation coordinates (gff file). The CDS and intonic fastas can be obtained by using the in-house program <b-link href="https://genome.crg.cat/software/geneid/docs/training/software/SSgff.tgz">SSgff (tar-gzipped version)</b-link>. </p>
           <p>The following wrapper <b-link href="http://en.wikipedia.org/wiki/Bash">BASH</b-link> script gives an example of how the CDS and intron sequences can be extracted from the genomic (<strong>training</strong>) fastas above: </p>
           <pre>
#!/bin/bash

mkdir -p ./intron
mkdir -p ./cds
mkdir -p ./fastas

cd ./fastas/

#obtain multi -fastas

TblToFastaFile pmarinus4training.tbl

while read genomic_id gene_id
do
echo $genomic_id
echo $gene_id
   egrep -w "$gene_id\$" pmarinus4training.gff >   /tmp/$$gff
   SSgff -cE ../fastas/$genomic_id   /tmp/$$gff \
      | sed -e 's/:/_/' -e 's/ CDS//' \
    > ../cds/$gene_id

   SSgff -iE ../fastas/$genomic_id   /tmp/$$gff \
      | sed -e 's/:/_/' -e 's/ Intron.*//' \
    > ../intron/$gene_id
done &lt; locus_id_training
           </pre>
       </b-card-body>
       <small><strong>NOTE:</strong> "locus_id_training" contains the list of all sequences and genes (fields $1 and $9 of the gff file). In the example above the genomic sequences are placed in a directory "fastas" and we the output CDS and intron fastas are output into directories "CDS" and "Intron".</small>
   </b-card>
   <b-card>
       <b-card-body>
           <p>A series of 765 single or multi-fasta files will be created in each of these 2 directories which should be concatenated into single multi-fasta files. It will also be necessary to convert these files to tabular format which can be done using the following awk script: <b-link href="https://genome.crg.cat/software/geneid/docs/training/software/FastaToTbl">FastaToTbl</b-link>. Finally the CDS sequences should be converted to proteins and the user should look for any sequences with in-frame stops and remove the from the training/evaluation set. Nucleotide CDS sequences can be converted to protein sequences using the <b-link href="https://genome.crg.cat/software/geneid/docs/training/software/Translate">Translate</b-link> script (To run Translate the user will also need <b-link href="https://genome.crg.cat/software/geneid/docs/training/software/genetic.code">genetic.code</b-link>). The user will also use <b-link href="https://genome.crg.cat/software/geneid/docs/training/software/TblToFastaFile">TblToFastaFile</b-link> to convert the multi-fasta file into separate fasta files. </p>
           <p>The following wrapper <b-link href="http://en.wikipedia.org/wiki/Bash">BASH</b-link> script gives an example of how the CDS and intron sequences can be extracted from the genomic (<strong>training</strong>) fastas above: </p>
           <pre>
#!/bin/bash

# Convert fasta files to tabular fasta

FastaToTbl all.cds.fa > all.cds.tbl

FastaToTbl all.intron.fa > all.intron.tbl

# Translate the CDS
mkdir./protein ; cd ./protein;

FastaToTbl ./cds/* | Translate | TblToFastaFile

# Checking for stop codons in the coding region

FastaToTbl./protein/* | grep "[A-Z]\*[A-Z]" |\
 gawk '{print $1}' | uniq
           </pre>
       </b-card-body>
   </b-card>
      <b-card>
       <b-card-body>
           <p>In a second step start and stop codons and all splice sites of each of the annotated genes given the fasta files and gff coordinates again using SSgff (tar-gzipped version). The following wrapper BASH script gives an example of how the splice sites and start/stop codons can be extracted from the genomic (training) fastas above: </p>
           <pre>
#!/bin/bash

mkdir -p ./sites

while read genomic_id gene_id
do
   echo $genomic_id
   echo $gene_id
   egrep -w $gene_id pmarinus4training.gff > /tmp/$$gff
  SSgff -dabeE ../fastas/$genomic_id /tmp/$$gff \
      > /tmp/$$all_sites

  for site in Acceptor Donor Stop Start
  do
    echo $site
    grep -A 1 $site /tmp/$$all_sites | sed '/--/d' \
    >> ../sites/${site}_sites
 
    done
done &lt; locus_id_training
           </pre>
       </b-card-body>
       <small><strong>NOTE:</strong>  "locus_id_training" contains the list of all sequences and genes (fields $1 and $9 of the gff file). In the example above the genomic sequences are placed in a directory "fastas" and we the output CDS and intron fastas are output into directories "sites". Four multi-fasta files will be created for each type of site (i.e. "Donor_sites"). </small>
   </b-card>
         <b-card>
       <b-card-body>
           <p> These files should be converted to tabular format as described above using FastaToTbl.</p>
           <p>It is also suggested that the user filter out those splice sites and start codons that are not canonical from the training set. This can be done by employing the following BASH script (example for Donor sites):</p>
           <pre>
#!/bin/bash

#####Donors

gawk '{print $2}' ./Donor_sites.tbl |\
 egrep -v '^[atcgNATCGn]{31}GT' > seqs_Don
#11 out of 4277 non-standard donors

egrep -f seqs_Don Donor_sites.tbl | gawk '{print $1}' - \
| sort | uniq >  seqs_wrong_Don

egrep -vf seqs_wrong_Don Donor_sites.tbl > Donor_sites_filter1.tbl
#4266 canonical donor sites
           </pre>
       </b-card-body>
   </b-card>
           <b-card>
       <b-card-body>
           <p>In the following step of the training process the user will derive frequency matrices for the donors, acceptors and start codons.</p>
           <p>However to do this the user will first have to parse the sequences (normally the sequences in which the gene models are embedded) for background dinucleotides ("GT","AG" or "ATG") flanked by approximately 30 nucleotides of sequence on each side. The awk program <b-link href="https://genome.crg.cat/software/geneid/docs/training/software/FindRegexp">"FindRegexp"</b-link> and the BASH script <b-link href="https://genome.crg.cat/software/geneid/docs/training/software/BoundarySites.sh">"BoundarySites.sh"</b-link> can be used to obtain these background sequences in an appropriate format. Furthermore in order to exclude the real donors, acceptors and starts from the background the user can use a combination of awk and linux commands (as shown below). It should be pointed out that this program can be very slow if we are dealing with large fasta files. </p>
           <p>The following BASH script demonstrates how the user can obtain the background data for "GT", "AG" and "ATG":</p>
           <pre>
#!/bin/bash

############# Obtaining all the GT sites

FindRegexp GT &lt; pmarinus4training.tbl \
 | join pmarinus4training.tbl - | BoundarySites.sh -2 31 \
 | gawk '{for (i=2;i&lt;=NF;i+=2) print $1"_"$i,$(i+1)}' | sort \
 > all.GTs
#981,326

# Obtaining the false donor sites

gawk '{print $1"_"$5+1}' pmarinus4training.gff | sort \
   |  join -v 1 all.GTs -  \
   > all.false_GTs.tbl
#979,004

#############  Obtaining all the AG sites

FindRegexp AG &lt; pmarinus4training.tbl\
 | join pmarinus4training.tbl  - | BoundarySites.sh +4 28 \
 | gawk '{for (i=2;i&lt;=NF;i+=2) print $1"_"$i,$(i+1)}' | sort \
 > all.AGs
#1,089,374

# Obtaining the false acceptor sites

gawk '{print $1"_"$4-2}'  pmarinus4training.gff | sort \
   |  join -v 1 all.AGs -  \
   > all.false_AGs.tbl
#1,087,071

############# Obtaining all the ATG sites 
FindRegexp ATG &lt; pmarinus4training.tbl \
 | join  pmarinus4training.tbl  - | BoundarySites.sh +2 30 \
 | gawk '{for (i=2;i&lt;=NF;i+=2) print $1"_"$i,$(i+1)}' | sort \
 > all.ATGs
#304,920


# Obtaining the false Start sites

gawk '{print $1"_"$4}' pmarinus4training.gff | sort \
   |  join -v 1 all.ATGs -  \
   > all.false_ATGs.tbl
#304,456
           </pre>
       </b-card-body>
   </b-card>
   <div>
       <b-card>
        <p> If the user goes through the training protocol described in the BASH scripts of the previous section she should now have the following files required in subsequent steps: </p>
       <p><strong>Set of files required in subsequent geneid training steps: </strong></p>
        <b-list-group>
            <b-list-group-item>Multi-fasta of training CDS sequences: <b-link href="https://genome.crg.cat/software/geneid/docs/training/output/all.cds.fa">all.cds.fa</b-link></b-list-group-item>
            <b-list-group-item>CDS sequences in tabular format: <b-link href="https://genome.crg.cat/software/geneid/docs/training/output/all.cds_filter1.tbl">all.cds.tbl</b-link></b-list-group-item>
            <b-list-group-item>Multi-fasta of training intronic sequences: <b-link href="https://genome.crg.cat/software/geneid/docs/training/output/all.intron.fa">all.intron.fa</b-link></b-list-group-item>
            <b-list-group-item>Intronic sequences in tabular format: <b-link href="https://genome.crg.cat/software/geneid/docs/training/output/all.intron.tbl">all.intron.tbl</b-link></b-list-group-item>
            <b-list-group-item>Annotation file corresponding to training set gene models: <b-link href="https://genome.crg.cat/software/geneid/docs/training/sequence/pmarinus4training.gff">pmarinus4training.gff</b-link></b-list-group-item>
            <b-list-group-item>Annotation file corresponding to training set gene models: <b-link href="https://genome.crg.cat/software/geneid/docs/training/sequence/pmarinus4evaluation.gff">pmarinus4evaluation.gff</b-link></b-list-group-item>
        </b-list-group>
       </b-card>
   </div>
    </b-col>
        </b-row>
    </b-container>
</template>
<script>
import PageHeadingComponent from '../components/PageHeadingComponent.vue'
export default {
    name: 'geneid-training',
    data() {
        return {
            header: {title: "geneid Training Tutorial"}
            // code1: ''
            
            
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
pre {
    color: #17a2b8 !important;
}
.training-container {
    max-height: 700px;
    overflow: scroll;
}
</style>