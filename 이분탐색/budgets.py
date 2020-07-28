def solution(budgets, M):
    answer = 0
    start = 0
    end = max(budgets)
    while start <= end:
        mid = (start + end) // 2
        sum = 0
        for i in budgets:
            if i < mid:
                sum += i
            else: sum += mid
        
        if sum <= M:
            start = mid + 1
        else : end = mid -1
    return start -1