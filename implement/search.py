from collections import Counter, defaultdict

def solution(research, n, k):

    searchLog = defaultdict(list)
    issueList = defaultdict(int)

    for i in research:
        result = Counter(i)

        for word, count in result.items():
            searchLog[word].append(count)

    for word, count in searchLog.items():
        totalIssue = 0
        totalCount = 0

        for ind, j in enumerate(count):
            if totalIssue == n:
                totalIssue -= 1
                totalCount -= count[ind - n - 1]
            if j >= k:
                totalIssue += 1
                totalCount += j
            else:
                totalIssue = 0
                totalCount = 0

            if totalIssue >= n and totalCount >= 2 * k * n:
                issueList[word] += 1

    if not issueList:
        return "None"
    return sorted(issueList.items(), key=lambda x: (-x[1], x[0]))[0][0]

r, n, k = ["yxxy","xxyyy","yz"], 2, 1
print(solution(r, n, k))
