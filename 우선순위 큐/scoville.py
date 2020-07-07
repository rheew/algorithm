import heapq
def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
        
    while K > heap[0]:
        if len(heap) < 2:
            return -1
        firstMin = heapq.heappop(heap)
        secondMin = heapq.heappop(heap)
        mix = firstMin + 2 * secondMin
        heapq.heappush(heap, mix)
        answer += 1
    return answer