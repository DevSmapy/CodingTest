# 프로그래머스 연습문제 > 둘만의 암호

def solution(s, skip, index):
    answer = ''
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    skip_char = list(skip)
    for select in skip_char:
        idx = alphabet.index(select)
        del alphabet[idx]
    t = ''.join(alphabet)*3
    n = 26 - len(skip)
    for select in s:
        idx = alphabet.index(select) + index
        #if n <= idx:
        #    idx -= n
        answer += t[idx]
    return answer

if __name__ == "__main__":
    answer = solution('aukks','wbqd',5)
