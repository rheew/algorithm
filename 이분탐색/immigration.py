def solution(n, times):
    answer = 0
    end = max(times) * n
    start = 1
    if end == 1 : return 1
    while start <= end :
        mid = (start + end) // 2
        cnt = 0
        for i in times :
            cnt += mid // i
        
        if cnt >= n :
            end = mid - 1
        else :
            start = mid + 1
        
    answer = end + 1
    return answer