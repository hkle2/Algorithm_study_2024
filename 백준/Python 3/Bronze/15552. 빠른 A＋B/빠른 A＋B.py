import sys

N = int(sys.stdin.readline().strip())

for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)