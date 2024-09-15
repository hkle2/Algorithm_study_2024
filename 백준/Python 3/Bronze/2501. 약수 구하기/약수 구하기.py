import sys

N, K = map(int, sys.stdin.readline().split())
k = 0

for q in range(1, N+1):
    if N % q == 0:
        k += 1
        if k == K:
            print(q)
            break
if k != K:
    print(0)