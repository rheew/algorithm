N = input()
M = 0
if int(N) < 10:
    N = N+'0'
cnt = 0
ans = N
while(1):
    cnt += 1

    M = sum([int(i) for i in N])
    if(M < 10):
        N = "".join([N[1],str(M)])
    else:
        N = "".join([N[1]+str(M)[1]])

    if(N == ans):
        break


print(cnt)