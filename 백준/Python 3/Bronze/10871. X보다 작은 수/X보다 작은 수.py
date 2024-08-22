import sys

N, X = map(int, sys.stdin.readline().split(" "))
l = list(map(int, sys.stdin.readline().split(" ")))

for i in range(N):
    if l[i] < X:
        print(l[i], end=" ")