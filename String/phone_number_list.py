import sys

input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    phone = set()
    N = (int(input().rstrip()))
    book = [input().rstrip() for _ in range(N)]
    book = sorted(book, reverse=True)
    flag = False

    for num in book:
        if num in phone:
            flag = True
            break

        for i in range(len(num)):
            cur = num[:i+1]
            phone.add(cur)
    if flag : print('NO') 
    else : print('YES')