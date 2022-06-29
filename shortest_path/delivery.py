import heapq

class Unit:

    def __init__(self, pos, cost):
        self.pos = pos
        self.cost = cost

    def move(self, pos, cost):
        self.pos = pos
        self.cost = cost

    def __lt__(self, other):
        if self.cost < other.cost:
            return True
        else:
            return False

def solution(N, road, K):
    answer = 0

    town = [[] for _ in range(N + 1)]
    townCost = [500001] * (N + 1)

    for i in road:
        a, b, cost = i
        town[a].append([b, cost])
        town[b].append([a, cost])

    visitNode(town, townCost)

    for cost in townCost:
        if K >= cost:
            answer += 1

    return answer

def visitNode(town, townCost):
    h = []
    heapq.heappush(h, Unit(1, 0))
    townCost[1] = 0
    while len(h):
        unit = heapq.heappop(h)
        nowPos = unit.pos

        if townCost[nowPos] < unit.cost:
            continue


        for nextPos, cost in town[nowPos]:
            nextCost = cost + townCost[nowPos]

            if townCost[nextPos] > nextCost:
                townCost[nextPos] = nextCost
                heapq.heappush(h, Unit(nextPos, nextCost))

N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3

print(solution(N, road, K))