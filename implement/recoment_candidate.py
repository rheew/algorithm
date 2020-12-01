import sys

input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())

recomends = list(map(int, input().rstrip().split()))
display = []
stays = [0] * 1001
scores = [0] * 1001

for i in recomends:
    scores[i] += 1
    if scores[i] != 1 : continue

    if len(display) < N :
        display.append(i)

    else :
        minvalue = 1001
        maxstay = 0
        index = 0

        for ind, j in enumerate(display) :

            stays[j] += 1
            nowvalue = scores[j]

            if minvalue > nowvalue :
                minvalue = nowvalue
                maxstay = stays[j]
                index = ind

            elif minvalue == nowvalue :
                if maxstay < stays[j]:
                    minvalue = nowvalue
                    maxstay = stays[j]
                    index = ind

        changevalue = display[index]
        display[index] = i
        stays[changevalue] = 0
        scores[changevalue] = 0

for i in sorted(display):
    print(i, end=' ')