def solution(num, k):
    answer = 0
    a = str(num)
    for i in range(len(a)):
        if int(a[i]) == k:
            answer = i + 1
            break
        else:
            answer = -1
    return answer