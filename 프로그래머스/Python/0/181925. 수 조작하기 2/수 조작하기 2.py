def solution(numLog):
    answer = ''
    for i in range(len(numLog)-1):
        n = numLog[i + 1] - numLog[i]
        if n == 1:
            answer += "w"
        elif n == -1:
            answer += "s"
        elif n == 10:
            answer += "d"
        else:
            answer += "a"
    return answer

def solution(numLog):
    answer = ''
    n = dict(zip([1, -1, 10, -10], ["w", "s", "d", "a"]))
    for i in range(len(numLog)-1):
        answer += n[numLog[i + 1] - numLog[i]]
    return answer