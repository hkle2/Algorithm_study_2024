import sys

N = int(sys.stdin.readline().strip())
papers = [[0 for _ in range(100)] for _ in range(100)]
answer = 0

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            papers[i][j] = 1

for i in range(100):
    answer += papers[i].count(1)

print(answer)