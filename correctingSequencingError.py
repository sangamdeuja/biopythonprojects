# http://rosalind.info/problems/corr/ As is the case with point
# mutations, the most common type of sequencing error occurs when a
# single nucleotide from a read is interpreted incorrectly.

# Given: A collection of reads of equal length in FASTA format. Some
# of these reads were generated with a single-nucleotide error. For
# each read s in the dataset, one of the following applies:

# s was correctly sequenced and appears in the dataset at least twice (possibly as a reverse complement)
# s is incorrect, it appears in the dataset exactly once, and its Hamming distance is 1 with respect to exactly one correct read in the dataset (or its reverse complement)
# 
# Write a function correct(data) where data is a string with the sequences in FASTA  formar
# and the function returns a list of [(s,s_corrected),(s,s_corrected),...]  pairs of sequences and their corrections:
# s should be one of the sequences in the data and s_corrected should be one of the sequences in the data or its reverse complement, such that the hamming distance of s and s_corrected is 1
# order does not matter
#
# For example for the data below, the function should return
#
# [("GAGGA","GATGA"),("TTCAT","TTGAT"),("TTTCC","TTTCA")]
#
# ...in whatever order

import Bio.Seq
import Bio.SeqIO
import StringIO

##This is much longer method :(


def correct(data):
    myDict={}
    myList=[]
    error_sequences=[]
    to_return=[]
##  for record in Bio.SeqIO.parse(data,'fasta')
    for record in Bio.SeqIO.parse(StringIO.StringIO(data),'fasta'):
        myList.append(record.seq)
##Identifying the sequence that does not repeats in list or has its reverse complement
    for item in myList:
        if myList.count(item)==1 and item.reverse_complement() not in myList:
            error_sequences.append(item)
##  print error_sequences
    nextList=myList

##Creating anotherList to save the sequences that doubles or has reverse complement in the original list    
    for item in error_sequences:
        if item in myList:
            nextList.remove(item)
    anotherList=nextList
    for item in nextList:
        if nextList.count(item)>1:
            anotherList.remove(item)
        elif item.reverse_complement() in nextList:
            anotherList.remove(item)
        else:
            continue

##  print anotherList
##Identifying the point mutation through hamming distance and returning incorrect sequence and corrected sequence
    for item1 in anotherList:
        for item2 in error_sequences:
            if hamming(item1,item2)==1:
                to_return.append((str(item2),str(item1)))
            elif hamming(item1.reverse_complement(),item2)==1:
                item3=item1.reverse_complement()
                to_return.append((str(item2),str(item3)))
            else:
                continue
        
    return to_return
        
        


         
def hamming(s1,s2):
    count=0
    if len(s1)!=len(s2):
        pass
    else:
        for i in range(0,len(s1)):
            if s1[i]!=s2[i]:
                count=count+1
        return count
    

##mydata=open('C:\\Users\\Amrit\\Desktop\\data.txt','r')
data="""
>Rosalind_52
TCATC
>Rosalind_44
TTCAT
>Rosalind_68
TCATC
>Rosalind_28
TGAAA
>Rosalind_95
GAGGA
>Rosalind_66
TTTCA
>Rosalind_33
ATCAA
>Rosalind_21
TTGAT
>Rosalind_18
TTTCC
"""

correct(data) 
