def solution(arr, k):
    answer = []
    for i in range(len(arr)):
        if arr[i] not in answer and len(answer) < k:
            answer.append(arr[i])
    if len(answer) != k:
        for i in range(k-len(answer)):
            answer.append(-1)
    return answer