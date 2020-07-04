flag = False
def DFS(tickets, find, temp, visit):
    global flag
    answer = []
    if temp == len(tickets):
        flag  = True
        answer += ans
        return ans
    
    for ind, i in enumerate(tickets):
        if visit[ind] or i[0] != find or flag: continue
        visit[ind] = True
        ans.append(i[1])
        answer.extend(DFS(tickets, i[1], temp + 1, visit, ans))
        ans.pop()
        visit[ind] = False
    return answer
def solution(tickets):
    
    
    tickets.sort( key = lambda x : x[1])
    visit  = [0 for _ in range(len(tickets))]
    answer = DFS(tickets, "ICN", 0, visit, ['ICN'])
    
    return answer