import sys

N = int(sys.stdin.readline().strip())
l = list(map(int, sys.stdin.readline().strip().split()))
v = int(sys.stdin.readline().strip())

print(l.count(v))