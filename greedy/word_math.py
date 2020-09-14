import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input().rstrip())

words = [input().rstrip() for _ in range(N)]
wordcost = defaultdict(int)
wordtoint = {}
for word in words:

    cost = 1
    for i in range(len(word)-1, -1, -1) :
        wordcost[word[i]] += cost
        cost *= 10

result = sorted(wordcost.items(), key=lambda x : -x[1])
num = 9
for i in result :
    wordtoint[i[0]] = num
    num -= 1

totalsum = 0
for word in words :
    transword = ''
    for i in word :
        transword += str(wordtoint[i])

    totalsum += int(transword)

print(totalsum)

