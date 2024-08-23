import sys

l = []

for i in range(9):
    l.append(int(sys.stdin.readline().strip()))

print(max(l))
print(l.index(max(l)) + 1)