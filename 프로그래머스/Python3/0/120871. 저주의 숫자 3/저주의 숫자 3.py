def solution(n):
    answer = 1
    for i in range(n-1):
        answer += 1
        while True:
            if answer % 3 == 0 or str(answer).count("3") != 0:
                answer += 1
            else:
                break
    return answer