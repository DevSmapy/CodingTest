# 프로그래머스 고득점 킷 > 해시 > 폰켓몬

def solution(nums):
    n = set(nums)
    s = len(nums)//2
    if s < len(n):
        return s
    else:
        return len(n)