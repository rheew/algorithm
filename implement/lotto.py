def solution(lottos, win_nums):
    wildCard = wildCardCount(lottos)
    collect = collectCount(win_nums, lottos)

    return [rank(wildCard + collect), rank(collect)]

def wildCardCount(userNums):
    return userNums.count(0)

def collectCount(answerNums, userNums):
    return len(set(answerNums) & set(userNums))

def rank(score):
    if score == 6:
        return 1
    elif score == 5:
        return 2
    elif score == 4:
        return 3
    elif score == 3:
        return 4
    elif score == 2:
        return 5
    return 6

l = [44, 1, 0, 0, 31, 25]
w = [31, 10, 45, 1, 6, 19]
print(solution(l, w))