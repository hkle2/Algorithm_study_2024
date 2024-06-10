def solution(numbers, k):
    n = 0
    for i in range(k - 1):
        n += 2
    n %= len(numbers)
    answer = numbers[n]
    return answer

def solution(numbers, k):
    answer = numbers[2 * (k - 1) % len(numbers)]
    return answer