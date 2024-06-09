def solution(arr):
    answer = []
    idx = []
    for i in range(len(arr)):
        if arr[i] == 2:
            idx.append(i)
    if idx:
        answer = arr[idx[0]:idx[-1]+1]
    else:
        answer = [-1]
    return answer

def solution(arr):
    if 2 not in arr:
        answer = [-1]
    else:
        answer = arr[arr.index(2):len(arr)-arr[::-1].index(2)]
    return answer