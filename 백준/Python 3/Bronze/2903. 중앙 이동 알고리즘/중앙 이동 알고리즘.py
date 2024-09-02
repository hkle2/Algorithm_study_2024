import sys

N = int(sys.stdin.readline().strip())
d = 2

for _ in range(N):
    d = 2 * d - 1
    
print(d**2)