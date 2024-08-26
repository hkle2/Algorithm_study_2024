import sys

N = int(sys.stdin.readline().strip())
answer = 0

for n in range(N):
    flag = True
    seen = []
    s = sys.stdin.readline().strip()
    for i in range(len(s)):
        if s[i] not in seen:
            seen.append(s[i])
        else:
            if s[i-1] == s[i]:
                continue
            else:
                flag = False
                break
    if flag:
        answer += 1

print(answer)