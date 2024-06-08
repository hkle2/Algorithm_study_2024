def solution(n):
    answer = 1
    f = 1
    while f <= n:
        answer += 1
        f *= answer
    answer -= 1
    return answer

import math

def solution(n):
    answer = 1
    while math.factorial(answer) <= n:
        answer += 1
    answer -= 1
    return answer