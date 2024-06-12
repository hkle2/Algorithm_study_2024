def solution(dots):
    answer = 0
    x = []
    y = []
    for i, j in dots:
        x.append(i)
        y.append(j)
    answer = (max(x)- min(x)) * (max(y)- min(y))
    return answer