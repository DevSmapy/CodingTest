# 프로그래머스 고득점 킷 > 스택/큐 > 기능개발

def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    days = []
    t = 1
    for i,j in zip(progresses,speeds):
        if (100-i)%j == 0:
            days.append((100-i)//j)
        else:
            days.append((100-i)//j+1)
    biggest = days[0]
    for i,j in zip(days[:-1],days[1:]):
        if biggest < j:
            biggest = j
            answer.append(t)
            t = 1
        else:
            t += 1
    answer.append(t)
    return answer