import sys

r = []

for i in range(10):
    r.append(int(sys.stdin.readline().strip()) % 42)

print(len(set(r)))