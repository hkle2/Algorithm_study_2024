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

def solution(myStr):
    arr = myStr.replace("a", " ").replace("b", " ").replace("c", " ")
    answer = arr.split()
    if not answer:
        answer = ["EMPTY"]
    return answer