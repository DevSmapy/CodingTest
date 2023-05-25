# 프로그래머스 고득점 킷 > 힙 > 더 맵게

import heapq
def solution(scoville, K):
    answer = 0
    q = []
    for s in scoville:
        heapq.heappush(q,s)
    while len(q)>1:
        a = heapq.heappop(q)
        if a >=K :
            break
        answer += 1
        b = heapq.heappop(q)
        c = a + (b*2)
        heapq.heappush(q,c)
    if heapq.heappop(q) >= K:
        return answer
    
    return -1