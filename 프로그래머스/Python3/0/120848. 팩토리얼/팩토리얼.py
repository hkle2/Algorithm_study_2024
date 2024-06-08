def solution(n):
    answer = 1
    while True:
        mul = 1
        for i in range(1, answer+1):
            mul *= i
        if mul == n:
            break
        if mul > n:
            answer -= 1
            break
        answer += 1
    return answer