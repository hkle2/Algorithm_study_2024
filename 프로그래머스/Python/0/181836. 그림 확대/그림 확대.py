def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        s = ""
        for j in picture[i]:
            s += j * k
        for j in range(k):
            answer.append(s)
    return answer

def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        for j in range(k):
            answer.append(picture[i].replace(".", "." * k).replace("x", "x" * k))
    return answer