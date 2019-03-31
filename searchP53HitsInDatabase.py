####Write a program which prints the number of hits for
##    protein name "p53" in the protein database with human
##    as the organism. As a second feature, the program should also
##    print the number of hits where the protein is not "partial"
##
from Bio import Entrez
from Bio import SeqIO
Entrez.email="sangam.deuja@utu.fi"
search_handle=Entrez.esearch(db='protein',retmax=50,term='(human[Organism]) AND p53[Protein Name]')
search_result=Entrez.read(search_handle)
##print search_result
print 'number of human protein p53 hits is ',search_result['Count']

efetch_handle=Entrez.efetch(db='protein',id=search_result['IdList'],rettype='gb')
seq_records=SeqIO.parse(efetch_handle,format='gb')
count=0
for record in seq_records:
##    print repr(record)
    if not 'partial' in record.description:
        count=count+1
print 'non-partial protein count is',count
