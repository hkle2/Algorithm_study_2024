def solution(l, r):
    answer = []
    for i in range(l, r+1):
        a = True
        s = str(i)
        for j in s:
            if int(j) % 5 != 0:
                a = False
        if a == True:
            answer.append(i)
    if not answer:
        answer.append(-1)
    return answer