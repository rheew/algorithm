from collections import defaultdict
def solution(genres, plays):
    answer = []
    li = []
    playSum = defaultdict(int)
    for ind, i in enumerate(genres):
        li.append([ind, i, plays[ind]])
        playSum[i] += plays[ind]
    result  =  sorted(li, key = lambda x : (-x[2],x[0]))
    playSum = dict(sorted(playSum.items(), key = lambda x: -x[1]))
    
    for genre in playSum.keys():
        count = 0
        for i in result:
            if count == 2 : break
            if i[1] == genre:
                answer.append(i[0])
                count += 1
    return answer