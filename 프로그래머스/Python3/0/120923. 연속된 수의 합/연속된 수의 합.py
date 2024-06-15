def solution(num, total):
    answer = []
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

def solution(num, total):
    answer = []
    m = total // num
    s = int(m - (num - 1) // 2)
    return [s+i for i in range(num)]