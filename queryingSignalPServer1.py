##Run the sequences from the previous exercise through the SignalP
##and TMHMM services (preferrably programmatically, but please
##don't crash that service ;) and gather, for each sequence,
##its ID and the YES/NO predictions from these two services.
##from Bio import SeqIO
##import StringIO
import requests
import re

##reading uniprot ids from someids.txt and returning sequence in fasta format form id list

ids=[]
myfile=open('someids.txt')
for line in myfile:
    line=line.strip()
    a=line.split()
    if not a==[]:
        ids.extend(a)
myfile.close()

def produceFasta(ids):
    fid=open('getFasta.fasta','w')
    for i in range(0,len(ids)):
        query_value='accession:'+ids[i]+' AND reviewed:yes'
        q={"query":query_value}
        q["format"]="fasta"
        r=requests.get("http://www.uniprot.org/uniprot",params=q)
        fid.write(r.text)
    fid.close()
    return 

fastaseq=produceFasta(ids)


q={"orgtype":"euk", "format":"short", "SEQPASTE":"getFasta.fasta", "configfile":"/usr/opt/www/pub/CBS/services/SignalP-4.1/SignalP.cf"}
r=requests.post("http://www.cbs.dtu.dk/cgi-bin/webface2.fcgi",data=q)
for line in r.text.split("\n"):
    match=re.search(r"jobid: (\S+)",line)
    if match:
        jobid=match.group(1)
        break
    

r=requests.get("http://www.cbs.dtu.dk//cgi-bin/webface2.fcgi",params={"jobid":jobid})
print r.text
