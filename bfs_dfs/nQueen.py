def DFS(n, temp, li):
    cnt = 0
    
    if temp == n:
        return 1
    
    for i in range(n):
        if temp > 0:
            flag = False
            for j in range(temp):
                dif = temp - j
                if abs(li[j] - i) == dif or li[j] == i:
                       flag = True
                       break
            if flag: continue
        li[temp] = i
        cnt += DFS(n, temp+1, li)
                       
    return cnt
                       
def solution(n):
    li = [0 for _ in range(n)]
    answer = DFS(n, 0, li)
    return answer