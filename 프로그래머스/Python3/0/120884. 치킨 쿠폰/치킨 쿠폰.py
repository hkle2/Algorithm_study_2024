def solution(chicken):
    answer = 0
    while chicken >= 10:
        answer += chicken // 10
        chicken = chicken // 10 + chicken % 10
    return answer

def solution(chicken):
    answer = 0
    while chicken >= 10:
        a, b = divmod(chicken, 10)
        answer += a
        chicken = a + b
    return answer

def solution(chicken):
    return (max(chicken, 1) - 1) // 9

def solution(chicken):
    return int(chicken * 0.111111)