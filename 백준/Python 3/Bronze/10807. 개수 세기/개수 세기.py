import sys
from collections import Counter

N = int(sys.stdin.readline())
c = Counter(list(map(int, sys.stdin.readline().split())))
v = int(sys.stdin.readline())

print(c[v])