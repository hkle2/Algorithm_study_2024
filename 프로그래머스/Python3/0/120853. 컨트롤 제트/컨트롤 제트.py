def solution(s):
    answer = 0
    l = s.split()
    for i in range(len(l)):
        if l[i] == "Z":
            answer -= int(l[i-1])
        else:
            answer += int(l[i])
    return answer