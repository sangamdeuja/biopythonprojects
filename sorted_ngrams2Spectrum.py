# Write a function spectrum(s,N) which calculates the N-gram spectrum
# of the string s (with alphabet ACGT). The spectrum is a vector (list
# of numbers) with one position for every possible string of length N
# sorted alphabetically so eg "AAAA" will correspond to position 0,
# "TTTT" will correspond to position 255. For every N-gram, the vector
# contains the count of the N-gram in s.
#
# For example spectrum("AATTT",2) should return the following list
# [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]
# 
# which encodes the counts of the 2-gram AA AT and TT
#
# You should solve the exercise "DNA Ngram Index" first, because you
# can use it in this one.

def ngram2i(ngram):
    myDict={'A':0,'C':1,'G':2,'T':3}
    count=0
    for item in ngram:
        count=count*4+myDict[item]
    return count


def spectrum(s,N):
    vector=[0]*4**N
    myDict={}
    myList=[]
    result=[]
    resultVal=[]
    for i in range(0,len(s)-(N-1)):
        myList.append(s[i:i+N])
    for item in myList:
        myDict[item]=myList.count(item)
    for key,value in myDict.iteritems():
        result.append(ngram2i(key))
        resultVal.append(value)
    for i in range(0,len(result)):
        vector[result[i]]=resultVal[i]
    return vector


spectrum('AATTT',1)
        
