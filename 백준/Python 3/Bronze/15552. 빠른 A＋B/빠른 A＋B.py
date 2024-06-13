import sys

N = int(sys.stdin.readline())
for i in range(N):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    print(A + B)