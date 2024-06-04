import numpy as np

def solution(n):
    answer = 2
    if np.sqrt(n) % 1 == 0:
        answer = 1
    return answer