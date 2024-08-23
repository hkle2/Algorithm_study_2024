import sys

l = []

for i in range(10):
    l.append(int(sys.stdin.readline().strip()) % 42)

print(len(set(l)))