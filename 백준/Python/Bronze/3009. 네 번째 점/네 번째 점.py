import sys

x_cor = []
y_cor = []

for _ in range(3):
    x, y = map(int, sys.stdin.readline().split())
    if x not in x_cor:
        x_cor.append(x)
    else:
        x_cor.remove(x)
    if y not in y_cor:
        y_cor.append(y)
    else:
        y_cor.remove(y)

print(x_cor[0], y_cor[0])