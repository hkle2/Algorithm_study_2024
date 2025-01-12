def solution(clothes):
    answer = 1
    c = {}
    for v, k in clothes:
        if k not in c:
            c[k] = ["none"]
        c[k] += [v]
    for i in c.values():
        answer *= len(i)
    answer -= 1
    return answer