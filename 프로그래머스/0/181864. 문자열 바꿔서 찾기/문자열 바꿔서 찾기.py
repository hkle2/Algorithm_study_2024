def solution(myString, pat):
    answer = 0
    new_string = ''
    for i in myString:
        if i == "A":
            new_string += "B"
        else:
            new_string += "A"
    if pat in new_string:
        answer = 1
    return answer