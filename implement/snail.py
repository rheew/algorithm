def fillArray(n, arr, temp, starti, startj):
    if n <= 0 : return
    
    for i in range(n) :
        arr[i+ starti][startj] = temp
        temp += 1
    
    for i in range(1,n-1) :
        arr[n-1 + starti][i + startj] = temp
        temp += 1
    
    for i in range(n-1) :
        arr[n-1-i + starti][n-1-i + startj] = temp
        temp += 1
    fillArray(n - 3, arr, temp, starti + 2, startj + 1)

def solution(n):
    answer = []
    top = []
    for i in range(1, n+1) :
        make = [0] * i
        top.append(make)
        
    fillArray(n, top, 1, 0, 0)

    for i in top :
        answer.extend(i)
        
    return answer