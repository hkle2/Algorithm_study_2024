import sys

l = []

for _ in range(9):
    l.append(int(sys.stdin.readline().strip()))

print(max(l))
print(l.index(max(l)) + 1)