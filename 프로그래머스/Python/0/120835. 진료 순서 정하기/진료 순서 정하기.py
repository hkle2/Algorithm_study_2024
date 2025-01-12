def solution(emergency):
    answer = []
    l = sorted(emergency, reverse=True)
    for i, e in enumerate(emergency):
        answer.append(l.index(e) + 1)
    return answer

def solution(emergency):
    answer = []
    dict = {}
    l = sorted(emergency, reverse=True)
    for i, e in enumerate(l):
        dict[e] = i + 1
    for e in emergency:
        answer.append(dict[e])
    return answer