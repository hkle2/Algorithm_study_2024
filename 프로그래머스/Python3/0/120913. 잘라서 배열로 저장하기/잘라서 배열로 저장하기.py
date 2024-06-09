def solution(my_str, n):
    answer = []
    s = ""
    for i in my_str:
        s += i
        if len(s) == n:
            answer.append(s)
            s = ""
    if s:
        answer.append(s)
    return answer

def solution(my_str, n):
    answer = []
    for i in range(0, len(my_str), n):
        answer.append(my_str[i:i+n])
    return answer