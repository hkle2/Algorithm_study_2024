import sys

N = int(sys.stdin.readline().strip())
answer = 1
i = 1

while i < N:
    i += 6 * answer
    answer += 1

print(answer)