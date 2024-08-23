import sys

N, M = map(int, sys.stdin.readline().split())
basket = [0] * N

for m in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    for c in range(i, j+1):
        basket[c-1] = k

for ball in basket:
    print(ball, end=" ")
