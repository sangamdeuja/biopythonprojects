##Given a sequence and its translation, find the coding table(s)
##which produced it. Print the number of the table.

from Bio.Seq import Seq                                                         
from Bio.Alphabet import IUPAC                                                  
import Bio.Data                                                              
                                                                                
##s=Seq("ATGGTCGATGACCTGTGAACTTAA")                                               
s_ref=Seq("MVDDLCT*",IUPAC.protein)
####if 'TAA' in CT.generic_by_id[1].stop_codons:
####    print 'true'
### Hint: Bio.Data.CodonTable.generic_by_id                                       
##                                                                                
### Print the number of the table which                                           
### produced s_ref from s                                                         
###for i in range(0,len(CT.generic_by_id.keys())):
##a=len(CT.generic_by_id.keys())
##print a
##for key in CT.generic_by_id:
##    if 'TAA' in CT.generic_by_id[key].stop_codons:
##        print key
       
print Bio.Data.CodonTable.generic_by_id.values()

