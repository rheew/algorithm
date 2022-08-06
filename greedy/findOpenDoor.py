def openDoor(time, start, close):

    for i in range(start, 5001):
        if i in close:
            break
        time[i] = True

def solution(openA, closeB):

    time = [False] * 5001
    for start in openA:
        if time[start]:
            continue

        openDoor(time, start, closeB)

    return time.count(True)

A, B = [4, 7, 9, 16], [2, 5, 12, 14, 20]
print(solution(A, B))
