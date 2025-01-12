import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    s = sys.stdin.readline().strip()
    print(s[0] + s[-1])