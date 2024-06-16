def solution(n):
    answer = 0
    for i in range(n):
        answer += 1
        while answer % 3 == 0 or str(answer).count("3") != 0:
            answer += 1
    return answer

def solution(n):
    answer = 0
    for i in range(n):
        answer += 1
        while answer % 3 == 0 or "3" in str(answer):
            answer += 1
    return answer