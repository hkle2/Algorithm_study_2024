def solution(n):
    a, b = 0, 1
    for i in range(n):
        # b, a = a, a+b
        a, b = b, a+b
    answer = a % 1234567
    return answer