import sys

N = int(sys.stdin.readline().strip())
string = sys.stdin.readline().strip()
answer = 0

for n in range(N):
    answer += int(string[n])

print(answer)