def solution(common):
    if common[2] - common[1] == common[1] - common[0]:
        answer = common[-1] + common[2] - common[1]
    else:
        answer = common[-1] * common[2] / common[1]
    return answer

def solution(common):
    a, b, c = common[:3]
    if b - a == c - b:
        answer = common[-1] + (b - a)
    else:
        answer = common[-1] * (b / a)
    return answer