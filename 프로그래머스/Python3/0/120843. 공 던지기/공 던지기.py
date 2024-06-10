def solution(numbers, k):
    n = len(numbers)
    l = 0
    for i in range(k - 1):
        l += 2
    l %= n
    answer = numbers[l]
    return answer