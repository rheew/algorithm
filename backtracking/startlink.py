import itertools
import sys
from functools import reduce
input = sys.stdin.readline

N = int(input())
li = [list(map(int, input().rstrip().split())) for _ in range(N)]

team = list(itertools.combinations(range(N),int(N/2)))
team = team[:int(len(team)/2)]
result = []
def teamStateSum(teamindex):
    x = teamindex[0]
    y = teamindex[1]
    return li[x][y] + li[y][x]

def teamReduce(teamCombi):
    result = (reduce(
        lambda x, y : (x + y), (teamStateSum(i) for i in teamCombi)
    ))

    return result

def teamCombiList(t):
    r = teamReduce(list(itertools.combinations(t, 2)))
    return r

for i in team:
    teamB = [j for j in range(N)]
    for j in i:
        teamB.remove(j)

    result.append(abs(teamCombiList(i) - teamCombiList(teamB)))

print(min(result))
