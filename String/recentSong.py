def replaceString(string):
    string = string.replace('C#','c')
    string = string.replace('D#','d')
    string = string.replace('F#','f')
    string = string.replace('G#','g')
    string = string.replace('A#','a')

    return string

def timeCount(time2, time1):
    hour1, min1 = map(int, time1.split(':'))
    hour2, min2 = map(int, time2.split(':'))

    if min1 < min2:
        min1 += 60
        hour1 -= 1
    return (hour1 - hour2) * 60 + min1 - min2
def solution(m, musicinfos):
    answer = ''
    di = {}
    m = replaceString(m)
    for ind, i in enumerate(musicinfos):
        s = i.split(',')
        s[3] = replaceString(s[3])
        slen = len(s[3])
        minute = timeCount(s[0],s[1])
        n = minute // slen
        music = (s[3] * n) + s[3][:minute%slen]
        di[music] = (ind, minute, s[2])
    ans = sorted(di.items(), key = lambda x : (-x[1][1],x[1][0]))

    for key, value in ans:
        if m in key:
            return di[key][2]
    return '(None)'