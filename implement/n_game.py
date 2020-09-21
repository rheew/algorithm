def trans(n, value):
    re = 0
    v = 0
    s = ''

    while value:
        v = value // n
        re = value % n
        if re >= 10:
            s = chr(65 + re - 10) + s
        else : s = str(re) + s
        value = v
    return s

def solution(n, t, m, p):
    answer = '0'
    num = t * m
    for i in range(1, num):
        answer += trans(n, i)

    return answer[p-1 : : m][:t]