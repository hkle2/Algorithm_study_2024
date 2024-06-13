def solution(arr):
    arr.remove(min(arr))
    if not arr:
        arr.append(-1)
    return arr

def solution(arr):
    answer = sorted(arr)
    arr.remove(answer[0])
    if not arr:
        arr.append(-1)
    return arr