def solution(a, b):
    answer = 0
    ab = int(str(a) + str(b))
    if ab >= 2 * a * b:
        answer = ab
    else:
        answer = 2 * a * b
    return answer