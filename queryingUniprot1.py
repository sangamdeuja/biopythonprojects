##In the UniProt materials is an unfinished program which grabs
##data from UniProt in a tabular format. Finish it such that the
##program produces a list of URec named tuples created from the
##tabular data. Preferably use the csv and StringIO modules.
##
##When submitting the exercise please also paste the relevant part
##of your program's output as a comment.

import requests
import collections
import csv #Check this one out
import StringIO

URec = collections.namedtuple('URec', 'id, entry_name, keywords')
q={"query":'organism:"Homo sapiens (Human) [9606]"',"columns":"id,entry name,keywords", "limit":10, "format":"tab"}
r=requests.get("http://www.uniprot.org/uniprot",params=q)


fileLike=StringIO.StringIO(r.text)
fieldNames=['id','entry_name','keywords']
# reads table in dictionary with key as fieldnames
f=csv.DictReader(fileLike,fieldnames=fieldNames,delimiter='\t')
for row in f:
    if not row['keywords']=='Keywords':
        print URec(**row)

    

