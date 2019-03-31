#finding sequence similarity of DNA sequence using hamming distance method
from Bio.Seq import Seq

def hamming(s1,s2):
    count=0
    if len(s1)!=len(s2):
        pass
    else:
        for i in range(0,len(s1)):
            if s1[i]!=s2[i]:
                count=count+1
        return count
    


#sequence objects s1 and s2
s1=Seq("ACG")
s2=Seq("ACG")

print hamming(s1,s2)    

