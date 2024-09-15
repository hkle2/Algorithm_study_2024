import sys

N, K = map(int, sys.stdin.readline().split())
q = 0

for p in range(1, N+1):
    if N % p == 0:
        q += 1
        if q == K:
            print(p)
            break
if q != K:
    print(0)