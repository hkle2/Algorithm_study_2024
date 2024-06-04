def solution(n):
    answer = []
    while True:
        if n % 2 == 0:
            answer.append(n)
            n /= 2
        else:
            answer.append(n)
            n = 3 * n + 1
        if n == 1:
            answer.append(n)
            break
    return answer