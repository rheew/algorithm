import re
from collections import defaultdict

def solution(word, pages):
    c = re.compile('(?<=[\W\d])'+word.upper()+'[\W\d]')
    meta = re.compile('<meta[\w.:"= /]+')
    a = re.compile('<a [\w.:"= /]+')
    https = re.compile('https:[\w\./]+')
    pageurl = defaultdict(list)
    link = defaultdict(list)
    
    ans = []
    
    for ind, i in enumerate(pages):
        metastring = meta.findall(i)
        astring = a.findall(i)
        httpsstring = ''

        for m in metastring:
            find = https.findall(m)
            if find : 
                httpsstring = find
        
        for s in astring:
            
            find = https.findall(s)
            if find : 
                link[httpsstring[0]].extend(find)
                
        li = c.findall(i.upper())
        
        pageurl[httpsstring[0]].extend([len(li), ind, 0])
    
    
    for key in list(pageurl.keys()) :
        
        for j in link[key]:
            if j in pageurl :
                pageurl[j][2] += pageurl[key][0] / len(link[key])

    for key in list(pageurl.keys()) :
        basic, index, linkscore= pageurl[key]
        ans.append([basic + linkscore, index])
        
    answer = sorted(ans, key=lambda x : -x[0])
    return answer[0][1]