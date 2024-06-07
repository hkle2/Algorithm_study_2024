def solution(myString, pat):
    answer = 0
    if pat in myString.replace("A", "C").replace("B", "A").replace("C", "B"):
        answer = 1
    return answer