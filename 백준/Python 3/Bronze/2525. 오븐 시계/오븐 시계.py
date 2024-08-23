import sys

A, B = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline().strip())

B += C
A += B // 60
B %= 60

if A < 24:
    print(A, B)
else:
    print(A - 24, B)