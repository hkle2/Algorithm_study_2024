def solution(arr):
    a, b = len(arr), len(arr[0])
    if a > b:
        for i in range(len(arr)):
            arr[i] += [0] * (a - b)
    elif a < b:
        for i in range(b - a):
            arr.append([0] * b)
    return arr