import sys

A, B = sys.stdin.readline().split()
A, B = A[::-1], B[::-1]

print(max(A, B))