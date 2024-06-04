def solution(numbers, n):
    answer = 0
    # for i in numbers:
    #     if answer <= n:
    #         answer += i
    #     else:
    #         break
    i = 0
    while answer <= n:
        answer += numbers[i]
        i += 1
    return answer