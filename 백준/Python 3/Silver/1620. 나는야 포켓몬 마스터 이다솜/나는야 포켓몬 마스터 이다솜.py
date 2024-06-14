import sys

d_id = {}
d_name = {}

N, M = map(int, sys.stdin.readline().rstrip().split())

for i in range(1, N+1):
    p = sys.stdin.readline().rstrip()
    d_id[i] = p
    d_name[p] = i

for i in range(M):
    q = sys.stdin.readline().rstrip()
    if q.isdigit():
        print(d_id[int(q)])
    else:
        print(d_name[q])