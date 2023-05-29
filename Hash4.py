# 프로그래머스 고득점 킷 > 해시 > 의상


from itertools import combinations
from math import prod
from collections import Counter


def solution(clothes):
    n = len(clothes)
    answer = n
    c = 2
    category_list = [a[1] for a in clothes]
    count_list = [v for k,v in dict(Counter(category_list)).items()]
    cloth_set = set(category_list)
    m = len(cloth_set)
    
    if m == 1:
        return answer
    elif m == 2:
        answer += prod(count_list)
        return answer
    
    for t in range(c,m+1):
        answer += sum([prod(comb) for comb in combinations(count_list,t)])
    return answer


if __name__ == "__main__":
    clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    answer = solution(clothes)
    print(answer)