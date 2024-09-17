import sys

N = int(sys.stdin.readline().strip())
x_min, x_max = 100001, -100001
y_min, y_max = 100001, -100001

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    x_max = max(x_max, x)
    x_min = min(x_min, x)
    y_max = max(y_max, y)
    y_min = min(y_min, y)

print((x_max - x_min) * (y_max - y_min))