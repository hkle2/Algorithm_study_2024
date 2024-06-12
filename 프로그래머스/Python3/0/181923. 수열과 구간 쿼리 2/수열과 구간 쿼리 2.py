def solution(arr, queries):
    answer = []
    l = []
    for i in range(len(queries)):
        s, e, k = queries[i]
        for j in range(s, e+1):
            if arr[j] > k:
                l.append(arr[j])
        if not l:
            answer.append(-1)
            l = []
        else:
            answer.append(min(l))
            l = []
    return answer