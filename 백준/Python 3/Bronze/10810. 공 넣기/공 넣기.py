import sys

N, M = map(int, sys.stdin.readline().split())
l = ["0"] * N

for m in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    for c in range(i, j+1):
        l[c-1] = str(k)

print(" ".join(l))