def solution(a, b, c):
    answer = 0
    e1 = a + b + c
    e2 = a**2 + b**2 + c**2
    e3 = a**3 + b**3 + c**3
    if a != b and b != c and a != c:
        answer = e1
    elif a == b == c:
        answer = e1 * e2 * e3
    else:
        answer = e1 * e2
    return answer

def solution(a, b, c):
    answer = 0
    n = set([a, b, c])
    e1 = a + b + c
    e2 = a**2 + b**2 + c**2
    e3 = a**3 + b**3 + c**3
    if len(n) == 3:
        answer = e1
    elif len(n) == 2:
        answer = e1 * e2
    else:
        answer = e1 * e2 * e3
    return answer