import re

def solution(lines):
    answer = 0
    time = []
    numcomp = re.compile('\d.\d+|\d')

    for i in lines:
        s = i.split()
        hour, minute, second = s[1].split(':')
        milisec = int(float(second) * 1000) 
        endTime = ((int(hour) * 60 + int(minute)) * 60) * 1000 + int(milisec)
        during = numcomp.search(s[2]).group(0)
        dTime = int(float(during) * 1000)
        startTime = endTime - dTime + 1
        time.append((startTime, endTime))

    time.sort(key = lambda x : x[1])
    for ind, i in enumerate(time):
        cnt = 1
        for j in range(ind+1 ,len(time)):
            if time[j][0] - 999 <= i[1] <= time[j][1] + 999: 
                cnt += 1

        answer = max(answer, cnt)

    return answer