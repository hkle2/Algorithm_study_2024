import sys

N = int(sys.stdin.readline().strip())
l = []

for _ in range(N):
    l.append(int(sys.stdin.readline().strip()))
l.sort()

for i in range(len(l)):
    print(l[i])