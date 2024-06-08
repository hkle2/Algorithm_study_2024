def solution(myString, pat):
    for i in range(1, len(myString)+1):
        if myString[:i].endswith(pat):
            answer = myString[:i]
    return answer

def solution(myString, pat):
    answer = myString[:myString.rfind(pat)+len(pat)]
    return answer
