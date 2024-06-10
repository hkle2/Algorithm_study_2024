import math

def solution(balls, share):
    answer = math.factorial(balls)
    answer /= math.factorial(share) * math.factorial(balls - share)
    return answer