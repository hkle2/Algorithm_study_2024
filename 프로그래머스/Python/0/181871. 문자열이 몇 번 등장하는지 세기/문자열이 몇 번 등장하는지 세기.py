def solution(myString, pat):
    answer = 0
    n = len(pat)
    for i in range(len(myString)):
        if myString[i:i+n] == pat:
            answer += 1
    return answer