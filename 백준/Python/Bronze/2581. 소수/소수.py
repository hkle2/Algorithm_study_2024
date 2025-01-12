import sys

M = int(sys.stdin.readline().strip())
N = int(sys.stdin.readline().strip())
prime = []

for i in range(M, N+1):
    if i != 1:
        check = True
        for j in range(2, i):
            if i % j == 0:
                check = False
        if check:
            prime.append(i)

if len(prime) != 0:
    print(sum(prime))
    print(prime[0])
else:
    print(-1)