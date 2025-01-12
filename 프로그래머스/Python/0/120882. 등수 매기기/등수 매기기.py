def solution(score):
    record = []
    for e, m in score:
        record.append(e + m)
    record.sort(reverse=True)
    return [record.index(e + m) + 1 for e, m in score]

def solution(score):
    record = [e + m for e, m in score]
    record.sort(reverse=True)
    return [record.index(e + m) + 1 for e, m in score]