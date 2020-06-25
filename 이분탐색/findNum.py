import sys
input = sys.stdin.readline

N = int(input())

li = set(map(int, input().rstrip().split()))

input()
findNum = list(map(int, input().rstrip().split()))

for i in findNum:
    if i in li:
        print(1)
    else : print (0)