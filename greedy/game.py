import sys

input = sys.stdin.readline

N = int(input().rstrip())

numbers = [int(input().rstrip()) for _ in range(N)]
pre = numbers[N - 1]

ans = 0

for i in range(N - 2, -1, -1) :
    if pre <= numbers[i] :
        dif = numbers[i] - pre + 1
        ans += dif
        pre = numbers[i] - dif
    else : pre = numbers[i]

print(ans)