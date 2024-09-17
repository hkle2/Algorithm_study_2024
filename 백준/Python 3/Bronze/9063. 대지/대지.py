import sys

N = int(sys.stdin.readline().strip())
x_min, x_max = 100001, -100001
y_min, y_max = 100001, -100001

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    x_min, x_max = min(x_min, x), max(x_max, x)
    y_min, y_max = min(y_min, y), max(y_max, y)

print((x_max - x_min) * (y_max - y_min))