def solution(num, total):
    answer = []
    sum = 0
    if num % 2 != 0:
        m = total // num - num // 2
        for i in range(num):
            answer.append(m)
            m += 1
    else:
        m = total // num - num // 2 + 1
        for i in range(num):
            answer.append(m)
            m += 1
    return answer