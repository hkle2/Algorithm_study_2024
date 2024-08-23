import sys

N, M = map(int, sys.stdin.readline().split())
l = [str(n) for n in range(1, N+1)]

for m in range(M):
    i, j = map(int, sys.stdin.readline().split())
    l[i-1], l[j-1] = l[j-1], l[i-1]

print(" ".join(l))