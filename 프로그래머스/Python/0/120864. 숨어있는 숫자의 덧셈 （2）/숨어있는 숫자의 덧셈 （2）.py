def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isalpha():
            my_string = my_string.replace(i, " ")
    arr = my_string.split()
    for i in arr:
        answer += int(i)
    return answer