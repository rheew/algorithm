def solution(A, B):
    answer = 0
    B.sort(reverse=True)
    A.sort(reverse=True)
    pre = 0
    post = len(B) - 1
    
    for i in range(len(A)) : 
        if A[i] >= B[pre] : continue
        pre += 1
        answer += 1
        
    return answer