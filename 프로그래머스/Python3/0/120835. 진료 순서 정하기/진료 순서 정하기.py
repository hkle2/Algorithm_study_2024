def solution(emergency):
    answer = []
    l = sorted(emergency, reverse=True)
    for i, e in enumerate(emergency):
        answer.append(l.index(e) + 1)
    return answer

def solution(emergency):
    answer = []
    l = sorted(emergency, reverse=True)
    for i, e in enumerate(emergency):
        answer.append(l.index(e) + 1)
    return answer