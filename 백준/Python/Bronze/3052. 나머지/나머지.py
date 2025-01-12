import sys

l = []

for _ in range(10):
    l.append(int(sys.stdin.readline().strip()) % 42)

print(len(set(l)))