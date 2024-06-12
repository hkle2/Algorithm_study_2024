def solution(dots):
    answer = 0
    x = []
    y = []
    for i in dots:
        x.append(i[0])
        y.append(i[1])
    a, b = set(x)
    c, d = set(y)
    answer = abs(a - b) * abs(c - d)
    return answer