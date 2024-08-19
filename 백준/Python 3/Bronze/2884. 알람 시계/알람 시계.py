import sys

h, s = map(int, sys.stdin.readline().split(" "))

if s >= 45:
    print(h, (s - 45))
elif h > 0 and s < 45:
    print((h - 1), (s + 15))
else:
    print(23, (s + 15))