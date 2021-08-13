# MarkovMatrices.awk
# rgs, imim, april 98
# usage=gawk -f MarkovMatrices order output_prefix cds_seqfile (.tbl)
#
# based on Borodosky and McIninch, Computers & Chemistry, 1993.

BEGIN {
  INF=99999999;
  k=ARGV[1];                   #order of the markov chain
  while (getline<ARGV[2]>0)    #initial probabilities
    P0[$1,$2]=$3;

  while (getline<ARGV[3]>0)
    P[$1,$2,$3]=$4;  #transition probabilities

  WLEN=ARGV[4];
  WSTEP=ARGV[5];
  STRAND=ARGV[6];
  ARGV[1]=ARGV[2]=ARGV[3]=ARGV[4]=ARGV[5]=ARGV[6]="";
  OFS="\t";
}

{
  locus=$1; sequence=$2;
  lseq=length(sequence); 
  printf ("%s\tMarkov\tMarkov\t0\t%d\t.\t%s\t.\tVector \"Markov\"\tscore;\tWindow %d;\tStep %d;\tScores",$1,lseq,STRAND,WLEN,WSTEP);

  lwseq=lseq-WLEN+1; # last position on the sequence to extract windows
  for (i=1; i<= lwseq; i+=WSTEP) {
    cu=-INF;
    wseq=substr(sequence, i, WLEN);
    for (F=0; F<3; F++)
      cu = max(cu, Markov(k,P0,P,wseq,WLEN,F)); 

    if (STRAND=="+")
	printf (" %.3f",cu);
    else
	v[i]=cu;
  }
}

END {
    if (STRAND=="-") 
	{
	    for(j=i;j>=0;j-=WSTEP)
		printf(" %.3f",v[j]);
	}
    printf "\n"}

function max(a,b) {
  return a > b ? a : b;
}

function Markov (k, P0, P, s, l, f,i){
  p=P0[(f%3),substr(s,1,k)];
  for (i=1;i<=l-k;i++) {
#    print ((i+f-1)%3)+1, substr(s,i,k+1),substr(s,i,k), P[((i+f-1)%3)+1,substr(s,i,k+1),substr(s,i,k)];
    p+=P[((i+f-1)%3),substr(s,i,k+1),substr(s,i,k)];
  }
  return p;
}

   
      
  
    
