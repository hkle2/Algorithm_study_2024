def solution(quiz):
    answer = []
    for i in quiz:
        q, a = i.split(" = ")
        if eval(q) == int(a):
            answer.append("O")
        else:
            answer.append("X")
    return answer

def solution(quiz):
    answer = []
    for q in quiz:
        eq = q.replace("=", "==")
        if eval(eq):
            answer.append("O")
        else:
            answer.append("X")
    return answer