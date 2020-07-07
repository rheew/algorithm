from collections import deque
def check(s1, s2, slen):
    for i in range(slen):
        if s1[i] != s2[i]: return False
    return True

def solution(s):
    answer = len(s)

    for i in range(1, len(s)):
        d = deque(s)
        temp  = 1
        newString = ''
        pre = ''
        for _ in range(i):
            pre += d.popleft()

        while len(d) >= i:
            now = ''
            for j in range(i):
                now += d.popleft()

            if check(pre[-i:], now, i):
                temp += 1
                if len(d) < i:
                    newString += str(temp) + pre
                    pre = ''
            else :
                if temp > 1:
                    newString += str(temp) + pre
                else : newString += pre

                pre = now
                temp = 1
        answer = min(answer, len(newString)+len(pre)+len(d))
    return answer