import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input().rstrip())

number = list(map(int, input().rstrip().split()))
li = []
number.reverse()
for i in number :
    ind = bisect_left(li, i)
    if ind == len(li) :
        li.append(i)
    else : li[ind] = i

print(len(li))