def solution(A, B):
    answer = 0
    if A == B:
        return 0
    for i in range(len(A)-1, -1, -1):
        answer += 1
        if A[i:] + A[:i] == B:
            return answer
    return -1