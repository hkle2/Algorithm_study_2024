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