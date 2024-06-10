def solution(sides):
    answer = 0
    sides.sort()
    a, b = sides
    for i in range(b-a+1, b+1):
        answer += 1
    for i in range(b+1, a+b):
        answer += 1
    return answer

def solution(sides):
    answer = 2 * min(sides) - 1
    return answer