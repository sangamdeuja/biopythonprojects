##The record number 223468685 in NCBI's nucleotide database
##contains several genes. One of them is a gene called "BTK"
##concatenate its CDSs together and tranlate them into a
##protein print its sequence 
from Bio import Entrez
from Bio import SeqIO


Entrez.email='sangam.deuja@utu.fi'
seq_record=SeqIO.read(Entrez.efetch(db='nucleotide',id='223468685',rettype='gb'),format='gb')
for feat in seq_record.features:
    if feat.type=='CDS'  and 'BTK' in feat.qualifiers['gene']:
        sequences=feat.sub_features[0].extract(seq_record)
        for count in range(1,len(feat.sub_features)):
            sequences=sequences+feat.sub_features[count].extract(seq_record)
            
print sequences.seq.translate()
