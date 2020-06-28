from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
li = [list(map(int, input().rstrip())) for _ in range(N)]

global dx, dy, visit
dx, dy = [0,0,1,-1], [-1,1,0,0]
visit = [[-1 for _ in range(M)] for _ in range(N)]

def BFS(N, M):

    d = deque()
    d.append([0,0])
    while len(d):
        nowd = d.popleft()
        for i in range(4):
            nextx = dx[i] + nowd[0];
            nexty = dy[i] + nowd[1];
            if nextx < 0 or nextx >= N or nexty < 0 or nexty >= M: continue
            if (visit[nextx][nexty] != -1 and visit[nextx][nexty] <= visit[nowd[0]][nowd[1]] + 1) or (li[nextx][nexty] == 0): continue
            if visit[nowd[0]][nowd[1]] == -1: visit[nowd[0]][nowd[1]] = 0
            visit[nextx][nexty] = visit[nowd[0]][nowd[1]] + 1
            d.append([nextx,nexty])

BFS(N,M)
print(visit[N-1][M-1] + 1)