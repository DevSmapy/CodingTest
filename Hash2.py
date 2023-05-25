# 프로그래머스 고득점 킷 > 해시 > 완주하지 못한 선수

def solution(participant, completion):
    answer = ''
    part_dict = {akey:0 for akey in participant}
    for part in participant:
        n = part_dict[part]
        part_dict[part] = n + 1
    for com in completion:
        n = part_dict[com]
        part_dict[com] = n-1
    for k,v in part_dict.items():
        for i in range(v):
            answer += ",{}".format(k)
    return answer.strip(",")

if __name__ == "__main__":
    participant = ["mislav", "stanko", "mislav", "ana"]
    completion = ["stanko", "ana", "mislav"]
    solution(participant, completion)