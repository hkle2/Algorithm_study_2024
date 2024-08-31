import sys

S = sys.stdin.readline().strip()

for n in range(97, 123):
    print(S.find(chr(n)), end=" ")