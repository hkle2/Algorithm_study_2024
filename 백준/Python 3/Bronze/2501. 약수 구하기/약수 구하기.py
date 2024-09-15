import sys

N, K = map(int, sys.stdin.readline().split())
q = []

for n in range(1, N+1):
    if N % n == 0:
        q.append(n)  
if len(q) >= K:
    print(q[K-1])
else:
    print(0)