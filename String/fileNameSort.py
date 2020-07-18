import re

def solution(files):
    di = {}
    headCompile = re.compile('\\D+')
    numberCompile = re.compile('\\d+')
    
    for ind, i in enumerate(files):
        head = headCompile.search(i).group(0)
        number = numberCompile.search(i).group(0)
        
        di[i] = (ind, head.lower(), int(number))
    answer = [i[0] for i in sorted(di.items(), key = lambda x : (x[1][1], x[1][2], x[1][0]))]
    print(di)
    return answer