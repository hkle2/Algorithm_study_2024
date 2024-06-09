def solution(arr):
    n = len(arr)
    i = 0
    while True:
        if 2**i >= n:
            break
        i += 1
    for i in range(2**i - n):
        arr.append(0)
    return arr

def solution(arr):
    n = len(arr)
    i = 0
    while True:
        if 2**i >= n:
            break
        i += 1
    answer = arr + [0] * (2**i - n)
    return answer