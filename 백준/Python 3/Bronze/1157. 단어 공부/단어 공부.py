import sys
from collections import Counter

s = sys.stdin.readline().strip().upper()
c = Counter(s)
answer = ""

for key, value in c.items():
    if value == max(c.values()):
        answer += key

if len(answer) == 1:
    print(answer)
else:
    print("?")