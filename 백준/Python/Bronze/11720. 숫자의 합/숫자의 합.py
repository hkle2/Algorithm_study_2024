import sys

N = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()
answer = 0

for n in range(N):
    answer += int(s[n])

print(answer)