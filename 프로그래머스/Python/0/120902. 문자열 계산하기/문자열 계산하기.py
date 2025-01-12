def solution(my_string):
    l = my_string.split()
    answer = int(l[0])
    for i in range(1, len(l)):
        if l[i] == "+":
            answer += int(l[i + 1])
        elif l[i] == "-":
            answer -= int(l[i + 1])
        else:
            continue
    return answer

def solution(my_string):
    answer = 0
    l = my_string.replace("- ", "+ -").split(" + ")
    for i in l:
        answer += int(i)
    return answer

def solution(my_string):
    answer = eval(my_string)
    return answer