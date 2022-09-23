import re


def checkLenLimit(log):
    return len(log) <= 100

def checkBlankNum(log):
    return len(log) == 5

def checkNotWord(log):
    if re.search("[^a-zA-Z]", log):
        return False
    return True

def validationPasing(log):
    if len(log.split(' ')) != 2:
        return False

    value, key = log.split(' ')

    if not key or not value:
        return False
    return checkNotWord(value)

def checkKeyNaming(log):
    if log[0] != 'team_name':
        return False

    for i in range(1, 4):
        if not validationPasing(log[i]):
            return False

    if not checkNotWord(log[4]):
        return False
    return True

def validationLog(log):
    if not checkLenLimit(log):
        return False

    log = log.split(" : ")

    if not checkBlankNum(log):
        return False

    return checkKeyNaming(log)
    return True

def solution(logs):
    answer = 0
    for log in logs:
        if not validationLog(log):
            answer += 1
    return answer

# logs = ["team_name : db application_name : dbtest error_level : info message : test",
#         "team_name : test application_name : i dont care error_level : error message : x",
#         "team_name : thisIsJustForTest application_name : TestAndTestAndTestAndTest error_level : test message : IAlasTestingAndWillTestForever",
#         "team_name : oberavability application_name : LogViewer error_level : error"]

logs = ["team_name : MyTeam application_name : YourApp error_level : info messag : IndexOutOfRange",
        "no such file or file or directory",
        "team_name : recommend application_name : recommend error_level : info message : RecommendSuccess11",
        "team_name : recommend application_name : recommend error_level : info message : Success!",
        "team_name : db application_name : dbtest error_level : info message: test",
        "team_name : TeamTest application_name : TestApplication error_level : info message: ThereIsNoError"]
print(solution(logs))
