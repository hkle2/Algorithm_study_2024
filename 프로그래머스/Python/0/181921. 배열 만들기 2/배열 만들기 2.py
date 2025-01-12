def solution(l, r):
    answer = []
    for i in range(l, r+1):
        s = str(i)
        a = True
        for j in s:
            if int(j) % 5 != 0:
                a = False
        if a == True:
            answer.append(i)
    if not answer:
        answer.append(-1)
    return answer

def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if not set(str(i)) - set(["0", "5"]):
            answer.append(i)
    if not answer:
        answer.append(-1)
    return answer