#fetching the sequence record of tp53 from genebank database
from Bio import Entrez
from Bio import SeqIO
Entrez.email='sangam.deuja@utu.fi'

tp53_rec_gene=SeqIO.read(Entrez.efetch(db="nucleotide",id=["NM_001276697.1"],rettype="gb"),"gb")
for f in tp53_rec_gene.features:
    if f.type=="CDS":
        print "CDS at", f.location
        extracted=f.extract(tp53_rec_gene)
        print extracted
        print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
        print repr(extracted)
        print extracted.seq
    
