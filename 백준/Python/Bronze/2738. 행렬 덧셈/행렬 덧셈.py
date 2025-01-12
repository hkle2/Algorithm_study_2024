import sys

N, M = map(int, sys.stdin.readline().split())
A = []
B = []

for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))
for _ in range(N):
    B.append(list(map(int, sys.stdin.readline().split())))

for i in range(len(A)):
    for j in range(len(A[0])):
        print(A[i][j] + B[i][j], end=" ")
    print()