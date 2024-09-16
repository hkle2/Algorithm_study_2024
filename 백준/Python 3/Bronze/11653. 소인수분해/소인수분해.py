import sys

N = int(sys.stdin.readline().strip())
i = 2

while N >= 1:
    if N == 1:
        break
    if N % i == 0:
        print(i)
        N //= i
    else:
        i += 1