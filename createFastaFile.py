##Below is a list of UniProt IDs. Make a text file with these IDs.
##Then write a program which will read this text file and produce a
##FASTA file with their sequences.
##
##P00915
##
##P00918
##
##P43166
##
##P07451
##
##Q8N1Q1
##
##P35219
##
##
##P35218
##
##Q9Y2D0
##
##
##P23280
##
##O75493
##
##Q9NS85
##
##
##Q16790
##
##O43570
##
##Q9ULX7
##
##P22748
##
##Q99N23
##


import requests

##read the file and saving the ids in list
ids=[]
file=open('someids.txt')
for line in file:
    line=line.strip()
    a=line.split()
    if not a==[]:
        ids.extend(a)

file.close()
fid=open('getFasta.fasta','w')
##producing query for exch item in list and generating the requests
for i in range(0,len(ids)):
    query_value='accession:'+ids[i]+' AND reviewed:yes'
    q={"query":query_value}
    q["format"]="fasta"
    r=requests.get("http://www.uniprot.org/uniprot",params=q)
    fid.write(r.text)
fid.close()


file=open('getFasta.fasta')
a=file.read()
print a
    

