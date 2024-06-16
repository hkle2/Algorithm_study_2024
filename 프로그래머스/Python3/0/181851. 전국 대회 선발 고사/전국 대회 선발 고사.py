def solution(rank, attendance):
    answer = []
    for i, a in enumerate(attendance):
        if a:
            answer.append([rank[i], i])
    answer = sorted(answer)
    return 10000 * answer[0][1] + 100 * answer[1][1] + answer[2][1]

def solution(rank, attendance):
    answer = sorted([[rank[i], i] for i, a in enumerate(attendance) if a])
    return 10000 * answer[0][1] + 100 * answer[1][1] + answer[2][1]