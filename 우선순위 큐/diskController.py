from collections import deque
import heapq
def solution(jobs):
    answer = 0
    deq = deque(sorted(jobs, key = lambda x : (x[0], x[1])))
    heap = []
    pretime = 0
    while len(heap) or len(deq):
        if not len(heap) and len(deq):
            d = deq.popleft()
            heapq.heappush(heap, (d[1], d[0]))
            pretime = d[0]
        while len(heap):
            time = heapq.heappop(heap)
            answer += pretime - time[1] + time[0] 
            pretime += time[0]
            print(answer, pretime)
            while len(deq) and deq[0][0] < pretime:
                d = deq.popleft()
                heapq.heappush(heap, (d[1], d[0]))
        
        
    return answer // len(jobs)