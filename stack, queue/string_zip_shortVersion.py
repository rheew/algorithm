def check(text, slen):
    textzip = [[text[i:i+slen]] for i in range(0,len(text),slen)]
   
    cnt = 1
    ans = ''
    for a, b in zip(textzip, textzip[1:]+['']):
        if a == b:
            cnt += 1
        else :
            if cnt > 1: ans += str(cnt) + a[0]
            else : ans += a[0]
            cnt = 1
    return ans
def solution(s):
    answer = len(s)
    for i in range(1, len(s)):
        answer = min(answer ,len(check(s, i)))
    
    return answer