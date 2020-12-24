def solution(routes):
    answer = 0
    
    routes_end = sorted(routes, key = lambda x : x[1])
    pre = -300001
    
    for start, end in routes_end:

        if pre >= start: continue
        pre = end
        answer += 1
        
        
    return answer