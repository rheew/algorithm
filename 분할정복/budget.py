import sys
input = sys.stdin.readline

N = int(input().rstrip())
budgets = list(map(int, input().rstrip().split()))
max_budget = int(input().rstrip())

start = 1
end = max(budgets)
ans = 0
while start <= end :
    mid = (start + end) // 2

    cnt = 0
    flag = True
    for budget in budgets :
        if budget < mid :
            cnt += budget
        else :
            cnt += mid

        if cnt > max_budget :
            flag = False
            break

    if flag :
        ans = mid
        start = mid + 1

    else :
        end = mid - 1

print(ans)