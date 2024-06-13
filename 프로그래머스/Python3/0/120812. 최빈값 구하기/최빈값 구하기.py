from collections import Counter

def solution(array):
    answer = 0
    c = Counter(array)
    for key, value in c.items():
        if value == max(c.values()) and answer == 0:
            answer = key
        elif value == max(c.values()):
            answer = -1
    return answer