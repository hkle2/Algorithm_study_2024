import sys

N, M = map(int, sys.stdin.readline().split())
basket = [n for n in range(1, N+1)]

for m in range(M):
    i, j = map(int, sys.stdin.readline().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

for ball in basket:
    print(ball, end=" ")