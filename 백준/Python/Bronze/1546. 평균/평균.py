import sys

N = int(sys.stdin.readline().strip())
scores = list(map(int, sys.stdin.readline().split()))
M = max(scores)

for i in range(N):
    scores[i] = scores[i] / M * 100

print(sum(scores) / len(scores))