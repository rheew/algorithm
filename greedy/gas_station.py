import sys
input = sys.stdin.readline

N = int(input().rstrip())
INF = int(1e10)

cost = list(map(int, input().rstrip().split()))
city = list(map(int, input().rstrip().split()))

min_cost = INF
sum_cost = 0

for i in range(len(city) -1) :
    min_cost = min(min_cost, city[i])
    sum_cost += min_cost * cost[i]

print(sum_cost)