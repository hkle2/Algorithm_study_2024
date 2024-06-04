def solution(num, k):
    answer = -1
    a = str(num)
    if a.find(str(k)) != -1:
        answer = a.find(str(k)) + 1
    return answer