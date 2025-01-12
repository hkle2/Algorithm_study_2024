import sys

X = int(sys.stdin.readline().strip())
N = int(sys.stdin.readline().strip())

answer = 0

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    answer += a * b

if X == answer:
    print("Yes")
else:
    print("No")