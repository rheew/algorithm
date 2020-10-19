import sys

input = sys.stdin.readline

N = int(input().rstrip())

numbers = [int(input().rstrip()) for _ in range(N)]
numbers.insert(0,0)
visit = [False] * (N + 1)

def check(init, node, visit, cnt) :
    if visit[node] and init == node : return True, cnt
    if visit[node] : return False, cnt
    visit[node] = True
    nextNode = numbers[node]

    return check(init, nextNode, visit, cnt + 1)

ans = 0
ansNumbers = []
for i in numbers :
    if visit[i] or i == 0 : continue
    nvisit = visit.copy()
    result, cnt = check(i, i, nvisit, 0)
    if result :
        for i in range(1, N+1):
            if visit[i] != nvisit[i] :
                ansNumbers.append(i)
                visit[i] = True
        ans += cnt

print(ans)
ansNumbers.sort()
for i in ansNumbers :
    print(i)