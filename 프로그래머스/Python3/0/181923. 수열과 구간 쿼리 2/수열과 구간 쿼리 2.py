def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        l = []
        for j in range(s, e+1):
            if arr[j] > k:
                l.append(arr[j])
        if not l:
            answer.append(-1)
        else:
            answer.append(min(l))
    return answer
