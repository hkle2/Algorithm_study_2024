import sys

x = int(sys.stdin.readline().strip())

for i in range(1, x+1):
    A, B = map(int, sys.stdin.readline().split())
    print(f"Case #{i}: {A} + {B} = {A + B}")