def solution(date1, date2):
    answer = 0
    for i in range(len(date1)):
        if date1[i] < date2[i]:
            answer = 1
            break
        elif date1[i] == date2[i]:
            answer = 0
        else:
            break
    return answer