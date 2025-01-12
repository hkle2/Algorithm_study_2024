import sys

N = int(sys.stdin.readline().strip())
l = list(map(int, sys.stdin.readline().split()))

print(min(l), max(l))
