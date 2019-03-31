##The record number 223468685 in NCBI's nucleotide database
##contains several genes, list them in order of appearance
from Bio import Entrez
from Bio import SeqIO
Entrez.email='sangam.deuja@utu.fi'
seq_record=SeqIO.read(Entrez.efetch(db='nucleotide',id='223468685',rettype='gb'),format='gb')
    ##print seq_record
for item in seq_record.features:
    ##    print item
    if item.type=='gene':
        print item.qualifiers['gene']
