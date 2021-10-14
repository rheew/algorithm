def solution(scores):
    answer = ''
    rotateArr = [list(i) for i in zip(*scores)]
    
    for i, score in enumerate(rotateArr):
        
        myScore = score[i]
        totalScore = sum(score)
        totalStudent = len(score)
        if score.count(myScore) == 1 and (max(score) == myScore or min(score) == myScore):
            totalScore -= myScore
            totalStudent -= 1
        
        avg = (totalScore / totalStudent)
        
        answer += grade(avg)
        
    return answer

def grade(avg):
    if avg >= 90: return 'A'
    elif 90 > avg >= 80: return 'B'
    elif 80 > avg >= 70: return 'C'
    elif 70 > avg >= 50: return 'D'
    else: return 'F'
