def solution(myString):
    answer = []
    l = myString.split("x")
    l.sort()
    for i in l:
        if i:
            answer.append(i)
    return answer

def solution(myString):
    answer = " ".join(myString.split("x")).split()
    answer = sorted(answer)
    return answer