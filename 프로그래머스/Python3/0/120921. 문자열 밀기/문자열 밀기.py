from collections import deque

def solution(A, B):
    answer = 0
    if A == B:
        return 0
    for i in range(len(A)-1, -1, -1):
        if A[i:] + A[:i] == B:
            answer += 1
            return answer
        answer += 1
    return -1