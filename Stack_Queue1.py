# 프로그래머스 고득점 킷 > 스택/큐 > 같은 숫자는 싫어

def solution(arr):
    answer = [arr[0]]
    for i in arr[1:]:
        if answer[-1] == i:
            pass
        else:
            answer.append(i)
    return answer