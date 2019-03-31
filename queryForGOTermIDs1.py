##Idea: we have go.ogo file which contains annotations of each GO term.
## we browsed the 200 longest record of human protein p53.
##We searched the GO term involved in each entry and found the celluar compomnent
##involved with these GO terms



import collections
import StringIO
import requests
from Bio import SeqIO


q={"query":'name:p53 AND reviewed:yes AND organism:"Homo sapiens (Human) [9606]"'}
q["limit"]=200
q["sort"]="length"
q["format"]="xml"
r=requests.get("http://www.uniprot.org/uniprot",params=q)
xml_data=r.text




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


myfile=open("C:\\Users\\Amrit\\Desktop\\Sangam\\go.obo")
myDict= myfunct(myfile)

putFlag=False
for records in SeqIO.parse(StringIO.StringIO(xml_data),"uniprot-xml"):
    lis=[]
    cellularComponents=[]
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
            if findValue.namespace=='cellular_component':
                termName=findValue.name
                cellularComponents.append(termName)
    
    ccInString=','.join(str(x) for x in cellularComponents)
    
    print saveNameID[0], saveNameID[1] , ":" ,ccInString
            










