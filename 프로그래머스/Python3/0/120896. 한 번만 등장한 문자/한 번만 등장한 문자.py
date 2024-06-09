def solution(s):
    answer = ''
    dict = {}
    for i in s:
        if i not in dict:
            dict[i] = 0
        dict[i] += 1
    for key, value in dict.items():
        if value == 1:
            answer += key
    answer = "".join(sorted(answer))
    return answer

def solution(s):
    answer = "".join(sorted(i for i in s if s.count(i) == 1))
    return answer

def solution(s):
    answer = ''
    for i in s:
        if s.count(i) == 1:
            answer += i
    answer = "".join(sorted(answer))
    return answer