##Write a function, which given the output of BLAST will
##, for each query sequence in the output, gather a list
##of (e-score, SequenceID) tuples, sorted by e-score in
##ascending order. I leave the details on you - do things
##the best way you see fit to incorporate the program into
##the larger task we are building (as discussed on lectures).



##Note:default handler result during blast is in xml format

from Bio.Blast import NCBIWWW,NCBIXML
import StringIO
import re
import requests

def getBlastHits(querySeq):
    e_threshold=1.0
    hit_list=[]
    ##Alternatively, instead of providing string we can provide sequence record for qblast.
    result_handle = NCBIWWW.qblast("blastp", "swissprot", querySeq)
    res=result_handle.read()
    blast_records=NCBIXML.parse(StringIO.StringIO(res))
    for b_rec in blast_records:
       for align in b_rec.alignments:
           for hsp in align.hsps:
               if hsp.expect<=e_threshold:
                   sp_id=re.search('sp\|(.*)\|',str(align.title)).group(1)
                   hit_list.append((hsp.expect,sp_id))
    sp_idSorted=sorted(hit_list)
    return sp_idSorted

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

## program starts here
fid=open('C:\\Users\\Amrit\\Desktop\\Sangam\\getFasta.fasta',"r")
fas=fid.read()
b=fas.count(">")

listedaaSeq=[]
aaSeq=""
counter=0
##capturing each fasta sequence as aaSeq(in stting format) and appending in listedaaSeq from fasta file
for lines in fas.split("\n"):
    if ">" in lines:
        counter=counter+1
        if aaSeq!="":
            listedaaSeq.append(aaSeq)

        aaSeq=""
        aaSeq=aaSeq+lines+"\n"
    else:
        aaSeq=aaSeq+lines.strip()
        if counter==b:
            counter=0
            listedaaSeq.append(aaSeq)
fid.close()
blastsPerIds={}
for item in range(0,len(ids)):
        blastsPerIds[ids[item]]=getBlastHits(listedaaSeq[item])

print blastsPerIds

##
##{'P00918': [(0.0, 'P00918.2'), (2.42754e-167, 'P00919.3'), (2.77623e-158, 'P00920.4'), (6.90025e-157, 'P00921.3'),
##(2.19759e-156, 'P27139.2'), (2.25327e-155, 'P00922.2'), (1.90984e-140, 'P07630.3'), (4.20168e-124, 'Q8UWA5.3'),
##(2.30858e-120, 'Q92051.2'), (6.78507e-117, 'P83299.1'), (1.52532e-116, 'Q9D6N1.1'), (4.34411e-112, 'P14141.3'),
##(4.68815e-112, 'P16015.3'), (3.22714e-111, 'Q8N1Q1.1'), (6.12207e-111, 'Q5S1S4.3'), (1.46262e-110, 'P07450.2'),
##(9.73052e-110, 'Q7M316.3'), (1.80792e-109, 'P07451.3'), (2.24968e-109, 'Q7M317.3'), (5.55692e-109, 'Q8HY33.1'),
##(6.68041e-109, 'P00915.2'), (2.77714e-108, 'Q3SZX4.3'), (5.88948e-108, 'P13634.4'), (9.30183e-108, 'B0BNN3.1'),
##(1.08326e-107, 'P00916.2'), (1.97084e-107, 'P35217.2'), (1.93635e-106, 'P48282.2'), (4.10209e-106, 'P00917.3'),
##(1.27426e-105, 'P43166.1'), (1.16585e-102, 'Q9ERQ8.2'), (2.99793e-102, 'Q1LZA1.3'), (7.81541e-95, 'P07452.1'),
##(3.54388e-93, 'Q9QZA0.2'), (1.98409e-92, 'Q66HG6.1'), (2.60119e-92, 'Q9Y2D0.1'), (2.03323e-87, 'P35218.1'),
##(1.31951e-86, 'P23589.2'), (1.40314e-84, 'P43165.1'), (2.57987e-60, 'P28651.5'), (3.31524e-60, 'P35219.3'),
##(1.54944e-59, 'Q5PPN4.3'), (1.18776e-45, 'Q8CI85.1'), (2.58831e-45, 'Q9WVT6.1'), (1.07789e-44, 'Q9ULX7.1'),
##(1.54147e-44, 'Q9MZ30.2'), (1.36361e-42, 'P18915.2'), (1.38343e-42, 'O43570.1'), (1.54585e-42, 'P23280.3'),
##(3.68236e-42, 'P18761.3'), (6.48984e-42, 'Q865C0.1')],
## 'P00915': [(0.0, 'P00915.2'), (0.0, 'P00916.2'),
##(0.0, 'P35217.2'), (0.0, 'Q7M316.3'), (0.0, 'Q7M317.3'), (4.30923e-160, 'P00917.3'), (6.457e-160, 'B0BNN3.1'),
##(3.84293e-155, 'P13634.4'), (1.51853e-151, 'P48282.2'), (1.10195e-148, 'Q1LZA1.3'), (2.19844e-141, 'Q8HY33.1'),
##(1.23997e-138, 'P07452.1'), (7.61792e-123, 'Q9D6N1.1'), (2.73101e-116, 'Q8N1Q1.1'), (6.00779e-115, 'Q8UWA5.3'),
##(3.52895e-113, 'Q92051.2'), (4.0676e-111, 'P00920.4'), (3.86863e-110, 'P83299.1'), (6.7061e-109, 'P00918.2'),
##(5.72223e-108, 'P00921.3'), (9.54306e-108, 'P00919.3'), (1.10393e-106, 'P07630.3'), (2.69402e-106, 'Q5S1S4.3'),
##(1.02694e-105, 'P27139.2'), (1.23556e-105, 'P16015.3'), (1.90916e-105, 'P00922.2'), (2.6459e-105, 'P14141.3'),
##(2.13587e-104, 'P07450.2'), (2.31194e-103, 'Q3SZX4.3'), (1.44024e-101, 'P07451.3'), (2.05262e-97, 'P43166.1'),
##(5.81547e-94, 'Q9ERQ8.2'), (2.2354e-85, 'Q66HG6.1'), (2.60071e-85, 'Q9QZA0.2'), (2.28265e-83, 'Q9Y2D0.1'),
##(4.26818e-80, 'P35218.1'), (1.9764e-78, 'P43165.1'), (3.97554e-77, 'P23589.2'), (3.19464e-59, 'P28651.5'),
##(6.93514e-59, 'P35219.3'), (1.24916e-58, 'Q5PPN4.3'), (2.74347e-49, 'Q8CI85.1'), (3.69476e-48, 'Q9MZ30.2'),
##(1.72853e-45, 'O43570.1'), (3.55171e-44, 'Q9WVT6.1'), (1.5017e-39, 'P18761.3'), (1.70274e-39, 'Q8VHB5.2'),
##(2.69023e-39, 'Q9ULX7.1'), (3.4715e-39, 'Q99N23.1'), (8.37363e-38, 'P94170.1')]}
           
