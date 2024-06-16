def solution(rank, attendance):
    answer = []
    for i, r in enumerate(attendance):
        if r:
            answer.append([rank[i], i])
    answer = sorted(answer)
    a, b, c = answer[0][1], answer[1][1], answer[2][1]
    return 10000 * a + 100 * b + c