import sys, itertools

input = sys.stdin.readline

N = int(input())
li = [0 for _ in range(N)]

def DFS(li, temp):
    sum = 0
    if temp == N:
        return 1
    for i in range(N):
        check = False

        for j in range(temp):
            dif = temp - j
            if li[j] == i or li[j] == i + dif or li[j] == i - dif:
                check = True
                break
            if check: break
        if check: continue
        li[temp] = i
        sum += DFS(li, temp+1)
    return sum

print(DFS(li, 0))