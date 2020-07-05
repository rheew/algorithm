from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = set()
    d = deque()
    for i in cities:
        i = i.upper()
        if i in cache:
            answer += 1
            d.remove(i)
            d.append(i)
        else :
            answer += 5
            if cacheSize == 0 : continue
            if len(cache) == cacheSize:
                old = d.popleft()
                cache.remove(old)
            cache.add(i)
            d.append(i)
        
    return answer