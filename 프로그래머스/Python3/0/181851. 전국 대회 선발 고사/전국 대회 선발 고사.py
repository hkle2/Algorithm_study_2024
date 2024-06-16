def solution(rank, attendance):
    answer = []
    for i, r in enumerate(attendance):
        if r:
            answer.append([rank[i], i])
    answer = sorted(answer)
    return 10000 * answer[0][1] + 100 * answer[1][1] + answer[2][1]