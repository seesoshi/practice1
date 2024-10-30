import re
import string

def extract_emails(emails):
    listtext=emails.split(' ')
    listemails=re.findall(r"([a-zA-Z0-9_.-]+@[a-zA-Z0-9.]+\.[a-zA-Z]{2,6})", emails)
    res=[]
    for x in listtext:
        if x.strip(string.punctuation) in listemails:
            res.append(x.strip(string.punctuation))
    return res

def extract_durations(text):
    listdur=[]
    flist=re.findall(r"\d+h?\s*\d*m?\s*\d*s?",text)
    for i in flist:
        b=True
        if 's' or 'm' in i:
            partlist=re.sub(r'[^(a-zA-Z )]','',i).split()
            numlist=re.sub(r'[^(0-9 )]','',i).split()
            for j in range(len(partlist)):
                if (int(numlist[j])>=60 and (partlist[j]=='m' or partlist[j]=='s')): b=False
        if b: listdur.append(i)
    return listdur