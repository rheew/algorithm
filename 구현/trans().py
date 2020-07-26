from collections import deque

def isCollect(s):
    d = deque()
    for i in s:
        if i == '(': 
            d.append('(')
        else :
            if not len(d): return False
            d.pop()
    return True

def reverse(s):
    reverse = ''
    for i in s:
        if i == '(': reverse += ')'
        else : reverse += '('
    return reverse

def division(w):
    for i in range(2, len(w), 2):
        u = w[:i]
        if u.count('(') == u.count(')') : return u, w[i:]
    return w, ''
def DFS(w):
    if not len(w): return w
    
    u, v = division(w)
    if isCollect(u):
        u += DFS(v)
        return u
    else :
        ns = '(' + DFS(v) + ')'
        u = u[1:-1]
        ns += reverse(u)
        return ns
    
def solution(p):
    answer = DFS(p)
    
    return answer