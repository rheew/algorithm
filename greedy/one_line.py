import sys

input = sys.stdin.readline

N = int(input().rstrip())

people = list(map(int, input().rstrip().split()))
ans = []
for i in range(N, 0, -1) :
    ans.insert(people[i-1], i)

for i in ans :
    print(i, end=' ')