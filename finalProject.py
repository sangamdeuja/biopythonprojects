##Combine all the bits and pieces from the many exercises in UniProt and GO and BLAST into a
##single program which, given a file with Uniprot identifiers will query Uniprot for their sequences
##, run them through NCBI Blast, pick the nearest neighbors, and estimate the likely
##functions of these proteins. Test your program on the identifiers given in the UniProt and GO exercises.



from Bio.Blast import NCBIXML,NCBIWWW
from Bio import SeqIO
import StringIO
import re
import requests
import collections

##for the given query, this function returns the blast hits, q can be id or fasta sequence
def getBlast(q):
    result_handle = NCBIWWW.qblast("blastp", "swissprot", q)
    res=result_handle.read()
    blast_records=NCBIXML.parse(StringIO.StringIO(res))
    cnt=0
    e_threshold=1.0

    blastsPerIds={}
    for b_rec in blast_records:
        hit_list=[]
        for align in b_rec.alignments:
            for hsp in align.hsps:
                if hsp.expect<=e_threshold:
                    hit_list.append((hsp.expect,str(align.accession)))
    
        sp_idSorted=sorted(hit_list)
        blastsPerIds[ids[cnt]]=sp_idSorted
        cnt=cnt+1
        return blastsPerIds

##for the each blast hits, this function returns the associated molecular function
def requestUniprot(accessionNum,molecularFunct):
  
    queryValue='accession:'+accessionNum
    print queryValue
    q={"query":queryValue}
    q["format"]="xml"
    r=requests.get("http://www.uniprot.org/uniprot",params=q)
    xml_data=r.text
   
    putFlag=False

    records=SeqIO.read(StringIO.StringIO(xml_data),"uniprot-xml")
    lis=[]
    
    print records.dbxrefs
    for item in records.dbxrefs:
    
        if "GO:GO:" in item:
            putFlag=True
            go_term=item.replace("GO:GO:","GO:")
            lis.append(go_term)
    if putFlag:
        saveNameID=[records.id, records.name]
        putFlag=False

    for ontology_num in lis:
        ## seaching Go term in myDict keys and also checking if namespace is cellular component
        if ontology_num in myDict.keys():
            findValue=myDict[ontology_num]
            if findValue.namespace=='molecular_function':
                termName=findValue.name
                molecularFunct.append(termName)
    
    return molecularFunct



##function that returns dictionary with Go term id as key and id,name,namespace
##and defination as (namedtuple) key 
def myfunct(myfile):
    readmyfile=myfile.read()
    myDictionary={}
    
    NamedTuples=collections.namedtuple("GOTerm","id, name, namespace, definition")
    for lines in readmyfile.split("\n"):
##      flag variable to identify the required content is in between [Term] and emptyline
        if lines.strip()=="[Term]":
            flag=True
            current_term={}
        elif not lines.strip():
            flag=False

        else:
            if ": " in lines:
                key,value=lines.split(": ",1)
                if key in ["id","name","namespace","def"]:
                    if key=="def":
                        key="definition"
                    if flag:
                        ## only saves the contents from our requirement 
                        current_term[key]=value
                        if len(current_term)==4:
                            term=NamedTuples(**current_term)
                            myDictionary[term.id]=term
                            current_term={}
    return myDictionary




##main program starts here

##for the given uniport ids given in text, the program stores the ids in list

ids=[]
file=open("C:\\Users\\Amrit\\Desktop\\Sangam\\someids.txt")
for line in file:
    line=line.strip()
    a=line.split()
    if not a==[]:
        ids.extend(a)
file.close()


fid=open('getFasta.fasta','w')
##producing query for each item in list and generating the requests
for i in range(0,len(ids)):
    query_value='accession:'+ids[i]+' AND reviewed:yes'
    q={"query":query_value}
    q["format"]="fasta"
    r=requests.get("http://www.uniprot.org/uniprot",params=q)
    fid.write(r.text)
fid.close()

fid=open('C:\\Users\\Amrit\\Desktop\\Sangam\\getFasta.fasta',"r")
fas=fid.read()
b=fas.count(">")

listedaaSeq=[]
aaSeq=""
counter=0
##capturing each fasta sequence as aaSeq(in string format) and appending in listedaaSeq from fasta file
##Alternatively sequence record can be formed to obtain sequence string by parsing fasta file
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



myfile=open("C:\\Users\\Amrit\\Desktop\\Sangam\\go.obo")
myDict= myfunct(myfile)





finalDict={}
molecularFunct=[]
count=0
for item in listedaaSeq:
    count=count+1
    getBlastResult=getBlast(item)
    for k,v in getBlastResult.iteritems():
        for ind in range(0,len(v)):
            accessionNum=v[ind][1]
            print accessionNum
            molecularFunct=requestUniprot(accessionNum,molecularFunct)
    functionSet=set(molecularFunct)
    finalDict[ids[count]]=functionSet
print functionSet



##{'P00918': set(['phosphatase activity', 'nickel cation binding', 'hydro-lyase activity', 'zinc ion binding', 'arylesterase activity', 'carbonate dehydratase activity', 'metal ion binding'])
##, 'Q9NS85': set(['phosphatase activity', 'nickel cation binding', 'hydro-lyase activity', 'zinc ion binding', 'arylesterase activity', 'carbonate dehydratase activity', 'metal ion binding']),
##'P07451': set(['phosphatase activity', 'nickel cation binding', 'hydro-lyase activity', 'zinc ion binding', 'arylesterase activity', 'carbonate dehydratase activity', 'metal ion binding']),
##'P43166': set(['phosphatase activity', 'nickel cation binding', 'hydro-lyase activity', 'zinc ion binding', 'arylesterase activity', 'carbonate dehydratase activity', 'metal ion binding']),
##'P22748': set(['protein tyrosine phosphatase activity', 'transmembrane receptor protein tyrosine phosphatase activity', 'phosphatase activity', 'nickel cation binding', 'hydro-lyase activity',
##               'fibroblast growth factor binding', 'identical protein binding', 'zinc ion binding', 'arylesterase activity', 'carbonate dehydratase activity', 'metal ion binding']),
##'P23280': set(['phosphatase activity', 'nickel cation binding', 'hydro-lyase activity', 'zinc ion binding', 'arylesterase activity', 'carbonate dehydratase activity', 'metal ion binding']),
##'Q9ULX7': set(['protein tyrosine phosphatase activity', 'transmembrane receptor protein tyrosine phosphatase activity', 'phosphatase activity', 'nickel cation binding', 'hydro-lyase activity',
##               'fibroblast growth factor binding', 'identical protein binding', 'zinc ion binding', 'arylesterase activity', 'carbonate dehydratase activity', 'metal ion binding']),
##'P00915': set(['phosphatase activity', 'nickel cation binding', 'hydro-lyase activity', 'zinc ion binding', 'arylesterase activity', 'carbonate dehydratase activity', 'metal ion binding']),
##'Q16790': set(['phosphatase activity', 'nickel cation binding', 'hydro-lyase activity', 'zinc ion binding', 'arylesterase activity', 'carbonate dehydratase activity', 'metal ion binding']),
##'O43570': set(['protein tyrosine phosphatase activity', 'transmembrane receptor protein tyrosine phosphatase activity', 'phosphatase activity', 'nickel cation binding', 'hydro-lyase activity',
##               'fibroblast growth factor binding', 'identical protein binding', 'zinc ion binding', 'arylesterase activity', 'carbonate dehydratase activity', 'metal ion binding']),
##'O75493': set(['phosphatase activity', 'nickel cation binding', 'hydro-lyase activity', 'zinc ion binding', 'arylesterase activity', 'carbonate dehydratase activity', 'metal ion binding']),
##'P35219': set(['phosphatase activity', 'nickel cation binding', 'hydro-lyase activity', 'zinc ion binding', 'arylesterase activity', 'carbonate dehydratase activity', 'metal ion binding']),
##'P35218': set(['phosphatase activity', 'nickel cation binding', 'hydro-lyase activity', 'zinc ion binding', 'arylesterase activity', 'carbonate dehydratase activity', 'metal ion binding']),
##'Q8N1Q1': set(['phosphatase activity', 'nickel cation binding', 'hydro-lyase activity', 'zinc ion binding', 'arylesterase activity', 'carbonate dehydratase activity', 'metal ion binding']),
##'Q99N23': set(['protein tyrosine phosphatase activity', 'transmembrane receptor protein tyrosine phosphatase activity', 'phosphatase activity', 'nickel cation binding', 'hydro-lyase activity',
##               'fibroblast growth factor binding', 'identical protein binding', 'zinc ion binding', 'arylesterase activity', 'carbonate dehydratase activity', 'metal ion binding']),
##'Q9Y2D0': set(['phosphatase activity', 'nickel cation binding', 'hydro-lyase activity', 'zinc ion binding', 'arylesterase activity', 'carbonate dehydratase activity', 'metal ion binding'])}
