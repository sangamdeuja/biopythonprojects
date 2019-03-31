import requests
import time
import re
##Note:
##for me the code of SignalP seems correct however the server provides 'N' signal everytime.
##Even I provided whole fastafile with n number of fasta sequences, similar response shown by signalp server
##tmhmm works perfectly well



##function that requests for signal prediciton for given fasta sequence
def requestSignalP(listedaaSeq):        
    for record in listedaaSeq:
        q={"orgtype":"euk", "format":"short", "SEQPASTE":record, "configfile":"/usr/opt/www/pub/CBS/services/SignalP-4.1/SignalP.cf"}
        r=requests.post("http://www.cbs.dtu.dk/cgi-bin/webface2.fcgi",data=q)
        time.sleep(10)
        for line in r.text.split("\n"):
            match=re.search(r"jobid: (\S+)",line)
            if match:
                jobid=match.group(1)
                break
        getSignalP(jobid)

##function that extract information from signalp job request
def getSignalP(jobid):
    r=requests.get("http://www.cbs.dtu.dk//cgi-bin/webface2.fcgi",params={"jobid":jobid})
    mytext=r.text
    valueList=[]
    flag=False
    print mytext
    for lines in mytext.split("\n"):
        if "# name" in lines:
            flag=True
        elif "name" not in lines and flag==True:
            a=lines.split(" ")
            for item in a:
                if item!="":
                    valueList.append(str(item))
            flag=False
            
        else:
            continue
    print "id is {} and signal p is {}".format(valueList[0],valueList[9])
    time.sleep(10)

    
##method to read whole result of n fasta sequences at a single submission from signalP server  
##def getSignalP(jobid):
##    print jobid
##    r=requests.get("http://www.cbs.dtu.dk//cgi-bin/webface2.fcgi",params={"jobid":jobid})
##    mytext=str(r.text)
##    print mytext
##    nameList=[]
##    valueList=[]
##    flag=False
##    for lines in mytext.split("\n"):
##        if "# name" in lines:
##            flag=True
##        elif "name" not in lines and flag==True:
##            a=lines.split(" ")
##            print a
##            signals=[item for item in a if item!=""]
##            print signals
##            valueList.append(signals[9])
##            nameList.append(signals[0])
##        elif "<hr>" in lines:
##            flag=False
##        else:
##            continue
##    for item in range(0,len(valueList)):
##        print "jobid is" ,nameList[item],"and signalP is ", valueList[item]
##         
##    return 



    
##function that requests for transmembrane helix prediction for given fasta sequence
def requestTmhmm(listedaaSeq):
    for record in listedaaSeq:
        q={ "outform":"-noplot", "SEQ":record, "configfile":"/usr/opt/www/pub/CBS/services/TMHMM-2.0/TMHMM2.cf"}
        r=requests.post("http://www.cbs.dtu.dk/cgi-bin/webface2.fcgi",data=q)
        time.sleep(10)
        for line in r.text.split("\n"):
            match=re.search(r"jobid: (\S+)",line)
            if match:
                jobid=match.group(1)
                break
        tmhmm(jobid)

##function that extract information from tmhmm job request
def tmhmm(jobid):
    r=requests.get("http://www.cbs.dtu.dk//cgi-bin/webface2.fcgi",params={"jobid":jobid})
    mytext=r.text
    for lines in mytext.split("\n"):
        if "Number of predicted TMHs" in str(lines):
            a=lines.split()
            print "id is {} and number of transmembrane helix is {}".format(a[1],a[6])



            
## program starts here
fid=open('C:\\Users\\Amrit\\Desktop\\Sangam\\getFasta.fasta',"r")
fas=fid.read()
b=fas.count(">")

listedaaSeq=[]
aaSeq=""
counter=0
##capturing each fasta sequence as aaSeq and appending in listedaaSeq from fasta file
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

user_choice=raw_input("please enter 1 for signalP service or 2 for tmhmm service\n ")
if user_choice=="1":
    requestSignalP(listedaaSeq)    
if user_choice=="2":
    requestTmhmm(listedaaSeq)

    


