##Write a function sorted_ngrams(s,N) where s is a string and N is an integer.
##The function should print all unique substrings of s of length N, together
##with their count, and sorted from least to most common and alphabetically
##if of same frequency. For example for the string "ACGCTGAGGCTGAAAAAA"
##the output would be
##
##AC 1
##AG 1
##CG 1
##GG 1
##CT 2
##GA 2
##GC 2
##TG 2
##AA 5
import operator
def sorted_ngrams(s,N):
    counter=len(s)-N+1
    seqList=[]
    myDict={}
    
    
    for i in range(0,counter):
        seqList.append(operator.getslice(s,i,i+N))
    for item in seqList:
        myDict[item]=operator.countOf(seqList,item)
     
    for v in sorted(myDict.iteritems(),key=lambda(k, v): (v, k)):
        print v[0], v[1]
        
    
sorted_ngrams("ACGCTGAGGCTGAAAAAA",1)
    
        
