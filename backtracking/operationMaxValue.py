import re
from itertools import permutations

def countOper(oper, numbers, opers):
    di = { '-' : lambda x,y : x - y, '*' : lambda x,y : x * y, '+' : lambda x,y : x + y}
    num = numbers[:]
    op = opers[:]
    
    for i in oper:
        for j in i:
            for _ in range(op.count(j)):
                ind = op.index(j)
                x, y = int(num[ind]), int(num[ind+1])
                num[ind] = di[j](x,y)
                del num[ind+1]
                del op[ind]
        
    return abs(int(num[0]))

def solution(expression):
    answer = 0
    numberList = re.findall('\d+',expression)
    operList = re.findall('[-*+]',expression)
    operSet = set(operList)
    oper = list(permutations(operSet,len(operSet)))
    
    for i in oper:
        answer = max(countOper(i, numberList, operList), answer)

    return answer