import requests

q={"query":'name:p53 AND reviewed:yes AND organism:"Homo sapiens (Human) [9606]"'}
q["limit"]=200
q["sort"]="length"
q["format"]="xml"
r=requests.get("http://www.uniprot.org/uniprot",params=q)
print r.text

f=open("human_200.xml","w")
f.close()
