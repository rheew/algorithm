import sys
input = sys.stdin.readline

N = int(input())
li = [input().split() for _ in range(N)]
z = [ i for i in range(N)]
l =list(zip(li, z))

for i in sorted(l, key=lambda x : (int(x[0][0]),x[1])):
    print(i[0][0], i[0][1])