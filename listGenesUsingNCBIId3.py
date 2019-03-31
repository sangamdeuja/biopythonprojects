# http://rosalind.info/problems/prtm/
#
# now that you can translate the BTK gene, calculate the
# weight of the resulting protein
# using the following per-residue weight table
#
# Google the published weight. Did you get close?

from Bio import Entrez
from Bio import SeqIO


Entrez.email='sangam.deuja@utu.fi'
seq_record=SeqIO.read(Entrez.efetch(db='nucleotide',id='223468685',rettype='gb'),format='gb')
for feat in seq_record.features:
    if feat.type=='CDS'  and 'BTK' in feat.qualifiers['gene']:
        sequences=feat.sub_features[0].extract(seq_record)
        for count in range(1,len(feat.sub_features)):
            sequences=sequences+feat.sub_features[count].extract(seq_record)
protein_seq=str(sequences.seq.translate())
print protein_seq



weights={'A':71.03711,'C':103.00919,'D':115.02694,'E':129.04259,'F':147.06841,'G':57.02146,'H':137.05891,'I':113.08406,
         'K':128.09496,'L':113.08406,'M':131.04049,'N':114.04293,'P':97.05276,'Q':128.05858,'R':156.10111,'S':87.03203,
         'T':101.04768,'V':99.06841,'W':186.07931,'Y':163.06333,'*':0}
print weights


total_weight=0
for letter in protein_seq:
    total_weight=total_weight+weights[letter]
print total_weight

