##Below is a list of UniProt protein IDs.
##Map these to RefSeq protein IDs using the UniProt ID mapping service.
##Best will be to write a function which takes a list of IDs and returns a dictionary
##where each protein is a key and the value is a list of RefSeq identifiers.


import urllib,urllib2


def uniProtIdMapping(ids):
    url = 'http://www.uniprot.org/mapping/'

    params = {
    'from':'ACC+ID',
    'to':'P_REFSEQ_AC',
    'format':'tab',
    'query':ids
    }

    data = urllib.urlencode(params)
    request = urllib2.Request(url, data)
    response = urllib2.urlopen(request)
    page = response.read()


    idDict={}
    for lines in page.split("\n"):
        if not lines.strip() is "":
            k,v=lines.split()
            idDict.setdefault(k,[]).append(v)
    if "From" in idDict.keys():
        del idDict["From"]
    return idDict
     

myFile=open("C:\\Users\\Amrit\\Desktop\\Sangam\\UniProtIDs.txt")
ids=myFile.read()
print uniProtIdMapping(ids)

