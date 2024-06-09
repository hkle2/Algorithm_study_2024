def solution(myStr):
    answer = []
    s = ""
    for i in myStr:
        if i not in ["a", "b", "c"]:
            s += i
        else:
            if s != "":
                answer.append(s)
                s = ""
    answer.append(s)
    if answer == [""]:
        answer = ["EMPTY"]
    return answer