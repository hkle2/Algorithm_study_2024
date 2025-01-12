import sys

N = int(sys.stdin.readline().strip())
answer = 0

for _ in range(N):
    seen = []
    string = sys.stdin.readline().strip()
    for s in string:
        if (s not in seen) or (seen[-1] == s):
            seen.append(s)
        else:
            seen = []
            break
    if len(seen) != 0:
        answer += 1

print(answer)